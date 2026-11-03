"""Tile thumbnails into a labelled contact sheet: python sheet.py out.jpg cols img1 img2 ..."""
import sys
from PIL import Image, ImageDraw
out, cols, files = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
W = 600
ims = []
for f in files:
    im = Image.open(f); im = im.resize((W, int(im.height * W / im.width))); ims.append((f, im))
H = max(i.height for _, i in ims)
rows = (len(ims) + cols - 1) // cols
S = Image.new("RGB", (cols * W, rows * H), "white"); d = ImageDraw.Draw(S)
for k, (f, im) in enumerate(ims):
    x, y = (k % cols) * W, (k // cols) * H
    S.paste(im, (x, y)); d.rectangle([x, y, x + 90, y + 22], fill="yellow"); d.text((x + 4, y + 4), f.split("/")[-1][:5], fill="black")
S.save(out, quality=80)
