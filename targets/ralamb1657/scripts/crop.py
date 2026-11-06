"""python crop.py <img> <out> x0 y0 x1 y1 [width]  (fractions of the full image; output resized to width, default 1800)"""
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass
from PIL import Image, ImageOps
im = Image.open(sys.argv[1]); W, H = im.size
x0, y0, x1, y1 = [float(v) for v in sys.argv[3:7]]
w = int(sys.argv[7]) if len(sys.argv) > 7 else 1800
c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
c = ImageOps.autocontrast(c.convert('L'), cutoff=1)
c = c.resize((w, int(c.height * w / c.width)), Image.LANCZOS)
c.save(sys.argv[2], quality=90)
