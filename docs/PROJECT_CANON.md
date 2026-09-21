# Figma Layer Decomposer — Project Canon

## Purpose

Canonical continuity handoff for the Figma Layer Decomposer project.

The product turns approved flat visual concepts into faithful, genuinely editable layered Figma compositions and stops at a bounded `PROMOTION_READY` handoff.

## Authority order

When sources conflict:

1. Jim's explicit current instruction in the active session.
2. Immutable master PNG for visual acceptance.
3. This file for current accepted product state and architecture.
4. `docs/EXECUTION_CONTRACT.md` for the active package's inputs, tool policy, candidate limit, QA and promotion state.
5. Generic implementation contracts only when the active execution contract explicitly puts them in scope.
6. Machine-readable schemas/manifests.
7. Historical issues, old handoffs, rejected artifacts and prior chat plans.

Do not infer approval from the existence of an artifact.

## Mission

Reconstruct flat concept images as normal Photoshop/Figma-style layered designs.

The canonical decomposition model is:

1. **Layer 01 — Full Clean Background**
2. **Layer 02 — Editorial / Environmental Effects**
3. **Layer 03 — Portrait / Subject**
4. **Layer 04 — Devices / Graphic Overlays**
5. **Layer 05 — Editable UI / Typography**

The product goal is **faithful + editable + reusable layered composition**.

It is not forensic recovery of every unknowable hidden pixel from the flattened source.

## User entry point — canonical happy path

The Decomposer has **one user-facing entry point: the Figma/Image project chat in ChatGPT**.

There is **no separate web front end today**. GitHub is an implementation repository, not the user interface. Figma is the output/editing destination, not the place where the user starts the reconstruction request.

The minimum user interaction is:

1. Open the Figma/Image project chat in ChatGPT.
2. Upload the approved PNG/JPG **or** paste/link the Figma reference frame/node.
3. Provide the target Figma file/page/frame, or say to create a new reconstruction frame.
4. Say: **Rebuild this approved design as an editable Figma composition.**

Optional source hints may also be supplied for known portraits, product/device assets, logos, or other authoritative source material. These are optional; their absence does not require the user to manage the reconstruction workflow.

Everything else is internal implementation detail.

### Required system behavior

After the request, the system owns the workflow end to end:

1. capture and freeze the approved source as the immutable visual reference;
2. inspect the source and classify the five canonical layer roles;
3. recover authoritative source assets when available;
4. generate/reconstruct missing independent visual layers when necessary;
5. rebuild text, buttons, navigation, vectors, and other semantic UI natively in Figma;
6. preserve exact canvas geometry, z-order, and layer independence;
7. install the reconstruction into the specified Figma destination;
8. run deterministic QA against the immutable reference;
9. present the user with a visual review of **reference vs reconstructed composition**;
10. accept plain-language visual corrections and apply them inside the same reconstruction package;
11. stop at `PROMOTION_READY` when fidelity and editability are accepted.

### User interaction contract

The user is expected to make only product/visual decisions, for example:

- `Approve.`
- `The portrait needs more shadow on the right.`
- `The TV is too large.`
- `That headline is not aligned with the reference.`

The user must **not** be required to:

- create or approve masks;
- understand clean-plate stages;
- edit manifests;
- run repository commands;
- manually transfer, rename, reconcile, or re-upload intermediate files;
- decide which executor/tool should perform an internal substep;
- coordinate ChatGPT, Codex, Figma, Drive, or image-generation tools manually.

If an internal executor needs another executor, the project owns that handoff. Jim is never middleware.

### Entry-point acceptance test

For the next non-DIRECTV mockup, success means Jim can start in the Figma/Image ChatGPT project chat, provide the source design + Figma destination once, receive a materially complete editable reconstruction, and perform any remaining correction through ordinary visual feedback without being exposed to internal reconstruction mechanics.

If the next mockup again requires bespoke user-managed workflow orchestration, the Decomposer has failed its user-entry-point requirement and must be simplified rather than expanded.

## Core architecture

Use the simplest truthful layer strategy:

- recover authoritative source assets when they exist;
- rebuild semantic text/UI/vector content natively;
- generate/rebuild complete independent visual layers when source pixels do not exist;
- compose layers deterministically;
- compare the result against the immutable reference.

If a complete independent layer can solve the requirement, prefer that over reconstructing local holes in the flattened master.

Masks may exist transiently inside a tool, but they are not product artifacts, roadmap items, approval objects, persistent Figma structures, or cross-agent coordination objects.

## Current proof object

DIRECTV hero, canvas `1586 × 992`.

Repository:

- `jimmarkunas/figma-layer-decomposer`

Default branch:

- `main`

Current state:

- **DIRECTV E2E LAYERED RECONSTRUCTION ACTIVE**

Current exit:

- `PROMOTION_READY`

Current execution contract:

- `docs/EXECUTION_CONTRACT.md`

## Immutable visual target

- path: `input/directv-hero-01/master.png`
- dimensions: `1586 × 992`
- SHA-256: `d5a66264cc44c449f0e29d045d729c81fe51564b768b371fd9544b34b60f22e6`

Never mutate the immutable master.

## Active Figma workspace

File:

- `JM-Personal-Brand-V2`
- file key `3ZYkEtZVyRH9B2DfVpersf`

Active workspace:

- page `155:63 — 999 - Test 2`
- immutable reference `160:3 — DIRECTV / REFERENCE — LOCKED`
- production target `160:4 — DIRECTV / PRODUCTION — EDITABLE`

The older `240:4 / 240:5` workspace is historical staging.

## Accepted foreground layers

### Layer 03 — Portrait / Jim

Accepted basis:

- asset `runs/directv-pr1b-candidate5/portrait-candidate.png`
- dimensions `1048 × 1501`, RGBA
- SHA-256 `50a24aa6ccffd5ea99e1d7c4247786830666530a09a051f2eb0163ce3fab8326`
- active Figma node `278:2`

The older `191:5` portrait is rejected as source truth and remains superseded.

### Layer 04 — Devices / Graphic Overlays

Accepted current device layers:

- TV `161:14`
- phone `236:18`

Preserve them as independent foreground layers unless a specific material defect is proven.

### Layer 05 — Editable UI / Typography

`160:4` already contains native/editable major UI/text content, including:

- header/navigation;
- hero headline/subcopy;
- CTA;
- KPIs/proof metrics;
- process strip;
- wall quote/divider;
- footer phrase.

Preserve/reuse this native content. Do not rasterize or duplicate it.

## Current Layer 01 requirement

Create one complete full-width architectural background for the entire `1586 × 992` frame.

The background must contain the complete environment beneath foreground layers:

- concrete architecture;
- opening/sky relationship;
- floor/perspective;
- coherent material/lighting;
- right-side architectural/neon relationship where intrinsic to the space.

It must not contain Jim, TV, phone, UI, typography, wall quote, process graphics, or the left editorial black field as a baked design overlay.

Hidden areas may be plausibly synthesized. Exact historical hidden pixels are not required.

## Current Layer 02 requirement

Recreate the editorial/environmental treatment independently over Layer 01, preferably as editable Figma layers/effects:

- left black editorial field/rectangle;
- right-edge fade/gradient;
- glow/lighting treatment required for reference fidelity;
- independently controllable accent effects where practical.

Turning Layer 02 off must reveal the complete Layer 01 architectural background.

## Superseded execution paths

The following are historical/rejected for the current package and must not be restarted unless Jim explicitly changes architecture:

- A1/A2/B1/B2 patch programs;
- cyan edit-input workflows;
- source-removal mask packages;
- mask contact sheets and approval stages;
- registered occupancy pipelines;
- V1/V2/V3 deterministic cleanplate iteration;
- whole-canvas forensic hidden-pixel recovery as the product goal;
- user-mediated intermediate file transfer.

`docs/CLEAN_PLATE_CONTRACT.md` remains generic historical/supporting capability documentation. It is **not the active DIRECTV execution contract** unless a future approved package explicitly invokes it.

## Current delivery package

Execute as one package under `docs/EXECUTION_CONTRACT.md`:

1. preserve/hash-verify immutable master and accepted layers;
2. generate one complete Layer 01 background;
3. background-alone QA;
4. install accepted Layer 01 into production frame;
5. construct Layer 02 editorial/environmental effects;
6. preserve Layer 03 Jim;
7. preserve Layer 04 TV/phone;
8. preserve Layer 05 editable UI;
9. eliminate duplicate/obsolete repair layers that materially interfere;
10. compare `160:4` against locked reference `160:3`;
11. correct deterministic composition defects inside the same package;
12. verify independent layer toggles and final visual fidelity;
13. exit `PROMOTION_READY` only when the execution contract's acceptance tests pass.

## Anti-drift rules

### Layer-first

Every task must directly advance one of Layers 01–05.

Before consequential mutation, resolve:

- `PRODUCT LAYER`
- `TARGET ACCEPTANCE TEST`
- `METHOD`

If unclear: no mutation.

### Two-failure circuit breaker

After two material failures of the same strategy, stop that strategy.

Do not create attempt 3, V4/V5, another mask package, another candidate family, or another coordination artifact.

Return to the layer output and choose the simplest sufficient method.

### No workaround cascades

A blocker does not authorize new architecture.

Report the exact missing capability and use the smallest allowed workaround.

### Jim is never middleware

Jim must not be required to manually rename, move, reconcile, or transport intermediate binary artifacts between executors.

## Repository/worktree facts

Known unrelated local state may include:

- modified `decomposer/directv_pr2_qa.py`;
- untracked `input/` source material.

Preserve unrelated work. Its presence alone is not a blocker.

## Product boundary

This repository owns reconstruction through `PROMOTION_READY`.

After `PROMOTION_READY`, Personal Career Brand / PBDS owns:

- canonical `JM-Personal-Brand` Figma promotion;
- reusable template/component definition;
- semantic content contract;
- non-source content substitution proof;
- React consumption;
- editable PowerPoint consumption.

See `docs/PROMOTION_HANDOFF_CONTRACT.md` before downstream promotion work.
