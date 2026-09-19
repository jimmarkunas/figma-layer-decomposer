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
- Clean-plate reconstruction happens outside Figma using the `figma-layer-decomposer` pipeline.
- Figma is the destination and composition layer, not the raster-reconstruction engine.
- Every raster layer must have deterministic coordinates and a machine-readable manifest.
- No Figma upload or promotion occurs until automated QA and human visual QA pass.
- Later steps may not repair failed earlier steps.
- Work incrementally: one bounded operation → validate → stop.
- Prefer deterministic scripting, masks, pixel diffs, and repeatable tooling over manual approximation.
- Use Codex for bounded local implementation tasks involving image processing, tests, manifests, file operations, and automation.
- Use ChatGPT for architecture, decomposition strategy, acceptance criteria, Figma QA, and technical review.

## Repository

- Repository: `https://github.com/jimmarkunas/figma-layer-decomposer`
- Default branch: `main`
- Current implementation branch: `feature/3b1-clean-plate-engine`
- Current implementation issue: `#1 — 3B.1 — Implement deterministic clean-plate pipeline`

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
- 3B.1 — Deterministic clean-plate engine — NEXT IMPLEMENTATION PACKAGE

## Approved DIRECTV removal geometry

All coordinates are relative to the 1586 × 992 master.

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

The cleanup sequence is cumulative:

`Portrait → TV → Phone → Wall slogan → Wall underline`

Later stages consume the approved output of the prior stage. Do not generate unrelated independent patches from the original master and stack them.

## Automated QA requirements

At minimum:

- validate manifest schema
- validate canvas dimensions
- validate bounds
- validate masks
- zero changed pixels outside approved reconstruction zone
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
- CONT-4A — Canonical GitHub continuity file — COMPLETE when this file is merged/present on `main`
- CONT-4B — Notion mirror/index — pending
- CONT-4C — ChatGPT Project continuity pointer/update — pending
- DEV-2 — Create local Development folder — pending
- DEV-3 — Clone repository — pending
- DEV-4 — Sync/switch to `feature/3b1-clean-plate-engine` — pending
- DEV-5 — Create Python `.venv` — pending
- DEV-6 — Configure VS Code + Codex — pending
- DEV-7 — Add immutable DIRECTV master locally — pending
- DEV-8 — Validate local environment — pending

## Pipeline roadmap

- 3B.1 — Codex implements deterministic clean-plate engine
- 3B.2 — Generate DIRECTV portrait clean-plate candidate
- 3B.3 — Automated QA
- 3B.4 — Human visual QA
- 3B.5 — Push approved clean plate into Figma
- 3C — TV removal
- 3D — Phone removal
- 3E — Wall slogan removal
- 3F — Wall underline removal
- 3G — Full clean-background QA
- 3H — Final approved background
- 4A–4F — Portrait extraction + QA
- 5A–5I — Device extraction + QA
- P1–P4 — Generalize and package for mock-ups #2–#6

## Current next step

`CONT-4B — Create a Notion mirror/index that points back to this GitHub canon.`

After continuity setup is complete:

`DEV-2 — Create the local Development folder.`

## Continuity protocol

At the start of any new ChatGPT or Codex session:

1. Read `docs/PROJECT_CANON.md` from `main`.
2. Read `README.md`.
3. Read `docs/CLEAN_PLATE_CONTRACT.md` when working on M3 clean-plate implementation.
4. Confirm current branch / issue / roadmap before editing.
5. Perform one bounded operation, validate it, then stop.

Update this file whenever the accepted roadmap state, next step, canonical coordinates, or source-of-truth locations materially change.