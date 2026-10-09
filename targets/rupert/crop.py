"""crop.py <img> <out> x0 y0 x1 y1 [maxw] : fractional coords (0-1) crop, resized to maxw (default 1800)."""
import sys
from PIL import Image
a = sys.argv
im = Image.open(a[1]); W, H = im.size
x0, y0, x1, y1 = [float(v) for v in a[3:7]]
c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
mw = int(a[7]) if len(a) > 7 else 1800
if c.width > mw: c = c.resize((mw, int(c.height*mw/c.width)))
c.save(a[2], quality=88)
