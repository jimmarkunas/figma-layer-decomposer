# Source Asset Recovery & Decomposition Gate

Status: mandatory architecture gate for every mock-up before extraction or reconstruction.

## 1. Purpose

The Figma Layer Decomposer is a decomposition-and-recomposition system, not an inpainting-first system.

Before the pipeline extracts pixels from a flattened master or reconstructs missing content, it MUST first determine whether the exact source asset already exists and can be reused.

Preferred strategy:

1. recover exact source assets;
2. verify provenance and alignment against the immutable master;
3. classify each material layer by implementation method;
4. rebuild a foreground raster from a trustworthy source only when the flattened master cannot contain the complete independent layer;
5. reconstruct only genuinely hidden background pixels for which no trustworthy source can be recovered.

The existence of an artifact is never proof of provenance or approval.

## 2. Hard gate

No extraction mask, source-guided raster rebuild, clean-plate candidate, inpainting run, texture synthesis, or other raster reconstruction may begin for a layer until the source-recovery gate for that layer is complete.

A layer may enter clean-plate reconstruction only when the decomposition plan explicitly classifies the required pixels as `RECONSTRUCT_HIDDEN_PIXELS` and records why exact source recovery was not sufficient.

A layer may enter source-guided foreground rebuilding only when the decomposition plan explicitly classifies it as `REBUILD_RASTER_FROM_SOURCE` and records why neither `RECOVER_SOURCE` nor `EXTRACT_FROM_MASTER` can produce the required complete independent layer.

## 3. SR-1 — Source asset inventory

Inventory all plausible source assets before manipulating the flattened master.

Search in this order when available and in scope:

1. immutable master/reference metadata;
2. original/raw image fills and linked assets in Figma;
3. assets in the current repository;
4. explicitly authorized related GitHub repositories or asset libraries;
5. explicitly configured shared artifact storage;
6. only then, the flattened master itself as an extraction source.

For every candidate source record, capture source location, stable identifier, dimensions, file type, SHA-256 when available, Figma reference when applicable, candidate role, and whether provenance is known, inferred, or unknown.

Cross-repository reads must still follow `AGENTS.md` scope rules. Cross-repository writes require explicit approval.

## 4. SR-2 — Provenance and exact-match verification

A source candidate is not considered recovered merely because it looks similar.

Verify candidates against the immutable master using the strongest evidence available: exact hashes, pixel-exact crop/transform comparison, deterministic scaling/cropping/placement alignment, matching dimensions/composition transform, Figma raw-image provenance, or documented source relationship.

A visually similar substitute is not an exact recovered source. If the exact asset cannot be proven, do not silently promote it to `RECOVER_SOURCE`.

A source may still be used as an explicitly documented guide for `REBUILD_RASTER_FROM_SOURCE` when user-supplied provenance establishes that the approved mock-up was derived from that source and the complete standalone foreground cannot be recovered from the flattened master.

## 5. SR-3 — Per-layer decomposition classification

Every material layer must receive exactly one primary implementation classification before production work continues.

### `RECOVER_SOURCE`

Use an exact original asset that has been recovered and verified.

### `EXTRACT_FROM_MASTER`

Use pixels from the immutable master when the required independent layer is fully represented there and an exact standalone source is unavailable. Extraction must preserve master pixels rather than reinterpret them.

Do not use this classification when occlusion means the master cannot contain the complete layer that must exist independently in Figma.

### `REBUILD_RASTER_FROM_SOURCE`

Rebuild a complete raster foreground layer from a trustworthy related source when:

- the approved mock-up was derived from that source;
- no exact standalone final asset is recoverable;
- the flattened master contains only a partially visible/occluded version of the layer; and
- the product requires the complete layer to exist independently beneath occluding foreground objects.

Visible portions of the rebuilt layer must be validated against the immutable master. Newly reconstructed content is allowed only where the required standalone layer is hidden/occluded in the master. The immutable master remains the visual acceptance authority.

### `REBUILD_NATIVE`

Recreate the layer as native Figma text, vector, component, or UI where editability is required and raster recovery is not the correct representation.

### `RECONSTRUCT_HIDDEN_PIXELS`

Use deterministic clean-plate reconstruction only for background/environment pixels genuinely hidden behind foreground content and not recoverable from a trustworthy source asset.

## 6. SR-4 — Decomposition-plan approval gate

Before raster production resumes, record and review the decomposition plan for the mock-up.

For each layer, identify canonical layer name, source candidate/status, provenance result, implementation classification, exact placement/transform when known, whether reconstruction is permitted, and unresolved risks.

The gate passes only when every material layer has an explicit classification and no fallback path is being used merely because it is convenient.

If a layer remains unresolved, stop at `BLOCKED` for that layer rather than guessing.

## 7. Reconstruction authorization

When a layer is classified `RECONSTRUCT_HIDDEN_PIXELS`, the clean-plate package may run only after source-recovery search, insufficiency reason, approved zone, approved removal mask/equivalent authorization, neighboring foreground exclusions, and required automated/human QA gates are recorded.

`docs/CLEAN_PLATE_CONTRACT.md` governs clean-background reconstruction after this authorization exists.

When a layer is classified `REBUILD_RASTER_FROM_SOURCE`, a target-specific rebuild contract must define source inputs, immutable-master comparison requirements, visible-region preservation requirements, hidden-region allowance, placement/alignment, output artifacts, automated QA, and human approval before Figma promotion.

## 8. DIRECTV corrective state

For the DIRECTV hero:

- 3B.1 deterministic clean-plate engine remains valid as fallback infrastructure.
- SR-1 through SR-4, ARC-1, and EX-0 were completed under the earlier plan.
- The earlier portrait classification `EXTRACT_FROM_MASTER` is superseded by new user-supplied provenance: the DIRECTV portrait was derived from the user's website portrait, while TV/phone occlusion prevents a crop/extraction from producing the complete independent portrait layer required by the product.
- Portrait is therefore reclassified `REBUILD_RASTER_FROM_SOURCE`.
- Prior GrabCut, semantic-mask, source-proxy-mask, and subtractive semantic-correction attempts remain rejected for production use.
- No new portrait removal mask or clean-plate candidate is authorized until the standalone portrait rebuild is approved and its occupancy geometry can be derived from the approved rebuilt asset.

## 9. Anti-drift rule

When a local implementation path becomes increasingly sophisticated while the higher-level source strategy is unresolved, stop and re-evaluate the decomposition classification before adding more tooling.

Do not optimize a fallback technique until the project has proven that the fallback is actually required.
