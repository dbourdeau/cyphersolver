"""python crop.py img x0 y0 x1 y1 out [maxw]: crop a local full-size scan (no server request)."""
import sys
from PIL import Image
f, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
mw = int(sys.argv[7]) if len(sys.argv) > 7 else 1900
im = Image.open(f).crop((x0, y0, x1, y1))
if im.width > mw: im = im.resize((mw, int(im.height * mw / im.width)))
im.save(out, quality=88)
