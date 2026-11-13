"""python hi.py <man> <i> [L|R|B] [px=2200] [top bottom as fractions]: one image at high resolution, a half (L/R) or both, optional vertical band -> scratch/hi/"""
import sys, os
import rik
man, i = sys.argv[1], int(sys.argv[2]); side = sys.argv[3] if len(sys.argv) > 3 else 'B'; px = int(sys.argv[4]) if len(sys.argv) > 4 else 2200
t0 = float(sys.argv[5]) if len(sys.argv) > 5 else 0; t1 = float(sys.argv[6]) if len(sys.argv) > 6 else 1
os.makedirs(rik.SP + '/hi', exist_ok=True); p0 = f'{rik.SP}/hi/{man}_{i:05d}_{px}.jpg'
from PIL import Image
if os.path.exists(p0): im = Image.open(p0)
else: im = rik.crop(rik.img(man, i, px, True)); im.save(p0, quality=85)
w, h = im.size; x0, x1 = (0, w // 2 + 20) if side == 'L' else (w // 2 - 20, w) if side == 'R' else (0, w)
c = im.crop((x0, int(h * t0), x1, int(h * t1)))
if c.size[0] > 1500: c = c.resize((1500, int(c.size[1] * 1500 / c.size[0])))
p = f'{rik.SP}/hi/{man}_{i:05d}_{side}_{t0}_{t1}.jpg'; c.save(p, quality=85); print(p, c.size)
