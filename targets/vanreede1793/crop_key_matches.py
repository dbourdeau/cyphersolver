"""Make contact sheets of exact EasyOCR numeric matches in the R2846 key."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance


ROOT = Path(__file__).parent
SCANS = ROOT / ".." / "vanreede1787" / "decode"


def make_sheet(numbers: list[str], pages: list[int], destination: Path) -> None:
    tiles: list[Image.Image] = []
    for page in pages:
        index_file = ROOT / f"easy_p{page}.json"
        if not index_file.exists():
            continue
        found = json.loads(index_file.read_text(encoding="utf-8"))
        source = Image.open(SCANS / f"IMG_R2846_I19098_P{page}.jpg").convert("RGB")
        for item in found:
            value = item["text"]
            if value not in numbers:
                continue
            xs = [point[0] for point in item["box"]]
            ys = [point[1] for point in item["box"]]
            cx, cy = sum(xs) / len(xs), sum(ys) / len(ys)
            crop = source.crop((max(0, int(cx - 760)), max(0, int(cy - 95)), min(source.width, int(cx + 180)), min(source.height, int(cy + 95))))
            crop = ImageEnhance.Contrast(crop).enhance(1.25)
            crop.thumbnail((940, 190))
            tile = Image.new("RGB", (970, 235), "white")
            ImageDraw.Draw(tile).text((8, 6), f"{value}  P{page}  ({int(cx)},{int(cy)})  conf={item['confidence']:.2f}", fill="black")
            tile.paste(crop, (8, 32))
            tiles.append(tile)
    cols = 1
    rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 970, max(235, rows * 235)), "white")
    for index, tile in enumerate(tiles):
        sheet.paste(tile, ((index % cols) * 970, (index // cols) * 235))
    sheet.save(destination, quality=95)
    print(f"wrote {destination.name}: {len(tiles)} matches")


if __name__ == "__main__":
    import sys

    make_sheet(sys.argv[1].split(","), [int(value) for value in sys.argv[2].split(",")], Path(sys.argv[3]))
