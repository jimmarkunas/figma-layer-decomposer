from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
import pytest
import yaml
from PIL import Image

from decomposer.operation_guard import (
    OperationContractError,
    authorize_tool,
    execution_receipt,
    load_operation_contract,
    verify_exact_edit,
    verify_input_hashes,
)


SCHEMA_PATH = Path("schema/edit-operation.schema.json")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _base_contract(source: Path) -> dict:
    return {
        "version": "1.0",
        "operation_id": "test-op",
        "operation_class": "EXACT_EDIT",
        "inputs": {
            "source": {
                "path": str(source),
                "sha256": _sha256(source),
                "role": "immutable source",
            }
        },
        "authorized_mask": {
            "file": "mask.png",
            "meaning": "authorized exact-edit pixels",
        },
        "tool_policy": {
            "image_gen": "DENIED",
            "deterministic_raster": "ALLOWED",
            "segmentation": "DENIED",
            "alternate_source": "DENIED",
        },
        "execution": {
            "candidates_allowed": 1,
            "fail_closed": True,
            "silent_fallback_allowed": False,
        },
        "must_preserve": ["all pixels outside mask"],
        "may_synthesize_only": [],
        "must_not_generate": ["background", "halo", "glow"],
        "qa": {
            "verify_input_hashes": True,
            "dimensions_unchanged_when_applicable": True,
            "zero_changed_pixels_outside_mask_when_applicable": True,
        },
        "human_gate": "PENDING",
        "promotion": "NOT_PROMOTED",
    }


def test_exact_edit_schema_rejects_image_gen(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    Image.new("RGBA", (4, 4), (0, 0, 0, 255)).save(source)
    contract = _base_contract(source)
    contract["tool_policy"]["image_gen"] = "ALLOWED"
    contract_file = tmp_path / "operation.yaml"
    contract_file.write_text(yaml.safe_dump(contract), encoding="utf-8")

    with pytest.raises(OperationContractError):
        load_operation_contract(contract_file, SCHEMA_PATH)


def test_authorize_tool_denies_unapproved_tool(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    Image.new("RGBA", (4, 4), (0, 0, 0, 255)).save(source)
    contract = _base_contract(source)

    with pytest.raises(OperationContractError):
        authorize_tool(contract, "image_gen")

    authorize_tool(contract, "deterministic_raster")


def test_execution_receipt_contains_required_guardrails(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    Image.new("RGBA", (4, 4), (0, 0, 0, 255)).save(source)
    contract = _base_contract(source)

    receipt = execution_receipt(contract)

    assert receipt["operation_id"] == "test-op"
    assert receipt["operation_class"] == "EXACT_EDIT"
    assert receipt["candidates_allowed"] == 1
    assert receipt["tool_policy"]["image_gen"] == "DENIED"
    assert receipt["human_gate"] == "PENDING"
    assert receipt["promotion"] == "NOT_PROMOTED"


def test_verify_input_hashes_fails_closed_on_mismatch(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    Image.new("RGBA", (4, 4), (0, 0, 0, 255)).save(source)
    contract = _base_contract(source)
    contract["inputs"]["source"]["path"] = source.name
    contract["inputs"]["source"]["sha256"] = "0" * 64

    with pytest.raises(OperationContractError):
        verify_input_hashes(contract, tmp_path)


def test_verify_exact_edit_passes_when_changes_stay_inside_mask(tmp_path: Path) -> None:
    original = np.zeros((4, 4, 4), dtype=np.uint8)
    original[:, :, 3] = 255
    candidate = original.copy()
    candidate[1, 1, 0] = 50
    mask = np.zeros((4, 4), dtype=np.uint8)
    mask[1, 1] = 255

    original_path = tmp_path / "original.png"
    candidate_path = tmp_path / "candidate.png"
    mask_path = tmp_path / "mask.png"
    Image.fromarray(original, "RGBA").save(original_path)
    Image.fromarray(candidate, "RGBA").save(candidate_path)
    Image.fromarray(mask, "L").save(mask_path)

    report = verify_exact_edit(original_path, candidate_path, mask_path)

    assert report["changed_pixels_total"] == 1
    assert report["changed_pixels_inside_mask"] == 1
    assert report["changed_pixels_outside_mask"] == 0


def test_verify_exact_edit_rejects_outside_mask_change(tmp_path: Path) -> None:
    original = np.zeros((4, 4, 4), dtype=np.uint8)
    original[:, :, 3] = 255
    candidate = original.copy()
    candidate[3, 3, 0] = 50
    mask = np.zeros((4, 4), dtype=np.uint8)
    mask[1, 1] = 255

    original_path = tmp_path / "original.png"
    candidate_path = tmp_path / "candidate.png"
    mask_path = tmp_path / "mask.png"
    Image.fromarray(original, "RGBA").save(original_path)
    Image.fromarray(candidate, "RGBA").save(candidate_path)
    Image.fromarray(mask, "L").save(mask_path)

    with pytest.raises(OperationContractError):
        verify_exact_edit(original_path, candidate_path, mask_path)
