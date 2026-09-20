# DIRECTV Source-Guided Portrait Reconstruction Contract

Status: canonical implementation contract for PR-1B; candidate selection LOCK #5 APPROVED

## 1. Purpose

Create exactly one complete standalone DIRECTV portrait RGBA asset by reconstructing from the user's website portrait source relationship while using the immutable DIRECTV master as the visual acceptance target.

This stage exists because PR-1 proved that simple deterministic affine alignment of the website portrait is insufficient.

This is not:

- another portrait-removal-mask experiment;
- a crop from the flattened master;
- background reconstruction;
- device reconstruction;
- a redesign of the approved portrait.

## 2. Preconditions

PR-1 is complete with automated FAIL.

Recorded PR-1 evidence:

- source: `hero-jim-01-cutout-v2.png`
- source SHA-256: `06294961581f4fd3a0b08dae8af3eacf7c05e2efb3d61fe72fb517abe2995100`
- candidate SHA-256: `00957d6b3d12fa1ac590e2737f2a21cfe8619d7711e06e76e063cd5354221ea5`
- transform: scale `0.2046033889`, translation `(528.4569, 9.2964)`, rotation `0°`
- visible pixels compared: `87959`
- visible mismatches: `40395`
- mean absolute error: `30.34`
- max error: `249`
- master unchanged: `true`
- automated gate: `FAIL`
- evidence directory: `runs/directv-portrait-rebuild-20260920T082824Z/`

The failure establishes that the website source is related but cannot be reproduced to the approved DIRECTV portrait by deterministic scale/translation alone.

## 3. Classification

Portrait remains `REBUILD_RASTER_FROM_SOURCE`.

PR-1B changes the implementation method within that classification from deterministic affine alignment to source-guided portrait reconstruction.

The immutable master remains the visual acceptance authority.

## 4. Inputs

Authoritative target:

- `input/directv-hero-01/master.png`
- dimensions: `1586 × 992`
- SHA-256: `d5a66264cc44c449f0e29d045d729c81fe51564b768b371fd9544b34b60f22e6`

Source identity/reference:

- `hero-jim-01-cutout-v2.png`
- SHA-256: `06294961581f4fd3a0b08dae8af3eacf7c05e2efb3d61fe72fb517abe2995100`
- source repository: `jimmarkunas/portfolio`
- pinned commit: `5af5f3191cdbd26cef48d3290fa1e979b04f0a73`

No other portrait source may be substituted in PR-1B without explicit approval.

## 5. Target geometry

Portrait target core:

- `x=620`
- `y=78`
- `width=382`
- `height=717`

Surrounding QA zone:

- `x=596`
- `y=54`
- `width=430`
- `height=765`

Known foreground occlusion:

TV core:
- `x=913 y=413 w=544 h=397`

Phone core:
- `x=791 y=532 w=132 h=280`

## 6. Reconstruction rule

Produce one complete standalone RGBA portrait with transparent background.

The reconstruction must use both:

1. the website portrait as the source identity/reference;
2. the immutable DIRECTV master as the exact visible target for identity, face, hair, pose, crop, jacket/clothing treatment, lighting, scale, and placement.

New portrait content is permitted only where the complete standalone portrait is hidden by TV/phone occlusion in the master.

Do not redesign, beautify, restyle, or reinterpret the subject.

Do not alter unrelated background, UI, TV, phone, wall content, or typography.

## 7. Visible-region fidelity rule

Visible portrait pixels in the immutable master are the acceptance anchor.

PR-1B must generate evidence comparing the reconstructed-and-aligned portrait to the master in portrait-visible regions not covered by known foreground devices/UI.

The visible portion should be treated as constrained reconstruction, not free generation.

A plausible portrait that materially differs from the approved master fails.

## 8. Hidden-region allowance

Only the portrait content behind TV/phone occlusion may be newly synthesized where the original standalone pixels are unknowable.

Hidden completion must be consistent with:

- the website source;
- the visible DIRECTV portrait;
- the approved pose and clothing treatment.

Hidden completion does not need to reproduce unknowable original hidden pixels exactly.

## 9. One-candidate rule

PR-1B is a one-candidate implementation package.

Do not create:

- candidate variants;
- model bake-offs;
- prompt sweeps;
- mask experiments;
- manual retouch variants.

If the first bounded reconstruction fails visual QA, stop and reassess before any second candidate.

## 10. Required outputs

Emit one run-specific evidence directory containing at minimum:

- `portrait-candidate.png`
- `portrait-aligned-preview.png`
- `portrait-master-overlay.png`
- `portrait-visible-diff.png`
- `portrait-alpha.png`
- `report.json`

`portrait-candidate.png` must be a complete standalone RGBA portrait with transparent non-portrait background.

## 11. Required report fields

`report.json` must include at minimum:

- stage: `PR-1B`;
- classification: `REBUILD_RASTER_FROM_SOURCE`;
- reconstruction method/tool/model identifier;
- exact source path and SHA-256;
- source repository and pinned commit;
- immutable master path and SHA-256 before/after;
- target placement;
- output dimensions;
- candidate SHA-256;
- visible-region comparison method;
- visible-region pixel count;
- visible-region mismatch metrics;
- hidden-region designation;
- master unchanged boolean;
- automated gate;
- human gate = `PENDING`;
- promotion status = `NOT_PROMOTED`.

## 12. Automated fail conditions

Fail closed if any of the following occurs:

- immutable master hash changes;
- source provenance is not recorded;
- output is not complete RGBA with transparent background;
- reconstruction includes TV, phone, UI, or environment pixels;
- new portrait content appears outside the portrait footprint without justification;
- visible target fidelity materially diverges from the immutable master;
- rejected prior masks are used as geometry authority;
- more than one candidate is produced;
- the stage proceeds into background reconstruction or Figma mutation.

## 13. Human QA

Human review must confirm:

- face/identity match the approved master;
- hair/head silhouette match the approved master;
- pose and crop match the approved master;
- jacket/clothing/body treatment match the approved master;
- edges are natural and contain no unrelated composition pixels;
- hidden TV/phone-covered body completion is plausible and consistent;
- the portrait can function as an independent toggleable Figma layer.

## 14. Promotion gate

Candidate #5 is approved as the standalone portrait asset by explicit user decision:

- path: `runs/directv-pr1b-candidate5/portrait-candidate.png`
- SHA-256: `50a24aa6ccffd5ea99e1d7c4247786830666530a09a051f2eb0163ce3fab8326`
- human gate for portrait asset selection: `PASS`
- promotion status: `NOT_PROMOTED` until the separate promotion/handoff stage

No further portrait candidate generation, regeneration, retouching, or bake-off is authorized. Any later full-frame fidelity discussion must not reopen portrait-candidate generation unless explicitly authorized by the user.

Portrait occupancy/alpha must now be derived from the exact approved portrait asset itself for the next promotion/use handoff. Only after that downstream gate may the derived occupancy be used for later portrait-exposed background reconstruction.

No background clean plate or Figma mutation is authorized by PR-1B itself.
