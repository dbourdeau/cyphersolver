"""Cut cipher-only strips (one cipher line each, without the clear line above) for sign-first transcription.
usage: strips.py IMG OUTPREFIX HALF_H SCALE NPARTS c1 c2 ...   (centres in image rows)
Each output image holds one cipher line split into a left and a right half, stacked, with a red guide line between.
"""
import sys
from PIL import Image, ImageDraw, ImageOps

img, pref, hh, sc, n = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5])
cs = [int(x) for x in sys.argv[6:]]
im = Image.open(img).convert("L")
W = im.width
mid = W // 2
for i, c in enumerate(cs):
    step = W // n
    parts = [im.crop((max(0, k * step - 120), c - hh, min(W, (k + 1) * step + 120), c + hh)) for k in range(n)]
    pw = max(p.width for p in parts)
    out = Image.new("L", (pw, n * (parts[0].height + 6)), 255)
    for k, p in enumerate(parts):
        out.paste(p, (0, k * (parts[0].height + 6)))
    out = ImageOps.autocontrast(out, cutoff=1)
    out = out.resize((int(out.width * sc), int(out.height * sc)), Image.LANCZOS).convert("RGB")
    d = ImageDraw.Draw(out)
    for k in range(1, n):
        y = int(k * (parts[0].height + 6) * sc) - 2
        d.line([(0, y), (out.width, y)], fill=(255, 0, 0), width=2)
    out.save(f"{pref}{i:02d}.png")
    print(f"{pref}{i:02d}.png", c)
