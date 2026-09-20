import json
import hashlib
from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from extract.core import extract

ROOT = Path(__file__).parents[1]

def case(tmp_path, *, kind="raster_extract", mode="full_canvas", placement=(2, 1, 4, 3), mask_bounds=None, mask_size=None, canvas=(8, 6)):
    tmp_path.mkdir(parents=True, exist_ok=True)
    w, h = canvas; source = np.arange(w*h*3, dtype=np.uint8).reshape(h,w,3); source_path=tmp_path/"source.png"; Image.fromarray(source).save(source_path)
    x,y,pw,ph=placement
    if mode == "bounded": mw,mh = mask_size or (mask_bounds[2],mask_bounds[3]); mask=np.zeros((mh,mw),np.uint8); mask[:,:]=0; mask[0,0]=64; mask[0,1]=128; mask[1:,1:]=255
    else: mw,mh=mask_size or canvas; mask=np.zeros((mh,mw),np.uint8); mask[y:y+ph,x:x+pw]=255; mask[y,x]=0; mask[y,min(x+1,mw-1)]=64; mask[y,min(x+2,mw-1)]=128
    mask_path=tmp_path/"mask.png"; Image.fromarray(mask).save(mask_path)
    spec={"file":"mask.png","mode":mode};
    if mask_bounds: spec["bounds"]={"x":mask_bounds[0],"y":mask_bounds[1],"width":mask_bounds[2],"height":mask_bounds[3]}
    manifest={"version":"0.1.0","mockup_id":"synthetic","canvas":{"width":w,"height":h},"source":{"file":"source.png","immutable":True,"sha256":None},"targets":{"target":{"kind":kind,"core_bounds":{"x":x,"y":y,"width":pw,"height":ph},"approved_zone":{"x":0,"y":0,"width":w,"height":h},"halo_px":0,"mask":spec,"output":{"canonical_file":"x","preview_file":"x","qa_report":"x"},"figma_placement":{"name":"x","destination_group":"x","bounds":{"x":x,"y":y,"width":pw,"height":ph}}}},"sequence":["target"]}
    mp=tmp_path/"manifest.json"; mp.write_text(json.dumps(manifest)); return mp,source_path,mask_path

def run_case(tmp_path, **kwargs):
    mp,sp,mask=case(tmp_path,**kwargs); return extract(mp,ROOT/"schema/layer-manifest.schema.json",sp,mask,"target",tmp_path/"run")

def test_full_canvas_and_intermediate_alpha_exact_rgb_and_transparency(tmp_path):
    report=run_case(tmp_path); out=np.asarray(Image.open(tmp_path/"run/extracted.png").convert("RGBA")); assert report["automated_gate"]=="PASS" and report["partial_alpha_pixel_count"]==2; assert out[0,0,3]==0
    src=np.asarray(Image.open(tmp_path/"source.png").convert("RGB")); assert np.array_equal(out[:,:,:3][out[:,:,3]>0],src[1:4,2:6,:][out[:,:,3]>0])

@pytest.mark.parametrize("kind", ["raster_extract","screen_extract"])
def test_supported_kinds_and_bounded_mask(tmp_path, kind):
    report=run_case(tmp_path,kind=kind,mode="bounded",mask_bounds=(2,1,4,3)); assert report["mask_mode"]=="bounded" and report["output"]=={"width":4,"height":3}

def test_invalid_inputs_fail(tmp_path):
    mp,sp,mask=case(tmp_path,kind="clean_plate")
    with pytest.raises(ValueError,match="kind"): extract(mp,ROOT/"schema/layer-manifest.schema.json",sp,mask,"target",tmp_path/"r1")
    mp,sp,mask=case(tmp_path/"bad"); manifest=json.loads(mp.read_text()); manifest["canvas"]["width"]=9; mp.write_text(json.dumps(manifest))
    with pytest.raises(ValueError,match="source dimensions"): extract(mp,ROOT/"schema/layer-manifest.schema.json",sp,mask,"target",tmp_path/"r2")

def test_invalid_bounds_mask_dimensions_and_missing_target_fail(tmp_path):
    mp,sp,mask=case(tmp_path,placement=(7,1,1,3))
    manifest=json.loads(mp.read_text()); manifest["targets"]["target"]["figma_placement"]["bounds"]["width"]=4; mp.write_text(json.dumps(manifest))
    with pytest.raises(ValueError,match="outside canvas"): extract(mp,ROOT/"schema/layer-manifest.schema.json",sp,mask,"target",tmp_path/"r1")
    mp,sp,mask=case(tmp_path/"bounded",mode="bounded",mask_bounds=(2,1,4,3),mask_size=(3,3))
    with pytest.raises(ValueError,match="bounded mask dimensions"): extract(mp,ROOT/"schema/layer-manifest.schema.json",sp,mask,"target",tmp_path/"r2")
    mp,sp,mask=case(tmp_path/"missing")
    with pytest.raises(ValueError,match="unknown target"): extract(mp,ROOT/"schema/layer-manifest.schema.json",sp,mask,"missing",tmp_path/"r3")

def test_serialization_and_source_immutability(tmp_path):
    mp,sp,mask=case(tmp_path); before=hashlib.sha256(sp.read_bytes()).hexdigest(); report=extract(mp,ROOT/"schema/layer-manifest.schema.json",sp,mask,"target",tmp_path/"run"); after=hashlib.sha256(sp.read_bytes()).hexdigest(); assert report["source_unchanged"] and before==after; assert Image.open(tmp_path/"run/extracted.png").mode=="RGBA"; assert Image.open(tmp_path/"run/extracted.png").size==(4,3)
