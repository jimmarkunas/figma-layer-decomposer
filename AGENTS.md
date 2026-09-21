# Figma Layer Decomposer — Agent Guardrails

Repository: `jimmarkunas/figma-layer-decomposer`

## Mandatory preflight

Before any mutation:

1. Read `docs/PROJECT_CANON.md`.
2. Read `docs/DECOMPOSITION_FIRST_VISUAL_ARCHITECTURE_CONTRACT.md` for the shared new/legacy layered-composition architecture.
3. Read `docs/EXECUTION_CONTRACT.md` when it exists for the active package.
4. Confirm the active Git root is this repository with `git rev-parse --show-toplevel`.
5. Confirm active branch and working-tree status.
6. If the Git root is not this repository, stop and report `BLOCKED`.
7. If the working tree contains changes, classify them:
   - overlapping/unexplained changes inside the intended mutation surface are a blocker;
   - known unrelated changes must be preserved and left untouched, but are not by themselves a blocker.
8. Do not treat `~/Development` or a multi-root VS Code workspace as the project root.

## Canonical authority

When sources conflict, use this order:

1. Jim's explicit current instruction in the active session.
2. Immutable master PNG for visual acceptance.
3. `docs/PROJECT_CANON.md` for current accepted product state.
4. `docs/DECOMPOSITION_FIRST_VISUAL_ARCHITECTURE_CONTRACT.md` for shared decomposition-first architecture, including the legacy full-background exception and mask rule.
5. `docs/EXECUTION_CONTRACT.md` for the active task's inputs, tool policy, candidate limit, QA and promotion state.
6. `docs/CLEAN_PLATE_CONTRACT.md` only when the current execution contract explicitly puts hidden-background reconstruction in scope.
7. `schema/layer-manifest.schema.json` for machine-readable placement/QA contracts.
8. Active GitHub issue text only when `docs/PROJECT_CANON.md` explicitly names it as the current delivery package.
9. Notion / ChatGPT Project copies as pointers only.

Never infer approval from the mere existence of an artifact.

## Product output constraint

The product converts a flattened concept into a reusable layered design.

Canonical output stack:

1. Full clean background
2. Editorial / environmental effects
3. Portrait / subject
4. Devices / graphic overlays
5. Editable UI / typography

Every development task must directly advance one or more of these outputs.

If a proposed task does not directly advance the layer stack, stop with:

`STOP — NON-PRODUCT WORK`

Do not execute it without explicit approval.

## Layer-first rule

Always solve the problem as ordinary layered composition first.

Preferred order:

1. recover an existing source asset;
2. rebuild semantically editable content as native Figma layers;
3. generate/rebuild a complete independent layer when source pixels do not exist;
4. compose the layers;
5. compare the reconstruction against the locked reference.

Do not default to forensic recovery of hidden pixels from the flattened image.

If a complete layer can solve the requirement, build the complete layer instead of reconstructing local holes.

## Mask rule

Masks are implementation details only.

They may be used temporarily inside a tool when required, but they must not become:

- product artifacts;
- roadmap items;
- persistent Figma structures;
- GitHub handoff packages;
- user-reviewed assets;
- named development phases;
- cross-agent coordination objects.

If Jim has to inspect, transfer, approve, name, or reason about a mask:

`ARCHITECTURAL DRIFT DETECTED — NO MUTATION`

## Pre-mutation drift gate

Before every consequential mutation, resolve all three fields:

- `PRODUCT LAYER:` 01 / 02 / 03 / 04 / 05
- `TARGET ACCEPTANCE TEST:` exact test from the active execution contract
- `METHOD:` one sentence

If any answer is unclear, do not mutate.

The active execution contract's user-visible acceptance test is more important than implementation technique.

## Two-failure circuit breaker

If the same technical strategy fails materially twice:

STOP.

Do not create attempt 3, V4/V5, another mask, another package, another prompt sweep, or another coordination artifact.

Report:

- `FAILED STRATEGY:`
- `PRODUCT OUTPUT STILL NEEDED:`
- `SIMPLER ALTERNATIVE:`

Then return to the product acceptance test and choose the simplest sufficient method.

## No workaround cascades

A blocker does not authorize new architecture.

When blocked:

1. identify the exact missing capability;
2. attempt the smallest direct workaround allowed by the active contract;
3. if unavailable, report the blocker.

Do not respond to a transfer problem by creating a new reconstruction method.
Do not respond to a generation problem by creating a new datastore.
Do not respond to a Figma problem by redesigning the product architecture.

## Jim is never middleware

Jim must never be required to:

- rename intermediate assets;
- manually move agent files;
- determine which anonymous image belongs to which slot;
- reconcile conflicting versions;
- act as binary transport between executors.

If automation cannot complete a handoff, report:

`BLOCKED — <specific missing transport capability>`

Do not convert Jim into the workaround.

## Repository isolation

- Read/write only inside this repository unless Jim explicitly requests cross-repository work.
- Do not modify sibling repositories, shared workspace files, global VS Code settings, shell profiles, or global Python environments.
- Cross-repository reads require explicit task scope; cross-repository writes require explicit approval.
- Keep project dependencies and tooling repository-local.

## Source recovery

Source recovery remains preferred when an authoritative source exists, but it is subordinate to the active execution contract and layer-first product goal.

Use `docs/SOURCE_ASSET_RECOVERY.md` when recovery is actually needed.

Do not force a source-recovery or hidden-pixel workflow when a complete independent layer is the approved output.

## Promotion handoff boundary

This repository terminates at `PROMOTION_READY` for reusable Personal Brand work.

Before claiming reusability or promoting into canonical Personal Brand Figma, read `docs/PROMOTION_HANDOFF_CONTRACT.md`.

The reconstruction/staging file `JM-Personal-Brand-V2` is not the permanent design-system authority. Promoted reusable templates belong in canonical `JM-Personal-Brand` Figma under PBDS ownership.

## Execution rules

- One bounded delivery package → inspect → execute → validate internally → correct deterministic defects within the package → stop at the acceptance gate or a genuine blocker.
- Do not stop after every internal step merely because an intermediate artifact exists.
- Do not skip unresolved permission/provenance gates.
- Do not re-run historical stages that are complete or superseded.
- Never overwrite the immutable master PNG.
- Preserve accepted source assets unless a specific material defect is proven.
- Figma is the destination/composition layer, not a reason to invent a new raster pipeline.
- No `PROMOTION_READY` claim until the active execution contract's QA passes.
- Fail closed when a consequential target/source/permission is genuinely ambiguous.
- Do not optimize/generalize a fallback technique before proving it is required.

## Verification rules

- Never claim a GitHub change, local edit, test result, Figma mutation, artifact, QA gate, or approval unless actually performed or verified.
- Before committing/handing off, report exact files changed and relevant validation results.
- For Figma writes, verify consequential mutations directly and report exact affected node IDs at package completion.

## Current project boundary

Current reference: DIRECTV hero, `1586 × 992`.

Current staging file: `JM-Personal-Brand-V2` (`3ZYkEtZVyRH9B2DfVpersf`).

Active reconstruction workspace:

- page `155:63 — 999 - Test 2`
- immutable reference `160:3 — DIRECTV / REFERENCE — LOCKED`
- production target `160:4 — DIRECTV / PRODUCTION — EDITABLE`

Current milestone: DIRECTV end-to-end layered reconstruction to a `PROMOTION_READY` candidate.

For exact current execution, defer to `docs/EXECUTION_CONTRACT.md`.
