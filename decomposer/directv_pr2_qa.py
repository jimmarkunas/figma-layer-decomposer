from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops

MASTER_SHA256 = "d5a66264cc44c449f0e29d045d729c81fe51564b768b371fd9544b34b60f22e6"
CANDIDATE_SHA256 = "7e0dff885056dcab3d0a3995f7c86ffb0eccdce38c4b2d9af17ded970fd1864f"

PORTRAIT_CORE = (620, 78, 382, 717)
PORTRAIT_QA_ZONE = (596, 54, 430, 765)
TV_CORE = (913, 413, 544, 397)
PHONE_CORE = (791, 532, 132, 280)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _rect_mask(size: tuple[int, int], rect: tuple[int, int, int, int]) -> np.ndarray:
    width, height = size
    x, y, w, h = rect
    mask = np.zeros((height, width), dtype=bool)
    x0, y0 = max(0, x), max(0, y)
    x1, y1 = min(width, x + w), min(height, y + h)
    if x1 > x0 and y1 > y0:
        mask[y0:y1, x0:x1] = True
    return mask


def _alpha_bbox(alpha: np.ndarray) -> tuple[int, int, int, int]:
    ys, xs = np.nonzero(alpha > 0)
    if len(xs) == 0:
        raise ValueError("candidate alpha is empty")
    x0, x1 = int(xs.min()), int(xs.max()) + 1
    y0, y1 = int(ys.min()), int(ys.max()) + 1
    return x0, y0, x1, y1


def _align_candidate(candidate: Image.Image, canvas_size: tuple[int, int]) -> tuple[Image.Image, dict]:
    rgba = candidate.convert("RGBA")
    alpha = np.asarray(rgba.getchannel("A"))
    x0, y0, x1, y1 = _alpha_bbox(alpha)
    cropped = rgba.crop((x0, y0, x1, y1))

    _, _, _, target_h = PORTRAIT_CORE
    scale = target_h / cropped.height
    resized_w = max(1, round(cropped.width * scale))
    resized_h = target_h
    resized = cropped.resize((resized_w, resized_h), Image.Resampling.LANCZOS)

    target_x, target_y, _, _ = PORTRAIT_CORE
    aligned = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    aligned.alpha_composite(resized, (target_x, target_y))

    placement = {
        "method": "alpha-bbox crop; uniform scale by portrait-core height; top-left anchor to portrait core",
        "source_alpha_bbox": {"x": x0, "y": y0, "width": x1 - x0, "height": y1 - y0},
        "scale": scale,
        "x": target_x,
        "y": target_y,
        "width": resized_w,
        "height": resized_h,
    }
    return aligned, placement


def run_pr2(master_path: Path, candidate_path: Path, run_dir: Path) -> dict:
    run_dir.mkdir(parents=True, exist_ok=True)

    master_sha_before = sha256_file(master_path)
    candidate_sha = sha256_file(candidate_path)
    if master_sha_before != MASTER_SHA256:
        raise ValueError(f"master SHA mismatch: {master_sha_before}")
    if candidate_sha != CANDIDATE_SHA256:
        raise ValueError(f"candidate SHA mismatch: {candidate_sha}")

    master = Image.open(master_path).convert("RGBA")
    original_candidate = Image.open(candidate_path)
    if original_candidate.mode != "RGBA":
        raise ValueError(f"candidate must be RGBA, got {original_candidate.mode}")
    candidate_alpha = np.asarray(original_candidate.getchannel("A"))
    if not np.any(candidate_alpha == 0) or not np.any(candidate_alpha > 0):
        raise ValueError("candidate must contain both transparent and non-transparent pixels")

    aligned, placement = _align_candidate(original_candidate, master.size)
    aligned_arr = np.asarray(aligned)
    master_arr = np.asarray(master)
    alpha = aligned_arr[:, :, 3]

    qa_zone = _rect_mask(master.size, PORTRAIT_QA_ZONE)
    tv = _rect_mask(master.size, TV_CORE)
    phone = _rect_mask(master.size, PHONE_CORE)
    occlusion = tv | phone
    portrait_pixels = alpha > 0
    unauthorized_geometry = portrait_pixels & ~qa_zone & ~occlusion

    visible_opaque = (alpha >= 250) & ~occlusion
    visible_count = int(visible_opaque.sum())
    if visible_count == 0:
        raise ValueError("no opaque visible portrait pixels available for fidelity comparison")

    rgb_delta = np.abs(aligned_arr[:, :, :3].astype(np.int16) - master_arr[:, :, :3].astype(np.int16))
    visible_delta = rgb_delta[visible_opaque]
    mae = float(visible_delta.mean())
    rmse = float(np.sqrt(np.mean(np.square(visible_delta.astype(np.float64)))))
    max_error = int(visible_delta.max())
    pixel_mismatch = np.any(rgb_delta > 0, axis=2) & visible_opaque
    mismatch_count = int(pixel_mismatch.sum())
    mismatch_ratio = mismatch_count / visible_count

    aligned.save(run_dir / "portrait-aligned-preview.png")
    Image.fromarray(alpha, mode="L").save(run_dir / "portrait-alpha.png")

    overlay_candidate = aligned.copy()
    overlay_candidate.putalpha(Image.fromarray((alpha.astype(np.float32) * 0.5).astype(np.uint8), mode="L"))
    overlay = master.copy()
    overlay.alpha_composite(overlay_candidate)
    overlay.save(run_dir / "portrait-master-overlay.png")

    diff_strength = rgb_delta.max(axis=2).astype(np.uint8)
    diff_rgba = np.zeros_like(aligned_arr)
    diff_rgba[:, :, 0] = diff_strength
    diff_rgba[:, :, 1] = diff_strength
    diff_rgba[:, :, 2] = diff_strength
    diff_rgba[:, :, 3] = np.where(visible_opaque, 255, 0).astype(np.uint8)
    Image.fromarray(diff_rgba, mode="RGBA").save(run_dir / "portrait-visible-diff.png")

    master_sha_after = sha256_file(master_path)
    mechanical_failures: list[str] = []
    if int(unauthorized_geometry.sum()) > 0:
        mechanical_failures.append("aligned portrait has non-occluded pixels outside approved portrait QA zone")
    if master_sha_after != master_sha_before:
        mechanical_failures.append("immutable master hash changed")
    if aligned.size != master.size:
        mechanical_failures.append("aligned preview dimensions do not equal master dimensions")

    gate = "FAIL" if mechanical_failures else "PASS"
    report = {
        "stage": "PR-2",
        "classification": "REBUILD_RASTER_FROM_SOURCE",
        "candidate_path": str(candidate_path),
        "candidate_sha256": candidate_sha,
        "master_path": str(master_path),
        "master_sha256_before": master_sha_before,
        "master_sha256_after": master_sha_after,
        "master_unchanged": master_sha_before == master_sha_after,
        "target_placement": placement,
        "output_dimensions": {"width": master.width, "height": master.height},
        "visible_region_comparison_method": "RGB absolute difference on aligned alpha>=250 pixels excluding TV/phone core occlusion",
        "visible_region_pixel_count": visible_count,
        "visible_region_mismatch_count": mismatch_count,
        "visible_region_mismatch_ratio": mismatch_ratio,
        "visible_region_mae": mae,
        "visible_region_rmse": rmse,
        "visible_region_max_error": max_error,
        "unauthorized_geometry_pixel_count": int(unauthorized_geometry.sum()),
        "hidden_region_designation": ["TV core", "phone core"],
        "fidelity_threshold_note": "No numeric visual-fidelity PASS threshold is defined by the canonical PR-1B contract; metrics are emitted for human PR-3 review.",
        "mechanical_failures": mechanical_failures,
        "automated_gate": gate,
        "human_gate": "PENDING",
        "promotion_status": "NOT_PROMOTED",
    }
    (run_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Run deterministic DIRECTV PR-2 portrait alignment and fidelity QA.")
    parser.add_argument("--master", type=Path, default=Path("input/directv-hero-01/master.png"))
    parser.add_argument("--candidate", type=Path, default=Path("runs/directv-pr1b-001/portrait-candidate.png"))
    parser.add_argument("--run-dir", type=Path, default=Path("runs/directv-pr2-001"))
    args = parser.parse_args()

    try:
        report = run_pr2(args.master, args.candidate, args.run_dir)
    except Exception as exc:
        print(json.dumps({"automated_gate": "FAIL", "error": str(exc)}, indent=2))
        return 2

    print(json.dumps(report, indent=2))
    return 0 if report["automated_gate"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
