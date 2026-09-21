# Decomposer Bridge Contract

Status: **NEXT BUILD PACKAGE — BRIDGE-1**

## Purpose

The Decomposer Bridge is **executable backend code inside `jimmarkunas/figma-layer-decomposer`**. It is not a chat, a Notion page, a GitHub workflow, or a Drive folder.

Its job is to make the canonical ChatGPT user entry point actually work without Jim becoming middleware.

Canonical flow:

```text
Jim
→ Figma Decomposer ChatGPT Project chat
→ Decomposer Bridge
→ ChatGPT/Figma Connector
→ Figma
```

ChatGPT is the user interface and judgment layer. The Bridge owns binary artifacts and deterministic reconstruction execution. The existing ChatGPT/Figma Connector owns Figma reads/writes.

## Public operation

BRIDGE-1 exposes one reconstruction operation:

```text
reconstruct_design(source_design, figma_target, optional_source_assets)
```

The exact HTTP/MCP adapter may vary. The backend contract must not.

### Required inputs

- source design bytes or an authorized artifact reference that resolves to the exact bytes;
- target Figma file/page/frame identity;
- optional authoritative source assets.

Jim must not provide masks, manifests, internal job IDs, executor routing, or intermediate files.

### Required result

Return a structured result containing:

- job ID;
- immutable source SHA-256;
- source dimensions;
- produced layer artifacts and their SHA-256 values;
- Figma placement manifest;
- deterministic QA result;
- generation provenance;
- final state;
- exact blocker when not ready for Figma.

## Deterministic job model

Every accepted request creates or resumes exactly one job workspace:

```text
jobs/<job-id>/
  source.png
  request.json
  layers/
  qa/
  result.json
```

The logical state machine is:

```text
RECEIVED
→ SOURCE_FROZEN
→ LAYERS_CLASSIFIED
→ ASSETS_CREATED
→ QA_PASSED
→ READY_FOR_FIGMA
→ COMPLETE
```

Failure is explicit. A failed stage does not silently advance.

### Idempotency

The same logical request must resolve to the same job when the immutable inputs and pipeline version are unchanged. At minimum, identity derives from:

- source SHA-256;
- normalized Figma target identity;
- authoritative optional-source hashes;
- pipeline version.

A retry resumes the existing job rather than creating another interpretation of the same request.

## Generation determinism boundary

Generative image pixels are probabilistic. The **production process around generation is deterministic**.

For every generated raster asset, record:

- immutable source SHA-256;
- pipeline version;
- prompt-template version;
- model identifier;
- requested dimensions;
- attempt number;
- output SHA-256;
- QA state.

Candidate policy:

- one primary generation;
- one targeted correction maximum for a concrete material defect;
- no prompt sweep, candidate family, or open-ended retry loop.

If the correction still fails materially, return an exact blocker. Do not invent a new reconstruction architecture inside the run.

## Reuse from the current repository

BRIDGE-1 should reuse the proven deterministic utilities already present where they fit:

- SHA-256 hashing;
- image loading/serialization;
- dimension validation;
- bounds/geometry validation where applicable;
- output artifact validation;
- pixel-difference/unchanged-region QA primitives where applicable;
- JSON-schema validation patterns.

The existing mask-first `cleanplate` workflow remains an internal legacy/fallback utility. It is not the Bridge API and must not shape the user-facing contract.

## Minimum implementation surface

Expected bounded implementation:

```text
bridge/
  api.py
  job.py
  artifacts.py
  image_backend.py
  qa.py
  models.py

schema/
  reconstruction-job.schema.json

tests/
  test_bridge.py
```

Names may change if implementation evidence justifies it. The responsibilities may not expand into a generic orchestration platform.

## Storage boundary

GitHub stores code, schemas, tests, and contracts — **not mutable run binaries**.

Run binaries live in temporary/object storage owned by the Bridge. Google Drive is an acceptable first transport/storage adapter if it is the smallest available implementation.

Jim must never manually rename, move, reconcile, download, or re-upload intermediate assets.

## Figma boundary

The Bridge does not become a second Figma integration stack.

The Bridge returns validated layer artifacts plus placement metadata. The existing ChatGPT/Figma Connector remains the canonical Figma read/write mechanism unless a concrete connector limitation requires an explicitly approved change.

## BRIDGE-1 acceptance

BRIDGE-1 is accepted only when one representative reconstruction proves:

1. source image enters programmatically;
2. source bytes are frozen and hashed;
3. the required raster layer generation is invoked programmatically;
4. intermediate binaries are stored/transferred without Jim;
5. deterministic validation/QA runs;
6. the Bridge returns hashed layer artifacts plus a placement manifest;
7. a repeated identical request resumes the same logical job;
8. a real failure returns an exact failed state/blocker;
9. no user-visible masks, cleanplate stages, file shuttling, or executor coordination are required.

This acceptance proves the backend. The subsequent end-to-end product proof is the next non-DIRECTV mockup through the ChatGPT Project entry point and ChatGPT/Figma Connector.

## Non-goals

BRIDGE-1 does not authorize:

- another scheduler;
- a generic agent/orchestration framework;
- a permanent duplicate datastore;
- a new Figma plugin stack;
- broad decomposition generalization;
- new mask/reconstruction architecture;
- PBDS/template/rendering work;
- rebuilding DIRECTV-specific visual logic unless required to prove the Bridge boundary.

## Build estimate

Current inventory supports a bounded estimate of approximately **4–7 focused engineering hours** for the usable backend plus deployment/integration plumbing, assuming required credentials and hosting are available.

The implementation starts from current `main`; no code build is authorized by this canonization-only change.