"""Locate handwritten numeric code groups in the R2846 key scans."""

from __future__ import annotations

import json
from pathlib import Path

import easyocr


ROOT = Path(__file__).parent
SCANS = ROOT / ".." / "vanreede1787" / "decode"


reader = easyocr.Reader(["en"], gpu=False, verbose=False)
for page in (1, 3, 4, 5, 6, 7, 8, 9, 12):
    destination = ROOT / f"easy_p{page}.json"
    if destination.exists() and destination.stat().st_size > 10:
        continue
    image = SCANS / f"IMG_R2846_I19098_P{page}.jpg"
    print(f"OCR P{page}", flush=True)
    found = reader.readtext(
        str(image),
        detail=1,
        paragraph=False,
        canvas_size=4096,
        mag_ratio=1.0,
        allowlist="0123456789",
    )
    serializable = [
        {
            "box": [[float(x), float(y)] for x, y in box],
            "text": text,
            "confidence": float(confidence),
        }
        for box, text, confidence in found
    ]
    destination.write_text(
        json.dumps(serializable, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"P{page}: {len(found)}", flush=True)
