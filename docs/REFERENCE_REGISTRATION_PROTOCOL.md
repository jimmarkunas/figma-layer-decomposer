# Reference Registration Protocol

**Status:** Canonical operating protocol  
**Owner:** Jim Markunas  
**Effective:** 2026-09-21  
**Governed by:** `docs/DECOMPOSITION_FIRST_VISUAL_ARCHITECTURE_CONTRACT.md`  
**Applies to:** Approved-reference reconstruction and matching in canonical Figma/PBDS work, including presentations, website concepts, case-study visuals, one-pagers, and reusable branded compositions.

## 1. Core rule

When an approved visual reference already exists, the task is **registration, not design**.

Do not reinterpret, rebalance, simplify, improve, compensate, or redesign the approved reference unless Jim explicitly requests a redesign.

The approved flattened reference remains the **visual acceptance oracle**. Figma remains the editable composition source.

## 2. Required pre-mutation inspection

Before changing Figma:

1. Render the current target frame.
2. Inspect the immutable approved reference.
3. Inventory every supplied raster/vector asset and every native Figma layer involved in the composition.
4. Identify 6–10 visual anchors that connect the reference to the editable target.
5. Determine each raster/vector asset transform independently.
6. Decide which native Figma layers actually require geometry changes.

Do not begin by moving assets until the anchors and independent asset roles are understood.

## 3. Anchor registration

Use stable visible anchors such as:

- major object corners or centers;
- subject/device edges;
- mountain/terrain peaks;
- milestone nodes;
- path intersections;
- headline baselines;
- card boundaries;
- divider lines;
- footer/takeaway baselines;
- strong negative-space boundaries.

Judge alignment by visible content relationships, not by the outer rectangular bounds of transparent raster assets.

## 4. Independent asset rule

Register every supplied raster/vector asset independently.

Never assume two assets share:

- x/y position;
- scale;
- crop;
- aspect treatment;
- visible-content bounds;
- opacity;
- stacking relationship;

merely because they belong to the same scene or visual system.

A background/terrain asset and a milestone/path asset, for example, may require different transforms to reproduce the approved composition.

## 5. Native-layer rule

Preserve native Figma typography, chrome, labels, vectors, UI, and reusable design-system components unless the approved reference demonstrates that their geometry must change.

Semantic content that is editable must remain native/editable.

Do not flatten native text or UI merely to match a reference.

## 6. Intentional overlap rule

Intentional overlap is not automatically a defect.

Do not move imagery merely to avoid native copy when the approved reference deliberately places text over terrain, photography, glow, devices, or other visual material.

The question is not “does anything overlap?”

The question is “does the editable composition reproduce the approved hierarchy, legibility, spacing, and visual relationship?”

## 7. No compensation layers

Do not invent masks, veils, gradients, shadows, containers, vignettes, glows, or other corrective layers merely to hide incorrect registration.

A new effect layer is allowed only when the approved reference actually demonstrates that effect or Jim explicitly approves it.

If geometry is wrong, fix geometry.

## 8. One variable class per pass

Change only one class of variables per pass whenever practical:

1. asset registration — position, scale, crop, rotation;
2. native layout — text, vectors, component geometry;
3. effects — opacity, glow, shadow, editorial treatment.

Render after every meaningful pass.

If a pass materially worsens fidelity, revert it instead of compensating elsewhere.

## 9. Visual QA loop

For every approved-reference task:

```text
inspect reference
→ identify anchors
→ register asset 1
→ render
→ compare
→ register asset 2
→ render
→ compare
→ align native layers
→ render
→ compare
→ correct demonstrated deltas only
→ freeze
```

Do not declare completion from metadata alone.

Do not declare completion because the file is editable.

Do not declare completion because the composition is aesthetically plausible.

Completion requires a rendered Figma frame that materially matches the approved reference at intended viewing size.

## 10. Acceptance checklist

Before claiming completion, verify:

- major anchors register to the approved reference;
- each independent asset has the correct transform;
- visible crop/scale relationships match;
- intentional overlaps are preserved;
- negative space and hierarchy match;
- native UI/text remains editable;
- no invented compensation layer was added;
- no unrelated design-system element changed;
- final render was compared directly with the approved reference;
- demonstrated deltas were corrected;
- accepted transforms are frozen/documented where reuse requires it.

If any applicable item fails, the task is not complete.

## 11. Canonical worked example — PDMA Slide 04

The accepted worked example is the current canonical Figma composition:

**`PDMA / FINAL 04 / JUDGMENT + WORK MAP`**  
Figma file: `JM Personal Brand V2`  
File key: `3ZYkEtZVyRH9B2DfVpersf`  
Frame: `475:369`

Direct link:

https://www.figma.com/design/3ZYkEtZVyRH9B2DfVpersf/JM-Personal-Brand-V2?node-id=475-369

Why it is canonical:

- the mountain/terrain raster and milestone/path raster are registered independently;
- native typography and chrome remain native;
- intentional terrain/text overlap is preserved rather than treated as an automatic defect;
- no invented corrective veil is required to compensate for bad geometry;
- the approved flattened reference controls visual fidelity;
- the final Figma composition is the reusable editable source.

This example defines **method**, not a universal slide layout. Future approved-reference work should follow the same registration discipline while preserving the design requirements of its own reference.

## 12. Anti-drift rule

For approved-reference work:

> **REFERENCE MATCHING = REGISTRATION, NOT REDESIGN.**

The operating sequence is:

> **Inspect → anchor → register assets independently → align native layers → render → compare → correct demonstrated deltas → freeze.**

Any agent that changes the visual concept, invents compensating layers, or claims completion without rendered reference comparison has drifted from this protocol.
