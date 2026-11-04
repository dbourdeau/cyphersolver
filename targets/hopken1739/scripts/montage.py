"""Full-resolution crops of disputed groups stacked into one image. Spec: label:img:x0,y0,x1,y1"""
import sys
from PIL import Image, ImageDraw
out = sys.argv[1]; tiles = []
for spec in sys.argv[2:]:
    lab, img, box = spec.split(":")
    im = Image.open(f"scans/00{img}_wmax.jpg").crop(tuple(map(int, box.split(","))))
    tiles.append((lab, im))
W = max(t.width for _, t in tiles) + 160; H = sum(t.height + 10 for _, t in tiles)
S = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(S); y = 0
for lab, t in tiles:
    d.text((5, y + 10), lab, fill="red"); S.paste(t, (160, y)); y += t.height + 10
S.save(out, quality=92)
