# Figma Layer Decomposer → Personal Brand Design System — Promotion Handoff Contract

## Purpose

This contract defines the ownership boundary between the independent `figma-layer-decomposer` project and the Jim Markunas Personal Brand Design System (PBDS) inside LIFE OS.

The decomposer recovers and faithfully reconstructs approved visual concepts. PBDS owns what happens once a reconstruction is ready to become a reusable Jim Markunas design-system asset.

## Canonical ownership split

### Figma Layer Decomposer owns

- source asset inventory and provenance
- exact-match verification
- per-layer decomposition classification
- raster extraction
- fallback hidden-pixel reconstruction where explicitly authorized
- deterministic manifests and coordinates
- automated fidelity QA
- human visual-acceptance evidence
- editable reconstruction in the staging/reconstruction Figma workspace
- the bounded `PROMOTION_READY` handoff package

### PBDS / Personal Career Brand owns after handoff

- promotion into the canonical `JM-Personal-Brand` Figma file
- reusable template/component definition
- canonical visual-template identity
- semantic content/template contract
- React presentation consumption
- PowerPoint presentation consumption
- cross-surface reuse and later template-library expansion

The decomposer must not create a second permanent design system, renderer architecture, presentation framework, or downstream template authority.

## Lifecycle states

`RECONSTRUCTION_ACTIVE → PROMOTION_READY → PROMOTED → CONSUMABLE`

- `RECONSTRUCTION_ACTIVE` — Decomposer owns the artifact.
- `PROMOTION_READY` — decomposition/reconstruction, editability, provenance, and visual acceptance are complete enough for PBDS to evaluate promotion.
- `PROMOTED` — PBDS has accepted the reusable pattern into canonical `JM-Personal-Brand` Figma. PBDS becomes authoritative from this point forward.
- `CONSUMABLE` — PBDS has defined the bounded semantic template contract and approved downstream consumers can populate the template without reverse-engineering pixels or ad-hoc layer names.

## `PROMOTION_READY` acceptance

A reconstruction may enter `PROMOTION_READY` only when all applicable conditions are satisfied:

1. The immutable master/reference is identified and preserved.
2. Required source-recovery and provenance work is complete.
3. Every material layer has an accepted implementation classification.
4. The reconstructed composition is genuinely editable where editability is required for reuse.
5. Automated fidelity/unchanged-region QA has passed for all applicable reconstruction work.
6. Human full-frame visual QA has accepted the reconstruction against the immutable master.
7. The staging Figma file/frame is identified precisely.
8. The handoff identifies which visual roles are native/editable, replaceable raster/media, fixed brand elements, or reconstruction-only artifacts.
9. Relevant source/provenance manifests and Git commit/revision are referenced.
10. No unresolved fidelity or provenance ambiguity is represented as accepted.

## Minimum handoff package

The exact serialization format may evolve, but the handoff must communicate at least:

- source mock-up / master identity
- immutable master hash or other deterministic identity where available
- decomposer Git commit or accepted revision
- staging Figma file + exact frame/node
- full-frame fidelity QA result
- human visual QA result
- relevant provenance/source records
- relevant placement/decomposition manifests
- semantic-candidate layer roles, without redefining PBDS semantics
- editable/native roles
- replaceable media/raster roles
- fixed/background/reconstruction-only roles
- known constraints or exceptions
- canonical PBDS promotion target

## Semantic-candidate roles

The decomposer may describe obvious candidate roles to make the handoff legible, for example:

- background / environment
- portrait / subject
- primary media / device
- secondary media / device
- eyebrow / label
- headline
- supporting copy
- metrics
- environmental message
- process strip
- signature / footer

These descriptions are handoff metadata only. PBDS owns the final semantic contract and may rename, merge, split, or bind roles to canonical components after promotion.

## Canonical destination

- Reconstruction/staging workspace: `JM-Personal-Brand-V2`
- Canonical reusable design-system authority: `JM-Personal-Brand`
- LIFE OS durable product owner: Personal Career Brand / PBDS-4 — Canonical Figma Library

A reusable template is not considered promoted merely because it exists in the reconstruction workspace.

## Context-continuity rule

Do not duplicate the full PBDS roadmap, brand doctrine, or downstream renderer implementation in this repository.

The decomposer should retain only:

- this handoff contract;
- the pointer to the PBDS owner;
- source/provenance/reconstruction evidence;
- the terminal state `PROMOTION_READY`.

PBDS should retain only the accepted promotion pointer back to the decomposer source package, not a copy of the decomposer implementation roadmap.

## Agent rule

Any agent working in this repository must read this file before:

- claiming a reconstruction is reusable as a Personal Brand template;
- promoting or proposing promotion into canonical `JM-Personal-Brand` Figma;
- defining semantic template contracts;
- implementing React or PowerPoint rendering;
- generalizing a reconstruction into a downstream Personal Brand template system.

If the requested task starts after `PROMOTION_READY`, the agent must treat PBDS / Personal Career Brand as the owning product context and must not continue implementation inside the decomposer merely because the source artifact originated here.

## Non-goals

This handoff does not authorize:

- a generic Figma-to-code compiler;
- a generic template DSL;
- a renderer registry;
- bidirectional Figma/React/PowerPoint synchronization;
- a second design-system store;
- broad multi-repository mutation from this project;
- downstream PBDS implementation before the relevant LIFE OS package is activated.
