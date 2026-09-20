# Figma Layer Decomposer — Agent Guardrails

Repository: `jimmarkunas/figma-layer-decomposer`

## Mandatory preflight

Before any mutation:

1. Read `docs/PROJECT_CANON.md` from this repository.
2. Confirm the active Git root is this repository with `git rev-parse --show-toplevel`.
3. Confirm the active branch and working-tree status.
4. If the Git root is not this repository, stop and report `BLOCKED`.
5. If the working tree contains changes, classify them before acting:
   - overlapping or unexplained changes inside the intended mutation surface are a blocker;
   - known unrelated changes must be preserved, reported, and left untouched, but are not by themselves a blocker.
6. Do not treat `~/Development` or any multi-root VS Code workspace as the project root.

## Repository isolation

- Read and write only inside this repository unless Jim explicitly requests cross-repository work.
- Do not modify sibling repositories, shared workspace files, global VS Code settings, shell profiles, or global Python environments as part of this project.
- Cross-repository reads require explicit task scope; cross-repository writes require explicit approval.
- Keep project dependencies and tooling repository-local.

## Canonical authority

When sources conflict, use this order:

1. Jim's explicit current instruction in the active session.
2. Immutable master PNG for reconstruction fidelity.
3. `docs/PROJECT_CANON.md` for current product state, active delivery package, Figma target, and current authorization.
4. `docs/CLEAN_PLATE_CONTRACT.md` when hidden-background reconstruction is actually in scope.
5. `schema/layer-manifest.schema.json` for machine-readable placement and QA contracts.
6. Active GitHub issue text only when it is explicitly named as the current delivery package by `docs/PROJECT_CANON.md`.
7. Notion / ChatGPT Project copies as pointers only.

Never infer approval from the mere existence of an artifact.

## Source-first decomposition gate

Before extraction, masking, inpainting, or other clean-plate reconstruction for any layer:

1. Read `docs/SOURCE_ASSET_RECOVERY.md`.
2. Attempt source-asset recovery in the approved search order.
3. Verify candidate provenance/alignment against the immutable master.
4. Classify the layer as exactly one of:
   - `RECOVER_SOURCE`
   - `EXTRACT_FROM_MASTER`
   - `REBUILD_NATIVE`
   - `RECONSTRUCT_HIDDEN_PIXELS`
5. Do not run reconstruction unless the layer is explicitly classified `RECONSTRUCT_HIDDEN_PIXELS` and the reason source recovery was insufficient is recorded.

Clean-plate reconstruction is a fallback capability, not the default decomposition strategy.

When `docs/PROJECT_CANON.md` explicitly authorizes hidden-pixel reconstruction for the current delivery package, deriving an exact occupancy/removal mask from a verified foreground asset or verified native Figma layer is authorized implementation work. A second bespoke mask-approval document is not required.

If source strategy is genuinely unresolved, stop and report `BLOCKED` rather than adding more masking/reconstruction tooling.

## Promotion handoff boundary

This repository terminates at `PROMOTION_READY` for reusable Personal Brand work.

Before any task that claims a reconstruction is reusable, promotes or proposes promotion into canonical Personal Brand Figma, defines a semantic template contract, or implements React/PowerPoint consumption:

1. Read `docs/PROMOTION_HANDOFF_CONTRACT.md`.
2. Confirm whether the artifact is still `RECONSTRUCTION_ACTIVE` or has reached `PROMOTION_READY`.
3. If the task starts after `PROMOTION_READY`, treat Personal Career Brand / PBDS-4 as the owning product context.
4. Do not implement PBDS-owned reusable-template, semantic-contract, React-renderer, or PowerPoint-renderer work inside this repository merely because the source reconstruction originated here.
5. Do not duplicate Personal Brand doctrine, the PBDS roadmap, or canonical Figma design-system rules into this repository. Follow the handoff pointers instead.

The reconstruction/staging file `JM-Personal-Brand-V2` is not the permanent design-system authority. Promoted reusable templates belong in canonical `JM-Personal-Brand` Figma under PBDS ownership.

## Execution rules

- One bounded delivery package → inspect → execute → validate internally → correct deterministic defects within the package → stop at the package acceptance gate or a genuine blocker.
- A delivery package may contain multiple deterministic implementation steps and multiple verified Figma mutations. Do not stop after every internal step merely because an intermediate artifact was produced.
- Do not skip unresolved permission/provenance gates, but do not re-run historical stages that `docs/PROJECT_CANON.md` records as complete or superseded.
- Preserve untouched source pixels exactly wherever possible.
- Prefer exact recovered source assets over extraction; prefer extraction over reconstruction when the required pixels already exist in the immutable master.
- Clean-plate reconstruction happens outside Figma and only after the source-recovery gate authorizes it.
- Figma is the destination/composition layer, not the raster reconstruction engine.
- Never overwrite or mutate the immutable master PNG.
- Generated candidates, previews, diffs, reports, masks, and temporary outputs must remain separate from source assets.
- Do not use generative image tooling for approved clean-plate reconstruction unless `docs/PROJECT_CANON.md` explicitly authorizes a bounded source-guided reconstruction path for the current asset.
- No `PROMOTION_READY` or canonical Figma promotion claim until required automated QA and human visual QA pass.
- Fail closed when a consequential target, source, bounds, or permission is genuinely ambiguous and cannot be resolved from the current package evidence.
- Do not optimize or generalize a fallback technique before proving that the fallback is actually required for the layer.

## Verification rules

- Never claim a GitHub change, local edit, test result, Figma mutation, artifact, QA gate, or approval unless it was actually performed or verified.
- Before committing or handing off, report the exact files changed and relevant validation results.
- For Figma writes, make only mutations inside the authorized delivery package. Verify consequential mutations directly, continue correcting within the package when defects are deterministic, and report the exact affected node IDs at package completion.

## Current project boundary

Current reference: DIRECTV hero, `1586 × 992`.

Current staging file: `JM-Personal-Brand-V2` (`3ZYkEtZVyRH9B2DfVpersf`).

Current active reconstruction workspace:

- page `155:63 — 999 - Test 2`
- immutable reference `160:3 — DIRECTV / REFERENCE — LOCKED`
- production target `160:4 — DIRECTV / PRODUCTION — EDITABLE`

The older `240:4 / 240:5` workspace is historical staging and is not the active DIRECTV target.

Current milestone: DIRECTV end-to-end reconstruction to a `PROMOTION_READY` candidate.

For current accepted assets, rejected/superseded artifacts, reconstruction authorization, exact package exit, and next action, defer to `docs/PROJECT_CANON.md` rather than duplicating mutable project state here.
