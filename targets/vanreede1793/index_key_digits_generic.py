"""Index handwritten numeric cells on a downloaded DECODE key."""

import json
from pathlib import Path
import sys

import easyocr


root = Path(__file__).parent
record, image_id = sys.argv[1], sys.argv[2]
pages = [int(value) for value in sys.argv[3].split(",")]
reader = easyocr.Reader(["en"], gpu=False, verbose=False)
for page in pages:
    destination = root / f"easy_R{record}_P{page}.json"
    if destination.exists() and destination.stat().st_size > 10:
        continue
    source = root / ".." / "vanreede1787" / "decode" / f"IMG_R{record}_I{image_id}_P{page}.jpg"
    print(f"OCR R{record} P{page}", flush=True)
    found = reader.readtext(
        str(source), detail=1, paragraph=False, canvas_size=4096,
        mag_ratio=1.0, allowlist="0123456789",
    )
    destination.write_text(json.dumps([
        {"box": [[float(x), float(y)] for x, y in box], "text": text, "confidence": float(confidence)}
        for box, text, confidence in found
    ], indent=2) + "\n", encoding="utf-8")
    print(f"P{page}: {len(found)}", flush=True)
