# Figma Layer Decomposer — Agent Guardrails

Repository: `jimmarkunas/figma-layer-decomposer`

## Mandatory preflight

Before mutation:

1. Read `docs/PROJECT_CANON.md`.
2. If BRIDGE-1 or user-entry-point backend work is in scope, read `docs/BRIDGE_CONTRACT.md`.
3. If DIRECTV reconstruction work is in scope, read `docs/EXECUTION_CONTRACT.md`.
4. Read other generic contracts only when the active canon/package explicitly invokes them.
5. Confirm this repository is the active Git root, then confirm branch and working-tree status.
6. Overlapping unexplained local changes block mutation; known unrelated changes must be preserved.

## Authority

1. Jim's explicit current instruction.
2. Immutable visual reference for fidelity decisions.
3. `docs/PROJECT_CANON.md`.
4. Active package contract: `docs/BRIDGE_CONTRACT.md` or `docs/EXECUTION_CONTRACT.md`.
5. Machine-readable schemas/manifests.
6. Historical issues, old handoffs, rejected artifacts, prior chats.

Notion is a pointer/index for this project. GitHub canon is authoritative.

## Product output

The product turns a flattened concept into a faithful, editable Figma design using the canonical layer model:

1. Full clean background
2. Editorial/environmental effects
3. Portrait/subject
4. Devices/graphic overlays
5. Editable UI/typography

Ordinary reconstruction work must directly advance those outputs.

### Explicit infrastructure exception — BRIDGE-1

`BRIDGE-1` is **authorized product infrastructure**, not `STOP — NON-PRODUCT WORK`.

It exists solely to make the approved user entry point executable:

```text
Jim
→ Figma Decomposer ChatGPT Project chat
→ Decomposer Bridge
→ ChatGPT/Figma Connector
→ Figma
```

Bridge work is valid only when it directly implements the bounded responsibilities in `docs/BRIDGE_CONTRACT.md`: job identity/state, binary artifact handling, image-generation adapter, deterministic QA/provenance, placement result, and one public reconstruction operation.

Do not use this exception to build a generic agent framework, scheduler, second Figma stack, permanent duplicate datastore, or unrelated platform infrastructure.

## Reconstruction rules

Prefer, in order:

1. recover an authoritative source asset;
2. rebuild semantic UI/text/vector content natively;
3. generate/rebuild a complete independent visual layer when source pixels do not exist;
4. compose deterministically;
5. compare with the immutable reference.

Do not default to forensic hidden-pixel recovery. Masks may exist transiently inside tools, but they are not product artifacts, roadmap items, persistent Figma structures, or user-reviewed/cross-agent coordination objects.

## Two-failure circuit breaker

If the same strategy fails materially twice, stop that strategy. Do not create attempt 3, V4/V5, another mask package, prompt sweep, or coordination artifact. Return to the product output and use the simplest sufficient alternative.

## No workaround cascades

A blocker does not authorize new architecture.

- transfer problem ≠ new reconstruction system;
- generation problem ≠ new datastore/orchestrator;
- Figma problem ≠ second Figma integration stack.

Report the exact missing capability and use the smallest allowed workaround.

## Jim is never middleware

Jim must never be required to rename, move, reconcile, download, re-upload, or route intermediate binary artifacts between executors.

If automated transport cannot complete, report:

`BLOCKED — <specific missing transport capability>`

## Figma connector continuity

The ChatGPT/Figma Connector remains the canonical Figma read/write mechanism.

If it has worked earlier in the active session, a temporarily deferred/missing tool surface is not proof of unavailability. Rediscover the Figma connector, load the required Figma skill, and attempt the operation before claiming it is unavailable. Report the exact connector error if the direct attempt fails.

BRIDGE-1 must return validated artifacts + placement metadata; it must not replace the connector with a second Figma stack absent Jim's explicit approval.

## Repository isolation

- Read/write only inside this repository unless Jim explicitly authorizes cross-repository work.
- Do not modify sibling repositories, global VS Code settings, shell profiles, or global Python environments.
- Keep dependencies/tooling repository-local.
- Never overwrite the immutable master/reference image.

## Execution

Use one bounded package:

`inspect → execute → validate → correct bounded defects → stop at acceptance or genuine blocker`

Do not stop after every intermediate artifact. Do not reopen superseded work. Do not generalize fallback techniques before proving they are required.

## Verification

Never claim code, tests, Figma writes, artifacts, QA, or acceptance unless actually performed and verified.

Before handoff, report exact files changed and relevant proof. For Figma writes, verify consequential mutations and report affected node IDs.

## Current state

Current visual proof object: DIRECTV hero `1586 × 992`.

Current staging file: `JM-Personal-Brand-V2` (`3ZYkEtZVyRH9B2DfVpersf`).

DIRECTV detailed execution remains in `docs/EXECUTION_CONTRACT.md`.

**Next development package: BRIDGE-1 — Minimal Deterministic Decomposer Bridge.** Build scope and acceptance are exclusively defined in `docs/BRIDGE_CONTRACT.md`.
