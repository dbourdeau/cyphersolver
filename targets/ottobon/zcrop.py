"""2x three-segment crops of given lines: python zcrop.py <tag> <png> x0 x1 y0 y1 <lines...>
Same box and line detection as cut_decode.py (two strips); segment k=0,1,2 left to right -> img/dl/z_<tag>_<NN>_<k>.png"""
import sys
import numpy as np
from PIL import Image, ImageFilter
tag, png = sys.argv[1], sys.argv[2]
x0, x1, y0, y1 = [float(v) for v in sys.argv[3:7]]
lines = [int(v) for v in sys.argv[7:]]
im = Image.open(png).convert('L'); s = im.width / 1200.0
box = (int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s))
pg = im.crop(box)
bg = pg.filter(ImageFilter.GaussianBlur(25))
a = np.clip(np.array(pg).astype(float) / np.maximum(np.array(bg).astype(float), 1), 0, 1) ** 2.2
a = (a * 255).astype(np.uint8)
W = a.shape[1]; ov = int(W * 0.04); NP = 2
cents = []
for p in range(NP):
    xa = max(0, p * W // NP - ov); xb = min(W, (p + 1) * W // NP + ov)
    ink = (a[:, xa:xb] < 110).sum(1).astype(float)
    sm = np.convolve(ink, np.ones(21) / 21, mode='same')
    z = sm - sm.mean(); ac = np.correlate(z, z, 'full')[len(z) - 1:]
    lo = int(40 * s / 2.6); hi = int(120 * s / 2.6)
    sp = lo + int(np.argmax(ac[lo:hi]))
    c = []; y = int(np.argmax(sm[:sp]))
    while y < len(sm):
        w0 = max(0, y - sp // 3); w1 = min(len(sm), y + sp // 3)
        y = w0 + int(np.argmax(sm[w0:w1]))
        if sm[y] > sm.max() * 0.15: c.append(y)
        y += sp
    cents.append(c)
off = int(sys.argv[0] and 0)
for L in lines:
    i0 = min(L - 1, len(cents[0]) - 1); i1 = min(L - 1, len(cents[1]) - 1)
    segs = [(0, W // 3 + 40, cents[0][i0]), (W // 3 - 40, 2 * W // 3 + 40, (cents[0][i0] + cents[1][i1]) // 2), (2 * W // 3 - 40, W, cents[1][i1])]
    for k, (xa, xb, cy) in enumerate(segs):
        cr = Image.fromarray(a[max(0, cy - 60):cy + 60, xa:xb])
        cr.resize((cr.width * 2, cr.height * 2), Image.LANCZOS).save('img/dl/z_%s_%02d_%d.png' % (tag, L, k))
print([len(c) for c in cents])
