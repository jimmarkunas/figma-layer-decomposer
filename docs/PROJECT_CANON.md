# Figma Layer Decomposer — Project Canon

## Purpose

This file is the canonical continuity handoff for the Figma Layer Decomposer project. It exists so ChatGPT, Codex, local development sessions, and future conversations can recover the current state without relying on one chat transcript.

## Authority order

When sources conflict, use this order:

1. **Immutable master PNG** — visual acceptance authority.
2. `docs/CLEAN_PLATE_CONTRACT.md` — clean-plate implementation contract.
3. `schema/layer-manifest.schema.json` — machine-readable manifest contract.
4. This file — current project state, accepted decisions, roadmap, and next step.
5. Notion mirror / ChatGPT Project uploads — convenience copies only.

Do not infer approval from the mere existence of an artifact.

## Mission

Turn approved flat mock-up PNGs into genuinely editable layered Figma compositions while preserving 1:1 visual fidelity to the immutable master image.

## Core rules

- The master PNG is the acceptance authority.
- Do not redesign, reinterpret, beautify, or improve approved mock-ups.
- Preserve untouched source pixels exactly wherever possible.
- Use a hybrid decomposition model: photographic/environmental content stays raster; editable text/UI/vectors are rebuilt natively in Figma.
- **Source recovery comes before extraction or reconstruction.** Recover and verify exact original assets whenever possible.
- Clean-plate reconstruction is a fallback for genuinely hidden pixels that cannot be recovered from a trustworthy source asset.
- Clean-plate reconstruction happens outside Figma using the `figma-layer-decomposer` pipeline.
- Figma is the destination and composition layer, not the raster-reconstruction engine.
- Every raster layer must use deterministic coordinates and a machine-readable manifest.
- No Figma upload or promotion occurs until automated QA and human visual QA pass.
- Later steps may not repair failed earlier steps.
- Work incrementally: one bounded operation → validate → stop.
- Prefer deterministic scripting, exact source recovery, masks, pixel diffs, and repeatable tooling over manual approximation.
- Use Codex for bounded local implementation tasks involving asset inventory, image processing, tests, manifests, file operations, and automation.
- Use ChatGPT for architecture, decomposition strategy, acceptance criteria, source/provenance review, Figma QA, and technical review.
- Do not introduce abstractions, services, packages, or infrastructure speculatively. Add reusable architecture only after DIRECTV proves a second real consumer or repeated mechanic.

## Repository

- Repository: `https://github.com/jimmarkunas/figma-layer-decomposer`
- Default branch: `main`
- Current implementation branch: `feature/3b2-directv-portrait-candidate`
- Current implementation issue: `#4 — 3B.2 — Generate DIRECTV portrait clean-plate candidate` — PAUSED until target-specific reconstruction prerequisites are satisfied
- Completed source-recovery issue: `#5 — SR-1–SR-4 — Source asset recovery and decomposition gate`
- Completed extraction-engine issue: `#7 — EX-0 — Deterministic master-pixel extraction engine`
- Completed implementation issue: `#1 — 3B.1 — Implement deterministic clean-plate pipeline`
- Local repository path: `/Users/jimmarkunas/Development/Jim/figma-layer-decomposer`
- Product status: standalone product inside the shared Jim development workspace.

## Figma

- File: `https://www.figma.com/design/3ZYkEtZVyRH9B2DfVpersf/JM-Personal-Brand-V2?node-id=240-4`
- File key: `3ZYkEtZVyRH9B2DfVpersf`
- Page: `999-1 Asset Rebuild`
- Reference frame: `240:4 — 00_Master_Reference`
- Editable frame: `240:5 — Editable Master Reference 01 — Layered`
- Canvas: `1586 × 992`

## Current reference mock-up

DIRECTV hero, 1586 × 992.

## Accepted Figma structure

Top-level groups inside the editable frame:

- `00_MASTER_REFERENCE`
- `01_BACKGROUND`
- `02_PORTRAIT`
- `03_DEVICES`
- `04_HEADER`
- `05_HERO_COPY`
- `06_METRICS`
- `07_WALL_MESSAGE`
- `08_PROCESS_STRIP`
- `09_BOTTOM_SIGNATURE`

## Source-first decomposition gate

`docs/SOURCE_ASSET_RECOVERY.md` defines the mandatory operating procedure before extraction or clean-plate reconstruction.

Every material layer must be classified as exactly one of:

- `RECOVER_SOURCE`
- `EXTRACT_FROM_MASTER`
- `REBUILD_NATIVE`
- `RECONSTRUCT_HIDDEN_PIXELS`

No mask generation, inpainting, semantic segmentation, texture synthesis, or clean-plate candidate run is authorized until source recovery has been attempted and the relevant layer is explicitly classified `RECONSTRUCT_HIDDEN_PIXELS`.

The mandatory gate is:

- **SR-1 — Source asset inventory** — inspect Figma raw/image assets, current-repo assets, explicitly authorized related repositories, and other approved source locations.
- **SR-2 — Provenance / exact-match verification** — verify candidate assets against the immutable master using hashes, pixel alignment, deterministic transforms, and/or Figma provenance.
- **SR-3 — Per-layer decomposition classification** — assign one approved implementation method to every material layer.
- **SR-4 — Decomposition-plan approval** — review the inventory/classification and explicitly authorize any `RECONSTRUCT_HIDDEN_PIXELS` work before reconstruction resumes.

For DIRECTV, SR-1 through SR-4 are COMPLETE. The approved plan is `docs/DIRECTV_DECOMPOSITION_PLAN.md` with structured mirror `examples/directv/decomposition-plan.json`.

## Approved DIRECTV decomposition classification

- Background/environment — `RECONSTRUCT_HIDDEN_PIXELS` only for genuinely hidden pixels exposed by approved foreground removal; all already-visible background pixels remain exact master pixels.
- Portrait — `EXTRACT_FROM_MASTER`.
- TV hardware — `EXTRACT_FROM_MASTER`.
- TV screen content — `EXTRACT_FROM_MASTER`.
- Phone hardware — `EXTRACT_FROM_MASTER`.
- Phone screen content — `EXTRACT_FROM_MASTER`.
- Header/navigation — `REBUILD_NATIVE`.
- Hero copy/CTA — `REBUILD_NATIVE`.
- Metrics — `REBUILD_NATIVE`.
- Wall slogan — `REBUILD_NATIVE`.
- Wall underline — `REBUILD_NATIVE`.
- Process strip — `REBUILD_NATIVE`.
- Bottom signature — `REBUILD_NATIVE`.

Portrait source recovery remains inconclusive; no portfolio portrait candidate is approved as `RECOVER_SOURCE`.

## ARC-1 architecture checkpoint

`docs/ARC_1_ARCHITECTURE_CHECKPOINT.md` records the approved post-SR architecture review.

ARC-1 result: **PASS WITH MINIMAL ARCHITECTURE ADDITION**.

Approved architecture changes:

1. Keep `cleanplate` focused exclusively on `RECONSTRUCT_HIDDEN_PIXELS` fallback reconstruction.
2. Add one focused deterministic `EXTRACT_FROM_MASTER` subsystem because DIRECTV has five real extraction consumers.
3. Permit one minimal project-specific shared-primitives module for mechanics now proven to have two real consumers: bounds, hashing, manifest/schema validation, RGB loading, mask loading, and bounds validation.
4. Keep extraction-specific QA inside the extraction subsystem for now; do not create a general QA framework yet.
5. Do not productize provenance/source recovery yet.
6. Do not add a workflow/orchestration framework, database, queue, plugin architecture, service/API layer, GUI, or broad package restructuring.
7. Do not expand `schema/layer-manifest.schema.json` unless EX-0 proves a concrete missing field or invariant; it already supports `raster_extract` and `screen_extract`.
8. Native Figma rebuild remains outside the Python raster engine.

## EX-0 extraction engine

EX-0 is COMPLETE.

- `extract/` provides deterministic `EXTRACT_FROM_MASTER` execution for `raster_extract` and `screen_extract` targets.
- Output is bounded RGBA using deterministic Figma placement bounds.
- Participating RGB pixels are exact immutable-master pixels.
- Alpha values are preserved exactly, including intermediate alpha.
- Source immutability is verified by SHA-256 before/after execution.
- `decomposer/primitives.py` is the approved minimal shared seam for bounds, hashing, manifest validation, RGB loading, mask loading, and bounds validation.
- `cleanplate` remains reconstruction-only; extraction does not depend on `cleanplate` internals.
- No production DIRECTV extraction was performed during EX-0.

Accepted implementation commits:

- `1c3767561d39f503fc41cdc3eb804d31099fbb67` — extraction engine
- `e2e433f848b7e83cfc86ca9a1ec9b7c6e30989d2` — isolate shared decomposition primitives

Before P1 generalization, add a reproducibility checkpoint that pins/locks runtime dependencies used for deterministic raster output. The lock/pin must cover at least Pillow, NumPy, OpenCV, and jsonschema, and must not interrupt the current DIRECTV proof unless a version mismatch is actively causing non-deterministic behavior.

## Completed work

### M2 — Structure

- 2A — Verify source + editable frames — PASS
- 2B — Verify top-level groups — PASS
- 2C — Verify locked master reference — PASS
- 2D — Audit internal production structure — PASS
- 2E — Full-resolution structure QA — PASS WITH FINDING

### M3 — Background / source strategy

- 3A — Define exact removal geometry — PASS
- 3A.1 — Remove unapproved wall cleanup patches — PASS
- 3B.0 — Canonical clean-plate contract + repo bootstrap — COMPLETE
- 3B.1 — Deterministic clean-plate engine — COMPLETE as reusable fallback subsystem
- SR-1 — Source asset inventory — COMPLETE
- SR-2 — Provenance / exact-match verification — COMPLETE; portrait candidates INCONCLUSIVE
- SR-3 — Per-layer decomposition classification — COMPLETE
- SR-4 — Decomposition-plan approval — PASS
- ARC-1 — Post-SR architecture checkpoint — PASS WITH MINIMAL ARCHITECTURE ADDITION
- EX-0 — Deterministic master-pixel extraction engine — COMPLETE
- 3B.2 — Generate DIRECTV portrait clean-plate candidate — PAUSED until a target-specific trustworthy mask and all clean-plate prerequisites are validated

### Corrective findings

- The initial 3B.2 GrabCut portrait-mask candidate failed human visual review and is REJECTED.
- The failed GrabCut mask remains unapproved and must not be promoted or used for production reconstruction.
- A later portrait overlay was visually promising, but artifact existence and visual promise do not constitute production-mask approval.
- A semantic-segmentation replacement is not automatically authorized merely because source recovery was inconclusive.
- The architectural error was treating clean-plate reconstruction as the default path before proving source recovery was insufficient.
- 3B.1 remains valid infrastructure; its role is fallback reconstruction only.

## Approved DIRECTV removal geometry

All coordinates are relative to the 1586 × 992 master.

These bounds are reconstruction limits only. They do not, by themselves, authorize reconstruction.

### Portrait

Core: `x=620 y=78 w=382 h=717`

Approved reconstruction zone: `x=596 y=54 w=430 h=765`

Halo: `24 px`

### TV

Core: `x=913 y=413 w=544 h=397`

Approved reconstruction zone: `x=889 y=389 w=592 h=445`

### Phone

Core: `x=791 y=532 w=132 h=280`

Approved reconstruction zone: `x=767 y=508 w=180 h=328`

### Wall slogan

Core: `x=1044 y=190 w=145 h=135`

Approved reconstruction zone: `x=1020 y=166 w=193 h=183`

### Wall underline

Core: `x=1060 y=338 w=62 h=5`

Approved reconstruction zone: `x=1036 y=314 w=110 h=53`

## Cumulative cleanup rule

When reconstruction stages are actually authorized, cleanup is cumulative:

`Portrait → TV → Phone → Wall slogan → Wall underline`

Later reconstruction stages consume the approved output of the prior authorized reconstruction stage. Do not generate unrelated independent patches from the original master and stack them.

Source recovery or extraction may eliminate some reconstruction work entirely.

## Automated QA requirements

For any authorized reconstruction stage, at minimum:

- validate manifest schema
- validate canvas dimensions
- validate bounds
- validate masks
- prove zero changed pixels outside the approved reconstruction zone
- output dimensions equal source dimensions
- emit candidate image
- emit preview image
- emit difference image
- emit unchanged-region diff
- emit machine-readable report
- exit non-zero on failed automated gate
- human gate remains `PENDING` until reviewed

For `EXTRACT_FROM_MASTER`, the extraction engine must prove exact immutable-master RGB preservation wherever extraction alpha is non-zero and transparent/non-participating pixels outside the extraction mask.

## Development environment status

- DEV-1A — Verify Git / Python 3.12 / GitHub CLI / VS Code — PASS
- DEV-1B — Authenticate GitHub CLI — PASS
- CONT-1 — Create ChatGPT Project — PASS
- CONT-2 — Move active conversation into project — PASS
- CONT-3 — Add ChatGPT Project instructions — PASS
- CONT-4A — Canonical GitHub continuity file — PASS
- CONT-4B — Notion mirror/index — PASS
- CONT-4C — ChatGPT Project continuity pointer/update — PASS
- DEV-2 — Create local Development folder — PASS (`/Users/jimmarkunas/Development`)
- DEV-3 — Clone repository — PASS
- WS-1 / WS-2 — Repository isolation + repo-local `AGENTS.md` guardrails — PASS
- WS-4 — Repository-root / branch / clean-tree preflight — PASS
- DEV-4 — Sync/switch local and remote `feature/3b1-clean-plate-engine` to current protected baseline — PASS
- DEV-5 / WS-3 — Repository-local Python `.venv` using Python 3.12 — PASS (`Python 3.12.14`; recreated after repo relocation and verified at the new path)
- DEV-6 — Integrate repository into the shared multi-root VS Code / AI development environment while preserving repo-local execution boundaries — PASS
- DEV-7 — Add immutable DIRECTV master locally — PASS
- DEV-8 — Validate local environment — PASS

## Workspace isolation rule

The shared VS Code environment may contain multiple sibling repositories, but this project must treat only `/Users/jimmarkunas/Development/Jim/figma-layer-decomposer` as its writable project root. `/Users/jimmarkunas/Development/Jim` and `~/Development` are workspace/container directories only and must not become Git repositories or shared mutation roots. Repo-local `AGENTS.md` defines mandatory agent preflight and cross-repository boundaries. Shared extensions and MCP availability may live at the VS Code environment/profile level; Git state, dependencies, Python environments, project guardrails, and execution remain repository-local.

## Corrected pipeline roadmap

- M2 — Structure — COMPLETE
- 3A — Removal geometry — PASS
- 3A.1 — Remove unapproved wall patches — PASS
- 3B.0 — Clean-plate contract + repo bootstrap — COMPLETE
- 3B.1 — Deterministic clean-plate engine — COMPLETE as fallback infrastructure
- SR-1 — Source asset inventory — COMPLETE
- SR-2 — Provenance / exact-match verification — COMPLETE
- SR-3 — Per-layer decomposition classification — COMPLETE
- SR-4 — Decomposition-plan approval gate — PASS
- ARC-1 — Post-SR architecture checkpoint — PASS WITH MINIMAL ARCHITECTURE ADDITION
- EX-0 — Deterministic master-pixel extraction engine — COMPLETE
- **3B.2A — Validate and promote a trustworthy DIRECTV portrait reconstruction mask — NEXT**
- 3B.2 — Generate DIRECTV portrait clean-plate candidate — only after 3B.2A passes
- 3B.3 — Automated unchanged-region QA
- 3B.4 — Human visual QA
- 3B.5 — Push approved clean plate into Figma
- 3C — TV removal — only if reconstruction remains necessary after extraction/source decisions
- 3D — Phone removal — only if reconstruction remains necessary after extraction/source decisions
- 3E — Wall slogan removal/native rebuild according to approved classification
- 3F — Wall underline removal/native rebuild according to approved classification
- 3G — Full clean-background QA
- 3H — Final approved background
- 4A–4F — Portrait extraction + QA according to `EXTRACT_FROM_MASTER`
- 5A–5I — Device extraction + QA according to `EXTRACT_FROM_MASTER`
- DEP-1 — Deterministic dependency lock/pinning — complete before P1 generalization; pin/lock raster-processing/runtime dependencies for reproducible output
- P1–P4 — Generalize and package for mock-ups #2–#6, preserving the source-first gate

## Current next step

`3B.2A — Validate and promote a trustworthy DIRECTV portrait reconstruction mask.`

Use existing successful portrait-overlay evidence as a candidate input if available, but do not infer approval from its existence. Validate exact mask geometry against the immutable master, foreground exclusions, approved reconstruction zone, and human visual acceptance before any clean-plate candidate run.

Do not perform 3B.2 reconstruction, production extraction, or Figma mutation until 3B.2A passes.

## Continuity protocol

At the start of any new ChatGPT or Codex session:

1. Read `docs/PROJECT_CANON.md` from `main`; if active work exists only on an accepted feature branch, also read the feature-branch canon and the relevant issue/PR.
2. Read `README.md`.
3. Read `docs/SOURCE_ASSET_RECOVERY.md` before any extraction or reconstruction decision.
4. Read `docs/DIRECTV_DECOMPOSITION_PLAN.md` for the approved DIRECTV per-layer classification.
5. Read `docs/ARC_1_ARCHITECTURE_CHECKPOINT.md` before changing package boundaries.
6. Read `docs/CLEAN_PLATE_CONTRACT.md` only when a layer has been authorized for reconstruction.
7. Confirm current Git root, branch, working-tree status, issue, and roadmap before editing.
8. Perform one bounded operation, validate it, then stop.

Update this file whenever the accepted roadmap state, next step, canonical coordinates, source-recovery state, architecture checkpoint state, dependency reproducibility state, or source-of-truth locations materially change.
