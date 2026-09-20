# DIRECTV Portrait Rebuild Contract

Status: canonical implementation contract for the standalone DIRECTV portrait layer

## 1. Purpose

Create a complete standalone portrait raster for the DIRECTV hero that can exist independently beneath the TV/phone layers while preserving the approved master appearance.

This is not a crop of the flattened master and not another portrait-removal-mask experiment.

The immutable DIRECTV master remains the visual acceptance authority.

## 2. Classification

Portrait classification: `REBUILD_RASTER_FROM_SOURCE`.

Reason:

- the DIRECTV portrait was derived from the user's website portrait;
- no exact final standalone DIRECTV portrait asset is recoverable;
- TV/phone occlusion hides part of the portrait in the master;
- therefore `EXTRACT_FROM_MASTER` cannot produce the complete independent layer required by the product.

## 3. Inputs

Authoritative target:

- immutable DIRECTV master: `input/directv-hero-01/master.png`
- dimensions: `1586 × 992`
- SHA-256: `d5a66264cc44c449f0e29d045d729c81fe51564b768b371fd9544b34b60f22e6`

Source guidance:

- canonical website portrait candidates from `jimmarkunas/portfolio` pinned at commit `5af5f3191cdbd26cef48d3290fa1e979b04f0a73`
- exact candidate bytes/paths must be recorded in the run report before use
- these candidates are not `RECOVER_SOURCE`; they are source guidance for the rebuild

## 4. Target placement

Portrait target core:

- `x=620`
- `y=78`
- `width=382`
- `height=717`

Approved surrounding QA/reconstruction zone:

- `x=596`
- `y=54`
- `width=430`
- `height=765`

The surrounding zone is not a crop instruction and does not authorize changing unrelated pixels.

## 5. Rebuild rule

The output must be a complete RGBA portrait layer with transparent background.

The rebuild may reconstruct portrait content only where the final standalone portrait is hidden by TV/phone occlusion in the immutable master.

Where the portrait is visibly represented in the immutable master, the rebuilt asset must be aligned and validated against that visible target appearance.

Do not redesign the person, clothing, pose, lighting, crop, or styling.

Do not use rejected portrait-removal masks as geometry authority.

## 6. Visible-region fidelity

The visible portrait region is the acceptance anchor.

Automated QA must compare the rebuilt-and-aligned portrait against the immutable master in portrait-visible regions that are not covered by known foreground devices/UI.

The report must distinguish:

- visible target pixels used for fidelity checking;
- device-occluded portrait regions where new portrait content is permitted;
- transparent/non-portrait regions.

A candidate that materially changes the visible approved portrait fails, even if the hidden completion looks plausible.

## 7. Hidden-region allowance

Newly reconstructed portrait content is permitted only behind foreground occlusion where the complete standalone portrait requires content that cannot be recovered from the master.

The hidden completion must be visually consistent with the source portrait and the visible DIRECTV portrait, but it is not required to reproduce unknowable original hidden pixels exactly.

This allowance applies to the portrait asset only. It does not authorize background clean-plate generation.

## 8. Occupancy geometry

Do not generate another portrait removal mask first.

After a portrait candidate passes automated and human QA, derive portrait occupancy/alpha geometry from the approved standalone portrait asset itself.

That approved geometry may then be used as the portrait foreground footprint for later background reconstruction, subject to clean-plate contract gates.

## 9. Required outputs

Each portrait rebuild run must emit at least:

- `portrait-candidate.png` — complete standalone RGBA portrait
- `portrait-aligned-preview.png` — candidate positioned at target placement
- `portrait-master-overlay.png` — visual comparison against immutable master
- `portrait-visible-diff.png` — visible-region comparison artifact
- `portrait-alpha.png` — candidate alpha/occupancy preview
- `report.json` — machine-readable provenance and QA report

Generated evidence belongs under `runs/` and is not committed.

## 10. Required report fields

`report.json` must record at least:

- stage identifier;
- source candidate path/identifier;
- source candidate SHA-256;
- source repository and pinned commit;
- master path and SHA-256 before/after;
- target placement;
- output dimensions;
- portrait candidate SHA-256;
- visible-region comparison method;
- visible-region mismatch metrics;
- hidden-region designation;
- master unchanged boolean;
- automated gate result;
- human gate result;
- promotion status.

Human gate remains `PENDING` until reviewed.

## 11. Automated fail conditions

Fail closed if any of the following occurs:

- master hash changes;
- source candidate/provenance is not recorded;
- output is not RGBA with transparent non-portrait background;
- output placement is not deterministic;
- the candidate materially alters visible approved portrait appearance beyond the documented acceptance tolerance;
- new portrait content appears outside the portrait footprint without justification;
- the run uses a rejected prior mask as geometry authority;
- the run proceeds to background reconstruction or Figma promotion before human QA.

## 12. Human QA

Human review must confirm:

- identity and face match the approved master;
- pose/crop match the approved master;
- visible clothing/body appearance matches the approved master;
- edges are natural and do not include unrelated UI/device/background pixels;
- hidden completion is plausible and consistent with the source/visible portrait;
- toggling the portrait independently would produce the intended layer behavior.

## 13. Promotion gate

Only after automated PASS and explicit human PASS may the portrait candidate be treated as the approved standalone portrait asset.

Only then may its alpha/occupancy be used to authorize the portrait-exposed background reconstruction stage.

No Figma mutation occurs under this contract until the approved portrait asset and later background stage both satisfy their own promotion gates.
