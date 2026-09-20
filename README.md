# figma-layer-decomposer

Deterministic production pipeline for turning an approved flat mock-up PNG into a layered Figma composition **without redesigning it**.

The project exists to preserve the visual fidelity of an immutable master image while making selected elements independently editable or replaceable.

It is also the recovery/reconstruction front-end for a broader reusable-template workflow: **approved concept image → editable Figma reconstruction → promoted Personal Brand template → React / PowerPoint presentation outputs**. The decomposer does not replace the canonical Jim Markunas Personal Brand design system; accepted reusable templates are promoted into that existing Figma authority.

## Core principle

> The master PNG is the acceptance authority for faithful reconstruction. Recover exact source assets first. Extract from the master only when necessary. Reconstruct only genuinely hidden pixels that cannot be recovered from a trustworthy source.

## Ownership boundary

This repository owns:

- source-asset inventory and decomposition planning
- raster layer extraction
- alpha masks
- fallback clean-plate reconstruction
- deterministic compositing
- coordinate manifests
- pixel-diff / SSIM QA
- Figma placement manifests
- reproducible outputs for multiple mock-ups
- the proof that an accepted reconstruction can be promoted into a reusable Personal Brand template

This repository does **not** own:

- redesigning the approved composition
- changing typography, spacing, layout, lighting, or art direction during reconstruction
- silently substituting visually similar assets for exact recovered sources
- silently modifying pixels outside an approved reconstruction zone
- final human visual approval
- a second permanent Personal Brand design system or template library
- speculative generic Figma-to-code, template-registry, renderer, or bidirectional-sync infrastructure

Native Figma text, buttons, navigation, vectors, and components are reconstructed separately after the decomposition plan classifies them `REBUILD_NATIVE`.

## Business-case gate

DIRECTV is the reference reconstruction. Before the project generalizes through mock-ups #2–#6, it must prove that the accepted DIRECTV composition can become a **reusable template**, not merely an editable one-off reconstruction.

That proof must demonstrate:

- promotion into the existing canonical Jim Markunas Personal Brand Figma library
- a second, non-DIRECTV variation produced by substituting content/media without rebuilding the layout
- one bounded semantic template/content contract
- one React presentation slide populated from that contract
- one PowerPoint slide populated from the same contract, with editable text and replaceable media where practical

A flattened screenshot-only PowerPoint does not satisfy the proof. See `docs/PROJECT_CANON.md` for the authoritative `TP-1 — Template Promotion & Consumption Proof` contract.

## Source-first decomposition pipeline

```text
MASTER PNG (immutable)
      |
      v
SOURCE ASSET INVENTORY
  - Figma raw/image assets
  - current repo assets
  - explicitly authorized related repos/libraries
      |
      v
PROVENANCE / EXACT-MATCH VERIFICATION
      |
      v
PER-LAYER CLASSIFICATION
  - RECOVER_SOURCE
  - EXTRACT_FROM_MASTER
  - REBUILD_NATIVE
  - RECONSTRUCT_HIDDEN_PIXELS
      |
      v
DECOMPOSITION PLAN APPROVAL
      |
      +---------------------------+
      |                           |
      v                           v
Recover / extract /          Clean-plate reconstruction
rebuild native layers        ONLY where explicitly authorized
      |                           |
      +-------------+-------------+
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
                    |
                    v
Accepted editable reconstruction
                    |
                    v
Template promotion proof
  - canonical Personal Brand Figma library
  - semantic content contract
  - React slide
  - editable PowerPoint slide
```

See [`docs/SOURCE_ASSET_RECOVERY.md`](docs/SOURCE_ASSET_RECOVERY.md) for the mandatory source-recovery gate and [`docs/CLEAN_PLATE_CONTRACT.md`](docs/CLEAN_PLATE_CONTRACT.md) for fallback reconstruction once a layer is explicitly authorized.

## Non-negotiable guardrails

1. `master.png` is immutable.
2. Recover and verify exact source assets before extraction or reconstruction.
3. Clean-plate reconstruction is fallback-only and requires explicit `RECONSTRUCT_HIDDEN_PIXELS` classification.
4. Canvas coordinates are always relative to the master image origin `(0, 0)`.
5. Pixels outside an authorized reconstruction mask/halo must remain byte-equivalent to the source after normalization to the same color mode.
6. Every generated raster asset must have a machine-readable placement record.
7. A later stage may not repair a failed earlier stage.
8. No Figma upload occurs until automated QA and human visual QA pass.
9. Existing approved mock-ups are reference material, not prompts for reinterpretation.
10. Every run must be reproducible from inputs + manifest + pipeline version.
11. If source strategy is unresolved, stop `BLOCKED` rather than increasing fallback-tool complexity.
12. The reconstruction workspace must not become a second permanent Personal Brand design system; reusable templates promote into the existing canonical Figma library.
13. Do not generalize through additional mock-ups until the DIRECTV template-promotion business case is proven.

## Current reference mock-up

The first production case is the DIRECTV hero mock-up:

- canvas: `1586 x 992`
- current milestone: **M3 Background / source-recovery gate**
- 3B.1 deterministic clean-plate engine: **COMPLETE as fallback infrastructure**
- SR-1 source asset inventory: **COMPLETE for current DIRECTV inventory scope**
- **SR-2 provenance / exact-match verification: ACTIVE**
- 3B.2 portrait clean-plate candidate: **PAUSED** pending SR-2 through SR-4 and ARC-1
- current next step: **SR-2 — provenance / exact-match verification for the DIRECTV portrait candidates**

The failed GrabCut portrait-mask candidate is rejected and unapproved. Do not generate another portrait mask or clean-plate candidate until SR-1 through SR-4 and ARC-1 are complete.

## Local clean-plate commands

These commands are valid only after the source-recovery/decomposition gate explicitly authorizes reconstruction for the target layer.

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

After reconstruction is authorized, run a clean-plate stage with a manifest, schema, source, mask, target, and unique run directory:

```bash
./.venv/bin/clean-plate \
  --manifest examples/directv/manifest.example.json \
  --schema schema/layer-manifest.schema.json \
  --source input/directv-hero-01/master.png \
  --mask input/directv-hero-01/masks/portrait.png \
  --target portrait \
  --run-dir runs/directv-portrait-$(date +%Y%m%d-%H%M%S)
```

Each authorized reconstruction run emits `candidate.png`, `preview.png`, `difference.png`, `unchanged-region-diff.png`, and `report.json` under its run directory. The command exits non-zero when any automated gate fails; `human_gate` remains `PENDING`.

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

The exact reusable-template semantic schema is intentionally **not** added to this output structure yet. `TP-1` will define the smallest schema actually required after the DIRECTV reconstruction is accepted.

## Roadmap

### M2 — Structure

Complete.

### M3 — Background / decomposition

- 3A — removal geometry specification ✅
- 3A.1 — remove unapproved wall cleanup patches ✅
- 3B.0 — clean-plate pipeline contract ✅
- 3B.1 — deterministic clean-plate engine ✅ fallback infrastructure
- SR-1 — source asset inventory ✅ current DIRECTV inventory scope
- **SR-2 — provenance / exact-match verification — ACTIVE**
- SR-3 — per-layer decomposition classification
- SR-4 — decomposition-plan approval gate
- ARC-1 — post-SR architecture checkpoint; `NO CHANGE` is an acceptable result
- 3B.2 — portrait clean-plate candidate, only if reconstruction remains necessary
- 3B.3 — automated unchanged-region QA
- 3B.4 — human visual QA
- 3B.5 — push approved portrait clean plate to Figma
- 3C — TV removal, only if reconstruction remains necessary
- 3D — phone removal, only if reconstruction remains necessary
- 3E — wall slogan treatment according to SR classification
- 3F — wall underline treatment according to SR classification
- 3G — full clean-background QA
- 3H — finalize approved clean background
- 4A–4F — portrait recovery/extraction + QA according to SR classification
- 5A–5I — device recovery/extraction + QA according to SR classification
- DTV-FINAL — complete editable DIRECTV reconstruction + full-frame 1:1 visual acceptance

### TP-1 — Template Promotion & Consumption Proof

After `DTV-FINAL` and before broader generalization:

- promote the accepted DIRECTV reconstruction into the canonical Personal Brand Figma library
- create a non-DIRECTV variant through content/media substitution rather than layout reconstruction
- define the minimum semantic template/content contract
- render one React presentation slide from that contract
- render one editable PowerPoint slide from that same contract
- visually validate the three outputs against the approved template

### Reusable pipeline

Only after TP-1 is accepted:

- lock/pin deterministic raster dependencies before broad generalization
- generalize for mock-ups #2–#6
- preserve the source-first gate, schema, and SOP
- treat each additional mock-up as a candidate reusable Personal Brand template, not decomposition-only output
- automate Figma placement from manifest where the proven mechanics justify it
- extract shared template/rendering primitives only after real repeated consumers demonstrate the need
- package the proven mechanics as a reusable project/tool without creating a second design system
