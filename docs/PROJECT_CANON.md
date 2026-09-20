# Figma Layer Decomposer — Project Canon

## Purpose

This file is the canonical continuity handoff for the Figma Layer Decomposer project. It exists so ChatGPT, Codex, local development sessions, and future conversations can recover the current state without relying on one chat transcript.

## Authority order

When sources conflict, use this order:

1. **Immutable master PNG** — visual acceptance authority for reconstruction fidelity.
2. `docs/CLEAN_PLATE_CONTRACT.md` — clean-plate implementation contract.
3. `schema/layer-manifest.schema.json` — machine-readable manifest contract.
4. This file — current project state, accepted decisions, roadmap, and next step.
5. Notion mirror / ChatGPT Project uploads — convenience copies only.

Do not infer approval from the mere existence of an artifact.

The authority order above governs decomposition and faithful reconstruction. After an approved reconstruction is promoted into the canonical Personal Brand Figma library, that canonical Figma template becomes the visual authority for reusable template variants. React and PowerPoint outputs are downstream renderings of the approved template contract; they do not become competing design-system authorities.

## Mission

Turn approved flat mock-up PNGs into genuinely editable layered Figma compositions while preserving 1:1 visual fidelity to the immutable master image.

The business outcome does not stop at decomposition. The decomposer is the recovery and reconstruction front-end for a reusable personal-brand template pipeline: approved concept image → editable Figma reconstruction → reusable canonical Figma template → semantic template contract → React and PowerPoint presentation outputs.

## Product north star

The project succeeds when an approved AI-generated concept can be recovered without losing the visual quality Jim approved, promoted into the existing Jim Markunas Personal Brand design system, and reused repeatedly without reconstructing the composition from scratch.

The intended end-to-end flow is:

`APPROVED CONCEPT PNG → SOURCE RECOVERY / DECOMPOSITION → 1:1 EDITABLE FIGMA → TEMPLATE PROMOTION → SEMANTIC CONTENT CONTRACT → REACT / POWERPOINT`

Product boundaries:

- This repository owns source recovery, decomposition, faithful reconstruction, placement manifests, and the proof that a reconstructed composition can be promoted into a reusable template.
- The existing Jim Markunas Personal Brand Figma file remains the canonical design-system and reusable-template authority. Do not create a second permanent design system inside this repository or the reconstruction workspace.
- The current `JM-Personal-Brand-V2` Figma file is a reconstruction/staging workspace for this project, not a replacement design-system authority.
- React and PowerPoint are downstream consumers of approved templates. They should consume semantic template/content contracts rather than reverse-engineer pixels or invent their own layout rules.
- A successful PowerPoint output must preserve editability of text and replaceable media where practical; a flattened full-slide screenshot is not the target success path.
- Do not generalize through mock-ups #2–#6 merely to prove more decomposition. First prove that the DIRECTV reconstruction can become a reusable template and feed both downstream presentation formats.
- Do not build a generic design compiler, Figma plugin framework, renderer registry, template DSL, bidirectional sync system, or other broad infrastructure before the DIRECTV template-promotion proof demonstrates the exact reusable mechanics actually needed.

## Core rules

- The master PNG is the acceptance authority for faithful reconstruction.
- Do not redesign, reinterpret, beautify, or improve approved mock-ups during reconstruction.
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
- Use ChatGPT for architecture, decomposition strategy, acceptance criteria, source/provenance review, Figma QA, template-promotion QA, and technical review.
- Do not introduce abstractions, services, packages, or infrastructure speculatively. Add reusable architecture only after DIRECTV proves a second real consumer or repeated mechanic.
- Reusable template promotion must consume the canonical Personal Brand design system rather than duplicating brand tokens, typography, components, or visual rules inside the decomposer.

## Repository

- Repository: `https://github.com/jimmarkunas/figma-layer-decomposer`
- Default branch: `main`
- Current implementation branch: `feature/3b2-directv-portrait-candidate` — PAUSED pending source-recovery gate
- Current implementation issue: `#4 — 3B.2 — Generate DIRECTV portrait clean-plate candidate` — PAUSED pending source-recovery gate
- Completed implementation issue: `#1 — 3B.1 — Implement deterministic clean-plate pipeline`
- Local repository path: `/Users/jimmarkunas/Development/Jim/figma-layer-decomposer`
- Product status: standalone product inside the shared Jim development workspace.

## Figma

### Reconstruction workspace

- File: `https://www.figma.com/design/3ZYkEtZVyRH9B2DfVpersf/JM-Personal-Brand-V2?node-id=240-4`
- File key: `3ZYkEtZVyRH9B2DfVpersf`
- Page: `999-1 Asset Rebuild`
- Reference frame: `240:4 — 00_Master_Reference`
- Editable frame: `240:5 — Editable Master Reference 01 — Layered`
- Canvas: `1586 × 992`

### Canonical Personal Brand design system / promotion destination

- Canonical Figma: `https://www.figma.com/design/euxFg8XeKtFJRw7PWOJRWa/JM-Personal-Brand`
- The canonical Personal Brand Figma file owns reusable design-system foundations, components, presentation assets, and promoted templates.
- The decomposer workspace may prove and stage reconstructed assets, but an accepted reusable template must ultimately be promoted into the canonical Personal Brand Figma authority rather than establishing a parallel permanent library.

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

These groups are decomposition/reconstruction structure. Template promotion may map them into semantic template slots and canonical design-system components after the DIRECTV reconstruction passes 1:1 acceptance; do not prematurely redesign the current reconstruction hierarchy around a speculative downstream schema.

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

If the source strategy is unresolved, stop `BLOCKED` rather than increasing fallback-tool complexity.

## Architecture checkpoint

After SR-4 and before production decomposition resumes, run a bounded architecture checkpoint:

- compare the approved DIRECTV decomposition plan against the existing package boundaries;
- identify only reusable mechanics DIRECTV has actually proven are needed;
- extract shared primitives only when there is a real second consumer or demonstrated duplication;
- keep `cleanplate` as a focused fallback subsystem rather than turning it into a general orchestration monolith;
- do not add speculative services, queues, databases, UI frameworks, plugin systems, abstract factories, or package layers;
- explicitly decide whether source recovery/provenance, extraction, QA, manifest handling, and orchestration need reusable modules now or should remain deferred;
- record any approved architecture changes before implementation resumes.

This checkpoint is a scalability guardrail, not a refactor mandate. If the current structure is sufficient, the correct result is `NO CHANGE`.

Before P1 generalization, add a reproducibility checkpoint that pins/locks runtime dependencies used for deterministic raster output. The lock/pin must cover at least Pillow, NumPy, OpenCV, and jsonschema, and must not interrupt the current DIRECTV proof unless a version mismatch is actively causing non-deterministic behavior.

## Template Promotion & Consumption proof

**TP-1 is a required business-case gate after the complete DIRECTV editable reconstruction passes and before broad generalization to mock-ups #2–#6.** It is not active implementation while DIRECTV source recovery/reconstruction remains unfinished.

### Activation gate

- The DIRECTV composition has been reconstructed as a genuinely editable Figma composition.
- Full-frame human visual QA confirms the reconstructed DIRECTV composition preserves the approved master at the required fidelity.
- The reconstruction contains the editable/native elements required for practical reuse rather than only a stack of flattened raster layers.

### User outcome

Starting from the accepted DIRECTV reconstruction, Jim can create a new branded presentation variant without reconstructing the design, then use the same template semantics to produce both a React presentation slide and an editable PowerPoint slide.

### Minimum semantic template roles

TP-1 must define the smallest useful semantic contract for the roles actually present in the accepted template. Expected roles include, where applicable:

- background / environment
- portrait / subject
- primary media or device
- secondary media or device
- eyebrow / label
- headline
- supporting copy
- metrics collection
- environmental message / wall treatment
- process strip / steps
- signature / footer

The exact schema, file name, or serialization format is deliberately deferred until TP-1 implementation. Do not retrofit the current decomposition manifest into a generic template DSL before the real template proof shows what is required.

### Required proof

1. **Canonical Figma promotion** — promote the accepted DIRECTV reconstruction into the existing canonical Personal Brand Figma library as a reusable template/component pattern, with no second permanent design-system authority.
2. **Content substitution** — create at least one non-DIRECTV variant from the promoted template by changing the project/company identity, headline/supporting copy, at least two metrics, and at least one major portrait/media/device asset without rebuilding the composition from scratch.
3. **Brand-system binding** — reusable typography, colors, spacing, components, and other brand mechanics must reference or conform to the canonical Personal Brand design system rather than creating decomposer-owned duplicates.
4. **Semantic consumption** — define one bounded content/template contract that can populate the approved template without downstream consumers scraping Figma pixels or layer names ad hoc.
5. **React proof** — render one presentation slide from the promoted template semantics in the approved React presentation path.
6. **PowerPoint proof** — render one PowerPoint slide from the same template semantics; text must remain editable and major media must remain replaceable where practical. A single flattened slide image does not satisfy this requirement.
7. **Visual acceptance** — Figma variant, React output, and PowerPoint output must preserve the approved template's recognizable composition, hierarchy, typography, and brand treatment. Renderer-specific deterministic checks and any cross-render tolerance may be defined during TP-1 because browser, Figma, and PowerPoint font/rendering engines differ.
8. **Reuse proof** — producing the variant must not require a new one-off reconstruction pipeline or hand-coded layout rewrite specific to the new content.

### TP-1 failure conditions

TP-1 is not accepted if:

- the DIRECTV reconstruction can only be reused by manually rebuilding its layout;
- the reusable template lives only in the reconstruction workspace and creates a second permanent brand library;
- React and PowerPoint each require unrelated one-off layout definitions rather than consuming the same bounded template semantics;
- PowerPoint is accepted only as a flattened screenshot;
- template promotion requires speculative generic infrastructure before a concrete second template/consumer proves the need.

### Non-goals for TP-1

TP-1 does not require:

- a universal Figma-to-code compiler;
- bidirectional Figma ↔ React ↔ PowerPoint synchronization;
- arbitrary third-party design import;
- an entire presentation-deck generator;
- a generic plugin framework or template registry;
- full automation of every future mock-up;
- decomposition of mock-ups #2–#6 before the reuse proof passes.

## Completed work

### M2 — Structure

- 2A — Verify source + editable frames — PASS
- 2B — Verify top-level groups — PASS
- 2C — Verify locked master reference — PASS
- 2D — Audit internal production structure — PASS
- 2E — Full-resolution structure QA — PASS WITH FINDING

### M3 — Background

- 3A — Define exact removal geometry — PASS
- 3A.1 — Remove unapproved wall cleanup patches — PASS
- 3B.0 — Canonical clean-plate contract + repo bootstrap — COMPLETE
- 3B.1 — Deterministic clean-plate engine — COMPLETE as reusable fallback subsystem
- 3B.2 — Generate DIRECTV portrait clean-plate candidate — PAUSED pending SR-1 through SR-4

### Corrective findings

- The initial 3B.2 GrabCut portrait-mask candidate failed human visual review and is REJECTED.
- The failed GrabCut mask remains unapproved and must not be promoted or used for production reconstruction.
- A semantic-segmentation replacement is NOT the next authorized step.
- The architectural error was treating clean-plate reconstruction as the default path before proving source recovery was insufficient.
- 3B.1 remains valid infrastructure; its role is fallback reconstruction only.

## Approved DIRECTV removal geometry

All coordinates are relative to the 1586 × 992 master.

These bounds are reconstruction limits only. They do not, by themselves, authorize reconstruction; SR-4 must authorize the layer first.

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

Source recovery may eliminate some reconstruction stages entirely.

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
- SR-1 — Source asset inventory — COMPLETE for current DIRECTV inventory scope
- **SR-2 — Provenance / exact-match verification — ACTIVE**
- SR-3 — Per-layer decomposition classification
- SR-4 — Decomposition-plan approval gate
- **ARC-1 — Post-SR architecture checkpoint** — review package boundaries and add only proven reusable primitives; `NO CHANGE` is an acceptable result
- 3B.2 — Generate DIRECTV portrait clean-plate candidate — RESUME ONLY if portrait/background hidden pixels are classified `RECONSTRUCT_HIDDEN_PIXELS`
- 3B.3 — Automated unchanged-region QA
- 3B.4 — Human visual QA
- 3B.5 — Push approved clean plate into Figma
- 3C — TV removal — only if reconstruction remains necessary after SR
- 3D — Phone removal — only if reconstruction remains necessary after SR
- 3E — Wall slogan removal — reconstruction/native method determined by SR classification
- 3F — Wall underline removal — reconstruction/native method determined by SR classification
- 3G — Full clean-background QA
- 3H — Final approved background
- 4A–4F — Portrait recovery/extraction + QA according to SR classification
- 5A–5I — Device recovery/extraction + QA according to SR classification
- **DTV-FINAL — Complete editable DIRECTV reconstruction + full-frame 1:1 visual acceptance**
- **TP-1 — Template Promotion & Consumption Proof** — promote the accepted reconstruction into the canonical Personal Brand Figma library, prove a non-DIRECTV reusable variant, then prove one React slide and one editable PowerPoint slide from the same semantic template contract
- **DEP-1 — Deterministic dependency lock/pinning** — complete before P1 generalization; pin/lock raster-processing/runtime dependencies for reproducible output
- **P1–P4 — Generalize and package for mock-ups #2–#6 only after TP-1 is ACCEPTED**, preserving the source-first gate and treating each additional mock-up as a candidate reusable template rather than decomposition-only output

## Current next step

`SR-2 — Provenance / exact-match verification for the DIRECTV portrait candidates.`

Do not generate another portrait mask or clean-plate candidate before SR-1 through SR-4 and ARC-1 are complete.

TP-1 is canonized but inactive. Do not start template-promotion, React-renderer, or PowerPoint-renderer implementation until the DIRECTV reconstruction reaches `DTV-FINAL` acceptance.

## Continuity protocol

At the start of any new ChatGPT or Codex session:

1. Read `docs/PROJECT_CANON.md` from `main`.
2. Read `README.md`.
3. Read `docs/SOURCE_ASSET_RECOVERY.md` before any extraction or reconstruction decision.
4. Read `docs/CLEAN_PLATE_CONTRACT.md` only when a layer has been authorized for reconstruction.
5. Confirm current Git root, branch, working-tree status, issue, and roadmap before editing.
6. Perform one bounded operation, validate it, then stop.

Update this file whenever the accepted roadmap state, next step, canonical coordinates, source-recovery state, architecture checkpoint state, dependency reproducibility state, template-promotion state, downstream-consumption proof, or source-of-truth locations materially change.
