# Figma Layer Decomposer — Project Canon

## Purpose

This file is the canonical continuity handoff for the Figma Layer Decomposer project. It exists so ChatGPT, Codex, local development sessions, and future conversations can recover the current accepted state without relying on one chat transcript.

## Authority order

When sources conflict, use this order:

1. **Jim's explicit current instruction** in the active working session.
2. **Immutable master PNG** — visual acceptance authority for reconstruction fidelity.
3. **This file** — current accepted product state, active delivery package, Figma target, and current reconstruction authorization.
4. `docs/CLEAN_PLATE_CONTRACT.md` — generic implementation contract when hidden-background reconstruction is actually in scope.
5. `schema/layer-manifest.schema.json` — machine-readable placement/QA contract.
6. A GitHub issue only when this file explicitly names that issue as the active delivery package.
7. Notion index / ChatGPT Project uploads — pointers only.

Do not infer approval from the mere existence of an artifact.

## Mission

Turn approved flat mock-up PNGs into genuinely editable layered Figma compositions while preserving 1:1 visual fidelity to the immutable master image, then emit a bounded `PROMOTION_READY` handoff to Personal Career Brand / PBDS.

The project owns source recovery, decomposition, faithful raster/native reconstruction, fidelity QA, and the staging Figma composition. It does **not** own the canonical Personal Brand design system, semantic template contract, React rendering, or PowerPoint rendering.

Cross-system flow:

`APPROVED CONCEPT PNG → SOURCE RECOVERY / DECOMPOSITION → 1:1 EDITABLE FIGMA → PROMOTION_READY → PBDS CANONICAL FIGMA PROMOTION → SEMANTIC CONTRACT → REACT / POWERPOINT`

## Two-part product boundary

This project is Part 1 of a two-part concept-to-production product.

### Part 1 — Figma Layer Decomposer

Owns:

- approved concept ingestion;
- source recovery and provenance;
- foreground/background inventory and classification;
- raster extraction/rebuild;
- hidden-background reconstruction when genuinely required;
- native Figma rebuild of editable text/UI/vector content;
- deterministic placement/manifests;
- fidelity QA;
- staging Figma composition;
- `PROMOTION_READY` handoff.

### Part 2 — Personal Brand Design System / PBDS-4

Owns after `PROMOTION_READY`:

- canonical `JM-Personal-Brand` Figma promotion;
- reusable template/component definition;
- semantic content/template contract;
- non-source content-substitution proof;
- React presentation consumption;
- editable PowerPoint consumption;
- later cross-surface/template-family generalization.

Do not collapse the two ownership boundaries. DIRECTV is the first proof object for Part 1 and the bridge specimen into Part 2; it is not the only slide/product.

## Hard anti-spin rule

The project is past architecture discovery for DIRECTV. Do not create another roadmap rewrite, segmentation/mask strategy, model bake-off, orchestration platform, issue-per-step program, or governance artifact before the current DIRECTV delivery package completes.

The current bounded operation is the **complete DIRECTV reconstruction delivery package**, not one mask, one patch, or one intermediate candidate.

Internal deterministic steps may iterate inside the package. Stop only at the package acceptance gate or a genuine unresolved blocker.

## Repository and current state

- Repository: `https://github.com/jimmarkunas/figma-layer-decomposer`
- Default branch: `main`
- Local repository: `/Users/jimmarkunas/Development/Jim/figma-layer-decomposer`
- Current reference: DIRECTV hero, `1586 × 992`
- Current product state: **DIRECTV E2E RECONSTRUCTION ACTIVE**
- Current package exit: **`PROMOTION_READY` candidate**
- Issue #11 / PR-1B is superseded by the accepted current state and is not the active execution contract.

Known local working-tree facts from the current session:

- `decomposer/directv_pr2_qa.py` contains an unrelated local modification and must remain untouched unless Jim explicitly expands scope.
- local `input/` source material may be untracked; its presence is not by itself a blocker and it must not be committed wholesale without explicit scope.

## Immutable visual target

- `input/directv-hero-01/master.png`
- canvas `1586 × 992`
- SHA-256 `d5a66264cc44c449f0e29d045d729c81fe51564b768b371fd9544b34b60f22e6`

The immutable master remains the visual acceptance authority and must never be mutated.

## Portrait state

Pinned related identity/source reference remains:

- repository `jimmarkunas/portfolio`
- pinned commit `5af5f3191cdbd26cef48d3290fa1e979b04f0a73`
- `public/jim/hero-jim-01-cutout-v2.png`
- SHA-256 `06294961581f4fd3a0b08dae8af3eacf7c05e2efb3d61fe72fb517abe2995100`

PR-1 proved deterministic affine alignment of that website portrait is insufficient. Do not continue affine tuning.

Jim has accepted the current **LOCK #5** portrait result as the portrait basis for continuation. The exact local LOCK #5 asset/path/bytes must be resolved and hash-verified before production use; inability to resolve the accepted asset is a genuine blocker.

The Figma node `191:5 — Portrait / Jim — TRUE CUTOUT (toggleable)` is **REJECTED AS A SOURCE ASSET** in its current state. Direct inspection shows that it reveals TV/environment/sky/floor pixels and therefore is not a clean standalone portrait. Do not treat that Figma node as portrait truth merely because of its name.

Use the accepted LOCK #5 asset as the portrait basis and replace/correct the Figma portrait implementation accordingly.

## Accepted broader decomposition boundary

Source-first recovery remains mandatory. Accepted implementation directions are:

- visible background pixels remain immutable-master pixels wherever possible;
- hidden background pixels may be reconstructed only where foreground removal exposes genuinely hidden content;
- portrait, TV, and phone must exist as independent foreground assets/layers;
- header/navigation, hero copy/CTA, metrics, wall message/divider, process strip, and bottom signature are native editable Figma content;
- foreground extraction/rebuild and hidden-background reconstruction are separate operations;
- rejected GrabCut/semantic/mask-first portrait paths remain rejected;
- the existing clean-plate engine remains valid fallback infrastructure rather than the default product architecture.

## Current reconstruction authorization

Jim explicitly authorizes the current DIRECTV end-to-end delivery package to reconstruct genuinely hidden **environment/background** pixels required to produce an independent background and faithful final recomposition.

This authorization is bounded by all of the following:

- source recovery/provenance work already completed for DIRECTV does not need to be re-run merely to satisfy historical stage sequencing;
- reconstruction applies only to environmental pixels genuinely hidden by foreground content or contaminated temporary repairs;
- exact visible master pixels must be preserved wherever they are available and suitable;
- reconstruction must stay inside verified foreground occupancy/removal geometry or another explicitly documented bounded repair region;
- exact foreground occupancy may be derived from the accepted standalone raster asset or the actual verified native Figma foreground node; producing that derived mask is implementation work and does not require a separate task-specific execution-contract document;
- no rejected portrait masks become geometry authority;
- no whole-image reinterpretation or redesign;
- automated guards and human full-frame visual QA remain required before `PROMOTION_READY`;
- deterministic defects found during the package must be corrected inside the same package instead of returned as a new micro-stage.

Absence of a pre-existing derived mask, intermediate patch, or duplicate repo-side visual spec is **not** a blocker when it can be deterministically derived from an accepted foreground asset/native layer during this authorized package.

## Active Figma workspace

File:

- `https://www.figma.com/design/3ZYkEtZVyRH9B2DfVpersf/JM-Personal-Brand-V2?node-id=155-63`
- file key `3ZYkEtZVyRH9B2DfVpersf`

Current active reconstruction workspace:

- page `155:63 — 999 - Test 2`
- workspace section `160:2 — DIRECTV / Reconstruction Workspace`
- immutable reference `160:3 — DIRECTV / REFERENCE — LOCKED`
- editable production target `160:4 — DIRECTV / PRODUCTION — EDITABLE`

The older page/frame pair:

- `240:4 — 00_Master_Reference`
- `240:5 — Editable Master Reference 01 — Layered`

is **historical staging and not the active DIRECTV target**. Do not use its empty groups to infer that current native reconstruction is missing.

### Current verified Figma facts

`160:4` already contains native/editable foreground for the major text/UI system, including the `162:*` header/hero/CTA/proof/system nodes plus editable wall quote `195:5` and divider `195:6`.

Preserve that native reconstruction unless full-frame comparison shows a specific material defect.

Known current visual defects include:

- large incorrect central dark/background slab;
- contaminated/incorrect environmental repair geometry;
- rejected contaminated portrait implementation at `191:5`;
- wall/background repair that requires faithful environmental continuation;
- raster/background seam and z-order verification around TV/phone.

The product task is therefore background/environment repair + correct independent raster foreground + final recomposition/QA, not another native-UI rebuild program.

## Current DIRECTV delivery package

Execute as one bounded package:

1. Inspect `160:3` and `160:4` and current local accepted assets.
2. Resolve/hash-verify the accepted LOCK #5 portrait asset.
3. Replace/correct the rejected contaminated Figma portrait implementation using the accepted asset.
4. Preserve/verify TV and phone as independent foreground assets; correct deterministic crop/alpha/z-order leakage if found.
5. Derive exact occupancy/removal geometry from verified foreground assets/native Figma layers as needed.
6. Reconstruct only the hidden environmental/background pixels needed for an independent clean background.
7. Remove or supersede temporary/contaminated repair layers that visibly break the composition.
8. Preserve existing native editable UI/text/vector content unless a specific visual defect requires a narrow correction.
9. Recompose the entire slide.
10. Render and compare `160:4` against immutable reference `160:3`.
11. Correct deterministic visual defects inside the same package.
12. Verify layer independence/editability and immutable-master integrity.
13. Exit as `PROMOTION_READY` candidate only after required automated evidence and human full-frame visual QA pass.

No Jim manual download/upload/rename/move step should be introduced for intermediate assets when available integrations/local tooling can perform the transfer directly.

## Genuine blockers

A `BLOCKED` result is valid when the package cannot safely continue because of an unresolved external or source-of-truth problem, for example:

- the accepted LOCK #5 asset cannot be located or hash-verified;
- required immutable source bytes are unavailable;
- Figma write access to the active target is unavailable;
- two explicit current requirements are mutually impossible;
- overlapping unexplained local changes make the intended mutation unsafe.

These are not blockers by themselves:

- an intermediate mask/patch does not already exist;
- a derived occupancy mask has not been separately approved;
- an internal candidate needs correction;
- existing native Figma nodes do not have duplicate repo-side specs;
- known unrelated local changes can be safely preserved outside the mutation surface.

## Figma layer outcome required for DIRECTV

The final editable composition must provide independent/toggleable roles equivalent to:

- background/environment;
- portrait;
- TV/device;
- phone/device;
- header/nav;
- hero copy/CTA;
- metrics/proof;
- wall message;
- process/system strip;
- bottom signature/footer.

Exact final node naming may follow the already-built `160:4` structure. Do not create a second permanent design system in the staging file.

## Promotion boundary

The Decomposer stops at `PROMOTION_READY`:

`RECONSTRUCTION_ACTIVE → PROMOTION_READY → PBDS PROMOTED → CONSUMABLE`

`PROMOTION_READY` requires:

- a genuinely editable DIRECTV composition;
- independent raster/background roles required for reuse;
- full-frame human visual acceptance against the immutable master;
- required automated reconstruction/fidelity QA;
- linked provenance and accepted asset evidence;
- exact staging Figma/frame identification;
- enough layer-role description for PBDS to evaluate reuse.

PBDS owns canonical Figma promotion, reusable-template/component definition, semantic content contract, React consumption, editable PowerPoint consumption, and later template generalization.

Do not generalize mock-ups #2–#6 until DIRECTV reaches `PROMOTION_READY` and PBDS proves one promoted concept can be reused through a non-source content variation, one semantic contract, one React slide, and one editable PowerPoint slide.

## Accepted completed work

- M2 structure verification — COMPLETE
- 3A removal geometry — PASS
- 3A.1 unapproved wall patch removal — PASS
- 3B.0 clean-plate contract/repo bootstrap — COMPLETE
- 3B.1 deterministic clean-plate engine — COMPLETE as fallback infrastructure
- SR-1 source inventory — COMPLETE
- SR-2 provenance review — COMPLETE
- SR-3 decomposition classification — COMPLETE as planning evidence
- SR-4 decomposition-plan review — PASS
- ARC-1 architecture checkpoint — COMPLETE; only bounded extraction/shared mechanics were justified
- EX-0 deterministic extraction engine — COMPLETE
- mask-first portrait strategies — REJECTED/SUPERSEDED
- PR-1 source-guided affine portrait proof — COMPLETE WITH AUTOMATED FAIL
- PR-1B historical portrait-candidate phase — SUPERSEDED by Jim's accepted LOCK #5 continuation state

## Current next step

**Complete the current DIRECTV end-to-end reconstruction package against `160:3 / 160:4` and prove the `PROMOTION_READY` candidate.**

Do not insert another roadmap, architecture, mask-approval, or micro-stage package in front of that work.

## Continuity protocol

At the start of a new implementation session:

1. Read this file from current branch/main.
2. Read `AGENTS.md`.
3. Read only the implementation contracts needed for the current package surface.
4. Confirm repository root, branch, working-tree state, active Figma target, and immutable master hash.
5. Classify existing local changes as overlapping vs. known unrelated; preserve unrelated changes without using them as a generic blocker.
6. Execute the bounded DIRECTV delivery package through its acceptance gate.
7. Stop at package completion or a genuine blocker.

Update this canon only when the accepted product state, active target, or product boundary actually changes.
