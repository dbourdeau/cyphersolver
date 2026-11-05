"""Cut an upscaled crop of a DECODE leaf for sign-by-sign reading.
usage: python crops.py img/<file>.png OUT.png x0 y0 x1 y1 [scale=2.4]   (coordinates in the original image)"""
import sys
from PIL import Image
f, out, x0, y0, x1, y1 = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
s = float(sys.argv[7]) if len(sys.argv) > 7 else 2.4
im = Image.open(f).convert('L').crop((x0, y0, x1, y1))
im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
im.save(out)
print(out, im.size)
