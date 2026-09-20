# figma-layer-decomposer

Deterministic production pipeline for turning an approved flat mock-up PNG into a layered Figma composition **without redesigning it**.

The project exists to preserve the visual fidelity of an immutable master image while making selected elements independently editable or replaceable.

## Core principle

> The master PNG is the acceptance authority. The pipeline may reconstruct only pixels that must be revealed when an extracted layer is hidden. Everything else must remain unchanged.

## Ownership boundary

This repository owns:

- raster layer extraction
- alpha masks
- clean-plate reconstruction
- deterministic compositing
- coordinate manifests
- pixel-diff / SSIM QA
- Figma placement manifests
- reproducible outputs for multiple mock-ups

This repository does **not** own:

- redesigning the approved composition
- changing typography, spacing, layout, lighting, or art direction
- deciding which elements should be native Figma objects
- silently modifying pixels outside an approved reconstruction zone
- final human visual approval

Native Figma text, buttons, navigation, vectors, and components are reconstructed separately after raster decomposition is accepted.

## Pipeline

```text
MASTER PNG (immutable)
      |
      v
Layer manifest + masks
      |
      v
Clean-plate reconstruction
      |
      v
Raster extraction
      |
      v
Deterministic recomposition
      |
      v
Automated QA
  - unchanged-pixel guard
  - canvas/coordinate checks
  - diff image
  - SSIM / error metrics
      |
      v
Human visual approval
      |
      v
Figma placement from manifest
```

## Non-negotiable guardrails

1. `master.png` is immutable.
2. Canvas coordinates are always relative to the master image origin `(0, 0)`.
3. Pixels outside the approved reconstruction mask/halo must remain byte-equivalent to the source after normalization to the same color mode.
4. Every generated raster asset must have a machine-readable placement record.
5. A later stage may not repair a failed earlier stage.
6. No Figma upload occurs until automated QA and human visual QA pass.
7. Existing approved mock-ups are reference material, not prompts for reinterpretation.
8. Every run must be reproducible from inputs + manifest + pipeline version.

## Current reference mock-up

The first production case is the DIRECTV hero mock-up:

- canvas: `1586 x 992`
- current milestone: **M3 Background**
- current bounded package: **3B Portrait clean plate**

See [`docs/CLEAN_PLATE_CONTRACT.md`](docs/CLEAN_PLATE_CONTRACT.md) for the implementation contract and [`examples/directv/manifest.example.json`](examples/directv/manifest.example.json) for the first manifest.

## Local 3B.1 commands

From the repository root, create/use the repository-local Python 3.12 environment and install the package:

```bash
python3.12 -m venv .venv
./.venv/bin/python -m pip install -e . pytest
```

Run the full test suite and whitespace validation:

```bash
./.venv/bin/pytest -q
git diff --check
```

Show the CLI help, and verify missing required arguments fail non-zero:

```bash
./.venv/bin/clean-plate --help
./.venv/bin/clean-plate
```

Run a clean-plate stage with a manifest, schema, source, mask, target, and unique run directory:

```bash
./.venv/bin/clean-plate \
  --manifest examples/directv/manifest.example.json \
  --schema schema/layer-manifest.schema.json \
  --source input/directv-hero-01/master.png \
  --mask input/directv-hero-01/masks/portrait.png \
  --target portrait \
  --run-dir runs/directv-portrait-$(date +%Y%m%d-%H%M%S)
```

Each run emits `candidate.png`, `preview.png`, `difference.png`, `unchanged-region-diff.png`, and `report.json` under its run directory. The command exits non-zero when any automated gate fails; `human_gate` remains `PENDING`.

## Planned output structure

```text
output/<mockup-id>/
├── background/
│   ├── clean-plate.png
│   └── clean-plate-preview.png
├── portrait/
│   ├── portrait.png
│   └── portrait-mask.png
├── devices/
│   ├── tv-hardware.png
│   ├── tv-screen.png
│   ├── phone-hardware.png
│   └── phone-screen.png
├── qa/
│   ├── reconstructed.png
│   ├── difference.png
│   ├── unchanged-region-diff.png
│   └── report.json
└── figma-manifest.json
```

## Roadmap

### M2 — Structure

Complete.

### M3 — Background

- 3A — removal geometry specification ✅
- 3A.1 — remove unapproved wall cleanup patches ✅
- 3B.0 — clean-plate pipeline contract ✅ in this repo bootstrap
- 3B.1 — implement deterministic pipeline
- 3B.2 — generate portrait clean-plate candidate
- 3B.3 — automated unchanged-region QA
- 3B.4 — human visual QA
- 3B.5 — push approved portrait clean plate to Figma
- 3C — TV removal using same pipeline
- 3D — phone removal using same pipeline
- 3E — wall slogan removal using same pipeline
- 3F — wall underline removal using same pipeline
- 3G — full clean-background QA
- 3H — finalize approved clean background

### Reusable pipeline

After the first mock-up passes:

- generalize for mock-ups #2–#6
- preserve schema + SOP
- automate Figma placement from manifest
- package as a reusable project/tool
