"""Re-check, part B: contact sheet and tiles for the corpus documents given fresh blind passes.
Usage: python recheck_prep.py sheet OUT.jpg | tiles OUT_DIR   (rotations in ROT, degrees clockwise)"""
import os
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = None
HERE = Path(__file__).resolve().parent
RECS = ["740", "7481", "7482", "852", "912"]
ROT = {}
MAXW, BAND, OVER = 2000, 1000, 90


def pages(rec):
    d = HERE / "decode_cache" / f"R{rec}"
    return sorted(d.glob("IMG_*"), key=lambda p: int(re.search(r"_P(\d+)", p.name).group(1)))


if sys.argv[1] == "sheet":
    cells = []
    for r in RECS:
        for i, p in enumerate(pages(r), 1):
            im = Image.open(p).convert("RGB"); im.thumbnail((300, 300)); cells.append((f"R{r} p{i}", im))
    cols = 5; rows = (len(cells) + cols - 1) // cols
    cv = Image.new("RGB", (cols * 310, rows * 330), "white"); dr = ImageDraw.Draw(cv)
    for k, (lab, im) in enumerate(cells):
        x0, y0 = (k % cols) * 310, (k // cols) * 330
        dr.text((x0 + 4, y0 + 2), lab, fill="red"); cv.paste(im, (x0, y0 + 24))
    cv.save(sys.argv[2], quality=80)
else:
    out = sys.argv[2]; os.makedirs(out, exist_ok=True)
    for r in RECS:
        for pi, p in enumerate(pages(r), 1):
            im = Image.open(p).convert("RGB")
            rot = ROT.get(f"R{r}", 0)
            if rot:
                im = im.rotate(-rot, expand=True)
            if im.width > MAXW:
                im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
            y, k = 0, 1
            while y < im.height:
                box = (0, y, im.width, min(im.height, y + BAND))
                im.crop(box).save(os.path.join(out, f"R{r}_p{pi}_t{k}.jpg"), quality=90)
                if box[3] >= im.height:
                    break
                y += BAND - OVER; k += 1
            print(f"R{r} p{pi} tiles {k}")
