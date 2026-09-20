# DIRECTV PR-1B Candidate #1 Reassessment

Status: completed reassessment after PR-2 automated FAIL. This document does not authorize a second candidate by itself.

## 1. Purpose

Explain why PR-1B candidate #1 failed and define the bounded correction strategy required before any candidate #2 generation.

This reassessment is subordinate to:

1. the immutable DIRECTV master;
2. `docs/DIRECTV_PORTRAIT_SOURCE_GUIDED_RECONSTRUCTION_CONTRACT.md`;
3. `docs/SOURCE_ASSET_RECOVERY.md`;
4. `docs/PROJECT_CANON.md`.

No image generation, Figma mutation, background reconstruction, segmentation, or new removal-mask work is authorized by this document.

## 2. Candidate #1 evidence

Candidate SHA-256:

`7e0dff885056dcab3d0a3995f7c86ffb0eccdce38c4b2d9af17ded970fd1864f`

PR-2 verified:

- immutable master SHA before/after unchanged;
- candidate SHA exact;
- output canvas `1586 × 992`;
- candidate alpha bbox before alignment: `x=65 y=21 w=1275 h=1003`;
- alpha-bbox aspect ratio: approximately `1.271`;
- approved portrait core: `x=620 y=78 w=382 h=717`;
- approved core aspect ratio: approximately `0.533`;
- approved QA zone: `x=596 y=54 w=430 h=765`;
- QA-zone aspect ratio: approximately `0.562`.

The first deterministic placement scaled candidate #1 uniformly by height to `717 px`. That produced an aligned alpha footprint approximately `911 × 717`, with `84,210` non-occluded portrait pixels outside the approved QA zone.

PR-2 therefore correctly returned automated `FAIL` and `NOT_PROMOTED`.

## 3. Root cause

Candidate #1 is not merely mis-positioned. Its generated portrait composition has the wrong foreground footprint for the approved master.

The immutable master uses a narrow, vertically oriented portrait silhouette. Candidate #1 uses a much broader torso/shoulder composition. The candidate alpha footprint is more than twice the approved portrait aspect ratio.

A uniform scale cannot simultaneously match the approved portrait height and width:

- fitting candidate #1 by approved height produces a portrait about `911 px` wide;
- fitting candidate #1 by approved width produces a portrait only about `301 px` high.

Therefore candidate #1 cannot be made contract-compliant by translation plus uniform scale.

The following are explicitly rejected as corrections:

- non-uniform stretching/squashing;
- arbitrary cropping that changes the approved pose/crop;
- masking away excess body solely to force geometry compliance;
- another affine-tuning loop;
- relaxing the approved portrait QA zone;
- treating the failed placement as permission to alter the immutable master.

Those approaches would repair the QA result rather than reconstruct the approved portrait.

## 4. Candidate #2 correction strategy

Any candidate #2 must be generated as a new source-guided reconstruction whose portrait composition is constrained to the approved master before post-generation alignment.

### 4.1 Foreground-only requirement

Candidate #2 must contain exactly one complete portrait on transparency.

It must not contain:

- background/environment;
- TV;
- phone;
- UI;
- wall content;
- text;
- halo/glow/environmental lighting pixels unrelated to the portrait.

### 4.2 Master-constrained pose and framing

The immutable master remains the exact visible target for:

- face identity and expression;
- head angle;
- hair/head silhouette;
- shoulder angle;
- body orientation;
- jacket/collar silhouette;
- visible crop;
- lighting and monochrome treatment.

Candidate #2 must reproduce the narrow master portrait composition rather than a generic broad studio bust.

### 4.3 Alpha-footprint constraint

Before any deterministic placement, candidate #2's non-transparent alpha bbox must be vertically narrow enough to fit the approved portrait geometry under uniform scaling.

Target portrait-core aspect ratio:

`382 / 717 = 0.5328...`

Maximum QA-zone aspect ratio:

`430 / 765 = 0.5620...`

Candidate #2 should target the approved core aspect ratio and must not require non-uniform scaling to fit the QA zone.

Mechanical preflight for candidate #2:

- alpha bbox exists;
- transparent and non-transparent pixels both exist;
- alpha-bbox aspect ratio is compatible with uniform scale into the approved QA zone;
- after uniform scale and deterministic placement, non-occluded alpha does not extend outside the approved QA zone.

Failure of that preflight stops PR-2 before fidelity scoring.

### 4.4 Deterministic placement rule

Candidate #2 may be post-processed only with deterministic operations that preserve portrait proportions:

1. crop transparent padding to the candidate alpha bbox;
2. uniform scale only;
3. deterministic translation only;
4. no perspective warp;
5. no non-uniform resize;
6. no geometry-repair masking.

The target placement remains constrained by the approved master portrait geometry, not by whichever transform yields the lowest pixel-diff score.

### 4.5 Hidden-region allowance

Only portrait content hidden by the TV/phone in the immutable master may be newly synthesized.

Hidden completion must continue the master-visible pose, jacket/body treatment, and source identity. It must not widen the foreground footprint beyond what the approved pose plausibly requires.

## 5. Candidate #2 acceptance sequence

If candidate #2 is explicitly authorized later, the sequence is:

1. generate exactly one corrected candidate;
2. pin its exact SHA-256;
3. run alpha-footprint/geometry preflight;
4. run deterministic alignment;
5. run visible-region fidelity comparison excluding approved TV/phone occlusion;
6. emit candidate, aligned preview, overlay, visible diff, alpha, and report;
7. automated PASS is required before human PR-3 review;
8. human gate remains `PENDING` until explicit review;
9. promotion remains `NOT_PROMOTED` until both gates pass.

If candidate #2 fails, stop again. Do not create candidate #3 without another explicit reassessment.

## 6. Current state

- PR-1B candidate #1: produced, SHA pinned, automated PR-2 `FAIL`, `NOT_PROMOTED`.
- Root cause: generated portrait footprint/pose framing materially diverges from the approved master geometry; this is not a simple placement error.
- Candidate #2 generation: **NOT RUN**.
- Figma mutation: **NONE**.
- Background reconstruction: **NONE**.
- Human gate: `PENDING`.

## 7. Next bounded action

Review/authorize the candidate #2 correction strategy. Only after explicit authorization may exactly one second source-guided portrait candidate be generated under these constraints.
