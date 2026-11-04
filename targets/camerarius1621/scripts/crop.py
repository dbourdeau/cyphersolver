"""crop.py SRC.jpg OUT.jpg x0 y0 x1 y1 [scale]  (fractions 0-1); upscales and autocontrasts"""
import sys
from PIL import Image, ImageOps
src, out = sys.argv[1], sys.argv[2]; x0, y0, x1, y1 = map(float, sys.argv[3:7]); sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.6
im = Image.open(src).convert('L'); W, H = im.size
c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
c = ImageOps.autocontrast(c, cutoff=1).resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
c.save(out, quality=92)
