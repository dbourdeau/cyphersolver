"""Crop wide context around OCR numeric matches in a selected key."""

import json
from pathlib import Path
import sys

from PIL import Image, ImageDraw, ImageEnhance


root = Path(__file__).parent
record, image_id = sys.argv[1], sys.argv[2]
numbers = sys.argv[3].split(",")
pages = [int(value) for value in sys.argv[4].split(",")]
destination = Path(sys.argv[5])
tiles = []
for page in pages:
    index_path = root / f"easy_R{record}_P{page}.json"
    if not index_path.exists():
        continue
    source = Image.open(root / ".." / "vanreede1787" / "decode" / f"IMG_R{record}_I{image_id}_P{page}.jpg").convert("RGB")
    for item in json.loads(index_path.read_text(encoding="utf-8")):
        if item["text"] not in numbers:
            continue
        xs = [point[0] for point in item["box"]]
        ys = [point[1] for point in item["box"]]
        cx, cy = sum(xs) / 4, sum(ys) / 4
        crop = source.crop((max(0, int(cx - 760)), max(0, int(cy - 95)), min(source.width, int(cx + 760)), min(source.height, int(cy + 95))))
        crop = ImageEnhance.Contrast(crop).enhance(1.25)
        crop.thumbnail((1520, 190))
        tile = Image.new("RGB", (1550, 235), "white")
        ImageDraw.Draw(tile).text((8, 6), f"{item['text']} P{page} ({int(cx)},{int(cy)}) conf={item['confidence']:.2f}", fill="black")
        tile.paste(crop, (8, 32))
        tiles.append(tile)
sheet = Image.new("RGB", (1550, max(235, len(tiles) * 235)), "white")
for index, tile in enumerate(tiles):
    sheet.paste(tile, (0, index * 235))
sheet.save(destination, quality=96)
print(f"wrote {destination}: {len(tiles)} matches")
