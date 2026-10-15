"""Index handwritten digits on candidate 1793 key R2851."""

from __future__ import annotations

import json
from pathlib import Path

import easyocr


ROOT = Path(__file__).parent
SCANS = ROOT / ".." / "vanreede1787" / "decode"
reader = easyocr.Reader(["en"], gpu=False, verbose=False)
for page in range(4, 10):
    destination = ROOT / f"easy_R2851_P{page}.json"
    if destination.exists() and destination.stat().st_size > 10:
        continue
    print(f"OCR P{page}", flush=True)
    found = reader.readtext(
        str(SCANS / f"IMG_R2851_I19192_P{page}.jpg"),
        detail=1,
        paragraph=False,
        canvas_size=4096,
        mag_ratio=1.0,
        allowlist="0123456789",
    )
    destination.write_text(
        json.dumps(
            [
                {
                    "box": [[float(x), float(y)] for x, y in box],
                    "text": text,
                    "confidence": float(confidence),
                }
                for box, text, confidence in found
            ],
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"P{page}: {len(found)}", flush=True)
