# 3B.2A — DIRECTV Portrait Reconstruction Mask Validation

Status: **NEXT / PENDING**

## Purpose

Validate and promote exactly one trustworthy DIRECTV portrait reconstruction mask before any 3B.2 clean-plate candidate run.

This gate exists because the original GrabCut mask failed human visual review, while a later portrait-overlay candidate appeared materially better but has not been validated or approved as production geometry.

## Authority

Use, in order:

1. immutable DIRECTV master PNG;
2. `docs/CLEAN_PLATE_CONTRACT.md`;
3. `schema/layer-manifest.schema.json`;
4. `docs/PROJECT_CANON.md`;
5. this validation record.

Artifact existence is not approval.

## Fixed portrait geometry

Canvas: `1586 × 992`

Portrait core:

- x=620
- y=78
- width=382
- height=717

Approved reconstruction zone:

- x=596
- y=54
- width=430
- height=765

Halo: `24 px`

## Foreground-preservation rule

At the portrait-removal stage, overlapping TV and phone pixels are foreground and must remain untouched. They are removed later in the cumulative sequence.

The production portrait reconstruction mask therefore must exclude visible TV and phone pixels even where those devices overlap the portrait core or approved reconstruction zone.

## Candidate input

If the later visually successful portrait-overlay artifact still exists in local evidence, it may be evaluated as the primary candidate.

The rejected GrabCut mask must remain rejected and must not be promoted.

If the successful candidate cannot be located as an exact artifact, stop `BLOCKED` rather than recreating it from memory or approximating it.

## Automated validation requirements

The candidate mask must:

- have deterministic provenance/path/hash;
- decode to a single exact alpha/removal mask;
- align to the 1586 × 992 immutable master coordinate system;
- contain no nonzero pixels outside the approved portrait reconstruction zone;
- preserve all visible TV and phone foreground pixels by excluding them from the removal mask;
- avoid known rejected GrabCut contamination such as the concrete/background wedge and geometric torso block;
- contain no hero-copy/text contamination;
- use only intended portrait-removal geometry;
- emit a machine-readable report with mask dimensions, nonzero bounding box, nonzero pixel count, outside-zone pixel count, foreground-exclusion violations, and candidate SHA-256.

Automated validation is necessary but not sufficient.

## Human visual gate

Human review must inspect an overlay of the candidate mask on the immutable master at full resolution.

The reviewer must explicitly confirm:

- head/hair silhouette follows the portrait;
- face/neck/jacket silhouette is coherent;
- no obvious background wedge or unrelated architecture is selected;
- visible TV and phone pixels remain excluded;
- no unrelated text/UI is selected;
- edge geometry is plausible for clean-plate reconstruction.

Human status remains `PENDING` until explicitly reviewed.

## Required evidence

Create a run-specific evidence directory containing at minimum:

- candidate-mask.png
- mask-overlay.png
- mask-only-preview.png
- exclusion-violations.png
- report.json

Do not generate a clean-plate candidate in 3B.2A.

## Promotion rule

A production portrait reconstruction mask may be promoted only if:

1. automated mask validation passes; and
2. human visual gate explicitly passes.

Promotion means copying the exact validated mask bytes to the approved production mask path and recording source path + SHA-256 + promoted path + promoted SHA-256.

Do not alter the mask during promotion.

## Non-scope

Do not:

- run clean-plate reconstruction;
- change portrait classification;
- perform portrait extraction;
- mutate Figma;
- start TV or phone removal;
- create a new segmentation algorithm;
- redesign the mask after validation begins.

## Stop condition

Stop after the candidate mask is either:

- validated and promoted with human gate PASS; or
- rejected / blocked with exact reasons.

Only a promoted PASS mask unlocks 3B.2.
