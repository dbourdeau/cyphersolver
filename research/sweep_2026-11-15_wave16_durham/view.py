"""python view.py <tag> <idx> [width]            : screening copy of a fetched frame (default 1100 px wide)
python view.py <tag> <idx> crop x0 y0 x1 y1   : full-resolution crop, fractions of the fetched frame"""
import os, sys, glob
from PIL import Image, ImageOps
here = os.path.dirname(os.path.abspath(__file__))
tag, idx = sys.argv[1], int(sys.argv[2])
f = glob.glob(os.path.join(here, 'img', tag, '%03d_*.jpg' % idx))[0]
im = Image.open(f); w, h = im.size
os.makedirs(os.path.join(here, 'img', 'v'), exist_ok=True)
if len(sys.argv) > 3 and sys.argv[3] == 'crop':
    x0, y0, x1, y1 = map(float, sys.argv[4:8])
    im = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    fn = os.path.join(here, 'img', 'v', 'crop_%s_%03d.jpg' % (tag, idx))
else:
    W = int(sys.argv[3]) if len(sys.argv) > 3 else 1100
    im = im.resize((W, int(h * W / w)), Image.LANCZOS)
    fn = os.path.join(here, 'img', 'v', '%s_%03d.jpg' % (tag, idx))
im.save(fn, quality=80); print(fn, im.size, os.path.basename(f))
