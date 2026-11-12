import sys
from PIL import Image, ImageOps
# crop.py in.jpg out.jpg x0 y0 x1 y1 (fractions) [width]
im = Image.open(sys.argv[1]); W, H = im.size
x0, y0, x1, y1 = [float(v) for v in sys.argv[3:7]]
c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
w = int(sys.argv[7]) if len(sys.argv) > 7 else c.width
c = c.resize((w, int(c.height*w/c.width)), Image.LANCZOS)
c = ImageOps.autocontrast(c.convert("L"), cutoff=1)
c.save(sys.argv[2], quality=90); print(c.size)
