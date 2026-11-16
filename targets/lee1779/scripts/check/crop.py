# crop.py src out x0 y0 x1 y1 [maxw]  -- fractions (0-1) or pixels
import sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
v = [float(a) for a in sys.argv[3:7]]
maxw = int(sys.argv[7]) if len(sys.argv) > 7 else 1400
im = Image.open(src); W, H = im.size
if all(a <= 1 for a in v): v = [v[0]*W, v[1]*H, v[2]*W, v[3]*H]
c = im.crop(tuple(int(a) for a in v))
if c.width > maxw: c = c.resize((maxw, int(c.height * maxw / c.width)))
c.save(out, quality=85)
print(out, c.size)
