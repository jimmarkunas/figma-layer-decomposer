# 3B.2A-R2 — Master-derived DIRECTV portrait matte

Status: **AUTHORIZED ONE-SHOT CANDIDATE SPIKE**

## Purpose

Generate exactly one new DIRECTV portrait reconstruction-mask candidate directly from the immutable master using a dedicated portrait-matting model. This replaces further proxy-mask experimentation.

## Why the strategy changed

Source recovery for the portrait is complete but inconclusive: no exact standalone portrait asset was proven. The portrait remains `EXTRACT_FROM_MASTER`; hidden background exposed by removing the portrait remains `RECONSTRUCT_HIDDEN_PIXELS`.

Two mask strategies failed human review:

1. the original GrabCut-derived candidate;
2. the later semantic candidate, which introduced geometric torso blocks, rectangular device cut-outs, and UI contamination.

A third source-guided proxy candidate based on `hero-jim-01-cutout-v2.png` also failed human review and was worse. Because that asset was only `INCONCLUSIVE` for exact source recovery, it is no longer permitted as portrait-mask geometry guidance.

The anti-drift rule therefore requires stopping proxy repair and deriving the next candidate from the immutable master itself.

## Selected method

Use **BiRefNet portrait matting** from the official `ZhengPeng7/BiRefNet` project as a one-shot candidate generator.

Rationale:

- it has dedicated portrait-matting weights trained for human portrait separation;
- it is trimap-free and does not require a SAM box/point prompt or manually constructed trimap;
- it predicts a soft matte directly, which is better aligned to hair and jacket-edge preservation than binary segmentation;
- the official project provides portrait/general matting variants and local inference support;
- this spike uses the model only to generate an unapproved candidate matte. Immutable-master pixels remain the acceptance authority.

Do not substitute a generic background remover, SAM-only mask, GrabCut, the failed semantic mask, or the portfolio cutout.

## Candidate-generation rule

Input: `input/directv-hero-01/master.png` only.

1. Verify the immutable master SHA-256 and dimensions first.
2. Run the pinned BiRefNet portrait-matting checkpoint against the full master image.
3. Preserve the model alpha output as emitted; do not threshold or binarize it.
4. Map/resize back to the master canvas only according to the official model inference path.
5. Clip alpha only to the approved portrait reconstruction zone.
6. Do not perform morphology, smoothing, dilation, erosion, feathering, manual editing, or device/UI cleanup.
7. Generate review artifacts and stop.

The candidate is evidence only. It is not an approved removal mask until automated and human gates pass.

## Model pinning requirement

Before inference, record:

- official repository URL;
- exact repository commit used;
- exact checkpoint/model identifier;
- checkpoint SHA-256 or immutable model revision when available;
- PyTorch/Transformers/Pillow versions;
- execution device;
- inference resolution/preprocessing path.

If the official portrait-matting checkpoint cannot be pinned deterministically, stop `BLOCKED`.

## Approved geometry

Canvas: `1586 x 992`

Portrait core: `x=620 y=78 w=382 h=717`

Approved reconstruction zone: `x=596 y=54 w=430 h=765`

All candidate alpha outside the approved reconstruction zone must be zeroed without altering alpha inside the zone.

## Required evidence

Emit one unique run directory containing:

- `candidate-mask.png`
- `mask-overlay.png`
- `mask-only-preview.png`
- `difference-vs-semantic.png`
- `difference-vs-sourceguided.png`
- `report.json`

## Automated gate

PASS requires:

- immutable master hash/dimensions match;
- exact official BiRefNet portrait-matting model/checkpoint is pinned;
- one inference run only;
- candidate remains `1586 x 992`;
- alpha outside approved reconstruction zone = 0;
- immutable master unchanged;
- no heuristic post-processing;
- human gate remains `PENDING`;
- promotion remains `NOT_PROMOTED`.

Automated PASS does not imply visual acceptance.

## Human gate

Review at full resolution for:

- head/hair contour;
- ear, face, neck, and collar detail;
- jacket shoulders and torso silhouette;
- TV occlusion boundary;
- phone occlusion boundary;
- no UI/text/metrics contamination;
- no geometric block artifacts;
- no obvious portrait false negatives;
- no obvious device false positives;
- plausible soft alpha transitions where hair/edge translucency exists.

Any retained foreground that would be overwritten by background reconstruction is a FAIL.
Any meaningful portrait pixels omitted from the removal matte are a FAIL.

## Non-scope

Do not:

- run clean-plate reconstruction;
- promote the mask;
- modify Figma;
- perform production portrait extraction;
- remove TV/phone;
- modify product code unless execution proves a concrete blocker;
- compare multiple matting models in the same package;
- tune thresholds or generate variants.

## Stop condition

Stop after exactly one pinned BiRefNet portrait-matting candidate is generated and the evidence package is ready for human review.
