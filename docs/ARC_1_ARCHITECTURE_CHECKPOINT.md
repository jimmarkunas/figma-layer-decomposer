# ARC-1 — Post-SR Architecture Checkpoint

Status: **PASS**

## Purpose

Review the approved DIRECTV decomposition plan against the current repository structure and authorize only the reusable architecture that DIRECTV has actually proven is needed.

This is a scalability checkpoint, not a refactor mandate.

## Inputs reviewed

- `docs/PROJECT_CANON.md`
- `docs/SOURCE_ASSET_RECOVERY.md`
- `docs/DIRECTV_DECOMPOSITION_PLAN.md`
- `examples/directv/decomposition-plan.json`
- `cleanplate/core.py`
- `cleanplate/cli.py`
- `schema/layer-manifest.schema.json`
- current clean-plate tests and package layout

## Current architecture finding

The repository is not bloated. The implemented production code is still small and focused around the deterministic clean-plate subsystem.

The current risk is not excessive code volume; it is allowing the clean-plate subsystem to become the general decomposition engine now that DIRECTV has proven multiple different implementation methods.

The approved DIRECTV plan contains five `EXTRACT_FROM_MASTER` consumers:

- portrait
- TV hardware
- TV screen content
- phone hardware
- phone screen content

That is enough repeated demand to justify one focused extraction subsystem. It does not justify a broad orchestration framework.

## Approved architecture decisions

### 1. Keep `cleanplate` focused

`cleanplate` remains the deterministic fallback subsystem for `RECONSTRUCT_HIDDEN_PIXELS` only.

Do not add source discovery, portrait extraction, device extraction, native Figma rebuild, workflow orchestration, or provenance logic to `cleanplate/core.py`.

### 2. Add one focused master-pixel extraction subsystem

A new deterministic extraction package is approved because DIRECTV already has five real `EXTRACT_FROM_MASTER` consumers.

The package should:

- read the immutable master without modifying it;
- accept deterministic bounds and mask input;
- preserve source RGB pixels exactly wherever alpha is non-zero;
- emit a transparent RGBA layer asset rather than reconstructing or recoloring pixels;
- validate canvas, bounds, and mask geometry;
- emit machine-readable QA/report evidence;
- fail closed on invalid or ambiguous input;
- support both `raster_extract` and `screen_extract` target kinds already present in the manifest schema;
- remain independent from Figma write operations.

The extraction subsystem must not perform semantic segmentation or invent missing pixels.

### 3. Approve a minimal shared-primitives seam

A second real consumer now exists for several mechanics already implemented inside `cleanplate/core.py`.

The following mechanics may be moved into a small shared module when the extraction subsystem is implemented:

- `Bounds` representation;
- SHA-256 helper;
- manifest loading/schema validation;
- RGB image loading;
- mask loading and bounded/full-canvas placement;
- bounds validation.

Preferred shape: a small project-specific shared module such as `decomposer/primitives.py`.

Do not create a large framework or generic utility package. Only move code that is genuinely shared by both clean-plate and extraction paths, preserving existing clean-plate behavior and tests.

### 4. Do not create a shared QA framework yet

Clean-plate QA and extraction QA have different acceptance semantics.

- Clean-plate QA proves unchanged pixels outside the approved reconstruction zone.
- Extraction QA must prove extracted visible RGB pixels are identical to the immutable master wherever the extraction alpha/mask is non-zero, and that pixels outside the extraction mask are transparent/non-participating.

Keep extraction QA inside the extraction subsystem until a real second QA consumer proves a reusable abstraction.

### 5. Do not productize source provenance yet

SR-1/SR-2 proved the source-first workflow, but only one reference mock-up has exercised it.

Do not add a provenance service/package/database or generalized asset-search engine yet. Keep source recovery procedural and evidence-driven until P1–P4 proves repeated mechanics.

### 6. Do not add orchestration infrastructure yet

No workflow engine, queue, task graph, database, plugin system, or general pipeline orchestrator is authorized.

The existing manifest `sequence` plus bounded commands remain sufficient for DIRECTV.

### 7. Do not expand the manifest schema speculatively

`schema/layer-manifest.schema.json` already supports:

- `clean_plate`
- `raster_extract`
- `screen_extract`
- `other`

Do not change the schema until the extraction implementation proves a concrete missing field or invariant.

### 8. Native Figma rebuild remains outside the raster engine

`REBUILD_NATIVE` layers remain ChatGPT/Figma composition work with deterministic measurements and QA. Do not add a native-UI rendering package to the Python raster pipeline.

## Approved next implementation package

### EX-0 — Deterministic master-pixel extraction engine

Build the smallest reusable extraction subsystem required by the five approved DIRECTV extraction targets.

Acceptance direction:

- exact immutable-master pixel preservation inside extraction alpha;
- transparent output outside extraction alpha;
- deterministic bounded/full-canvas mask handling;
- dimensions and bounds validated;
- machine-readable report;
- non-zero exit on automated QA failure;
- no Figma write;
- no hidden-pixel reconstruction;
- no semantic segmentation;
- no broad refactor beyond the minimal shared-primitives seam approved above.

Production portrait/device extraction remains separate from EX-0. EX-0 builds and proves the engine only.

## Explicit deferrals

Deferred until repeated evidence justifies them:

- generalized provenance/source-recovery package;
- shared QA framework;
- pipeline/orchestration framework;
- database/state store;
- plugin architecture;
- service/API layer;
- GUI;
- generalized multi-mock-up automation;
- broad package restructuring.

## Result

ARC-1 = **PASS WITH MINIMAL ARCHITECTURE ADDITION**.

Approved additions:

1. one focused `EXTRACT_FROM_MASTER` subsystem;
2. one minimal project-specific shared-primitives module used by clean-plate and extraction paths.

Everything else remains deferred.
