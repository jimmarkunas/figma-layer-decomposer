# Clean Plate Pipeline Contract

Status: canonical implementation contract for hidden-background cleanplate reconstruction.

This contract is reusable across DIRECTV and future mock-ups when source-first decomposition classifies hidden visual pixels as requiring reconstruction.

## 0. Source-first prerequisite

Cleanplate reconstruction is a fallback capability for pixels that cannot be recovered directly; it is not the default decomposition strategy.

Before this contract is used for a region, the project must have a source-first classification showing that one of the following applies:

- `RECOVER_SOURCE` is unavailable for the hidden pixels;
- `EXTRACT_FROM_MASTER` cannot reveal pixels that are actually occluded;
- `REBUILD_NATIVE` is not appropriate because the missing content is visual/environmental rather than semantic UI/text/vector content.

When those conditions hold, the region may be classified for hidden-pixel reconstruction. The current `docs/PROJECT_CANON.md` owns package-level authorization and may explicitly authorize reconstruction without reopening historical stage gates.

No reconstruction method should be inferred merely from the existence of a mask, candidate, donor, or model.

## 1. Objective

Given an immutable approved master image, verified source-removal geometry, preserve geometry, and bounded reconstruction region, produce an independent clean background that:

- preserves exact visible-source pixels wherever they are already available and suitable;
- removes foreground contamination attributable to removable objects/content;
- reconstructs genuinely hidden environmental pixels with visual continuity;
- records truthful provenance for reconstructed pixels;
- supports faithful full-frame recomposition with independent foreground layers.

This is a bounded reconstruction package, not a redesign package.

## 2. Approved reconstruction modes

The contract supports two approved execution modes behind a common integration/QA boundary.

### 2.1 `DETERMINISTIC_CLEAN_PLATE`

Use when hidden pixels can be reconstructed with sufficient fidelity from deterministic evidence such as:

- neighboring visible master pixels;
- donor patches;
- planar/perspective continuation;
- deterministic transforms;
- local texture continuation;
- patch sampling.

### 2.2 `GENERATE_BOUNDED_CLEANPLATE`

Use when:

- hidden pixels have no recoverable source;
- deterministic continuation is insufficient to meet visual fidelity;
- the reconstruction region is bounded and documented;
- the goal is visual continuity rather than false historical pixel recovery.

The image-generation model owns visual synthesis only. Deterministic tooling still owns masks/bounds, preserve geometry, file integrity, provenance, compositing, Figma placement, and QA.

`GENERATE_BOUNDED_CLEANPLATE` is not whole-image generation and does not authorize redesign.

## 3. Inputs

Required conceptual inputs:

```text
master.png
source-removal-matte.png
preserve-mask.png
reconstruction-boundary-preview.png
manifest / placement metadata
generation-brief.md   # required for generative mode
```

Optional inputs:

- donor/reference material;
- accepted foreground alpha/assets;
- foreground-effect ownership rules;
- previous rejected candidates as negative evidence only.

For DIRECTV:

- master size: `1586 × 992`
- immutable master SHA-256: `d5a66264cc44c449f0e29d045d729c81fe51564b768b371fd9544b34b60f22e6`

The pipeline must reject an input master whose dimensions/hash do not match current canonical state.

## 4. Coordinate contract

All coordinates are master-image coordinates.

- origin: top-left of master;
- x increases right;
- y increases down;
- bounds are represented as `x`, `y`, `width`, `height`;
- derived `right = x + width`;
- derived `bottom = y + height`.

No step may silently rescale the master, masks, preserve geometry, or output.

## 5. Source-removal and preserve-mask contract

### Source-removal matte

Identifies source pixels attributable to removable foreground content/effects that must not remain in the independent background.

It may be larger than the recovered foreground core alpha when the original flattened source contains attributable antialiasing, halos, shadows, reflections, or source-specific edge treatment.

It must remain tightly bounded and evidence-driven. Broad boxes/polygons that discard valid visible environment are prohibited.

### Preserve mask

Identifies pixels that must remain exact immutable-master source pixels.

For pixels outside authorized reconstruction/source-removal support:

```text
final_background_pixel = master_pixel
```

whenever practical.

The preserve mask and source-removal matte together define what the visual synthesis engine may and may not change.

## 6. Reconstruction boundary

The reconstruction engine may alter pixels only inside the explicitly authorized bounded region/matte support.

It must not alter preserved source pixels outside that region.

The deterministic integration layer must enforce this after reconstruction.

### Unchanged-region acceptance rule

After source and output are normalized to the same color mode:

```text
changed_pixels_outside_authorized_reconstruction_support == 0
```

unless a narrowly documented integration feather is explicitly permitted by the current package.

Any unexplained non-zero result is an automatic structural failure.

## 7. Reconstruction backend interface

Reconstruction remains backend-pluggable.

Conceptual interface:

```python
class ReconstructionBackend(Protocol):
    def reconstruct(
        self,
        master: np.ndarray,
        source_removal_matte: np.ndarray,
        preserve_mask: np.ndarray,
        approved_zone: Bounds,
        context: ReconstructionContext,
    ) -> np.ndarray:
        ...
```

Supported backends include:

- deterministic patch/texture continuation;
- local inpainting model;
- external image-generation/image-edit model operating on the bounded generation pack;
- externally generated bounded candidate imported as an explicit input and then deterministically composited/validated.

The backend may not reinterpret the entire image. Only authorized hidden/reconstruction regions may be synthesized.

## 8. Generative cleanplate contract

When mode = `GENERATE_BOUNDED_CLEANPLATE`, the generation pack must provide enough context for visual continuity without giving the model permission to redesign the scene.

The generation brief must specify:

- environmental surfaces/materials that must continue;
- perspective/architectural relationships;
- lighting/tonal behavior;
- foreground objects/text/UI that must be absent;
- preserve constraints;
- reconstruction bounds;
- any known donor/reference cues;
- uncertainty areas when applicable.

For the DIRECTV proof, the clean background should preserve the same visual scene character:

- dark left editorial field;
- concrete architectural wall/returns;
- sky aperture;
- magenta vertical light/neon;
- reflective dark floor;
- environmental shadows and tonal falloff.

It must not contain Jim, TV, phone, readable UI/text, wall quote text, or footer phrase.

The model should return one primary candidate and at most one alternate when an alternate materially helps selection. Candidate proliferation is not part of the product workflow.

## 9. Foreground-associated effects

A visual effect attributable to a removable foreground object does not automatically belong in the independent background.

Examples:

- device contact shadow;
- device reflection;
- glow/halo;
- soft object-specific edge treatment.

When necessary, reconstruct clean environmental pixels beneath the effect and emit the effect as `REBUILT_EFFECT` owned by the corresponding foreground asset so toggling the asset also toggles its effect.

## 10. Required pipeline stages

### A. Verify package authorization

Read current `docs/PROJECT_CANON.md` and confirm the region/mode is authorized.

### B. Validate inputs

Validate:

- immutable master exists and matches canonical dimensions/hash;
- source-removal matte exists and matches canvas/placement contract;
- preserve mask exists and matches canvas/placement contract;
- approved reconstruction support is inside the canvas;
- accepted foreground geometry/provenance is available.

### C. Build generation/reconstruction pack

Emit the deterministic inputs needed by the selected backend.

### D. Reconstruct target region

Run the selected backend only against the authorized bounded support.

### E. Composite deterministically

Composite the accepted candidate into a copy of the master according to the preserve/source-removal contract.

Never reconstruct directly into the sole immutable source buffer.

### F. Automated QA

Required checks:

1. output dimensions equal source dimensions;
2. output mode normalized consistently;
3. changed pixels outside authorized reconstruction support = `0` unless explicitly justified feather applies;
4. target removal/reconstruction coverage is non-zero;
5. no NaN/invalid pixel values;
6. output file is readable after serialization;
7. placement/recomposition inputs have valid coordinates;
8. immutable master hash remains unchanged;
9. provenance classification is present.

Recommended evidence:

- changed-pixel mask;
- source-removal matte preview;
- preserve-mask preview;
- reconstruction-boundary preview;
- background-alone preview;
- recomposition preview;
- boundary-band discontinuity metrics where useful.

### G. Human visual QA

Automation cannot approve reconstruction plausibility.

A human/visual agent must inspect:

- architecture continuity;
- perspective continuity;
- wall seam continuity;
- texture scale;
- tonal falloff;
- lighting continuity;
- edge halos;
- repeated texture artifacts;
- obvious object/text remnants;
- accidental deletion of neighboring objects;
- full-frame recomposition against the immutable reference.

Human visual QA is pass/fail for `PROMOTION_READY`.

A failed visual candidate is `FAIL / CONTINUE`, not `BLOCKED`, unless a genuine external/source-of-truth problem prevents another bounded attempt.

## 11. Required outputs

A production cleanplate run should emit at minimum:

```text
clean-background.png
source-removal-matte.png
preserve-mask.png
reconstruction-boundary-preview.png
background-preview.png
recomposition-preview.png
qa-report.json
```

For generative mode, also retain a concise generation brief and generated-provenance record.

Temporary candidate/diagnostic artifacts should live under a run-specific temporary directory. Only accepted/final evidence should be promoted to durable product paths.

## 12. Provenance contract

Each output/region must use one of the canonical provenance classes:

- `RECOVERED_SOURCE`
- `EXTRACTED_FROM_MASTER`
- `NATIVE_REBUILT`
- `GENERATED_RECONSTRUCTION`
- `REBUILT_EFFECT`

Generated cleanplate pixels must be classified `GENERATED_RECONSTRUCTION`.

Do not describe generated pixels as recovered/original source.

Minimum QA/provenance report fields should include:

```json
{
  "mockup_id": "directv-hero-01",
  "mode": "GENERATE_BOUNDED_CLEANPLATE",
  "source_sha256": "...",
  "output_sha256": "...",
  "canvas": {"width": 1586, "height": 992},
  "changed_pixels_outside_authorized_support": 0,
  "provenance": "GENERATED_RECONSTRUCTION",
  "automated_gate": "PASS",
  "human_gate": "PENDING",
  "notes": []
}
```

## 13. Figma handoff contract

Figma is a destination/composition environment, not the hidden-pixel synthesis engine.

No cleanplate asset is promoted into the production composition unless:

- reconstruction is authorized by current project canon;
- automated structural gate passes;
- visual gate passes for the background candidate or the current package explicitly requires in-Figma recomposition for the final visual gate.

Each approved output must include placement metadata.

For a full-canvas DIRECTV background:

```json
{
  "name": "Background / Independent Cleanplate",
  "x": 0,
  "y": 0,
  "width": 1586,
  "height": 992,
  "destination_role": "background/environment"
}
```

Final Figma QA must verify that foreground layers remain independently toggleable/editable and that the independent background does not contain material foreground residue.

## 14. Failure behavior

The pipeline fails closed for structural/integrity violations such as:

- reconstruction not authorized by current canon;
- source dimensions/hash mismatch;
- mask/preserve geometry mismatch;
- invalid reconstruction bounds;
- output dimensions mismatch;
- unexplained pixels changed outside authorized support;
- serialization failure;
- missing provenance;
- Figma write/integration failure that cannot be safely retried.

A candidate that simply looks visually wrong is a **QA failure requiring bounded correction**, not a genuine blocker.

A failed run must preserve diagnostics without overwriting the last accepted artifact.

## 15. Rollback behavior

Accepted assets are immutable by version/hash.

New attempts use new run IDs or temporary paths. Promotion to canonical product paths/Figma occurs only after the relevant acceptance gates.

Preserve known-good Figma state until a replacement is verified.

## 16. Acceptance criteria

A cleanplate/background stage is accepted only when all are true:

- [ ] reconstruction route is authorized;
- [ ] immutable master integrity is verified;
- [ ] required foreground content is absent from the independent background;
- [ ] no neighboring approved foreground object is unintentionally deleted;
- [ ] visible-source environment is preserved where available;
- [ ] hidden environment is visually continuous and plausible;
- [ ] no obvious rectangular/polygon patch boundary remains;
- [ ] output remains exactly the expected canvas size;
- [ ] zero unexplained changed pixels exist outside authorized reconstruction support;
- [ ] provenance is recorded truthfully;
- [ ] automated structural gate passes;
- [ ] human visual gate passes;
- [ ] full-frame recomposition is presentation-ready.

## 17. Reuse requirements for mock-ups #2–#6

No DIRECTV-specific coordinates or filenames may be hard-coded into reusable modules.

All mock-up-specific values must come from manifests/current package inputs.

Each future mock-up runs the same routing model:

```text
RECOVER_SOURCE
EXTRACT_FROM_MASTER
REBUILD_NATIVE
GENERATE_BOUNDED_CLEANPLATE
RECOVER_OR_REBUILD_EFFECT
DETERMINISTIC_COMPOSE
STRUCTURAL_AND_VISUAL_QA
```

Recovered source assets may eliminate reconstruction entirely. Hidden visual pixels with no source may use bounded generative cleanplate. The product should not force deterministic inpainting when it cannot satisfy visual fidelity.
