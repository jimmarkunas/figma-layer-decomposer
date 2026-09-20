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
   - `REBUILD_RASTER_FROM_SOURCE`
   - `REBUILD_NATIVE`
   - `RECONSTRUCT_HIDDEN_PIXELS`
5. Do not run reconstruction unless the approved per-layer classification and target-specific contract authorize it.

Clean-plate reconstruction is a fallback capability, not the default decomposition strategy.

If source strategy is unresolved, stop and report `BLOCKED` rather than adding more masking/reconstruction tooling.

## Execution-contract gate

Before any image-affecting operation:

1. Read `docs/EXECUTION_CONTRACT.md`.
2. Load the task-specific YAML execution contract.
3. Validate it against `schema/edit-operation.schema.json`.
4. Verify all immutable input hashes before execution.
5. Confirm the requested tool is explicitly `ALLOWED` by `tool_policy`.
6. Confirm `execution.candidates_allowed` has not been exhausted.
7. If any precondition fails or the requested method is unavailable, stop `BLOCKED`.
8. Never silently substitute another model, tool, source, mask, transform, or method.

For `EXACT_EDIT`:

- `image_gen` is forbidden;
- an authorized mask is required;
- deterministic raster processing only;
- dimensions must remain unchanged;
- changed pixels outside the authorized mask must equal zero;
- exactly one candidate is permitted unless a new contract is approved.

For chat-side image generation, the canonical YAML contract still governs the operation. Before generation, the executor must produce the contract execution receipt defined by `docs/EXECUTION_CONTRACT.md`. Chat-generated output is a candidate only and must re-enter repository QA before promotion.

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
- Fail closed when provenance, preconditions, bounds, masks, coordinates, tool authorization, candidate count, or QA state are uncertain.
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

For current roadmap state, branch, coordinates, source-recovery status, and next action, defer to `docs/PROJECT_CANON.md` rather than duplicating mutable project state here.
