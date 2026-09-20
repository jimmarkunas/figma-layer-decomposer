# DIRECTV Decomposition Plan

Status: approved plan amended for portrait source-guided rebuild; LOCK #5 approved

## Scope and evidence

This plan classifies the material layers in the immutable DIRECTV hero (`1586 × 992`). The immutable master remains the visual acceptance authority.

SR-1 found no standalone background, TV, phone, or screen source assets. Figma raster children are full-canvas master-pixel views under masks. The background/environment and TV were reported as created from scratch by ChatGPT; no original standalone source was recovered.

SR-2 compared the three canonical portfolio portrait candidates from `jimmarkunas/portfolio` at commit `5af5f3191cdbd26cef48d3290fa1e979b04f0a73`. Those candidates were `INCONCLUSIVE` as exact recovered final portrait assets.

New user-supplied provenance establishes that the DIRECTV portrait was derived from the user's website portrait. Because TV/phone occlusion hides part of the body, `EXTRACT_FROM_MASTER` cannot produce the complete independent portrait layer required for Figma. The portrait classification is therefore amended to `REBUILD_RASTER_FROM_SOURCE`.

## Per-layer classification

| Layer | Source status / evidence | Classification | Bounds / placement | Production mask | Hidden-pixel reconstruction | Figma destination | Confidence / risks |
|---|---|---|---|---|---|---|---|
| Background/environment | No standalone original recovered; visible pixels exist in immutable master | `RECONSTRUCT_HIDDEN_PIXELS` for hidden pixels only | Full canvas `1586×992`; reconstruction zones remain canonical per-target zones | Derived/authorized only after foreground asset approval | Candidate only, limited to pixels exposed by approved foreground removal | `01_BACKGROUND` | Medium; visible master pixels must remain exact |
| Portrait | Website portrait is the documented source relationship; exact final standalone DIRECTV portrait is not recoverable; master portrait is occluded by TV/phone | `REBUILD_RASTER_FROM_SOURCE` | Target core `(620,78,382,717)`; approved surrounding zone `(596,54,430,765)` remains a reconstruction/QA limit, not a crop instruction | Derive occupancy from approved rebuilt portrait asset; do not infer first from a failed segmentation mask | Only portrait content hidden by TV/phone may be newly reconstructed; visible target appearance must be validated against master | `02_PORTRAIT` | High that extraction is insufficient; rebuild must pass visible-region and full-composite QA |
| TV hardware | No standalone source recovered; Figma node `246:12` is full-canvas master pixels under a mask | `EXTRACT_FROM_MASTER` | Core `(913,413,544,397)` | Required | Background behind TV is separate | `03_DEVICES` | High for visible extraction; device overlap boundaries require QA |
| TV screen content | No standalone source recovered; Figma node `246:15` is full-canvas master pixels under a mask | `EXTRACT_FROM_MASTER` | Within TV core; exact sub-bounds require mask audit | Required | Background behind screen is separate | `03_DEVICES` | Medium; screen/hardware mask relationship must be preserved |
| Phone hardware | No standalone source recovered; Figma node `246:18` is full-canvas master pixels under a mask | `EXTRACT_FROM_MASTER` | Core `(791,532,132,280)` | Required | Background behind phone is separate | `03_DEVICES` | High for visible extraction; preserve overlap order |
| Phone screen content | No standalone source recovered; Figma node `246:21` is full-canvas master pixels under a mask | `EXTRACT_FROM_MASTER` | Within phone core; exact sub-bounds require mask audit | Required | Background behind screen is separate | `03_DEVICES` | Medium; screen/hardware mask relationship must be preserved |
| Header/navigation | Native text/UI/vector content intended to be editable | `REBUILD_NATIVE` | Header region; exact bounds from Figma audit | No raster extraction mask | No | `04_HEADER` | High; typography and spacing require native QA |
| Hero copy / CTA | Native typography and button/UI content | `REBUILD_NATIVE` | Left hero-copy region; exact bounds from Figma audit | No raster extraction mask | No | `05_HERO_COPY` | High; preserve hierarchy and overlap semantics |
| Metrics | Native metric text/dividers | `REBUILD_NATIVE` | Metrics region; exact bounds from Figma audit | No raster extraction mask | No | `06_METRICS` | High; numeric typography/dividers require native QA |
| Wall slogan | Native typography | `REBUILD_NATIVE` | Core `(1044,190,145,135)` | No raster extraction mask | No | `07_WALL_MESSAGE` | High; visible slogan may overlap raster layers |
| Wall underline | Native vector/divider | `REBUILD_NATIVE` | Core `(1060,338,62,5)` | No raster extraction mask | No | `07_WALL_MESSAGE` | High; preserve exact position/stroke appearance |
| Process strip | Native icons, labels, arrows, and dividers where possible | `REBUILD_NATIVE` | Bottom process-strip region; exact bounds from Figma audit | No raster extraction mask | No | `08_PROCESS_STRIP` | Medium; icon/vector details require audit |
| Bottom signature | Native text and accent line | `REBUILD_NATIVE` | Bottom-right signature region; exact bounds from Figma audit | No raster extraction mask | No | `09_BOTTOM_SIGNATURE` | Medium; typography/line placement require QA |

## Portrait rebuild contract

Portrait implementation is governed by `docs/DIRECTV_PORTRAIT_REBUILD_CONTRACT.md`.

Key rule: the rebuild exists to create a complete standalone portrait layer. It must not replace already-approved visible appearance casually. Visible target regions are validated against the immutable master; newly reconstructed portrait content is allowed only where TV/phone occlusion prevents recovery from the master.

The approved rebuilt portrait, not a rejected segmentation mask, becomes the source for portrait occupancy geometry used by later background reconstruction.

## Classification groups

### Source-guided raster rebuild

Portrait uses `REBUILD_RASTER_FROM_SOURCE` because a complete independent portrait is required and the flattened master is occluded.

### Extraction candidates

TV hardware, TV screen content, phone hardware, and phone screen content remain `EXTRACT_FROM_MASTER` for visible pixels. Foreground extraction is distinct from reconstruction of hidden background pixels.

### Reconstruction authorization candidates

Only hidden background/environment pixels exposed by approved foreground removal may use `RECONSTRUCT_HIDDEN_PIXELS`.

### Native rebuild candidates

Header/navigation, hero copy/CTA, metrics, wall slogan, wall underline, process strip, and bottom signature use `REBUILD_NATIVE`.

## Rejected portrait-mask paths

The following are not approved production inputs:

- initial GrabCut portrait mask;
- semantic portrait mask candidate;
- source-proxy mask attempt;
- subtractive semantic correction attempt.

Do not generate another portrait removal mask before the standalone portrait rebuild is complete and human-approved.

## Current execution order

1. Canonize portrait reclassification and rebuild contract.
2. Produce one source-guided full portrait candidate.
3. Validate alignment and visible-region fidelity against the immutable master.
4. Lock candidate #5 by explicit user decision; no further portrait candidate generation.
5. Derive portrait occupancy/alpha from the locked portrait asset.
6. Resume portrait-exposed background clean-plate reconstruction using that approved occupancy geometry.
7. Continue TV → Phone → native rebuilds → full recomposition QA → Figma promotion.

No Figma promotion is implied by any intermediate artifact.
