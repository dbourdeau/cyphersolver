# crop a region of a 2x viewer screenshot: python crop.py <scan> <x0> <y0> <x1> <y1> <out> [scale]
import sys
from PIL import Image
s, x0, y0, x1, y1, out = sys.argv[1:7]; sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(f'scans/p{int(s):04d}.png').crop((int(x0), int(y0), int(x1), int(y1)))
if sc != 1.0: im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
im.save(out)
