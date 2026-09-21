# Figma Layer Decomposer — Project Canon

## Purpose

The product turns approved flat visual concepts into faithful, genuinely editable layered Figma compositions and stops at a bounded `PROMOTION_READY` handoff.

## Authority order

When sources conflict:

1. Jim's explicit current instruction.
2. Immutable master/reference image for visual acceptance.
3. This file for current accepted product state and architecture.
4. `docs/BRIDGE_CONTRACT.md` when BRIDGE-1 or the user-entry-point backend is in scope.
5. `docs/EXECUTION_CONTRACT.md` for the active DIRECTV reconstruction package.
6. Other generic implementation contracts only when explicitly invoked by the active package.
7. Machine-readable schemas/manifests.
8. Historical issues, old handoffs, rejected artifacts and prior chat plans.

Do not infer approval from the existence of an artifact.

## Mission

Reconstruct flat concept images as normal Photoshop/Figma-style layered designs.

Canonical layer model:

1. **Layer 01 — Full Clean Background**
2. **Layer 02 — Editorial / Environmental Effects**
3. **Layer 03 — Portrait / Subject**
4. **Layer 04 — Devices / Graphic Overlays**
5. **Layer 05 — Editable UI / Typography**

The product goal is **faithful + editable + reusable layered composition**. It is not forensic recovery of every unknowable hidden pixel.

## Canonical user entry point

The user-facing entry point is the **Figma Decomposer ChatGPT Project chat**.

There is no separate web front end today. GitHub is the implementation repository. Figma is the output/editing destination.

Jim's happy path is:

1. Open the Figma Decomposer ChatGPT Project chat.
2. Upload the approved PNG/JPG or provide the Figma reference frame.
3. Provide the target Figma file/page/frame.
4. Say: **Rebuild this approved design as an editable Figma composition.**
5. Review reference vs reconstruction and provide ordinary visual feedback or approve.

Jim must not manage masks, manifests, cleanplate stages, repository commands, Drive transfers, internal job IDs, file naming, or executor/tool routing.

## Canonical runtime architecture

The approved execution shape is:

```text
Jim
→ Figma Decomposer ChatGPT Project chat
→ Decomposer Bridge
→ ChatGPT/Figma Connector
→ Figma
```

### ChatGPT Project chat

Owns the user conversation, visual/product judgment, and the natural-language reconstruction request.

### Decomposer Bridge

The Bridge is **real executable backend code in this repository**. It owns binary artifacts, deterministic job execution, programmatic image-generation calls, artifact provenance, and deterministic QA.

It is not an MD file, another chat, GitHub Actions, or a Drive folder.

Canonical contract: `docs/BRIDGE_CONTRACT.md`.

### ChatGPT/Figma Connector

Remains the canonical Figma read/write mechanism. The Bridge returns validated artifacts and placement metadata; it does not create a second Figma integration stack.

## Determinism boundary

Generative image pixels are probabilistic. The surrounding production workflow must be deterministic:

- freeze/hash immutable input bytes;
- fixed pipeline and prompt-template versions;
- explicit model/dimensions/provenance;
- one logical job per identical request;
- retries resume the same job;
- one primary generation + one targeted correction maximum;
- hashed outputs;
- deterministic geometry/placement/QA;
- explicit failed state/blocker instead of silent continuation.

## Next build package — BRIDGE-1

**Status: PLANNED — build starts next development session. No implementation is authorized by the current canonization-only change.**

Goal: build the smallest deterministic backend that makes the ChatGPT entry point executable without Jim becoming middleware.

Expected implementation surface:

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

Reuse existing deterministic utilities where useful: hashing, image serialization, dimension/bounds validation, output validation, diff/unchanged-region QA primitives, and JSON-schema validation patterns.

The existing mask-first `cleanplate` path is legacy/fallback infrastructure. It is not the public product API and must not drive BRIDGE-1 architecture.

BRIDGE-1 acceptance is defined only in `docs/BRIDGE_CONTRACT.md`.

Current inventory estimate: **4–7 focused engineering hours** for the usable backend plus deployment/integration plumbing, assuming required credentials and hosting are available.

## Current DIRECTV proof object

DIRECTV remains the current visual proof object, canvas `1586 × 992`.

Repository: `jimmarkunas/figma-layer-decomposer`

Active Figma workspace:

- file `JM-Personal-Brand-V2`
- file key `3ZYkEtZVyRH9B2DfVpersf`
- page `155:63 — 999 - Test 2`
- immutable reference `160:3 — DIRECTV / REFERENCE — LOCKED`
- production target `160:4 — DIRECTV / PRODUCTION — EDITABLE`

Immutable master:

- `input/directv-hero-01/master.png`
- `1586 × 992`
- SHA-256 `d5a66264cc44c449f0e29d045d729c81fe51564b768b371fd9544b34b60f22e6`

Accepted current foreground:

- portrait `278:2`, accepted asset SHA-256 `50a24aa6ccffd5ea99e1d7c4247786830666530a09a051f2eb0163ce3fab8326`;
- TV `161:14`;
- phone `236:18`;
- native editable major UI/text already present in `160:4`.

The detailed DIRECTV execution package remains in `docs/EXECUTION_CONTRACT.md`. Do not reopen mask/patch archaeology or create new DIRECTV architecture while BRIDGE-1 is the next product-development package.

## Core reconstruction architecture

Use the simplest truthful layer strategy:

- recover authoritative source assets when they exist;
- rebuild semantic text/UI/vector content natively;
- generate/rebuild complete independent visual layers when source pixels do not exist;
- compose layers deterministically;
- compare against the immutable reference.

If a complete independent layer solves the requirement, prefer it over reconstructing local holes.

Masks may be transient implementation details but are not product artifacts, roadmap items, approval objects, persistent Figma structures, or cross-agent coordination objects.

## Superseded execution paths

Do not restart without Jim explicitly changing architecture:

- A1/A2/B1/B2 patch programs;
- cyan edit-input workflows;
- source-removal mask packages/contact sheets/approval stages;
- registered occupancy pipelines;
- V1/V2/V3 deterministic cleanplate iteration;
- whole-canvas forensic hidden-pixel recovery;
- user-mediated intermediate file transfer.

## Anti-drift

- Jim is never middleware.
- A transfer problem does not authorize a new reconstruction method.
- A generation problem does not authorize a new datastore or orchestration framework.
- A Figma problem does not authorize a second Figma stack.
- After two material failures of the same strategy, stop that strategy and choose the simplest sufficient alternative.
- BRIDGE-1 must remain one bounded backend package, not a generic workflow platform.

## Product boundary

This repository owns reconstruction through `PROMOTION_READY`.

After `PROMOTION_READY`, Personal Career Brand / PBDS owns canonical Figma promotion, reusable template/component definition, semantic content contract, non-source variation proof, React consumption, and editable PowerPoint consumption.

See `docs/PROMOTION_HANDOFF_CONTRACT.md` for that handoff.