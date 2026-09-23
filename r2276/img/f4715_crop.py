# crop bands of BnF fr. 4715 f.2r (f4715_17.jpg): python f4715_crop.py y0 y1 [nparts] [scale] [out]
import sys
from PIL import Image
im = Image.open('f4715_17.jpg')
y0, y1 = int(sys.argv[1]), int(sys.argv[2])
n = int(sys.argv[3]) if len(sys.argv) > 3 else 3
sc = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
out = sys.argv[5] if len(sys.argv) > 5 else 'f4715_band.png'
X0, X1 = 380, 3700
w = (X1 - X0) // n
parts = []
for i in range(n):
    a = X0 + i * w - 60; b = X0 + (i + 1) * w + 60
    p = im.crop((max(a, 0), y0, min(b, im.width), y1))
    if sc != 1: p = p.resize((int(p.width * sc), int(p.height * sc)), Image.LANCZOS)
    parts.append(p)
W = max(p.width for p in parts); H = sum(p.height + 8 for p in parts)
o = Image.new('RGB', (W, H), 'white'); y = 0
for p in parts:
    o.paste(p, (0, y)); y += p.height + 8
o.save(out)
