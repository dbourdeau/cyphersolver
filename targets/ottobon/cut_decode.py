"""Line crops from the DECODE R2252 openings.  python cut_decode.py <tag> <png> x0 x1 y0 y1 [nparts]
Box in 1200-px-wide thumbnail coordinates.  Background-normalised, gamma to fade bleed-through; the box is split into
nparts vertical strips; line centres found per strip from the ink projection; crops written to img/dl/<tag>_lNN_pK.png
(1.5x).  Prints the centres per strip."""
import sys, os
import numpy as np
from PIL import Image, ImageFilter
tag, png = sys.argv[1], sys.argv[2]
x0, x1, y0, y1 = [float(v) for v in sys.argv[3:7]]
NP = int(sys.argv[7]) if len(sys.argv) > 7 else 2
im = Image.open(png).convert('L'); s = im.width / 1200.0
box = (int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s))
pg = im.crop(box)
bg = pg.filter(ImageFilter.GaussianBlur(25))
a = np.array(pg).astype(float) / np.maximum(np.array(bg).astype(float), 1)
a = np.clip(a, 0, 1) ** 2.2
a = (a * 255).astype(np.uint8)
os.makedirs('img/dl', exist_ok=True)
for f in os.listdir('img/dl'):
    if f.startswith(tag + '_'): os.remove(os.path.join('img/dl', f))
W = a.shape[1]; ov = int(W * 0.04)
allc = []
for p in range(NP):
    xa = max(0, p * W // NP - ov); xb = min(W, (p + 1) * W // NP + ov)
    ink = (a[:, xa:xb] < 110).sum(1).astype(float)
    sm = np.convolve(ink, np.ones(21) / 21, mode='same')
    # estimate spacing by autocorrelation
    z = sm - sm.mean(); ac = np.correlate(z, z, 'full')[len(z) - 1:]
    lo = int(40 * s / 2.6); hi = int(120 * s / 2.6)
    sp = lo + int(np.argmax(ac[lo:hi]))
    cents = []
    y = int(np.argmax(sm[:sp]))
    while y < len(sm):
        w0 = max(0, y - sp // 3); w1 = min(len(sm), y + sp // 3)
        y = w0 + int(np.argmax(sm[w0:w1]))
        if sm[y] > sm.max() * 0.15: cents.append(y)
        y += sp
    allc.append(cents)
    for i, c in enumerate(cents):
        ya = max(0, c - int(sp * 0.75)); yb = min(a.shape[0], c + int(sp * 0.75))
        cr = Image.fromarray(a[ya:yb, xa:xb])
        cr = cr.resize((int(cr.width * 1.5), int(cr.height * 1.5)), Image.LANCZOS)
        cr.save('img/dl/%s_l%02d_p%d.png' % (tag, i + 1, p))
    print('strip', p, 'spacing', sp, 'lines', len(cents), cents)
