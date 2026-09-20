# Execution Contract

Status: canonical execution guardrail for bounded decomposition/edit operations.

## Purpose

Prevent agent drift by requiring every image-affecting operation to declare, before execution:

- immutable inputs and hashes;
- operation class;
- allowed and denied tools;
- exactly what may change;
- exactly what must not change;
- candidate limit;
- fail-closed behavior;
- automated QA requirements;
- human approval state;
- promotion state.

The contract is machine-readable and validated against `schema/edit-operation.schema.json`.

## Mandatory rule

No image-affecting operation may begin without a valid execution contract.

If the requested method is unavailable, denied, or conflicts with the contract, stop `BLOCKED`.

Never substitute a different tool, model, source, mask, transformation, reconstruction strategy, or number of candidates without an explicitly amended contract.

## Operation classes

### `EXACT_EDIT`

Use when the user says, in substance: exact image, same image, preserve everything, only change X, or do not change anything else.

Rules:

- `image_gen` is always `DENIED`;
- deterministic raster processing is required;
- an authorized mask is required;
- exactly one candidate;
- dimensions remain unchanged;
- zero changed pixels outside the authorized mask;
- unchanged pixels must remain byte-identical after serialization where the file format permits exact comparison.

### `EXTRACT`

Use when recovering visible pixels from an approved source/master.

Rules:

- no synthesized content;
- source pixels are authoritative;
- output transparency/placement may change only as explicitly contracted.

### `REBUILD_NATIVE`

Use for editable text, UI, and vector rebuilds.

### `REBUILD_RASTER_FROM_SOURCE`

Use when a trustworthy related source exists but the complete independent layer cannot be recovered directly from the flattened master.

Generative reconstruction may be allowed only when the contract explicitly sets `tool_policy.image_gen: ALLOWED`.

### `RECONSTRUCT_HIDDEN_PIXELS`

Use only for genuinely hidden pixels that cannot be recovered from source assets.

### `GENERATIVE_EXPLORATION`

Use only for explicitly exploratory creative work. Exploratory outputs are never production-approved automatically.

## Chat execution rule

When ChatGPT image generation is allowed by a contract, ChatGPT must read the canonical contract from GitHub before generation and emit a concise pre-generation execution receipt containing:

- operation ID;
- operation class;
- immutable input hashes;
- tool authorization;
- candidates allowed;
- prohibited changes;
- human gate;
- promotion state.

If ChatGPT cannot produce that receipt from the canonical contract, generation is `BLOCKED`.

A chat-generated image is always a candidate only. It must be imported back into the repository workflow for QA and must not inherit approval from a previous candidate.

## Hash-based approval

Human approval promotes exact artifact bytes, not an idea or visual family.

An approved artifact must be referenced downstream by SHA-256. A regenerated approximation is a different artifact and has no inherited approval.

## Silent fallback prohibition

All contracts must set:

```yaml
execution:
  fail_closed: true
  silent_fallback_allowed: false
```

If the authorized method fails or is unavailable, stop `BLOCKED`.

## Tool policy

At minimum every contract declares:

```yaml
tool_policy:
  image_gen: ALLOWED|DENIED
  deterministic_raster: ALLOWED|DENIED
  segmentation: ALLOWED|DENIED
  alternate_source: ALLOWED|DENIED
```

The operation guard rejects a requested tool that is not explicitly `ALLOWED`.

`EXACT_EDIT` contracts are schema-enforced so `image_gen` cannot be allowed.

## Candidate limit

Every contract declares `execution.candidates_allowed`.

Agents must stop once that count is reached. A failed candidate does not authorize another candidate unless the contract is explicitly amended.

## Exact-edit QA

For `EXACT_EDIT`, automated QA must verify:

- original and candidate dimensions match;
- mask dimensions match;
- candidate differs from original only where mask alpha/value is nonzero;
- changed pixels outside the mask equal zero.

Any outside-mask change is an automated `FAIL`.

## Human gate

`human_gate` begins `PENDING` and changes only after explicit review.

Artifact existence, automated PASS, or visual similarity does not imply human approval.

## Promotion

`promotion` begins `NOT_PROMOTED`.

Only an explicit human PASS plus any required automated PASS may move an artifact to `APPROVED_SOURCE`.

## Current DIRECTV usage

- PR-1B source-guided reconstruction is governed by `examples/directv/pr-1b.yaml`.
- Any follow-on request such as “use this exact candidate and smooth skin only” is a new `EXACT_EDIT` operation and must use a new exact-edit contract. It may not reuse PR-1B generative authorization.

## Enforcement implementation

`decomposer/operation_guard.py` provides:

- YAML loading;
- JSON Schema validation;
- tool authorization;
- execution receipt generation;
- input hash verification;
- exact-edit unchanged-region verification.

The guardrail is intentionally small. It does not orchestrate models or replace domain-specific QA.
