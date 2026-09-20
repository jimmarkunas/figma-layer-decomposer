from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from decomposer.operation_guard import (
    OperationContractError,
    authorize_tool,
    execution_receipt,
    load_operation_contract,
    verify_exact_edit,
    verify_input_hashes,
)


DEFAULT_SCHEMA = Path("schema/edit-operation.schema.json")


def _load(args: argparse.Namespace) -> dict:
    return load_operation_contract(args.contract, args.schema)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate and enforce image-operation execution contracts.")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate")
    validate.add_argument("--contract", required=True)
    validate.add_argument("--root", default=".")

    receipt = sub.add_parser("receipt")
    receipt.add_argument("--contract", required=True)

    authorize = sub.add_parser("authorize")
    authorize.add_argument("--contract", required=True)
    authorize.add_argument("--tool", required=True)

    exact = sub.add_parser("verify-exact-edit")
    exact.add_argument("--original", required=True)
    exact.add_argument("--candidate", required=True)
    exact.add_argument("--mask", required=True)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "validate":
            contract = _load(args)
            verify_input_hashes(contract, args.root)
            print(json.dumps({"status": "PASS", "operation_id": contract["operation_id"]}, indent=2))
            return 0

        if args.command == "receipt":
            contract = _load(args)
            print(json.dumps(execution_receipt(contract), indent=2, sort_keys=True))
            return 0

        if args.command == "authorize":
            contract = _load(args)
            authorize_tool(contract, args.tool)
            print(json.dumps({"status": "PASS", "tool": args.tool}, indent=2))
            return 0

        if args.command == "verify-exact-edit":
            report = verify_exact_edit(args.original, args.candidate, args.mask)
            print(json.dumps({"status": "PASS", **report}, indent=2))
            return 0

    except OperationContractError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2), file=sys.stderr)
        return 2

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
