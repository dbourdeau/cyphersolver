# usage: sweep_gz.py : shape-only sweep. Class templates for g, z, q, p, f are built from the located cells by iterated alignment (no decoded text is used).
# Each g or z token is scored against each template within a small window round its stroke; tokens whose own label loses are listed for a look at the crop.
import json, sys
import numpy as np
from scipy import ndimage as ni
cells = json.load(open('round3/cells3.json'))
CL = ['g', 'z', 'q', 'p', 'f']
S = {}
def strip(L):
    if L not in S: S[L] = ni.gaussian_filter(255-np.load(f'scans/enh/strip_{L}.npy').astype(float), 1.4)[::2, ::2]
    return S[L]
Hh = 62  # half-res cell height
def cut(c, dx, dy):
    s = strip(c['line']); H = c['H']; up = int(.75*H)//2
    x = int(c['cx']/2)+dx; y0 = up-int(.42*H/2)+dy; y1 = y0+int(1.34*H/2); w = int(.34*H/2)
    if x-w < 0 or x+w > s.shape[1] or y0 < 0 or y1 > s.shape[0]: return None
    return s[y0:y1, x-w:x+w]
def resize(a, shape=(62, 40)):
    return ni.zoom(a, (shape[0]/a.shape[0], shape[1]/a.shape[1]), order=1)
def ncc(a, t):
    a = a-a.mean(); n = np.linalg.norm(a)
    return float((a*t).sum()/(n+1e-6))
def norm(t):
    t = t-t.mean(); return t/np.linalg.norm(t)
T = {}
for c0 in CL:
    v = [resize(cut(c, 0, 0)) for c in cells if c['tok'] == c0 and cut(c, 0, 0) is not None]
    T[c0] = norm(np.mean(v, axis=0))
DX = range(-10, 11, 2); DY = (-4, -2, 0, 2, 4)
def best(c, t):
    b = (-9, 0, 0)
    for dx in DX:
        for dy in DY:
            a = cut(c, dx, dy)
            if a is None: continue
            v = ncc(resize(a), t)
            if v > b[0]: b = (v, dx, dy)
    return b
for it in range(3):
    new = {c0: [] for c0 in CL}
    for c in cells:
        if c['tok'] in CL:
            v, dx, dy = best(c, T[c['tok']])
            if v > .35: new[c['tok']].append(resize(cut(c, dx, dy)))
    T = {c0: norm(np.mean(new[c0], axis=0)) for c0 in CL}
    print(it, {c0: len(new[c0]) for c0 in CL})
np.save('round3/templates.npy', np.array([T[c0] for c0 in CL]))
rows = []
for c in cells:
    if c['tok'] in 'gz':
        sc = {c0: best(c, T[c0])[0] for c0 in CL}
        w = max(sc, key=sc.get)
        rows.append(dict(line=c['line'], ti=c['ti'], tok=c['tok'], win=w, own=round(sc[c['tok']], 3), g=round(sc['g'], 3), z=round(sc['z'], 3), q=round(sc['q'], 3), cx=c['cx'], H=c['H'], m=c['m']))
json.dump(rows, open('round3/gz_scores.json', 'w'))
from collections import Counter
print(Counter((r['tok'], r['win']) for r in rows))
