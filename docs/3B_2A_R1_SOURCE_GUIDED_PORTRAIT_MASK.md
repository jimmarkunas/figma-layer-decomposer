# 3B.2A-R1 — Source-guided DIRECTV portrait mask candidate

Status: **AUTHORIZED CANDIDATE-GENERATION SPIKE**

## Purpose

Generate one new portrait reconstruction-mask candidate using the best already-inventoried portrait source asset only as deterministic geometry guidance, then stop for automated and human review.

This is not source recovery and does not change the approved portrait classification from `EXTRACT_FROM_MASTER`.

## Authority and constraints

- Immutable DIRECTV master remains visual authority.
- The prior GrabCut candidate is rejected.
- The prior semantic candidate failed human QA because of torso block geometry, rectangular device cut-outs, and UI contamination.
- Do not repair either failed mask heuristically.
- Do not run clean-plate reconstruction in this spike.
- Do not modify Figma.
- Do not promote any mask without automated PASS and explicit human PASS.

## Allowed guidance source

Use the previously inventoried portfolio portrait candidate:

`public/jim/hero-jim-01-cutout-v2.png`

from `jimmarkunas/portfolio` at pinned commit:

`5af5f3191cdbd26cef48d3290fa1e979b04f0a73`

Recorded SR-2 deterministic transform:

- scale: `0.2046033889`
- translation: `(528.4569, 9.2964)`
- rotation: `0°`

This asset was `INCONCLUSIVE` for exact source recovery. It may be used only as a geometry prior to generate a candidate mask; it must not be treated as exact source pixels or approval evidence.

## Candidate-generation rule

1. Load the cutout alpha exactly.
2. Apply only the recorded SR-2 transform.
3. Rasterize the transformed alpha onto the 1586×992 DIRECTV canvas.
4. Clip to the approved portrait reconstruction zone.
5. Do not dilate, erode, feather, smooth, close, open, simplify, or redraw edges.
6. Do not add rectangular TV/phone exclusions.
7. Preserve the transformed alpha as-is for the candidate.

If the cutout-v2 file cannot be resolved exactly at the pinned portfolio commit, stop `BLOCKED`.

## Validation evidence

Emit a new run directory with:

- `candidate-mask.png`
- `mask-overlay.png`
- `mask-only-preview.png`
- `difference-vs-prior-semantic.png`
- `report.json`

The report must include source asset path, source SHA-256, transform values, mask SHA-256, nonzero bbox/count, pixels outside approved zone, and prior-semantic comparison metrics.

## Automated gate

PASS requires:

- exact pinned source asset resolved;
- transform exactly matches recorded SR-2 values;
- canvas dimensions 1586×992;
- outside-approved-zone pixels = 0;
- immutable master unchanged;
- no heuristic post-processing performed.

Human gate remains `PENDING`.

## Human review

Review against the immutable master at full resolution for:

- head/hair contour;
- face/ear/neck contour;
- jacket shoulder and torso silhouette;
- absence of concrete/background wedge;
- absence of geometric torso blocks;
- absence of UI/text contamination;
- TV/phone overlap plausibility.

Any visible mismatch that would cause background reconstruction to overwrite retained foreground is a human FAIL.

## Stop condition

Stop after one source-guided candidate and its evidence are generated. Do not run clean-plate, promote the mask, or modify Figma.
