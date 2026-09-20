# DIRECTV Decomposition Plan

Status: SR-3 planning artifact — SR-4 approval pending

## Scope and evidence

This plan classifies the material layers in the immutable DIRECTV hero (`1586 × 992`). It does not authorize extraction, reconstruction, Figma mutation, or production promotion.

SR-1 found no standalone background, TV, phone, or screen source assets. Figma raster children are full-canvas master-pixel views under masks. The background/environment and TV were reported as created from scratch by ChatGPT; no original standalone source was recovered.

SR-2 compared the three canonical portfolio portrait candidates from `jimmarkunas/portfolio` at commit `5af5f3191cdbd26cef48d3290fa1e979b04f0a73`. All results were `INCONCLUSIVE`; none is authorized as `RECOVER_SOURCE`. Evidence is retained under `runs/directv-sr2-portrait-20260920T063917Z/`.

## Per-layer classification

| Layer | Source status / evidence | Classification | Bounds / placement | Production mask | Hidden-pixel reconstruction | Figma destination | Confidence / risks |
|---|---|---|---|---|---|---|---|
| Background/environment | No standalone original recovered; visible pixels exist in immutable master | `RECONSTRUCT_HIDDEN_PIXELS` for hidden pixels only | Full canvas `1586×992`; reconstruction zones remain the canonical per-target zones | Required for each authorized removal; not approved | Candidate only, limited to pixels exposed by approved foreground removal | `01_BACKGROUND` | Medium; requires SR-4 authorization and a trustworthy mask; visible master pixels remain exact |
| Portrait | Portfolio candidates exist but SR-2 is inconclusive; Figma portrait is a masked master-pixel view | `EXTRACT_FROM_MASTER` | Core `(620,78,382,717)`; approved zone `(596,54,430,765)` is not an extraction authorization | Required for bounded master-pixel extraction | Separate background pixels behind portrait may be reconstructed only if SR-4 authorizes | `02_PORTRAIT` | High for visible extraction; source provenance unresolved; preserve phone/TV/UI overlaps |
| TV hardware | No standalone source recovered; Figma node `246:12` is full-canvas master pixels under a mask | `EXTRACT_FROM_MASTER` | Core `(913,413,544,397)` | Required | Background behind TV is separate | `03_DEVICES` | High for visible extraction; device overlap boundaries require QA |
| TV screen content | No standalone source recovered; Figma node `246:15` is full-canvas master pixels under a mask | `EXTRACT_FROM_MASTER` | Within TV core; exact sub-bounds require mask audit | Required | Background behind screen is separate | `03_DEVICES` | Medium; screen/hardware mask relationship must be preserved |
| Phone hardware | No standalone source recovered; Figma node `246:18` is full-canvas master pixels under a mask | `EXTRACT_FROM_MASTER` | Core `(791,532,132,280)` | Required | Background behind phone is separate | `03_DEVICES` | High for visible extraction; preserve phone during portrait stage |
| Phone screen content | No standalone source recovered; Figma node `246:21` is full-canvas master pixels under a mask | `EXTRACT_FROM_MASTER` | Within phone core; exact sub-bounds require mask audit | Required | Background behind screen is separate | `03_DEVICES` | Medium; screen/hardware mask relationship must be preserved |
| Header/navigation | Native text/UI/vector content intended to be editable | `REBUILD_NATIVE` | Header region; exact bounds from Figma audit | No raster extraction mask; native geometry required | No | `04_HEADER` | High; typography and spacing require native QA |
| Hero copy / CTA | Native typography and button/UI content | `REBUILD_NATIVE` | Left hero-copy region; exact bounds from Figma audit | No raster extraction mask; native geometry required | No | `05_HERO_COPY` | High; preserve copy, hierarchy, and overlap semantics |
| Metrics | Native metric text/dividers | `REBUILD_NATIVE` | Metrics region; exact bounds from Figma audit | No raster extraction mask; native geometry required | No | `06_METRICS` | High; numeric typography and dividers require native QA |
| Wall slogan | Native typography | `REBUILD_NATIVE` | Core `(1044,190,145,135)` | No raster extraction mask; native geometry required | No | `07_WALL_MESSAGE` | High; visible slogan may overlap raster layers |
| Wall underline | Native vector/divider | `REBUILD_NATIVE` | Core `(1060,338,62,5)` | No raster extraction mask; native geometry required | No | `07_WALL_MESSAGE` | High; preserve exact position and stroke appearance |
| Process strip | Native icons, labels, arrows, and dividers where possible | `REBUILD_NATIVE` | Bottom process-strip region; exact bounds from Figma audit | No raster extraction mask; native geometry required | No | `08_PROCESS_STRIP` | Medium; icon/vector source details require audit |
| Bottom signature | Native text and accent line | `REBUILD_NATIVE` | Bottom-right signature region; exact bounds from Figma audit | No raster extraction mask; native geometry required | No | `09_BOTTOM_SIGNATURE` | Medium; typography and line placement require native QA |

## Classification groups

### Extraction candidates

Portrait, TV hardware, TV screen content, phone hardware, and phone screen content use `EXTRACT_FROM_MASTER` for visible pixels. Their extraction masks must preserve all neighboring foreground overlaps. Foreground extraction is distinct from reconstruction of hidden background pixels.

### Reconstruction authorization candidates

Only hidden background/environment pixels exposed by removing approved foreground layers may use `RECONSTRUCT_HIDDEN_PIXELS`. This is not approved by SR-3 alone. SR-4 must record the source-recovery insufficiency, approved zone, approved mask, neighboring foreground preservation, and human/automated QA gates.

### Native rebuild candidates

Header/navigation, hero copy/CTA, metrics, wall slogan, wall underline, process strip, and bottom signature use `REBUILD_NATIVE` where editability is required.

## Unresolved issues

- SR-4 has not approved any reconstruction.
- Portrait source provenance remains unresolved; no portfolio candidate is promoted as exact.
- A prior GrabCut portrait mask was rejected and remains unapproved. The later semantic-mask attempt is also not approval evidence.
- Exact sub-bounds and extraction masks for TV/phone hardware versus screens require a bounded Figma/source audit.
- Native typography, icon, and vector measurements require visual QA after implementation.

## Proposed SR-4 checklist

- [ ] Review this plan and confirm every material layer has exactly one classification.
- [ ] Confirm portrait remains `EXTRACT_FROM_MASTER` unless exact source provenance is later proven.
- [ ] Confirm visible background remains exact master pixels.
- [ ] Decide whether any hidden pixels genuinely require `RECONSTRUCT_HIDDEN_PIXELS`.
- [ ] If reconstruction is authorized, record source-recovery insufficiency, approved zones, masks, exclusions, and QA gates.
- [ ] Confirm no Figma promotion or human approval is implied by candidate artifacts.
- [ ] Approve or reject the plan before production extraction or reconstruction resumes.

SR-4 status: `PENDING`.
