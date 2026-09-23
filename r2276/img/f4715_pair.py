# interlinear + cipher for one line, 4 overlapping segments: python f4715_pair.py yleft [dy_right=-45] [out] [up=150] [down=55]
import sys
from PIL import Image
im = Image.open('f4715_17.jpg')
yc = int(sys.argv[1]); dy = int(sys.argv[2]) if len(sys.argv) > 2 else -45
out = sys.argv[3] if len(sys.argv) > 3 else 'f4715_p.png'
up = int(sys.argv[4]) if len(sys.argv) > 4 else 150
dn = int(sys.argv[5]) if len(sys.argv) > 5 else 55
xs = [(580, 1400), (1330, 2150), (2080, 2900), (2830, 3700)]
parts = []
for i, (a, b) in enumerate(xs):
    s = dy * i // 3
    p = im.crop((a, yc - up + s, b, yc + dn + s)); p = p.resize((int(p.width * 1.6), int(p.height * 1.6)), Image.LANCZOS)
    parts.append(p)
W = max(p.width for p in parts); H = sum(p.height + 8 for p in parts)
o = Image.new('RGB', (W, H), (255, 200, 200)); y = 0
for p in parts:
    o.paste(p, (0, y)); y += p.height + 8
o.save(out)
