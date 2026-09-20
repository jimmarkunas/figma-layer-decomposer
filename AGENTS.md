# Figma Layer Decomposer — Agent Guardrails

Repository: `jimmarkunas/figma-layer-decomposer`

## Mandatory preflight

Before any mutation:

1. Read `docs/PROJECT_CANON.md` from this repository.
2. Confirm the active Git root is this repository with `git rev-parse --show-toplevel`.
3. Confirm the active branch and working-tree status.
4. If the Git root is not this repository, or the working tree contains unexplained changes, stop and report `BLOCKED`.
5. Do not treat `~/Development` or any multi-root VS Code workspace as the project root.

## Repository isolation

- Read and write only inside this repository unless Jim explicitly requests cross-repository work.
- Do not modify sibling repositories, shared workspace files, global VS Code settings, shell profiles, or global Python environments as part of this project.
- Cross-repository reads require explicit task scope; cross-repository writes require explicit approval.
- Keep project dependencies and tooling repository-local.

## Canonical authority

When sources conflict, use this order:

1. Immutable master PNG
2. `docs/CLEAN_PLATE_CONTRACT.md`
3. `schema/layer-manifest.schema.json`
4. `docs/PROJECT_CANON.md`
5. Notion / ChatGPT Project copies

Never infer approval from the existence of an artifact.

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

If source strategy is unresolved, stop and report `BLOCKED` rather than adding more masking/reconstruction tooling.

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

- One bounded operation → validate → stop.
- Do not skip roadmap stages or repair a failed earlier stage in a later stage.
- Preserve untouched source pixels exactly wherever possible.
- Prefer exact recovered source assets over extraction; prefer extraction over reconstruction when the required pixels already exist in the immutable master.
- Clean-plate reconstruction happens outside Figma and only after the source-recovery gate authorizes it.
- Figma is the destination/composition layer, not the raster reconstruction engine.
- Never overwrite or mutate the immutable master PNG.
- Generated candidates, previews, diffs, reports, masks, and temporary outputs must remain separate from source assets.
- Do not use generative image tooling for approved clean-plate reconstruction.
- No Figma promotion until automated QA and human visual QA pass.
- Fail closed when provenance, preconditions, bounds, masks, coordinates, or QA state are uncertain.
- Do not optimize or generalize a fallback technique before proving that the fallback is actually required for the layer.

## Verification rules

- Never claim a GitHub change, local edit, test result, Figma mutation, artifact, QA gate, or approval unless it was actually performed or verified.
- Before committing or handing off, report the exact files changed and relevant validation results.
- For Figma writes, make the smallest bounded mutation, verify it, return exact affected node IDs, and stop.

## Current project boundary

Current reference: DIRECTV hero, `1586 × 992`.

Current milestone: `M3 Background`.

Cleanup, when reconstruction is actually authorized, is cumulative:

`Portrait → TV → Phone → Wall slogan → Wall underline`

For current roadmap state, branch, coordinates, source-recovery status, next action, and promotion-terminal state, defer to `docs/PROJECT_CANON.md` rather than duplicating mutable project state here.
