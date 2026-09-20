from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

import numpy as np
import yaml
from jsonschema import Draft202012Validator
from PIL import Image


class OperationContractError(ValueError):
    """Raised when an execution contract is invalid or violated."""


def _read_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise OperationContractError("Execution contract must be a YAML mapping.")
    return data


def _read_json(path: Path) -> dict[str, Any]:
    import json

    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise OperationContractError("Schema must be a JSON object.")
    return data


def load_operation_contract(contract_path: str | Path, schema_path: str | Path) -> dict[str, Any]:
    contract_file = Path(contract_path)
    schema_file = Path(schema_path)
    contract = _read_yaml(contract_file)
    schema = _read_json(schema_file)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(contract), key=lambda error: list(error.path))
    if errors:
        details = "; ".join(error.message for error in errors)
        raise OperationContractError(f"Execution contract schema validation failed: {details}")
    return contract


def authorize_tool(contract: dict[str, Any], tool_name: str) -> None:
    policy = contract.get("tool_policy", {})
    state = policy.get(tool_name)
    if state != "ALLOWED":
        raise OperationContractError(
            f"Tool '{tool_name}' is not authorized for operation {contract.get('operation_id', '<unknown>')}."
        )


def execution_receipt(contract: dict[str, Any]) -> dict[str, Any]:
    return {
        "operation_id": contract["operation_id"],
        "operation_class": contract["operation_class"],
        "inputs": {
            name: asset["sha256"]
            for name, asset in contract["inputs"].items()
        },
        "tool_policy": contract["tool_policy"],
        "candidates_allowed": contract["execution"]["candidates_allowed"],
        "must_not_generate": contract["must_not_generate"],
        "human_gate": contract["human_gate"],
        "promotion": contract["promotion"],
    }


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_input_hashes(contract: dict[str, Any], root: str | Path = ".") -> None:
    root_path = Path(root)
    failures: list[str] = []
    for name, asset in contract["inputs"].items():
        path = root_path / asset["path"]
        if not path.exists():
            failures.append(f"{name}: missing {path}")
            continue
        actual = sha256_file(path)
        expected = asset["sha256"].lower()
        if actual.lower() != expected:
            failures.append(f"{name}: SHA-256 mismatch ({actual} != {expected})")
    if failures:
        raise OperationContractError("Input verification failed: " + "; ".join(failures))


def verify_exact_edit(
    original_path: str | Path,
    candidate_path: str | Path,
    mask_path: str | Path,
) -> dict[str, int]:
    original = np.array(Image.open(original_path).convert("RGBA"))
    candidate = np.array(Image.open(candidate_path).convert("RGBA"))
    mask = np.array(Image.open(mask_path).convert("L"))

    if original.shape != candidate.shape:
        raise OperationContractError(
            f"EXACT_EDIT dimensions changed: original={original.shape[:2]}, candidate={candidate.shape[:2]}"
        )
    if mask.shape != original.shape[:2]:
        raise OperationContractError(
            f"Authorized mask dimensions do not match source: mask={mask.shape}, source={original.shape[:2]}"
        )

    changed = np.any(original != candidate, axis=2)
    authorized = mask > 0
    outside = changed & ~authorized

    changed_total = int(changed.sum())
    changed_inside = int((changed & authorized).sum())
    changed_outside = int(outside.sum())

    if changed_outside != 0:
        raise OperationContractError(
            f"EXACT_EDIT unauthorized pixel change: {changed_outside} changed pixels outside authorized mask."
        )

    return {
        "changed_pixels_total": changed_total,
        "changed_pixels_inside_mask": changed_inside,
        "changed_pixels_outside_mask": changed_outside,
    }
