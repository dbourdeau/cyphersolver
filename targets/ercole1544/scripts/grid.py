# line grid: dynamic programme over the ink profile picks exactly n line centres with gaps near the page's spacing. Corrects linecrop.py, which lost two lines on c. 78r.
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter1d
PAGES = {'A': ('0078r', 29), 'B': ('0078v', 27), 'C': ('0079r', 15), 'D': ('0174r', 25), 'E': ('0174v', 26), 'F': ('0175r', 26), 'G': ('0175v', 26)}
def load(k):
    return np.asarray(Image.open(f'scans/enh/{PAGES[k][0]}_page.png').convert('L'), dtype=float)
def grid(k):
    a = load(k); n = PAGES[k][1]; W = a.shape[1]
    ink = (a < 90).astype(float)[:, int(W*.12):int(W*.88)].sum(axis=1)
    s = gaussian_filter1d(ink, 10); s = s/s.max()
    # candidates: local maxima
    c = [i for i in range(14, len(s)-14) if s[i] == s[i-12:i+13].max() and s[i] > .12]
    best = None
    for H in range(85, 140, 1):
        # DP over candidates
        m = len(c); D = np.full((n, m), -1e9); P = np.zeros((n, m), int)
        D[0, :] = [s[y] for y in c]
        for i in range(1, n):
            for j in range(m):
                for l in range(j-1, max(-1, j-8), -1):
                    g = c[j]-c[l]
                    if g < .7*H or g > 1.45*H: continue
                    v = D[i-1, l] + s[c[j]] - .8*abs(g-H)/H
                    if v > D[i, j]: D[i, j] = v; P[i, j] = l
        j = int(np.argmax(D[n-1])); v = D[n-1, j]
        if best is None or v > best[0]:
            ys = [j]
            for i in range(n-1, 0, -1):
                j = P[i, j]; ys.append(j)
            best = (v, H, [c[x] for x in ys[::-1]])
    v, H, ys = best
    return a, np.array(ys), H
if __name__ == '__main__':
    import json
    out = {}
    for k in PAGES:
        a, ys, H = grid(k)
        out[k] = [int(y) for y in ys]
        print(k, a.shape, H, 'first', ys[:3], 'last', ys[-2:], 'gaps', np.diff(ys).min(), np.diff(ys).max())
    json.dump(out, open('round3/grid.json', 'w'))
