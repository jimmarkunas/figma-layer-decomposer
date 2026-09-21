# Decomposition-First Visual Architecture Contract

**Status:** Canonical shared architecture contract  
**Applies to:** Personal Career Brand / PBDS, reusable website and presentation concepts, canonical Figma templates, and `figma-layer-decomposer`  
**Purpose:** Ensure reusable visual concepts are created as deterministic layered compositions rather than irreversible flattened scenes.

---

## 1. Core Principle

Reusable visual work must be created **for decomposition from the beginning**.

The target architecture is:

> **Template → reusable assets → deterministic composition → finished reference**

The anti-pattern is:

> **Finished flattened image → forensic reconstruction → attempted template**

A rendered concept image is a **reference output**, not the reusable design source.

If a concept is intended to become a reusable website hero, case-study template, Figma component, slide pattern, or branded module, its reusable structure must exist independently of the flattened render.

---

## 2. Source-State Classification Gate

Classification is based on the state of the authoritative source, **not** when the design was created.

Before choosing a workflow, classify the concept as exactly one of:

### `DECOMPOSITION_FIRST`

Use this classification only when a clean background and independent component assets already exist, or are being created independently **before** final composition.

### `FLATTENED_REFERENCE`

Use this classification whenever the authoritative starting point is an already-composed raster/reference image and no canonical independent layer package exists — regardless of whether the image was created five years ago or five minutes ago.

`FLATTENED_REFERENCE` work follows the legacy reconstruction path, including the complete-background fallback when no recoverable clean plate exists.

Never infer `DECOMPOSITION_FIRST` from words such as **new**, **new design**, **current rebrand**, **recent concept**, or similar chronological language.

A supplied or approved final image is the immutable **visual reference**. It is not itself Layer 01 and it is not evidence that a clean background exists.

---

## 3. New Concept Architecture

For future concepts, build the composition in this order.

### 2.1 Generate the clean environment first

Create the environment/background with:

- no foreground subject;
- no product/device imagery;
- no interface overlays;
- no typography;
- no editorial dark field, glow, vignette, or similar removable treatment.

Examples include concrete architecture, walls, floors, landscape, material surfaces, lighting environments, and decorative environmental structure.

The accepted result becomes the canonical **clean background plate**.

### 2.2 Preserve the exact clean background

Save the accepted clean background unchanged before foreground composition begins.

Do not depend on later inpainting to reconstruct it after objects have been added.

### 2.3 Keep major photographic subjects separate

People, portraits, large props, vehicles, furniture, and other meaningful photographic subjects must exist as independent raster assets whenever they may need to be hidden, moved, replaced, resized, or reused.

Use transparency where practical.

### 2.4 Keep products/devices separate

TVs, phones, monitors, laptops, product renders, packaging, UI mockups, and similar foreground objects should remain independent assets when they are expected to be editable or replaceable.

### 2.5 Build semantic UI and typography natively

The following should normally be native Figma objects:

- navigation;
- headlines;
- body copy;
- labels;
- CTAs;
- buttons;
- statistics;
- dividers;
- chips/badges;
- cards;
- vectors;
- brand marks;
- grids;
- simple gradients and overlays;
- UI chrome.

If an element carries semantic meaning or may need copy/style changes, it should be genuinely editable.

### 2.6 Keep editorial/environmental effects separate

Dark fields, glows, vignettes, fades, gradients, contact shadows, atmospherics, and similar treatments should be separate layers when they are logically independent of the physical environment.

### 2.7 Compose from canonical components

The finished concept must be reproducible from preserved source layers without regenerating the whole scene.

### 2.8 Save a composition manifest

Every reusable concept should include a compact machine-readable manifest for raster layer placement and rendering.

At minimum record:

- semantic role;
- source asset;
- x/y position;
- width/height;
- crop;
- scale;
- rotation;
- opacity;
- blend mode;
- stacking order;
- visibility default;
- optional mask reference when actually required;
- Figma frame/layer reference when known.

### 2.9 Bounded generative fill rule for new concepts

For new decomposition-first concepts, generative fill should be limited to bounded reconstruction or extension where genuinely necessary.

Examples:

- extending environmental structure;
- completing architecture behind a removable subject;
- repairing a small missing region;
- extending floor/wall/background continuation.

**This bounded-fill rule applies to new decomposition-first concepts. For legacy flattened concepts, the Legacy Full-Background Exception in §8 overrides this default.**

---

## 4. Canonical Reusable Package

A reusable hero or concept should resolve into:

```text
background clean plate
foreground photographic subject(s)
product/device assets
environmental/editorial effects
native Figma UI/text
composition manifest
flattened visual reference
QA comparison artifacts when needed
```

This package—not the flattened PNG—is the reusable design asset.

### Mask rule

**Masks are optional implementation/support artifacts only when actually required.**

Masks are **not**:

- mandatory product layers;
- canonical package elements;
- acceptance deliverables;
- roadmap phases;
- handoff packages;
- persistent Figma structures by default;
- user approval objects.

A mask may exist transiently inside a tool, but the product is the finished canonical layer.

---

## 5. Recommended Package Structure

```text
<concept-slug>/
├── reference/
│   └── final-reference.png
├── background/
│   └── clean-plate.png
├── subjects/
│   ├── subject-primary.png
│   └── subject-secondary.png
├── products/
│   ├── product-01.png
│   └── device-01.png
├── effects/
│   ├── shadow-01.png
│   ├── atmosphere-01.png
│   └── masks/              # optional support artifacts only
├── manifest/
│   └── composition.json
└── qa/
    ├── recomposed.png
    ├── comparison.png
    └── notes.md
```

Empty categories may be omitted.

Use semantic names such as:

```text
background-clean-plate.png
portrait-primary.png
tv-left.png
phone-primary.png
wall-shadow.png
floor-contact-shadow.png
hero-reference.png
composition.json
```

Avoid tool-history names such as:

```text
final-final-2.png
mask-new.png
test3.png
generated-output.png
image-293-80.png
```

---

## 6. Composition Manifest Example

```json
{
  "schema_version": "1.0",
  "concept_id": "directv-material-hero",
  "canvas": {
    "width": 1586,
    "height": 992
  },
  "reference": {
    "file": "../reference/final-reference.png"
  },
  "layers": [
    {
      "id": "background",
      "role": "background_clean_plate",
      "source": "../background/clean-plate.png",
      "x": 0,
      "y": 0,
      "width": 1586,
      "height": 992,
      "scale_x": 1.0,
      "scale_y": 1.0,
      "rotation_deg": 0,
      "opacity": 1.0,
      "blend_mode": "normal",
      "z_index": 0,
      "visible": true
    },
    {
      "id": "portrait-primary",
      "role": "foreground_subject",
      "source": "../subjects/portrait-primary.png",
      "x": 980,
      "y": 80,
      "width": 520,
      "height": 850,
      "scale_x": 1.0,
      "scale_y": 1.0,
      "rotation_deg": 0,
      "opacity": 1.0,
      "blend_mode": "normal",
      "z_index": 20,
      "visible": true,
      "mask": null
    }
  ],
  "native_figma_layers": [
    {"name": "Hero / Headline", "role": "headline"},
    {"name": "Hero / CTA", "role": "cta"}
  ]
}
```

The manifest documents raster composition. It does **not** replace Figma as the source of truth for editable Figma-native typography, vectors, UI, and template structure.

---

## 7. Native Figma Layer Contract

Use semantic layer names where practical:

```text
Hero / Background
Hero / Effects / Editorial Field
Hero / Effects / Glow
Hero / Portrait
Hero / Product / TV
Hero / Product / Phone
Hero / Nav
Hero / Eyebrow
Hero / Headline
Hero / Body
Hero / CTA
Hero / Metrics
Hero / Process Strip
Hero / Signature
```

### Editable means editable

If an element is required to be editable, it must not merely be a visually separate raster crop.

Examples:

- header links → native text;
- CTA → native text + native/vector container;
- statistics → native text;
- wall quote → native text;
- divider → vector line;
- product image → independent raster/vector asset;
- portrait → independent raster asset.

---

## 8. Legacy Flattened Concepts

Legacy concepts are different because the flattened image may not contain:

- hidden background pixels;
- original masks;
- original clean plates;
- original object boundaries;
- original shadows;
- original generation state;
- original layer hierarchy.

The objective is **not** to recover mythical original layers.

The objective is to create the smallest deterministic reusable layer package that reproduces the accepted visual result and required editability.

### Legacy Full-Background Exception

When no recoverable clean plate exists:

> **Generate or rebuild one complete independent background layer, provided the final recomposed design matches the immutable reference at intended viewing size. Do not require exact preservation of flattened background pixels when those pixels contain foreground contamination, baked editorial treatment, or content that properly belongs on separate layers.**

This exception exists specifically to prevent legacy conversions from collapsing into hole-by-hole mask archaeology.

The accepted legacy objective is:

> **deterministic recomposition + visual fidelity + editability**

—not proof that every background pixel came from the flattened reference.

---

## 9. Deterministic Legacy Decision Tree

```text
Clean plate exists?
→ YES: recover/preserve it exactly.
→ NO: generate/rebuild ONE complete independent background layer.

Foreground subject/device exists?
→ Extract/recover it as a separate layer.

Editorial dark field, glow, fade, vignette, gradient, or removable shadow?
→ Build as a native/separate effects layer.

Text/UI?
→ Build natively in Figma.

Then:
compose
→ compare to immutable reference
→ correct demonstrated deltas
→ freeze.
```

Do not default back to hidden-pixel forensics once the complete-background path is selected.

---

## 10. Legacy Reconstruction Workflow

1. Freeze the immutable reference.
2. Record dimensions, checksum/source, and acceptance state.
3. Inventory visible components by semantic role.
4. Define which elements must be independently editable/toggleable.
5. Determine whether a recoverable clean plate exists.
6. If yes, preserve/recover it.
7. If no, rebuild **one complete independent background**.
8. Extract deterministic foreground subjects/products from authoritative sources where available.
9. Separate editorial/environmental effects.
10. Rebuild semantic UI/text natively.
11. Record canonical geometry in the manifest.
12. Recompose the full design.
13. Compare to the immutable reference.
14. Correct demonstrated deltas only.
15. Accept and freeze.

Once a layer strategy is accepted, do not reopen it merely because a later local correction is inconvenient.

---

## 11. Pixel Preservation

Pixel preservation applies to **recoverable source assets and accepted canonical layers**, not blindly to every pixel in a flattened legacy background.

### Preserve exactly when recoverable

Examples:

- portrait identity/edges;
- product/device imagery;
- logos;
- distinctive foreground details;
- accepted canonical raster assets.

### Background exception

When no clean plate exists, the complete legacy background may be rebuilt.

Exact preservation of original flattened background pixels is not required when those pixels contain:

- foreground contamination;
- baked shadows from removable objects;
- editorial dark fields;
- glows;
- gradients;
- vignettes;
- typography;
- UI;
- other treatments that belong on separate layers.

The immutable requirement is the **accepted recomposed appearance at intended viewing size**.

Once the rebuilt background is accepted, it becomes canonical and must not be casually regenerated.

---

## 12. QA and Acceptance

A concept is template-ready only when all applicable criteria pass.

### Visual fidelity

- recomposed design matches the accepted reference at intended viewing size;
- no unintended seams, halos, crop errors, or reconstruction artifacts;
- lighting and material relationships remain coherent.

### Editability

- required text/UI is native/editable;
- required products/devices can be hidden or replaced;
- required photographic subjects can be independently hidden/replaced;
- valid background pixels exist underneath removable foreground elements.

### Determinism

- canonical assets are saved;
- geometry is documented;
- composition can be rebuilt without generative rediscovery;
- manifest paths resolve;
- no required layer depends on undocumented transient tool state.

### Reuse

- copy can be changed without raster editing;
- portrait/product assets can be replaced without rebuilding the environment;
- reasonable content substitution does not restart decomposition.

### Legacy reference comparison

Recommended QA artifacts:

```text
qa/
├── recomposed.png
├── reference-vs-recomposed.png
├── difference.png
└── notes.md
```

Pixel comparison is useful for detecting geometry/crop/edge drift, but exact pixel identity is not required for legitimately reconstructed hidden/background areas.

The primary question is:

> **Does the canonical package reproduce the accepted composition while adding the required editability and reuse?**

---

## 13. Shadows and Effects Ownership

Classify effects deliberately.

### Object-owned effect

A shadow/reflection that belongs to a movable object may travel with that object or exist as an adjacent object-owned effects layer.

### Environment-owned effect

Structural lighting or environmental shading that remains when foreground objects are removed belongs to the background/environment.

### Editorial effect

Dark fields, vignettes, fades, glows, brand gradients, and similar compositional treatments should remain independently controllable where practical.

Toggling a foreground object off must not leave an obviously incorrect artifact.

---

## 14. Prohibited Anti-Patterns

Do not:

1. Treat a flattened generated image as the reusable source file.
2. Generate the full final scene first and assume layers can be recovered later.
3. Bake editable typography/UI into the environmental raster.
4. Bake replaceable products/devices into the background.
5. Destroy or overwrite the accepted clean plate.
6. Depend on undocumented masks or temporary node IDs.
7. Turn masks into roadmap phases, handoff objects, or acceptance deliverables.
8. Force a legacy concept into hole-by-hole reconstruction when no clean plate exists.
9. Regenerate the entire final hero as one flattened scene to fix a bounded defect.
10. Alter subject identity to simplify reconstruction.
11. Replace deterministic product crops with approximate generated substitutes.
12. Reopen settled architecture because a later extraction step is inconvenient.
13. Store canonical geometry only in chat history.
14. Call an element editable when it is merely a separate raster crop.
15. Let `figma-layer-decomposer` become a second design system.
16. Treat background pixel provenance as more important than accepted recomposed fidelity.
17. Create repeated V2/V3/V4 reconstruction programs after the product layer can be built directly.

---

## 15. Decomposer Responsibility

`figma-layer-decomposer` owns bounded reconstruction/recovery through `PROMOTION_READY`.

It may support:

- source asset recovery;
- foreground extraction;
- optional temporary masking where required;
- complete background reconstruction when appropriate;
- alpha cleanup;
- geometry capture;
- manifest generation/validation;
- reference comparison;
- QA previews;
- canonical asset packaging.

It does **not** own:

- permanent PBDS visual language;
- canonical brand governance;
- whole-scene generative design;
- semantic template ownership after promotion;
- React or PowerPoint presentation systems.

Figma remains the editable design/composition surface.

The decomposer exists to produce reusable canonical layers—not to become a separate visual architecture.

---

## 16. PBDS / Design-System Responsibility

Personal Career Brand / PBDS owns:

- reusable component patterns;
- typography;
- color;
- spacing;
- radii;
- navigation;
- buttons;
- cards;
- visual hierarchy;
- image treatment;
- template slots;
- asset roles;
- semantic content behavior;
- canonical Figma promotion;
- downstream React and presentation consumption.

The decomposer delivers accepted layers into this system.

It must not redefine the brand language per image.

---

## 17. Template Contract

A reusable template distinguishes:

### Stable structure

Examples:

- frame dimensions;
- nav placement;
- copy column;
- metrics row;
- process strip;
- signature position;
- image zones;
- major alignment rules.

### Swappable content

Examples:

- headline;
- body copy;
- CTA;
- statistics;
- portrait;
- product imagery;
- logo;
- case-study content;
- background plate when the variant calls for it.

### Environmental treatment

Examples:

- atmosphere;
- surface material;
- shadow style;
- editorial field;
- glow;
- gradient treatment;
- lighting.

These distinctions should be obvious in Figma.

---

## 18. Source-of-Truth Hierarchy

For reusable visual work:

1. **Canonical Figma** — editable layout, typography, UI, components, template structure.
2. **Canonical asset package** — raster subjects, products, clean background, required effects.
3. **Composition manifest** — deterministic raster placement and relationships.
4. **Flattened reference** — visual acceptance oracle.
5. **Temporary intermediates** — disposable implementation artifacts.

For legacy conversion, the original flattened reference remains immutable; after acceptance, the canonical package and Figma composition become the reusable production sources.

Masks do not become a separate source of truth.

---

## 19. Completion Definition

A concept is not “templated” merely because it exists in Figma.

It is templated when:

- semantic content is editable;
- reusable assets are independently addressable;
- clean environment exists underneath removable foreground elements;
- subjects/products can be swapped without image forensics;
- transforms are known;
- the composition is deterministic;
- the result remains faithful to the accepted reference;
- reuse does not restart the decomposition project.

---

## 20. Operating Workflows

### New reusable concept

```text
define editability
→ generate clean environment
→ freeze clean plate
→ create/isolate subjects
→ prepare product/device assets
→ build effects separately
→ build semantic UI/text natively
→ compose
→ save manifest
→ render reference
→ QA
→ freeze.
```

### Legacy flattened concept

```text
freeze reference
→ inventory layers
→ define editability
→ clean plate exists?
   → yes: recover it
   → no: rebuild ONE complete background
→ recover foreground assets
→ separate effects
→ rebuild native UI/text
→ compose
→ save manifest
→ compare to reference
→ correct demonstrated deltas
→ freeze.
```

---

## 21. Final Rule

**Never again generate a reusable branded concept as one irreversible flattened scene.**

For new work:

> **Generate components. Preserve sources. Compose deliberately. Flatten only as an output.**

For legacy work:

> **Recover exact clean assets where they exist. When the clean background does not exist, rebuild one complete independent background and judge success by deterministic recomposition, editability, and accepted visual fidelity—not by forensic pixel provenance.**
