from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core import extract


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--mask", type=Path, required=True)
    parser.add_argument("--target-id", required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(extract(args.manifest, args.schema, args.source, args.mask, args.target_id, args.run_dir), indent=2))
        return 0
    except Exception as exc:
        print(f"extract-master: {exc}", file=sys.stderr)
        return 1
