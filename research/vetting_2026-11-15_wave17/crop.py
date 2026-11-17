"""python -I -X utf8 crop.py <name> x0 y0 x1 y1 (fractions) [maxpx] -> img/<name>_c.jpg"""
import sys, os
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
n = sys.argv[1]; f = [float(x) for x in sys.argv[2:6]]; mx = int(sys.argv[6]) if len(sys.argv) > 6 else 1800
im = Image.open(os.path.join(here, 'img', n + '.jpg')); w, h = im.size
c = im.crop((int(f[0]*w), int(f[1]*h), int(f[2]*w), int(f[3]*h))); c.thumbnail((mx, mx))
suffix = sys.argv[7] if len(sys.argv) > 7 else 'c'
c.convert('RGB').save(os.path.join(here, 'img', f'{n}_{suffix}.jpg'), quality=88); print(c.size)
