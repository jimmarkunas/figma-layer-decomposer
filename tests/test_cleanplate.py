import json
from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from cleanplate.core import Bounds, changed_pixel_counts, run, validate_manifest

ROOT = Path(__file__).parents[1]

class SolidBackend:
    def reconstruct(self, master, target_mask, approved_zone):
        return np.full_like(master[approved_zone.y:approved_zone.bottom, approved_zone.x:approved_zone.right], 77)

def setup_case(tmp_path, *, zone=(2, 2, 4, 4), core=(3, 3, 2, 2), canvas=(10, 8), mask_size=None):
    w, h = canvas; source = np.arange(w*h*3, dtype=np.uint8).reshape(h, w, 3)
    source_path = tmp_path / "master.png"; mask_path = tmp_path / "mask.png"
    Image.fromarray(source).save(source_path)
    mw, mh = mask_size or canvas; mask = np.zeros((mh, mw), dtype=np.uint8); mask[3:min(5,mh), 3:min(5,mw)] = 255; Image.fromarray(mask).save(mask_path)
    manifest = {"version":"0.1.0","mockup_id":"synthetic","canvas":{"width":w,"height":h},"source":{"file":"master.png","immutable":True,"sha256":None},"targets":{"target":{"kind":"clean_plate","core_bounds":dict(zip(("x","y","width","height"),core)),"approved_zone":dict(zip(("x","y","width","height"),zone)),"halo_px":1,"mask":{"file":"mask.png","mode":"full_canvas"},"output":{"canonical_file":"candidate.png","preview_file":"preview.png","qa_report":"report.json"},"figma_placement":{"name":"x","destination_group":"01_BACKGROUND","bounds":dict(zip(("x","y","width","height"),zone))}}},"sequence":["target"]}
    mp = tmp_path / "manifest.json"; mp.write_text(json.dumps(manifest)); return mp, source_path, mask_path, manifest

def test_schema_validation_actually_runs(tmp_path):
    mp, *_ = setup_case(tmp_path); bad = json.loads(mp.read_text()); del bad["canvas"]; mp.write_text(json.dumps(bad))
    with pytest.raises(ValueError, match="schema validation"): validate_manifest(mp, ROOT / "schema/layer-manifest.schema.json")

@pytest.mark.parametrize("zone", [(9, 0, 2, 2), (-1, 0, 2, 2)])
def test_invalid_zone_fails(tmp_path, zone):
    mp, source, mask, _ = setup_case(tmp_path, zone=zone)
    with pytest.raises(ValueError): run(mp, ROOT/"schema/layer-manifest.schema.json", source, mask, "target", tmp_path/"run", SolidBackend())

def test_core_outside_zone_fails(tmp_path):
    mp, source, mask, _ = setup_case(tmp_path, zone=(2,2,2,2), core=(3,3,3,3))
    with pytest.raises(ValueError, match="contained"): run(mp, ROOT/"schema/layer-manifest.schema.json", source, mask, "target", tmp_path/"run", SolidBackend())

def test_canvas_mismatch_and_invalid_mask_fail(tmp_path):
    mp, source, mask, manifest = setup_case(tmp_path); manifest["canvas"]["width"] = 11; mp.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="dimensions"): run(mp, ROOT/"schema/layer-manifest.schema.json", source, mask, "target", tmp_path/"run1", SolidBackend())
    (tmp_path/"badmask").mkdir()
    mp, source, mask, _ = setup_case(tmp_path/"badmask", mask_size=(9,8))
    with pytest.raises(ValueError, match="mask dimensions"): run(mp, ROOT/"schema/layer-manifest.schema.json", source, mask, "target", (tmp_path/"run2"), SolidBackend())

def test_run_artifacts_unchanged_gate_and_serialization(tmp_path):
    mp, source_path, mask, _ = setup_case(tmp_path)
    report = run(mp, ROOT/"schema/layer-manifest.schema.json", source_path, mask, "target", tmp_path/"run", SolidBackend())
    assert report["automated_gate"] == "PASS" and report["changed_pixels_outside_zone"] == 0
    assert Image.open(tmp_path/"run/candidate.png").size == (10,8)
    for name in ("candidate.png","preview.png","difference.png","unchanged-region-diff.png","report.json"): assert (tmp_path/"run"/name).exists()
    original = np.asarray(Image.open(source_path)); assert np.array_equal(original, np.arange(10*8*3,dtype=np.uint8).reshape(8,10,3))

def test_deliberate_outside_pixel_fails_gate(tmp_path):
    mp, source_path, mask, _ = setup_case(tmp_path); run(mp, ROOT/"schema/layer-manifest.schema.json", source_path, mask, "target", tmp_path/"run", SolidBackend())
    source = np.asarray(Image.open(source_path)); output = np.asarray(Image.open(tmp_path/"run/candidate.png")).copy(); output[0,0] ^= 1
    assert changed_pixel_counts(source, output, Bounds(2,2,4,4))[1] == 1

def test_cumulative_sequencing_uses_prior_output(tmp_path):
    mp, source, mask, manifest = setup_case(tmp_path); first = run(mp, ROOT/"schema/layer-manifest.schema.json", source, mask, "target", tmp_path/"first", SolidBackend())
    second_mask = tmp_path/"mask2.png"; Image.fromarray(np.pad(np.zeros((2,2),dtype=np.uint8), ((3,3),(3,5)), constant_values=255)).save(second_mask)
    second = run(mp, ROOT/"schema/layer-manifest.schema.json", tmp_path/"first/candidate.png", second_mask, "target", tmp_path/"second", SolidBackend())
    assert second["source_sha256"] == __import__("hashlib").sha256((tmp_path/"first/candidate.png").read_bytes()).hexdigest()
