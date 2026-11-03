"""Zoom crops at disputed sign positions. Position = sign index along the line's inked extent; clear words weigh
0.7 sign per letter. usage: mzoom.py OUT M01@15 M02@13 ..."""
import sys, numpy as np
from PIL import Image, ImageOps, ImageDraw
C = [190, 378, 552, 743, 939, 1121, 1309, 1489, 1698, 1907]
P1 = {l.split('\t')[0]: l.rstrip('\n').split('\t')[1].split() for l in open('validation/pass1.txt', encoding='utf-8') if l.startswith('M')}
im = Image.open('scans/c13r_cipher.jpg').convert('L'); a = np.asarray(im); rows = []
for spec in sys.argv[2:]:
    ln, i = spec.split('@'); i = int(i); L = int(ln[1:]) - 1; c = C[L]
    w = [0.7 * len(t) if t.startswith('[') else 1.0 for t in P1[ln]]
    sig = [k for k, t in enumerate(P1[ln]) if not t.startswith('[')]
    pos = sum(w[:sig[min(i, len(sig) - 1)]]) + 0.5; frac = pos / sum(w)
    band = a[c - 50:c + 50]; cols = np.where((band < 120).sum(0) > 2)[0]; x0, x1 = cols.min(), cols.max()
    x = int(x0 + frac * (x1 - x0))
    r = ImageOps.autocontrast(im.crop((max(0, x - 420), c - 90, x + 420, c + 90)), cutoff=1).resize((640, 137)).convert('RGB')
    d = ImageDraw.Draw(r); d.rectangle([0, 0, 70, 16], fill='yellow'); d.text((2, 2), spec, fill='black'); d.line([(320, 125), (320, 136)], fill='red', width=3)
    rows.append(r)
o = Image.new('RGB', (1290, ((len(rows) + 1) // 2) * 141), 'blue')
for k, r in enumerate(rows): o.paste(r, ((k % 2) * 650, (k // 2) * 141))
o.save(sys.argv[1]); print(o.size)
