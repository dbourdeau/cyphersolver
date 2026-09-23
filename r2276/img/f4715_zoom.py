# zoom a region of f4715_17.jpg: python f4715_zoom.py x0 x1 y0 y1 [scale] [out]
import sys
from PIL import Image
im = Image.open('f4715_17.jpg')
x0, x1, y0, y1 = map(int, sys.argv[1:5])
sc = float(sys.argv[5]) if len(sys.argv) > 5 else 2.0
out = sys.argv[6] if len(sys.argv) > 6 else 'f4715_z.png'
p = im.crop((x0, y0, x1, y1)); p = p.resize((int(p.width * sc), int(p.height * sc)), Image.LANCZOS)
p.save(out)
