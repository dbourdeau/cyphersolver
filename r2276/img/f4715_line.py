# one line in 3 stacked segments: python f4715_line.py ytop ybot [scale] [out] [dy_right]
import sys
from PIL import Image
im = Image.open('f4715_17.jpg')
y0, y1 = int(sys.argv[1]), int(sys.argv[2])
sc = float(sys.argv[3]) if len(sys.argv) > 3 else 1.6
out = sys.argv[4] if len(sys.argv) > 4 else 'f4715_l.png'
dy = int(sys.argv[5]) if len(sys.argv) > 5 else 0   # shift of the band at the right edge (skew)
X = [600, 1680, 2700, 3750]
parts = []
for i in range(3):
    a, b = X[i] - 50, X[i + 1] + 30
    s = dy * i // 3
    p = im.crop((a, y0 + s, b, y1 + s)); p = p.resize((int(p.width * sc), int(p.height * sc)), Image.LANCZOS)
    parts.append(p)
W = max(p.width for p in parts); H = sum(p.height + 6 for p in parts)
o = Image.new('RGB', (W, H), 'white'); y = 0
for p in parts:
    o.paste(p, (0, y)); y += p.height + 6
o.save(out)
