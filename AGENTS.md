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

## Execution rules

- One bounded operation → validate → stop.
- Do not skip roadmap stages or repair a failed earlier stage in a later stage.
- Preserve untouched source pixels exactly wherever possible.
- Clean-plate reconstruction happens outside Figma.
- Figma is the destination/composition layer, not the raster reconstruction engine.
- Never overwrite or mutate the immutable master PNG.
- Generated candidates, previews, diffs, reports, masks, and temporary outputs must remain separate from source assets.
- Do not use generative image tooling for approved clean-plate reconstruction.
- No Figma promotion until automated QA and human visual QA pass.
- Fail closed when preconditions, bounds, masks, coordinates, or QA state are uncertain.

## Verification rules

- Never claim a GitHub change, local edit, test result, Figma mutation, artifact, QA gate, or approval unless it was actually performed or verified.
- Before committing or handing off, report the exact files changed and relevant validation results.
- For Figma writes, make the smallest bounded mutation, verify it, return exact affected node IDs, and stop.

## Current project boundary

Current reference: DIRECTV hero, `1586 × 992`.

Current milestone: `M3 Background`.

Current implementation package: `3B.1 — deterministic clean-plate engine`.

Cleanup is cumulative:

`Portrait → TV → Phone → Wall slogan → Wall underline`

For current roadmap state, branch, coordinates, and next action, defer to `docs/PROJECT_CANON.md` rather than duplicating mutable project state here.
