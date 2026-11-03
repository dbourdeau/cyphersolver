# usage: lines.py : deskews each page, fits each text line as a smooth curve y(x), writes scans/enh/ds_<page>.npy and round3/curves.json. No server requests.
import json
import numpy as np
from PIL import Image
from scipy import ndimage as ni
from scipy.ndimage import gaussian_filter1d
from grid import PAGES
curves = {}
for k, (p, n) in PAGES.items():
    im = Image.open(f'scans/enh/{p}_page.png').convert('L')
    best = None
    small = im.resize((im.width//3, im.height//3))
    for ang in np.arange(-3, 3.01, .1):
        r = np.asarray(small.rotate(ang, fillcolor=255, resample=Image.BILINEAR), dtype=float)
        W = r.shape[1]; pr = (r < 90)[:, int(W*.12):int(W*.88)].sum(axis=1).astype(float)
        v = ((pr[1:]-pr[:-1])**2).sum()
        if best is None or v > best[0]: best = (v, ang)
    ang = best[1]
    a = np.asarray(im.rotate(ang, fillcolor=255, resample=Image.BICUBIC), dtype=float)
    np.save(f'scans/enh/ds_{p}.npy', a.astype('uint8'))
    W = a.shape[1]; ink = (a < 100).astype(float)
    pr = gaussian_filter1d(ink[:, int(W*.12):int(W*.88)].sum(axis=1), 9); pr = pr/pr.max()
    c = [i for i in range(14, len(pr)-14) if pr[i] == pr[i-12:i+13].max() and pr[i] > .1]
    bestg = None
    for H in range(85, 140):
        m = len(c); D = np.full((n, m), -1e9); P = np.zeros((n, m), int); D[0] = [pr[y] for y in c]
        for i in range(1, n):
            for j in range(m):
                for l in range(j-1, max(-1, j-8), -1):
                    g = c[j]-c[l]
                    if .75*H <= g <= 1.35*H:
                        v = D[i-1, l]+pr[c[j]]-1.2*abs(g-H)/H
                        if v > D[i, j]: D[i, j] = v; P[i, j] = l
        j = int(np.argmax(D[n-1])); v = D[n-1, j]
        if bestg is None or v > bestg[0]:
            ys = [j]
            for i in range(n-1, 0, -1): j = P[i, j]; ys.append(j)
            bestg = (v, H, [c[x] for x in ys[::-1]])
    _, H, ys = bestg
    # per-line curve: block-wise offset search
    blocks = 12; bw = W//blocks; out = []
    for y in ys:
        off = []; xs = []
        for b in range(blocks):
            seg = ink[:, b*bw:(b+1)*bw].sum(axis=1)
            seg = gaussian_filter1d(seg, 7)
            r = int(H*.33); lo = max(0, y-r); w = seg[lo:y+r]
            if w.max() > 2: off.append(lo+int(np.argmax(w))-y); xs.append(b*bw+bw//2)
        off = np.array(off, float); xs = np.array(xs, float)
        if len(off) >= 3:
            f = np.polyfit(xs, off, 2)
            res = off-np.polyval(f, xs); keep = abs(res) < max(12, 1.5*res.std())
            f = np.polyfit(xs[keep], off[keep], 2)
        else:
            f = np.array([0, 0, 0.])
        out.append([float(v) for v in f]+[int(y)])
    curves[k] = dict(H=float(H), lines=out, ang=float(ang))
    print(k, 'angle', round(float(ang), 1), 'H', H, 'gaps', int(np.diff(ys).min()), int(np.diff(ys).max()))
json.dump(curves, open('round3/curves.json', 'w'))
