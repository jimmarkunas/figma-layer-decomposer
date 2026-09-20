from pathlib import Path

import numpy as np
from PIL import Image

from decomposer.directv_pr2_qa import _align_candidate, _alpha_bbox


def test_alpha_bbox_detects_nontransparent_content() -> None:
    alpha = np.zeros((6, 8), dtype=np.uint8)
    alpha[1:5, 2:7] = 255
    assert _alpha_bbox(alpha) == (2, 1, 7, 5)


def test_alignment_is_deterministic_and_uses_master_canvas() -> None:
    candidate = Image.new("RGBA", (20, 20), (0, 0, 0, 0))
    for x in range(5, 15):
        for y in range(2, 18):
            candidate.putpixel((x, y), (100, 100, 100, 255))

    aligned_a, placement_a = _align_candidate(candidate, (1586, 992))
    aligned_b, placement_b = _align_candidate(candidate, (1586, 992))

    assert aligned_a.size == (1586, 992)
    assert aligned_b.size == (1586, 992)
    assert placement_a == placement_b
    assert placement_a["x"] == 620
    assert placement_a["y"] == 78
    assert placement_a["height"] == 717
    assert aligned_a.tobytes() == aligned_b.tobytes()
