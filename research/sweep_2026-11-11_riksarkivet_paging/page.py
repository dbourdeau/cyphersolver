"""python page.py <man> [a b] : contact sheets (5 cols x 5 rows, 312 px a spread) from the local 900 px copies in scratch/pg/<man>,
every image a..b, written to scratch/ps/<man>_<a>-<b>.jpg; also prints an ink score per image (share of dark pixels
after local background removal) so that the densest leaves (struck-through cipher with interlinear text) can be re-checked."""
import os, sys, glob
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import rik
man = sys.argv[1]; d = f'{rik.SP}/pg/{man}'; o = f'{rik.SP}/ps'; os.makedirs(o, exist_ok=True)
fs = sorted(glob.glob(d + '/*.jpg')); ids = [int(os.path.basename(f)[:5]) for f in fs]
a = int(sys.argv[2]) if len(sys.argv) > 2 else ids[0]; b = int(sys.argv[3]) if len(sys.argv) > 3 else ids[-1]
sel = [(i, f) for i, f in zip(ids, fs) if a <= i <= b]
TW, COLS, PER = 312, 5, 25
def ink(im):
    g = im.convert('L'); bg = g.filter(ImageFilter.GaussianBlur(12))
    x = np.asarray(bg).astype(int) - np.asarray(g).astype(int)
    m = (x > 28).astype(float); h, w = m.shape; B = 90
    best = [m[r:r + B, c:c + B].mean() for r in range(0, h - B, 45) for c in range(0, w - B, 45)]
    best.sort(); return float(np.mean(best[-6:])) if best else 0.0
sc = {}
for k in range(0, len(sel), PER):
    ch = sel[k:k + PER]; tiles = []
    for i, f in ch:
        im = Image.open(f)
        if im.size[1] > im.size[0] * 1.6: im = im.crop((0, 0, im.size[0], int(im.size[0] * 1.3)))
        sc[i] = round(ink(im), 4)
        tiles.append(im.resize((TW, max(1, int(im.size[1] * TW / im.size[0])))))
    print(rik.grid(tiles, [i for i, _ in ch], COLS, TW, f'{o}/{man}_{ch[0][0]:03d}-{ch[-1][0]:03d}.jpg'))
top = sorted(sc.items(), key=lambda t: -t[1])[:25]
print('ink top:', top)
import json; json.dump(sc, open(f'{o}/{man}_ink.json', 'w'))
