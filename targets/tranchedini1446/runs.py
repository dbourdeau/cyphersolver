"""Cut texts/f139_seg.txt into cipher runs (texts/f139_runs.txt): a run is a maximal stretch of cipher signs; clear-text clusters (x),
other wide groups and the page's clear words break it; a run continues over a line break when the next line starts with a sign.
Wide flat signs (width <= 71, height >= 19, no ascender) become WV (bar-o-bar-o, Veneziani) or WC (three circles, che; row ratio >= 0.8).
Cluster 32 members taller than 23 px are clear-text fragments. usage: python runs.py"""
import json, numpy as np
from PIL import Image
a = np.array(Image.open('seg/deskew.png'))
d = json.load(open('seg/groups.json')); L = d['lines']
items = {(i['line'], tuple(i['box'])): i['c'] for i in json.load(open('seg/items.json'))}
CLEAR = {21, 6, 49, 30, 38, 45, 61, 84, 68, 17, 73, 27, 3, 40, 43, 16, 37}
seq = []   # (line, token) with None as break
for n in range(2, 42):
    c = L[n - 1]; toks = []
    for x0, y0, x1, y1, ink in d['groups'][str(n)]:
        cy = (y0 + y1) / 2
        if not (c - 22 <= cy <= c + 14): continue
        k = items.get((n, (x0, y0, x1, y1)))
        w, h = x1 - x0, y1 - y0
        if k is not None:
            if k in CLEAR or (k == 32 and h > 23): toks.append(None)
            else: toks.append(f'c{k}')
        elif w > 62:
            if w <= 71 and 19 <= h <= 26:
                g = a[y0:y1, x0:x1] < 120
                toks.append('WC' if g.sum(1).max() / g.shape[1] >= 0.8 else 'WV')
            else: toks.append(None)
    seq.append((n, toks))
runs = []; cur = []
for n, toks in seq:
    for t in toks:
        if t is None:
            if cur: runs.append(cur)
            cur = []
        else: cur.append(t)
    # a run may continue over the line break: keep cur
if cur: runs.append(cur)
runs = [r for r in runs if len(r) >= 3]
open('texts/f139_runs.txt', 'w').write('\n'.join(' '.join(r) for r in runs) + '\n')
n = sum(map(len, runs))
print(len(runs), 'runs', n, 'signs', len({t for r in runs for t in r}), 'types', sorted(map(len, runs))[-8:])
