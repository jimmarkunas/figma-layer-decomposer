from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image
from jsonschema import Draft202012Validator


@dataclass(frozen=True)
class Bounds:
    x: int
    y: int
    width: int
    height: int

    @property
    def right(self):
        return self.x + self.width

    @property
    def bottom(self):
        return self.y + self.height

    def as_dict(self):
        return {"x": self.x, "y": self.y, "width": self.width, "height": self.height}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_manifest(manifest_path: Path, schema_path: Path) -> dict:
    data = json.loads(manifest_path.read_text())
    schema = json.loads(schema_path.read_text())
    errors = sorted(Draft202012Validator(schema).iter_errors(data), key=lambda e: list(e.path))
    if errors:
        raise ValueError("manifest schema validation failed: " + "; ".join(e.message for e in errors))
    return data


def load_rgb(path: Path) -> np.ndarray:
    with Image.open(path) as image:
        return np.asarray(image.convert("RGB")).copy()


def validate_bounds(bounds: Bounds, canvas: tuple[int, int], label: str):
    w, h = canvas
    if bounds.x < 0 or bounds.y < 0 or bounds.width < 1 or bounds.height < 1 or bounds.right > w or bounds.bottom > h:
        raise ValueError(f"{label} is outside canvas")


def load_mask(path: Path, canvas: tuple[int, int], mode: str, bounds: Bounds | None = None) -> np.ndarray:
    with Image.open(path) as image:
        if mode == "full_canvas":
            if image.size != canvas:
                raise ValueError(f"mask dimensions {image.size} do not match canvas {canvas}")
            if image.mode == "RGBA":
                return np.asarray(image.getchannel("A"), dtype=np.uint8).copy()
            return np.asarray(image.convert("L"), dtype=np.uint8).copy()
        if mode != "bounded" or bounds is None:
            raise ValueError("bounded mask mode requires bounds")
        validate_bounds(bounds, canvas, "mask bounds")
        if image.size != (bounds.width, bounds.height):
            raise ValueError(f"bounded mask dimensions {image.size} do not match mask bounds")
        bounded = np.asarray(image.getchannel("A") if image.mode == "RGBA" else image.convert("L"), dtype=np.uint8)
        mask = np.zeros((canvas[1], canvas[0]), dtype=np.uint8)
        mask[bounds.y:bounds.bottom, bounds.x:bounds.right] = bounded
        return mask.copy()
