# Clean Plate Pipeline Contract

Status: canonical implementation contract for the first production package.

Current package: **3B — Portrait clean plate** for the DIRECTV hero mock-up.

The same contract must be reusable for TV, phone, wall-message, and future mock-ups.

## 1. Objective

Given an immutable approved master image, an approved removal mask, and a bounded reconstruction zone, produce a clean-plate candidate that reveals plausible background pixels where the removable foreground object used to be while preserving all pixels outside the approved zone.

This is an image-processing package, not a redesign package.

## 2. Inputs

Required:

```text
input/<mockup-id>/master.png
input/<mockup-id>/manifest.json
input/<mockup-id>/masks/<target-id>.png
```

For the first case:

- mockup id: `directv-hero-01`
- target id: `portrait`
- master size: `1586 x 992`
- portrait core bounds: `x=620, y=78, w=382, h=717`
- approved reconstruction zone: `x=596, y=54, w=430, h=765`
- approved reconstruction halo: `24 px`

The pipeline MUST reject a master whose dimensions do not match the manifest.

## 3. Coordinate contract

All coordinates are master-image coordinates.

- origin: top-left of master
- x increases right
- y increases down
- rectangles use integer pixel coordinates
- bounds are represented as `x`, `y`, `width`, `height`
- derived `right = x + width`
- derived `bottom = y + height`

No step may silently rescale the master, mask, or output.

## 4. Mask contract

The target mask is an 8-bit grayscale or RGBA PNG.

- black / alpha 0 = immutable source region
- white / alpha 255 = target removal region
- intermediate values may be used for feathering
- mask dimensions MUST equal the master dimensions unless the manifest explicitly declares a bounded mask with placement coordinates

The approved reconstruction zone is the hard maximum edit boundary. A mask may be smaller than the zone but may never authorize pixels outside it.

## 5. Reconstruction boundary

The reconstruction engine may alter pixels only where:

```text
approved_zone == true
```

The implementation MAY use a feathered blend inside the approved zone.

It MUST NOT alter source pixels outside the approved zone.

This is enforced after reconstruction by a byte-level unchanged-region guard.

### Unchanged-pixel acceptance rule

After both source and output are normalized to the same color mode:

```text
changed_pixels_outside_approved_zone == 0
```

Any non-zero result is an automatic failure.

## 6. Reconstruction backend

The pipeline must expose reconstruction through an interchangeable backend interface rather than hard-coding one algorithm.

Suggested interface:

```python
class ReconstructionBackend(Protocol):
    def reconstruct(
        self,
        master: np.ndarray,
        target_mask: np.ndarray,
        approved_zone: Bounds,
        context: ReconstructionContext,
    ) -> np.ndarray:
        ...
```

At least one backend is required for 3B.1.

Permitted implementation approaches include:

- OpenCV inpainting
- deterministic texture synthesis / patch sampling
- a locally available image inpainting model
- an externally generated candidate imported as an explicit input, followed by deterministic compositing and QA

The backend may not reinterpret the entire image. Only the bounded reconstruction zone may be synthesized.

## 7. Preferred libraries

Baseline runtime:

- Python 3.12+
- Pillow
- NumPy
- OpenCV (`opencv-python-headless`)
- scikit-image for SSIM / structural metrics when useful
- pytest

Avoid heavyweight dependencies unless they materially improve reconstruction quality and are isolated behind the backend interface.

## 8. Required pipeline stages

### A. Validate inputs

Validate:

- master exists
- master dimensions match manifest
- target exists in manifest
- mask exists
- mask dimensions/placement are valid
- approved zone is inside the canvas
- core target bounds are contained by the approved zone

### B. Build immutable-region map

Generate a boolean map representing every pixel outside the approved zone.

### C. Reconstruct target region

Run the chosen backend only against the approved target.

### D. Composite deterministically

Composite the candidate into a copy of the master using the approved edit mask.

Never reconstruct directly into the sole source buffer.

### E. Automated QA

Produce both metrics and visual artifacts.

Required checks:

1. output dimensions equal source dimensions
2. output mode normalized consistently
3. changed pixels outside approved zone = 0
4. target removal coverage is non-zero
5. no NaN/invalid pixel values
6. output file is readable after serialization
7. recomposition inputs have valid coordinates

Recommended metrics:

- changed pixel count inside zone
- changed pixel count outside zone
- mean absolute error outside zone; must be `0`
- SSIM for unchanged region; expected `1.0` after exact guard
- boundary-band discontinuity score

### F. Human visual QA

Automation cannot approve generative plausibility.

A human must inspect:

- architecture continuity
- wall seam continuity
- texture scale
- tonal falloff
- lighting continuity
- edge halos
- repeated texture artifacts
- obvious object remnants
- accidental deletion of neighboring objects

Human QA is pass/fail and must be recorded in the QA report before Figma handoff.

## 9. Required outputs

For target `portrait`:

```text
output/directv-hero-01/background/portrait-clean-plate.png
output/directv-hero-01/background/portrait-clean-plate-preview.png
output/directv-hero-01/qa/portrait-difference.png
output/directv-hero-01/qa/portrait-unchanged-region-diff.png
output/directv-hero-01/qa/portrait-report.json
```

The preview should make the changed zone easy to inspect without altering the canonical clean-plate output.

## 10. QA report contract

Minimum shape:

```json
{
  "mockup_id": "directv-hero-01",
  "target_id": "portrait",
  "pipeline_version": "0.1.0",
  "source_sha256": "...",
  "output_sha256": "...",
  "canvas": {"width": 1586, "height": 992},
  "core_bounds": {"x": 620, "y": 78, "width": 382, "height": 717},
  "approved_zone": {"x": 596, "y": 54, "width": 430, "height": 765},
  "changed_pixels_inside_zone": 0,
  "changed_pixels_outside_zone": 0,
  "automated_gate": "PASS",
  "human_gate": "PENDING",
  "notes": []
}
```

## 11. Figma handoff contract

Figma is a destination, not the reconstruction engine.

No clean-plate asset is uploaded to Figma unless:

- automated gate = `PASS`
- human gate = `PASS`

Each approved output must include placement metadata:

```json
{
  "name": "Portrait Clean Plate — 3B",
  "file": "background/portrait-clean-plate.png",
  "x": 596,
  "y": 54,
  "width": 430,
  "height": 765,
  "destination_group": "01_BACKGROUND"
}
```

If the exported asset is a full-canvas image, placement must instead be `x=0`, `y=0`, `width=1586`, `height=992`.

Do not infer placement from Figma after generation; placement comes from the manifest.

## 12. Failure behavior

The pipeline must fail closed.

It must not write an approved artifact or trigger Figma handoff when:

- source dimensions mismatch
- mask dimensions mismatch
- target is missing
- approved zone is invalid
- output dimensions mismatch
- pixels changed outside approved zone
- serialization fails
- automated QA fails

A failed run should preserve diagnostics under a run-specific temporary/output directory rather than overwriting the last approved artifact.

## 13. Rollback behavior

Approved artifacts are immutable by version.

New attempts use new run IDs. Promotion to the canonical output path happens only after QA.

Recommended structure:

```text
runs/<run-id>/...
approved/<mockup-id>/<target-id>/...
```

## 14. 3B acceptance criteria

3B is complete only when all are true:

- [ ] portrait is absent from the clean-plate candidate
- [ ] no neighboring approved foreground object is unintentionally deleted
- [ ] concrete architecture is visually plausible
- [ ] tonal falloff is continuous
- [ ] no obvious silhouette remnant remains
- [ ] no visible rectangular patch boundary
- [ ] output remains exactly `1586 x 992`
- [ ] zero changed pixels exist outside the approved zone
- [ ] QA artifacts are generated
- [ ] automated gate passes
- [ ] human visual gate passes
- [ ] only then is the asset eligible for Figma placement

## 15. Reuse requirements for mock-ups #2–#6

No DIRECTV-specific coordinates or filenames may be hard-coded in reusable modules.

All mock-up-specific values must come from the manifest.

The reusable engine must support multiple targets per mock-up and cumulative clean-plate sequencing, because later targets may overlap pixels reconstructed by earlier targets.

For the DIRECTV sequence:

```text
master
  -> portrait removed
  -> TV removed from portrait-clean result
  -> phone removed from portrait+TV-clean result
  -> wall slogan removed
  -> wall underline removed
```

Each stage consumes the approved output of the prior stage.

## 16. Scope exclusions for 3B.1

Do not implement yet:

- native Figma typography
- Figma buttons/components
- TV screen extraction
- phone screen extraction
- generalized Figma MCP mutation
- web UI
- cloud hosting
- job queues
- persistence/database layers

3B.1 should remain a small local CLI/library with tests.
