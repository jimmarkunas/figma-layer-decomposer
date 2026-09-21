# DIRECTV Layered Reconstruction — Execution Contract

Status: **ACTIVE**

This is the current task-specific execution contract for the DIRECTV reconstruction package. It supersedes mask-first / patch-first execution for this package.

## Product layer target

The required output is a normal Photoshop/Figma-style layered composition:

1. **Layer 01 — Full Clean Background**
2. **Layer 02 — Editorial / Environmental Effects**
3. **Layer 03 — Portrait / Jim**
4. **Layer 04 — Devices / Graphic Overlays**
5. **Layer 05 — Editable UI / Typography**

Success is defined by this layer stack and the acceptance tests below, not by recovery of unknowable hidden pixels from the flattened source.

## Current task

Produce the complete DIRECTV layered reconstruction in active production frame `160:4` and drive it to `PROMOTION_READY`.

The current bounded operation is **not** a mask, patch, cleanplate experiment, or hidden-pixel forensic recovery task.

## Inputs

### Immutable visual reference

- master: `input/directv-hero-01/master.png`
- canvas: `1586 × 992`
- SHA-256: `d5a66264cc44c449f0e29d045d729c81fe51564b768b371fd9544b34b60f22e6`
- Figma locked reference: `160:3 — DIRECTV / REFERENCE — LOCKED`

The immutable master is the visual acceptance authority. It must never be mutated.

### Active production target

- Figma file: `JM-Personal-Brand-V2`
- file key: `3ZYkEtZVyRH9B2DfVpersf`
- active production frame: `160:4 — DIRECTV / PRODUCTION — EDITABLE`

### Accepted existing layers

#### Layer 03 — Portrait / Jim

- Figma node: `278:2`
- accepted asset: `runs/directv-pr1b-candidate5/portrait-candidate.png`
- SHA-256: `50a24aa6ccffd5ea99e1d7c4247786830666530a09a051f2eb0163ce3fab8326`

No further portrait reconstruction is authorized unless full-frame QA proves a specific material defect.

#### Layer 04 — Devices / Graphic Overlays

- TV: `161:14`
- Phone: `236:18`

Preserve as independent foreground layers.

#### Layer 05 — Editable UI / Typography

Preserve/reuse the existing native editable content already present in `160:4`, including:

- header/navigation;
- hero typography;
- CTA;
- KPIs / proof metrics;
- process strip;
- wall quote/divider;
- footer phrase.

Do not rasterize or duplicate native editable content.

## Layer 01 — Full Clean Background

Create one complete **1586 × 992** architectural background image.

It should reproduce the same environment and composition language as the locked reference while remaining a complete scene beneath all foreground layers.

Required content:

- architectural concrete environment;
- opening / sky relationship;
- floor and perspective;
- right-side architectural/neon relationship where intrinsic to the environment;
- coherent lighting and material continuity.

Must not contain:

- Jim;
- TV;
- phone;
- UI;
- typography;
- wall quote;
- CTA / KPIs / process graphics;
- the left editorial black field as a baked-in design overlay.

Pixels hidden in the source may be plausibly synthesized. Exact forensic recovery of those unknowable pixels is **not required**.

No A1/A2/B1/B2 mask or patch workflow is required or authorized for the current package.

## Layer 02 — Editorial / Environmental Effects

Recreate the visual treatment independently from Layer 01 using editable Figma layers/effects where practical.

At minimum:

- left-side black editorial field / rectangle;
- right-edge fade / gradient from that dark field;
- glow / lighting treatment required to match the reference;
- independently controllable environmental accents where practical.

Turning Layer 02 off must reveal the complete full-width architectural background.

## Tool policy

### Allowed

- image generation for **one complete Layer 01 background**;
- one targeted correction pass to that background if the primary candidate has a specific material defect;
- deterministic Figma composition;
- native Figma rectangles, gradients, effects, blur, opacity and blend treatments for Layer 02;
- deterministic placement and z-order correction;
- direct Figma MCP/API asset upload;
- local tooling for deterministic file validation, sizing, hashing and comparison.

### Not allowed for this package

- A1/A2/B1/B2 patch workflows;
- cyan edit-input packages;
- persistent source-removal masks;
- mask contact sheets;
- mask approval stages;
- registered occupancy pipelines;
- patch-specific image generation;
- whole new orchestration or transport architecture;
- asking Jim to manually shuttle intermediate files;
- rebuilding accepted Jim / TV / phone unless a specific accepted-layer defect is proven;
- reopening cleanplate/mask strategy.

Temporary internal alpha/mask data used by an image tool is permitted only if invisible to product execution and discarded immediately. It must not become a first-class artifact or coordination object.

## Candidate limit

Layer 01 generation is bounded to:

- **1 primary full-background candidate**;
- **1 correction pass maximum** if the primary candidate has a concrete material defect.

No prompt sweep, candidate family, V3/V4/V5 series, or repeated strategy iteration is authorized.

If the corrected candidate still fails materially, stop and report the exact visual defect. Do not invent a new reconstruction methodology without Jim's explicit approval.

## Execution order

1. Preserve and hash-verify immutable master and accepted foreground assets.
2. Produce Layer 01 full clean background.
3. Run background-alone QA.
4. Install accepted Layer 01 at the bottom of `160:4`.
5. Build Layer 02 editorial/environmental effects natively in Figma where practical.
6. Preserve/reuse Layer 03 Jim.
7. Preserve/reuse Layer 04 TV + phone.
8. Preserve/reuse Layer 05 native editable UI/typography.
9. Remove/hide obsolete duplicated repair layers that materially interfere with the reconstruction.
10. Render `160:4` and compare against locked reference `160:3`.
11. Correct deterministic composition/z-order/duplication defects inside the same package.
12. Run final layer-independence and visual QA.
13. Exit as `PROMOTION_READY` only when the acceptance tests pass.

## Acceptance tests

### Test A — Background independence

Turn off Layers 02–05.

PASS when the result is a complete, believable architectural environment across the full `1586 × 992` canvas with no Jim, devices, UI, or typography.

### Test B — Effects independence

Enable Layer 02 only over Layer 01.

PASS when the dark editorial field / edge gradient / glow treatment recreates the reference mood and can still be toggled independently.

### Test C — Foreground independence

Enable Layers 03 and 04.

PASS when Jim, TV and phone read as independent foreground assets and the composition matches the reference at presentation scale without duplicate/ghost layers.

### Test D — Editable reconstruction

Enable Layer 05.

PASS when the full production composition matches `160:3` at presentation scale and the UI/typography remain editable/native.

### Integrity gates

Also required:

- immutable master SHA unchanged;
- LOCK #5 SHA unchanged;
- no duplicate portrait;
- no duplicated wall quote/divider;
- no duplicated nav/footer/process text;
- major layer groups independently toggleable;
- production frame only mutated after Layer 01 background-alone QA passes;
- direct visual verification after consequential Figma writes.

## Promotion state

Starting state: `RECONSTRUCTION_ACTIVE`

Permitted transition:

`RECONSTRUCTION_ACTIVE → PROMOTION_READY`

`PROMOTION_READY` requires Tests A–D and integrity gates to pass.

Do not perform PBDS canonical promotion, semantic template work, React rendering, or PowerPoint rendering inside this package. Those remain downstream of `PROMOTION_READY`.

## Anti-drift gates

Before every consequential mutation, state internally:

- `PRODUCT LAYER:` 01 / 02 / 03 / 04 / 05
- `TARGET ACCEPTANCE TEST:` A / B / C / D
- `METHOD:` one sentence

If any of these cannot be stated cleanly, do not mutate.

### Layer-first rule

Always attempt ordinary layered composition before forensic pixel recovery.

If the desired result can be represented as a complete independent layer, build that layer rather than reconstructing holes in the flattened master.

### Two-failure circuit breaker

If the same technical strategy fails materially twice, stop that strategy.

Do not create attempt 3, V4/V5, another mask package, or another transfer workaround.

Return to the product layer and choose the simplest sufficient method.

### Jim is never middleware

Jim must never be required to rename, move, reconcile, or manually transfer intermediate binary artifacts between project executors.

If an automated transport genuinely cannot complete, report the exact missing capability rather than using Jim as the transport layer.

## Reporting

Completed package report must include:

### STATUS

`PROMOTION_READY` or `BLOCKED — <exact blocker>`

### LAYER 01

- background artifact identity;
- dimensions;
- Figma node;
- background-alone QA result.

### LAYER 02

- Figma effect nodes;
- independent-toggle QA result.

### LAYER 03

- Jim node preserved.

### LAYER 04

- TV node preserved;
- phone node preserved.

### LAYER 05

- native editable groups preserved.

### FINAL QA

- reference vs production comparison;
- Tests A–D;
- integrity gates;
- exact defects if blocked.
