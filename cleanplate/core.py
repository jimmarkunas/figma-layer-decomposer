from __future__ import annotations

import hashlib, json
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import cv2
import numpy as np
from PIL import Image
from jsonschema import Draft202012Validator


@dataclass(frozen=True)
class Bounds:
    x: int; y: int; width: int; height: int
    @property
    def right(self): return self.x + self.width
    @property
    def bottom(self): return self.y + self.height
    def as_dict(self): return {"x": self.x, "y": self.y, "width": self.width, "height": self.height}

class ReconstructionBackend(Protocol):
    def reconstruct(self, master: np.ndarray, target_mask: np.ndarray, approved_zone: Bounds) -> np.ndarray: ...

class OpenCVInpaintingBackend:
    def __init__(self, radius: float = 3.0): self.radius = radius
    def reconstruct(self, master, target_mask, approved_zone):
        crop = master[approved_zone.y:approved_zone.bottom, approved_zone.x:approved_zone.right].copy()
        mask = target_mask[approved_zone.y:approved_zone.bottom, approved_zone.x:approved_zone.right]
        return cv2.inpaint(crop, mask, self.radius, cv2.INPAINT_TELEA)

def _bounds(raw): return Bounds(*(raw[k] for k in ("x", "y", "width", "height")))
def _sha256(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def validate_manifest(manifest_path: Path, schema_path: Path) -> dict:
    data = json.loads(manifest_path.read_text())
    schema = json.loads(schema_path.read_text())
    errors = sorted(Draft202012Validator(schema).iter_errors(data), key=lambda e: list(e.path))
    if errors: raise ValueError("manifest schema validation failed: " + "; ".join(e.message for e in errors))
    return data

def load_rgb(path: Path) -> np.ndarray:
    with Image.open(path) as image: return np.asarray(image.convert("RGB")).copy()

def load_mask(path: Path, canvas: tuple[int, int], mode: str, bounds: Bounds | None = None) -> np.ndarray:
    with Image.open(path) as image:
        if mode == "full_canvas":
            if image.size != canvas: raise ValueError(f"mask dimensions {image.size} do not match canvas {canvas}")
            if image.mode == "RGBA": return np.asarray(image.getchannel("A"), dtype=np.uint8).copy()
            return np.asarray(image.convert("L"), dtype=np.uint8).copy()
        if mode != "bounded" or bounds is None: raise ValueError("bounded mask mode requires bounds")
        validate_bounds(bounds, canvas, "mask bounds")
        if image.size != (bounds.width, bounds.height): raise ValueError(f"bounded mask dimensions {image.size} do not match mask bounds")
        bounded = np.asarray(image.getchannel("A") if image.mode == "RGBA" else image.convert("L"), dtype=np.uint8)
        mask = np.zeros((canvas[1], canvas[0]), dtype=np.uint8); mask[bounds.y:bounds.bottom, bounds.x:bounds.right] = bounded
        return mask.copy()

def validate_bounds(bounds: Bounds, canvas: tuple[int, int], label: str):
    w, h = canvas
    if bounds.x < 0 or bounds.y < 0 or bounds.width < 1 or bounds.height < 1 or bounds.right > w or bounds.bottom > h:
        raise ValueError(f"{label} is outside canvas")

def changed_pixel_counts(source: np.ndarray, output: np.ndarray, zone: Bounds) -> tuple[int, int]:
    if source.shape != output.shape: raise ValueError("source and output shapes differ")
    changed = np.any(source != output, axis=2)
    inside = np.zeros(changed.shape, dtype=bool); inside[zone.y:zone.bottom, zone.x:zone.right] = True
    return int((changed & inside).sum()), int((changed & ~inside).sum())

def assert_unchanged_region(source: np.ndarray, output: np.ndarray, zone: Bounds) -> None:
    _, outside_count = changed_pixel_counts(source, output, zone)
    if outside_count: raise ValueError(f"unchanged-region gate failed: {outside_count} outside-zone pixels changed")

def validate_candidate_patch(patch: np.ndarray, expected_shape: tuple[int, ...]) -> None:
    if not isinstance(patch, np.ndarray) or patch.shape != expected_shape:
        raise ValueError("backend candidate patch has incompatible shape/type")
    if patch.dtype.kind not in "uif":
        raise ValueError("backend candidate patch must use a numeric integer or floating-point type")
    if not np.isfinite(patch).all():
        raise ValueError("backend candidate patch contains non-finite pixel values")
    if np.any((patch < 0) | (patch > 255)):
        raise ValueError("backend candidate patch contains pixel values outside 0..255")

def run(manifest_path: Path, schema_path: Path, source_path: Path, mask_path: Path, target_id: str, run_dir: Path, backend=None) -> dict:
    manifest = validate_manifest(manifest_path, schema_path)
    if target_id not in manifest["targets"]: raise ValueError(f"unknown target: {target_id}")
    target = manifest["targets"][target_id]; canvas = (manifest["canvas"]["width"], manifest["canvas"]["height"])
    source = load_rgb(source_path)
    if (source.shape[1], source.shape[0]) != canvas: raise ValueError("source dimensions do not match canvas")
    core, zone = _bounds(target["core_bounds"]), _bounds(target["approved_zone"])
    validate_bounds(core, canvas, "core bounds"); validate_bounds(zone, canvas, "approved zone")
    if not (zone.x <= core.x and zone.y <= core.y and zone.right >= core.right and zone.bottom >= core.bottom): raise ValueError("core bounds are not contained by approved zone")
    mask_spec = target["mask"]; mask_bounds = _bounds(mask_spec["bounds"]) if "bounds" in mask_spec else None
    mask = load_mask(mask_path, canvas, mask_spec["mode"], mask_bounds)
    edit_mask = ((mask > 0) & (np.indices(mask.shape)[1] >= zone.x) & (np.indices(mask.shape)[1] < zone.right) & (np.indices(mask.shape)[0] >= zone.y) & (np.indices(mask.shape)[0] < zone.bottom))
    if not edit_mask.any(): raise ValueError("target mask has no pixels inside approved zone")
    backend = backend or OpenCVInpaintingBackend()
    patch = backend.reconstruct(source, (edit_mask.astype(np.uint8) * 255), zone)
    validate_candidate_patch(patch, source[zone.y:zone.bottom, zone.x:zone.right].shape)
    output = source.copy(); local = edit_mask[zone.y:zone.bottom, zone.x:zone.right]
    zone_output = output[zone.y:zone.bottom, zone.x:zone.right].copy(); zone_output[local] = patch[local]; output[zone.y:zone.bottom, zone.x:zone.right] = zone_output
    inside_count, outside_count = changed_pixel_counts(source, output, zone); changed = np.any(output != source, axis=2); outside = changed.copy(); outside[zone.y:zone.bottom, zone.x:zone.right] = False
    run_dir.mkdir(parents=True, exist_ok=False)
    Image.fromarray(output).save(run_dir / "candidate.png", format="PNG")
    preview = output.copy(); preview[zone.y:zone.bottom, zone.x:zone.right] = np.clip(preview[zone.y:zone.bottom, zone.x:zone.right] * .65 + np.array([40, 120, 255]) * .35, 0, 255).astype(np.uint8); Image.fromarray(preview).save(run_dir / "preview.png")
    diff = np.abs(output.astype(np.int16) - source.astype(np.int16)).astype(np.uint8); Image.fromarray(diff).save(run_dir / "difference.png")
    unchanged = np.zeros_like(diff); unchanged[outside] = 255; Image.fromarray(unchanged).save(run_dir / "unchanged-region-diff.png")
    reload_image = load_rgb(run_dir / "candidate.png")
    if reload_image.shape != source.shape: raise ValueError("serialized output dimensions changed")
    assert_unchanged_region(source, reload_image, zone)
    report = {"mockup_id": manifest["mockup_id"], "target_id": target_id, "pipeline_version": manifest["version"], "source_sha256": _sha256(source_path), "output_sha256": _sha256(run_dir / "candidate.png"), "canvas": {"width": canvas[0], "height": canvas[1]}, "core_bounds": core.as_dict(), "approved_zone": zone.as_dict(), "changed_pixels_inside_zone": inside_count, "changed_pixels_outside_zone": outside_count, "automated_gate": "PASS" if outside_count == 0 else "FAIL", "human_gate": "PENDING", "notes": []}
    (run_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    assert_unchanged_region(source, output, zone)
    return report
