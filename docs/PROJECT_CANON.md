# Figma Layer Decomposer — Project Canon

## Purpose

Canonical continuity handoff for the Figma Layer Decomposer project.

## Authority order

When sources conflict, use this order:

1. **Immutable master PNG** — visual acceptance authority.
2. `docs/CLEAN_PLATE_CONTRACT.md` — clean-plate implementation contract.
3. `schema/layer-manifest.schema.json` — machine-readable manifest contract.
4. This file — current project state, accepted decisions, roadmap, and next step.
5. Notion / ChatGPT Project copies — convenience only.

Do not infer approval from artifact existence.

## Mission

Turn approved flat mock-up PNGs into genuinely editable layered Figma compositions while preserving 1:1 visual fidelity to the immutable master.

## Core rules

- Do not redesign, reinterpret, beautify, or improve approved mock-ups.
- Preserve untouched source pixels exactly wherever possible.
- Use hybrid decomposition: photographic/environmental content stays raster; editable text/UI/vectors are rebuilt natively in Figma.
- Source recovery comes before extraction or reconstruction.
- Figma is the destination/composition layer, not the raster reconstruction engine.
- Every raster layer uses deterministic coordinates and machine-readable evidence.
- No Figma promotion until automated QA and human visual QA pass.
- Later stages may not repair failed earlier stages.
- One bounded operation → validate → stop.
- Prefer deterministic scripting, source recovery, masks, pixel diffs, and repeatable tooling over manual approximation.
- Clean-plate reconstruction remains fallback infrastructure for hidden background/environment pixels.

## Repository

- Repository: `https://github.com/jimmarkunas/figma-layer-decomposer`
- Default branch: `main`
- Active implementation branch: `feature/3b2-directv-portrait-candidate`
- Local path: `/Users/jimmarkunas/Development/Jim/figma-layer-decomposer`

## Figma

- File: `https://www.figma.com/design/3ZYkEtZVyRH9B2DfVpersf/JM-Personal-Brand-V2?node-id=240-4`
- File key: `3ZYkEtZVyRH9B2DfVpersf`
- Page: `999-1 Asset Rebuild`
- Reference frame: `240:4 — 00_Master_Reference`
- Editable frame: `240:5 — Editable Master Reference 01 — Layered`
- Canvas: `1586 × 992`

## Immutable DIRECTV master

- Local path: `input/directv-hero-01/master.png`
- Dimensions: `1586 × 992`
- SHA-256: `d5a66264cc44c449f0e29d045d729c81fe51564b768b371fd9544b34b60f22e6`

## Accepted Figma top-level structure

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

## Source-first classification model

`docs/SOURCE_ASSET_RECOVERY.md` is mandatory before extraction/reconstruction decisions.

Every material layer has exactly one primary implementation classification:

- `RECOVER_SOURCE`
- `EXTRACT_FROM_MASTER`
- `REBUILD_RASTER_FROM_SOURCE`
- `REBUILD_NATIVE`
- `RECONSTRUCT_HIDDEN_PIXELS`

`REBUILD_RASTER_FROM_SOURCE` is used when a trustworthy related source exists, the approved mock-up was derived from it, but the flattened master cannot contain the complete independent foreground layer because of occlusion.

## DIRECTV approved decomposition classification

- Background/environment — `RECONSTRUCT_HIDDEN_PIXELS` only for genuinely hidden pixels exposed by approved foreground removal; already-visible background remains exact master pixels.
- Portrait — `REBUILD_RASTER_FROM_SOURCE`.
- TV hardware — `EXTRACT_FROM_MASTER`.
- TV screen content — `EXTRACT_FROM_MASTER`.
- Phone hardware — `EXTRACT_FROM_MASTER`.
- Phone screen content — `EXTRACT_FROM_MASTER`.
- Header/navigation — `REBUILD_NATIVE`.
- Hero copy/CTA — `REBUILD_NATIVE`.
- Metrics — `REBUILD_NATIVE`.
- Wall slogan — `REBUILD_NATIVE`.
- Wall underline — `REBUILD_NATIVE`.
- Process strip — `REBUILD_NATIVE`.
- Bottom signature — `REBUILD_NATIVE`.

Canonical plan: `docs/DIRECTV_DECOMPOSITION_PLAN.md`.
Structured mirror: `examples/directv/decomposition-plan.json`.

## Portrait reclassification decision

Earlier portrait classification `EXTRACT_FROM_MASTER` is superseded.

User-supplied provenance establishes that the DIRECTV portrait was derived from the user's website portrait. SR-2 showed only that the website candidates were not provably the exact final standalone DIRECTV asset; it did not mean they were unrelated.

Extraction is insufficient because TV/phone occlusion hides part of the portrait. A crop from the master cannot produce the complete independent portrait layer required by the product.

Therefore the portrait remains `REBUILD_RASTER_FROM_SOURCE`.

The immutable DIRECTV master remains the exact visual target for visible identity, pose, crop, clothing treatment, lighting, and placement. Newly reconstructed portrait content is allowed only where the complete standalone portrait is hidden by TV/phone occlusion.

After human approval, portrait occupancy/alpha is derived from the approved rebuilt portrait itself. Do not generate another portrait-removal mask first.

## PR-1 deterministic rebuild result — FAIL

PR-1 attempted exactly one deterministic source-guided standalone portrait candidate using affine scale/translation from the website portrait.

Recorded result:

- source: `hero-jim-01-cutout-v2.png`
- source SHA-256: `06294961581f4fd3a0b08dae8af3eacf7c05e2efb3d61fe72fb517abe2995100`
- candidate SHA-256: `00957d6b3d12fa1ac590e2737f2a21cfe8619d7711e06e76e063cd5354221ea5`
- transform: scale `0.2046033889`, translation `(528.4569, 9.2964)`, rotation `0°`, Pillow BILINEAR affine
- alpha bbox: `x=635 y=71 width=578 height=557`
- visible pixels compared: `87959`
- visible mismatches: `40395`
- mean absolute error: `30.34`
- max error: `249`
- master unchanged: `true`
- automated gate: `FAIL`
- human gate: `PENDING`
- promotion status: `NOT_PROMOTED`
- evidence: `runs/directv-portrait-rebuild-20260920T082824Z/`

Conclusion: the website portrait is a valid related source, but simple deterministic affine alignment is not sufficient to reproduce the approved DIRECTV portrait. Do not iterate affine tweaks, source-candidate bake-offs, or another deterministic alignment loop.

## PR-1B source-guided portrait reconstruction

PR-1B is the next authorized portrait stage under `docs/DIRECTV_PORTRAIT_SOURCE_GUIDED_RECONSTRUCTION_CONTRACT.md`.

PR-1B must produce exactly one complete standalone RGBA portrait by using:

1. `hero-jim-01-cutout-v2.png` as the pinned identity/source reference;
2. the immutable DIRECTV master as the exact visible appearance target.

The reconstruction may synthesize portrait content only where TV/phone occlusion hides the required standalone portrait. The visible face, hair, pose, crop, jacket/clothing treatment, lighting, scale, and placement must remain constrained to the approved master.

PR-1B is not permission to redesign the portrait, generate background, alter devices/UI, run another removal-mask strategy, or mutate Figma.

One candidate only. If it fails automated or human QA, stop and reassess before any second candidate.

## LOCK #5 — approved standalone portrait

Candidate #5 is the explicitly user-approved standalone DIRECTV portrait asset:

- path: `runs/directv-pr1b-candidate5/portrait-candidate.png`
- SHA-256: `50a24aa6ccffd5ea99e1d7c4247786830666530a09a051f2eb0163ce3fab8326`
- dimensions: `1048 × 1501`
- mode: `RGBA`
- alpha bbox: `x=80 y=37 width=805 height=1464`

This explicit product decision locks candidate #5 despite the prior strict visible-face parity conflict against the immutable master. That fidelity criterion was the source of candidate churn and is superseded for standalone portrait asset selection by the user's LOCK #5 approval. The portrait remains a `REBUILD_RASTER_FROM_SOURCE` asset, approved by explicit user decision.

All further portrait generation and candidate iteration is stopped. Candidates #6 and #7 are rejected and irrelevant. The portrait stage is no longer “generate another portrait.” The next allowed portrait operation is to derive occupancy/alpha from this approved portrait asset and prepare its promotion/use in subsequent decomposition stages.

## Rejected portrait paths

The following remain rejected for production use:

- initial GrabCut portrait mask;
- semantic portrait mask candidate `65f996ccb4bb7d1e1f7ab98ea94b11866005b8b578c95d818767be3e23ad7acd`;
- source-proxy mask candidate;
- subtractive semantic correction candidate `cd450e0e01426f48a071e69f56de5289705ac814db32ab116e7d7b79e315f74d`;
- any new portrait-removal-mask loop before portrait rebuild approval;
- further affine/source-candidate tuning after the accepted PR-1 FAIL.

## Completed architecture / infrastructure

- M2 Structure — COMPLETE.
- 3A Removal geometry — PASS.
- 3A.1 Remove unapproved wall patches — PASS.
- 3B.0 Clean-plate contract + repo bootstrap — COMPLETE.
- 3B.1 Deterministic clean-plate engine — COMPLETE as fallback infrastructure.
- SR-1 Source asset inventory — COMPLETE.
- SR-2 Provenance/exact-match verification — COMPLETE; website portrait candidates were inconclusive as exact final assets.
- SR-3 Per-layer classification — COMPLETE, amended for portrait.
- SR-4 Decomposition-plan approval — PASS, amended for portrait.
- ARC-1 Architecture checkpoint — PASS WITH MINIMAL ARCHITECTURE ADDITION.
- EX-0 Deterministic master-pixel extraction engine — COMPLETE.
- PR-1 deterministic source-guided portrait rebuild — COMPLETE WITH AUTOMATED FAIL; no promotion.

EX-0 accepted commits:

- `1c3767561d39f503fc41cdc3eb804d31099fbb67`
- `e2e433f848b7e83cfc86ca9a1ec9b7c6e30989d2`

Accepted EX-0 validation: 17 full tests passed, 6 extraction tests passed, synthetic smoke PASS, RGB mismatches 0, alpha mismatches 0, source unchanged true, `git diff --check` PASS.

## Approved DIRECTV geometry

All coordinates are relative to the `1586 × 992` master.

Portrait:
- core: `x=620 y=78 w=382 h=717`
- surrounding QA/reconstruction zone: `x=596 y=54 w=430 h=765`

TV:
- core: `x=913 y=413 w=544 h=397`
- zone: `x=889 y=389 w=592 h=445`

Phone:
- core: `x=791 y=532 w=132 h=280`
- zone: `x=767 y=508 w=180 h=328`

Wall slogan:
- core: `x=1044 y=190 w=145 h=135`
- zone: `x=1020 y=166 w=193 h=183`

Wall underline:
- core: `x=1060 y=338 w=62 h=5`
- zone: `x=1036 y=314 w=110 h=53`

These are limits/placement references, not blanket authorization to rewrite pixels.

## Cumulative background cleanup rule

Background cleanup remains cumulative once authorized:

`Portrait → TV → Phone → Wall slogan → Wall underline`

The portrait stage consumes approved portrait occupancy derived from the approved standalone portrait asset, not a pre-rebuild segmentation mask.

## Portrait reconstruction QA

`docs/DIRECTV_PORTRAIT_SOURCE_GUIDED_RECONSTRUCTION_CONTRACT.md` governs PR-1B.

At minimum PR-1B requires:

- pinned website source candidate and SHA;
- pinned source repository commit;
- immutable master hash before/after;
- complete standalone RGBA portrait;
- deterministic final placement;
- visible-region comparison against immutable master;
- hidden-region designation limited to TV/phone occlusion;
- candidate/overlay/diff/alpha/report artifacts;
- one candidate only;
- automated gate;
- human gate `PENDING` until review;
- no background reconstruction or Figma mutation before approval.

## Clean-plate QA

For any later authorized background reconstruction stage:

- validate manifest schema;
- validate canvas dimensions/bounds/masks;
- prove zero changed pixels outside the approved reconstruction zone;
- output dimensions equal source dimensions;
- emit candidate, preview, difference, unchanged-region diff, and report;
- fail closed/non-zero on failed automated gate;
- human gate remains `PENDING` until reviewed.

## Workspace isolation

Only `/Users/jimmarkunas/Development/Jim/figma-layer-decomposer` is the writable project root. Parent development folders are containers only and must not become shared mutation roots. Repo-local `AGENTS.md` remains mandatory.

Generated evidence under `runs/` is local evidence and should not be committed.

## Current roadmap

- M2 — Structure — COMPLETE
- 3A / 3A.1 — geometry / patch correction — PASS
- 3B.0 / 3B.1 — clean-plate contract + engine — COMPLETE
- SR-1–SR-4 — COMPLETE, portrait classification amended
- ARC-1 — COMPLETE
- EX-0 — COMPLETE
- PR-1 — deterministic source-guided portrait candidate — COMPLETE / FAIL / NOT PROMOTED
- PR-1B — Produce one source-guided reconstructed DIRECTV portrait candidate — COMPLETE / LOCK #5 APPROVED
- PR-2 — Automated alignment + visible-region fidelity QA — COMPLETE / SUPERSEDED FOR ASSET SELECTION
- PR-3 — Human visual QA of standalone portrait + recomposed view — SUPERSEDED BY EXPLICIT LOCK #5
- **PR-4 — Derive occupancy alpha from locked portrait / prepare promotion handoff — NEXT**
- 3B.2 — Generate portrait-exposed background clean-plate candidate using approved portrait occupancy
- 3B.3 — Automated unchanged-region QA
- 3B.4 — Human background QA
- 3B.5 — Promote approved portrait-stage clean background into Figma only after gates pass
- 3C — TV removal/background reconstruction as still required
- 3D — Phone removal/background reconstruction as still required
- 3E / 3F — wall slogan/underline native rebuild and any required background cleanup
- 3G / 3H — full clean-background QA / final approved background
- 5A–5I — device extraction + QA
- native header/copy/metrics/process/signature rebuilds
- full recomposition QA
- Figma promotion
- DEP-1 dependency pinning before P1 generalization
- P1–P4 generalize/package for mock-ups #2–#6

## Current next step

`PR-4 — Derive portrait occupancy/alpha from the exact SHA-pinned LOCK #5 portrait asset and prepare promotion/use handoff.`

Do not run another portrait segmentation/removal-mask strategy. Do not run clean-plate reconstruction yet. Do not mutate Figma yet. Do not create multiple portrait variants.

## Continuity protocol

At the start of every ChatGPT/Codex session:

1. Read `docs/PROJECT_CANON.md` from `main` first.
2. Read the active feature-branch canon if accepted work is ahead of `main`.
3. Read `docs/SOURCE_ASSET_RECOVERY.md` before extraction/reconstruction decisions.
4. Read the target-specific contract for the active stage.
5. Confirm Git root, branch, working-tree status, issue/roadmap state.
6. Perform one bounded operation, validate it, then stop.

Update this file whenever accepted roadmap state, next step, classification, geometry, architecture, or source-of-truth locations materially change.
