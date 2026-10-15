"""Create labelled contact sheets for the remaining Fagel key thumbnails."""

import re
from pathlib import Path

from PIL import Image, ImageDraw


root = Path(__file__).parent / ".." / "vanreede1787" / "decode"
for record in (2842, 2843, 2844, 2845, 2847):
    paths = sorted(
        (root / f"thumbs_R{record}").glob("*.jpg"),
        key=lambda path: int(re.search(r"_P(\d+)", path.name).group(1)),
    )
    tiles = []
    for path in paths:
        page = re.search(r"_P(\d+)", path.name).group(1)
        image = Image.open(path).convert("RGB")
        image.thumbnail((360, 300))
        tile = Image.new("RGB", (380, 335), "white")
        ImageDraw.Draw(tile).text((8, 6), f"P{page}", fill="black")
        tile.paste(image, ((380 - image.width) // 2, 30))
        tiles.append(tile)
    cols = 4
    sheet = Image.new("RGB", (cols * 380, ((len(tiles) + cols - 1) // cols) * 335), "white")
    for index, tile in enumerate(tiles):
        sheet.paste(tile, ((index % cols) * 380, (index // cols) * 335))
    destination = root / f"R{record}_thumb_montage.jpg"
    sheet.save(destination, quality=92)
    print(destination)
