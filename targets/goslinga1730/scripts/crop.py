# crop a region of a scan screenshot: python crop.py <scan no> <x0> <y0> <x1> <y1> <out> [scale]
# coordinates in original screenshot pixels (2490x3400)
import sys, os
from PIL import Image, ImageOps
n, x0, y0, x1, y1, out = sys.argv[1:7]; s = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(os.path.join(os.environ.get('SD', 'scans'), f'p{int(n):04d}.png')).convert('L').crop((int(x0), int(y0), int(x1), int(y1)))
im = ImageOps.autocontrast(im, cutoff=1)
if s != 1: im = im.resize((int(im.width*s), int(im.height*s)), Image.LANCZOS)
im.save(out)
