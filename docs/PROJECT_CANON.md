# Figma Layer Decomposer — Project Canon

## Purpose

This file is the canonical continuity handoff for the Figma Layer Decomposer project. It exists so ChatGPT, Codex, local development sessions, and future conversations can recover the current state without relying on one chat transcript.

## Authority order

When sources conflict, use this order:

1. **Immutable master PNG** — visual acceptance authority for reconstruction fidelity.
2. The current bounded GitHub implementation issue for the active operation.
3. `docs/CLEAN_PLATE_CONTRACT.md` when hidden-background reconstruction is actually in scope.
4. `schema/layer-manifest.schema.json` for machine-readable placement/QA contracts.
5. This file — current accepted project state, boundaries, and next step.
6. Notion index / ChatGPT Project uploads — pointers only.

Do not infer approval from the mere existence of an artifact.

## Mission

Turn approved flat mock-up PNGs into genuinely editable layered Figma compositions while preserving 1:1 visual fidelity to the immutable master image, then emit a bounded `PROMOTION_READY` handoff to Personal Career Brand / PBDS.

The project owns source recovery, decomposition, faithful raster/native reconstruction, fidelity QA, and the staging Figma composition. It does **not** own the canonical Personal Brand design system, semantic template contract, React rendering, or PowerPoint rendering.

Cross-system flow:

`APPROVED CONCEPT PNG → SOURCE RECOVERY / DECOMPOSITION → 1:1 EDITABLE FIGMA → PROMOTION_READY → PBDS CANONICAL FIGMA PROMOTION → SEMANTIC CONTRACT → REACT / POWERPOINT`

## Hard anti-spin rule

The project is now past architecture discovery for the DIRECTV portrait. Do not add another roadmap rewrite, segmentation/mask strategy, model bake-off, decomposition framework, orchestration layer, handoff contract, or governance artifact before the active visual proof completes.

**Current product proof = one source-guided standalone DIRECTV portrait candidate.**

If that candidate fails, the failure may authorize exactly one bounded correction based on the observed defect. It does not authorize a new architecture program.

## Repository and current state

- Repository: `https://github.com/jimmarkunas/figma-layer-decomposer`
- Default branch: `main`
- Main before this canon repair: `ed4e3b86ec942375519d99016d9cd02fb688f3f3`
- Local repository: `/Users/jimmarkunas/Development/Jim/figma-layer-decomposer`
- Current reference: DIRECTV hero, `1586 × 992`
- Current implementation issue: **#11 — PR-1B — Produce source-guided reconstructed DIRECTV portrait candidate**
- Superseded clean-plate issue #4: **CLOSED / NOT PLANNED**
- Mask-first issues #8 and #9: **CLOSED / superseded**
- PR-1 issue #10: **COMPLETE WITH AUTOMATED FAIL** — deterministic affine alignment was insufficient
- Current execution state: **PR-1B ACTIVE — no approved portrait artifact yet**

## Current accepted portrait facts

Pinned source identity/reference:

- `jimmarkunas/portfolio`
- pinned commit `5af5f3191cdbd26cef48d3290fa1e979b04f0a73`
- `public/jim/hero-jim-01-cutout-v2.png`
- SHA-256 `06294961581f4fd3a0b08dae8af3eacf7c05e2efb3d61fe72fb517abe2995100`

Immutable visual target:

- `input/directv-hero-01/master.png`
- `1586 × 992`
- SHA-256 `d5a66264cc44c449f0e29d045d729c81fe51564b768b371fd9544b34b60f22e6`

Portrait geometry:

- target core: `x=620 y=78 w=382 h=717`
- QA zone: `x=596 y=54 w=430 h=765`
- TV core: `x=913 y=413 w=544 h=397`
- Phone core: `x=791 y=532 w=132 h=280`

The website portrait is a valid related source but is not pixel-identical to the approved DIRECTV portrait. PR-1 proved a deterministic affine transform is insufficient: its single candidate failed automated visible-region fidelity QA. Do not continue affine tuning.

The portrait implementation classification is therefore **`REBUILD_RASTER_FROM_SOURCE`** for the complete standalone portrait: use the pinned website portrait as identity/source reference and the immutable DIRECTV master as the visible target. Newly synthesized portrait content is permitted only where TV/phone occlusion hides portrait pixels required for the complete standalone layer.

## PR-1B execution contract

Issue #11 is the bounded execution contract for the active operation.

Produce exactly one complete portrait RGBA candidate and evidence package under one run-specific `runs/` directory:

- `portrait-candidate.png`
- `portrait-aligned-preview.png`
- `portrait-master-overlay.png`
- `portrait-visible-diff.png`
- `portrait-alpha.png`
- `report.json`

The report must identify the exact reconstruction method/tool/model, pinned source/provenance, master and candidate hashes, deterministic placement, visible-region comparison, hidden-region designation, automated gate, `human_gate = PENDING`, and `promotion_status = NOT_PROMOTED`.

Fail closed if the master changes, provenance is missing, the output is not complete RGBA with transparency, device/UI/environment pixels contaminate the portrait, visible fidelity materially diverges, more than one candidate is generated, or work proceeds into background reconstruction/Figma mutation.

Stop after the one candidate and evidence package. Human review decides the next stage.

## Explicit PR-1B non-scope

Do not:

- generate a second candidate;
- run a prompt/model sweep;
- restart GrabCut/semantic/matting/removal-mask experiments;
- perform clean-plate/background reconstruction;
- extract or rebuild TV/phone;
- mutate Figma;
- promote any asset;
- redesign or beautify the portrait;
- create another architecture/checkpoint/governance document.

## Accepted broader decomposition boundary

Source-first recovery remains mandatory. The prior SR work established these broad implementation directions:

- visible background pixels remain immutable-master pixels;
- hidden background pixels may be reconstructed only where approved foreground removal exposes genuinely hidden content;
- TV/phone visible raster content is handled separately from hidden-background reconstruction;
- header/navigation, hero copy/CTA, metrics, wall message/divider, process strip, and bottom signature are intended as native editable Figma content;
- foreground extraction/rebuild and hidden-background reconstruction are separate operations;
- the rejected GrabCut/semantic/mask-first portrait paths remain rejected.

The existing clean-plate engine remains valid fallback infrastructure. It is not the current portrait solution.

## Figma destinations

Reconstruction workspace:

- `https://www.figma.com/design/3ZYkEtZVyRH9B2DfVpersf/JM-Personal-Brand-V2?node-id=240-4`
- reference frame `240:4 — 00_Master_Reference`
- editable frame `240:5 — Editable Master Reference 01 — Layered`

Accepted top-level groups:

- `00_MASTER_REFERENCE`
- `01_BACKGROUND`
- `02_PORTRAIT`
- `03_DEVICES`
- `04_HEADER`
- `05_HERO_COPY`
- `06_METRICS`
- `07_WALL_MESSAGE`
- `08_PROCESS_STRIP`
- `09_BOTTOM_SIGNATURE`

Canonical Personal Brand Figma / promotion destination:

- `https://www.figma.com/design/euxFg8XeKtFJRw7PWOJRWa/JM-Personal-Brand`

The staging file is not a second design-system authority.

## Promotion boundary

The Decomposer stops at `PROMOTION_READY`:

`RECONSTRUCTION_ACTIVE → PROMOTION_READY → PBDS PROMOTED → CONSUMABLE`

`PROMOTION_READY` requires a genuinely editable DIRECTV composition, full-frame human visual acceptance against the immutable master, required automated QA, linked provenance, exact staging Figma/frame identification, and enough layer-role description for PBDS to evaluate reuse.

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

## Active sequence

1. **PR-1B — ACTIVE:** produce exactly one source-guided reconstructed portrait candidate.
2. Human visual review of that one candidate.
3. If accepted, derive authoritative portrait occupancy/alpha from the approved portrait asset.
4. Resume only the bounded DIRECTV raster/background work needed for the editable composition.
5. Rebuild native text/UI/vector content in Figma.
6. Full-frame 1:1 DIRECTV visual acceptance.
7. Emit `PROMOTION_READY` handoff to PBDS.

No new milestone may be inserted between steps 1 and 2 unless PR-1B itself proves a concrete blocker.

## Current next step

**Execute Issue #11. Produce the portrait.**

No additional documentation/architecture package is the next step.

## Continuity protocol

At the start of a new implementation session:

1. Read this file from current `main`.
2. Read the active GitHub issue (#11 while PR-1B remains active).
3. Read only the exact implementation surface required by that issue.
4. Confirm repository root, fresh main, clean tree, and bounded mutation surface.
5. Execute one bounded product operation and prove it.
6. Stop.

Update this canon only when the accepted product state or active next operation actually changes.