from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from .core import run

def main(argv=None):
    p = argparse.ArgumentParser(); p.add_argument("--manifest", type=Path, required=True); p.add_argument("--schema", type=Path, required=True); p.add_argument("--source", type=Path, required=True); p.add_argument("--mask", type=Path, required=True); p.add_argument("--target", required=True); p.add_argument("--run-dir", type=Path, required=True)
    args = p.parse_args(argv)
    try:
        print(json.dumps(run(manifest_path=args.manifest, schema_path=args.schema, source_path=args.source, mask_path=args.mask, target_id=args.target, run_dir=args.run_dir), indent=2)); return 0
    except Exception as exc: print(f"clean-plate: {exc}", file=sys.stderr); return 1
