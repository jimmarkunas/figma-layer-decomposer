# DIRECTV Portrait LOCK #5 Decision

Status: approved by explicit user decision; promotion not yet performed.

## Problem

Strict visible-portrait fidelity against the immutable master conflicted with the desired standalone portrait candidate. That conflict caused repeated candidate and alignment reassessment work, while candidate #5 was the accepted standalone visual direction.

## Decision

Lock candidate #5 as the approved standalone DIRECTV portrait asset. Stop all further portrait generation and candidate iteration. Candidates #6 and #7 are rejected and irrelevant.

## Pinned asset

- path: `runs/directv-pr1b-candidate5/portrait-candidate.png`
- SHA-256: `50a24aa6ccffd5ea99e1d7c4247786830666530a09a051f2eb0163ce3fab8326`
- dimensions: `1048 × 1501`
- mode: `RGBA`
- alpha bbox: `x=80 y=37 width=805 height=1464`

## Superseded assumptions

The prior strict visible-face parity requirement is superseded for standalone portrait asset selection by the explicit LOCK #5 decision. This does not authorize changing the immutable master, regenerating the candidate, or reopening portrait generation through later full-frame fidelity discussion.

## Next allowed step

Derive portrait occupancy/alpha from the exact locked portrait asset and prepare the separate promotion/use handoff. Background reconstruction and Figma mutation remain unauthorized at this stage.
