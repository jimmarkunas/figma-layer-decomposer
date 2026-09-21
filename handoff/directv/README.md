# DIRECTV Shared Handoff

This directory is the shared machine handoff surface for the DIRECTV reconstruction workflow.

## Purpose

Use this path instead of `/tmp`, ad-hoc Figma staging nodes, or manual user downloads for cross-agent file exchange.

Both Codex and Web ChatGPT should read/write artifacts here on branch `handoff/directv-live`.

## Directory contract

- `authoritative/` — immutable accepted source/reference assets and manifests only.
- `working/` — active machine-generated intermediates.
- `approved/` — assets that have passed the current acceptance gate.
- `rejected/` — failed candidates retained only when needed for provenance/debugging.

## Naming

Use explicit semantic names. Do not use opaque generated filenames.

Examples:

- `authoritative/master.png`
- `authoritative/portrait-lock5.png`
- `authoritative/tv-cutout.png`
- `authoritative/phone-cutout.png`
- `working/A1-corrected-edit-input.png`
- `working/A2-corrected-edit-input.png`
- `working/B1-corrected-edit-input.png`
- `working/B2-corrected-edit-input.png`
- `working/corrected-edit-inputs-contact-sheet.png`
- `working/manifest.json`
- `approved/background-independent-final.png`

## Rules

1. Never ask Jim to download/rename/re-upload a file for agent-to-agent handoff when the artifact can be committed here.
2. Figma remains the composition/design surface, not the transport layer.
3. `/tmp` may be used for local computation but is never the handoff source of truth.
4. Every binary handoff must include a manifest with dimensions, SHA-256, provenance, semantic role, and current status.
5. Rejected assets must not be reused silently.
6. Promotion to `approved/` requires the relevant visual/structural acceptance gate.
7. Production Figma mutations remain gated separately.

## Current branch

`handoff/directv-live`
