# Source Asset Recovery & Decomposition Gate

Status: mandatory architecture gate for every mock-up before extraction or clean-plate reconstruction.

## 1. Purpose

The Figma Layer Decomposer is a decomposition-and-recomposition system, not an inpainting-first system.

Before the pipeline extracts pixels from a flattened master or reconstructs hidden background pixels, it MUST first determine whether the exact source asset already exists and can be reused.

The preferred strategy is always:

1. recover exact source assets;
2. verify provenance and alignment against the immutable master;
3. classify each visible layer by implementation method;
4. reconstruct only genuinely hidden pixels for which no trustworthy source can be recovered.

Clean-plate reconstruction is therefore a fallback capability, not the default decomposition strategy.

## 2. Hard gate

No extraction mask, clean-plate candidate, inpainting run, texture synthesis, or other raster reconstruction may begin for a layer until the source-recovery gate for that layer is complete.

A layer may enter clean-plate reconstruction only when the decomposition plan explicitly classifies the required pixels as `RECONSTRUCT_HIDDEN_PIXELS` and records why exact source recovery was not sufficient.

The existence of an artifact is never proof of provenance or approval.

## 3. SR-1 — Source asset inventory

Inventory all plausible source assets before manipulating the flattened master.

Search in this order when available and in scope:

1. immutable master/reference metadata;
2. original/raw image fills and linked assets in Figma;
3. assets in the current repository;
4. explicitly authorized related GitHub repositories or asset libraries;
5. explicitly configured shared artifact storage;
6. only then, the flattened master itself as an extraction source.

For every candidate source record:

- source location;
- filename or stable identifier;
- dimensions;
- file type;
- SHA-256 when bytes are available;
- Figma node/image reference when applicable;
- candidate role in the composition;
- whether provenance is known, inferred, or unknown.

Cross-repository reads must still follow `AGENTS.md` scope rules. Cross-repository writes require explicit approval.

## 4. SR-2 — Provenance and exact-match verification

A source candidate is not considered recovered merely because it looks similar.

Verify the candidate against the immutable master using the strongest evidence available:

- exact source hash where the same file is embedded or referenced;
- pixel-exact crop/transform comparison;
- deterministic scaling/cropping/placement alignment;
- matching dimensions and composition transform;
- Figma raw-image or image-fill provenance;
- documented source relationship from the repository or design file.

A visually similar substitute is not an exact recovered source.

If the exact asset cannot be proven, keep its status unresolved and do not silently promote it.

## 5. SR-3 — Per-layer decomposition classification

Every material layer must receive exactly one primary implementation classification before production work continues:

### `RECOVER_SOURCE`

Use an exact original asset that has been recovered and verified.

Examples: original portrait image, original background/environment image, original device render.

### `EXTRACT_FROM_MASTER`

Use pixels from the immutable master because the visible layer is fully represented there and an exact standalone source is unavailable.

Extraction must preserve master pixels rather than reinterpret them.

### `REBUILD_NATIVE`

Recreate the layer as native Figma text, vector, component, or UI where editability is required and raster recovery is not the correct representation.

Examples: typography, navigation, buttons, metrics, simple vector dividers.

### `RECONSTRUCT_HIDDEN_PIXELS`

Use deterministic clean-plate reconstruction only for pixels that are genuinely hidden behind foreground content and cannot be recovered from a trustworthy source asset.

This classification requires explicit evidence that source recovery was attempted first.

## 6. SR-4 — Decomposition-plan approval gate

Before raster production resumes, record and review the decomposition plan for the mock-up.

For each layer, the plan must identify:

- canonical layer name;
- source candidate or source status;
- provenance result;
- implementation classification;
- exact placement/transform when known;
- whether reconstruction is permitted;
- unresolved risks or missing evidence.

The gate passes only when every material layer has an explicit classification and no reconstruction path is being used merely because it is convenient.

If a layer remains unresolved, stop at `BLOCKED` for that layer rather than guessing.

## 7. Reconstruction authorization

When a layer is classified `RECONSTRUCT_HIDDEN_PIXELS`, the clean-plate package may run only after the following are recorded:

- source-recovery search completed;
- searched locations/systems;
- reason no exact reusable source is sufficient;
- approved reconstruction zone;
- approved removal mask or equivalent deterministic authorization;
- neighboring foreground that must be preserved;
- required automated and human QA gates.

`docs/CLEAN_PLATE_CONTRACT.md` governs the reconstruction implementation after this authorization exists.

## 8. DIRECTV corrective state

For the current DIRECTV hero reference:

- 3B.1 deterministic clean-plate engine remains valid and complete as a reusable fallback subsystem.
- 3B.2 portrait clean-plate generation is PAUSED.
- The GrabCut portrait-mask candidate is REJECTED and remains unapproved.
- A semantic-segmentation replacement is NOT authorized as the next step.
- Source recovery must be performed for background, portrait, TV, phone, and other material raster assets before deciding which reconstruction work is actually necessary.

The current next operation is SR-1: source asset inventory.

## 9. Anti-drift rule

When a local implementation path becomes increasingly sophisticated while the higher-level source strategy is unresolved, stop and re-evaluate the decomposition classification before adding more tooling.

Do not optimize a fallback technique until the project has proven that the fallback is actually required.
