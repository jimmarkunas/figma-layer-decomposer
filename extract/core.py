from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

from cleanplate.core import Bounds, load_mask, load_rgb, validate_bounds, validate_manifest


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract(manifest_path: Path, schema_path: Path, source_path: Path, mask_path: Path, target_id: str, run_dir: Path) -> dict:
    manifest = validate_manifest(manifest_path, schema_path)
    if target_id not in manifest["targets"]:
        raise ValueError(f"unknown target: {target_id}")
    target = manifest["targets"][target_id]
    if target["kind"] not in {"raster_extract", "screen_extract"}:
        raise ValueError("target kind must be raster_extract or screen_extract")
    canvas = (manifest["canvas"]["width"], manifest["canvas"]["height"])
    source_before = sha256(source_path)
    source = load_rgb(source_path)
    if (source.shape[1], source.shape[0]) != canvas:
        raise ValueError("source dimensions do not match manifest canvas")
    placement = Bounds(**target["figma_placement"]["bounds"])
    validate_bounds(placement, canvas, "figma placement bounds")
    mask_spec = target["mask"]
    mask_bounds = Bounds(**mask_spec["bounds"]) if "bounds" in mask_spec else None
    mask = load_mask(mask_path, canvas, mask_spec["mode"], mask_bounds)
    alpha = mask[placement.y:placement.bottom, placement.x:placement.right].copy()
    rgb = source[placement.y:placement.bottom, placement.x:placement.right].copy()
    rgba = np.dstack((rgb, alpha))
    if rgba.shape != (placement.height, placement.width, 4):
        raise ValueError("extraction output dimensions are invalid")
    run_dir.mkdir(parents=True, exist_ok=False)
    extracted_path = run_dir / "extracted.png"
    Image.fromarray(rgba, mode="RGBA").save(extracted_path, format="PNG")
    alpha_path = run_dir / "alpha-mask.png"
    Image.fromarray(alpha, mode="L").save(alpha_path, format="PNG")
    preview = Image.new("RGB", (placement.width, placement.height), (224, 224, 224))
    draw = ImageDraw.Draw(preview)
    tile = 16
    for y in range(0, placement.height, tile):
        for x in range(0, placement.width, tile):
            if ((x // tile) + (y // tile)) % 2: draw.rectangle((x, y, x + tile, y + tile), fill=(192, 192, 192))
    preview.paste(Image.fromarray(rgb, mode="RGB"), mask=Image.fromarray(alpha, mode="L"))
    preview.save(run_dir / "preview.png", format="PNG")
    reloaded = np.asarray(Image.open(extracted_path).convert("RGBA"))
    if reloaded.shape != rgba.shape or not np.array_equal(reloaded, rgba):
        raise ValueError("serialized extraction does not preserve RGBA semantics")
    participating = alpha > 0
    exact_rgb = int(np.all(reloaded[:, :, :3][participating] == rgb[participating], axis=1).sum())
    rgb_mismatch = int(participating.sum()) - exact_rgb
    alpha_mismatch = int(np.count_nonzero(reloaded[:, :, 3] != alpha))
    transparent = int((alpha == 0).sum())
    partial = int(((alpha > 0) & (alpha < 255)).sum())
    source_after = sha256(source_path)
    source_unchanged = source_before == source_after
    report = {
        "mockup_id": manifest["mockup_id"], "target_id": target_id, "target_kind": target["kind"],
        "source_sha256_before": source_before, "source_sha256_after": source_after,
        "output_sha256": sha256(extracted_path), "source_canvas": {"width": canvas[0], "height": canvas[1]},
        "extraction_bounds": placement.as_dict(), "output": {"width": placement.width, "height": placement.height},
        "mask_mode": mask_spec["mode"], "participating_pixel_count": int(participating.sum()),
        "transparent_pixel_count": transparent, "partial_alpha_pixel_count": partial,
        "exact_rgb_match_pixels": exact_rgb, "rgb_mismatch_pixels": rgb_mismatch,
        "alpha_mismatch_pixels": alpha_mismatch, "source_unchanged": source_unchanged,
        "automated_gate": "PASS" if rgb_mismatch == 0 and alpha_mismatch == 0 and source_unchanged else "FAIL",
        "notes": []
    }
    (run_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    if report["automated_gate"] != "PASS": raise ValueError("extraction automated gate failed")
    return report
