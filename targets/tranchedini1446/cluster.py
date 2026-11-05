"""Cluster the narrow glyph groups of f. 139 into candidate sign types and write contact sheets.
usage: python cluster.py [k=90]   -> seg/items.json, seg/clu_<k>.png"""
import json, sys
import numpy as np
from PIL import Image, ImageDraw
from sklearn.cluster import AgglomerativeClustering
k = int(sys.argv[1]) if len(sys.argv) > 1 else 90
d = json.load(open('seg/groups.json')); L = d['lines']
im = Image.open('seg/deskew.png'); a = np.array(im)
items = []
for n, gs in d['groups'].items():
    c = L[int(n) - 1]
    for x0, y0, x1, y1, ink in gs:
        cy = (y0 + y1) / 2; w, h = x1 - x0, y1 - y0
        if c - 22 <= cy <= c + 14 and w <= 62 and 14 <= h <= 52 and int(n) >= 2:
            items.append(dict(line=int(n), box=[x0, y0, x1, y1], ink=ink))
def feat(it):
    x0, y0, x1, y1 = it['box']
    cr = Image.fromarray(255 - a[y0:y1, x0:x1])
    s = 26 / max(cr.size)
    cr = cr.resize((max(1, round(cr.width * s)), max(1, round(cr.height * s))), Image.LANCZOS)
    can = Image.new('L', (30, 30)); can.paste(cr, ((30 - cr.width) // 2, (30 - cr.height) // 2))
    v = np.array(can, float).ravel() / 255
    return np.concatenate([v, [it['box'][2] - it['box'][0], it['box'][3] - it['box'][1]] / np.array([40, 40]) * 0.8])
F = np.array([feat(i) for i in items])
lab = AgglomerativeClustering(n_clusters=k, linkage='ward').fit_predict(F)
for it, l in zip(items, lab): it['c'] = int(l)
json.dump(items, open('seg/items.json', 'w'))
order = sorted(range(k), key=lambda c: -sum(1 for l in lab if l == c))
sheet_rows = []
CW = 60
for c in order:
    mem = [it for it in items if it['c'] == c]
    row = Image.new('L', (60 + 14 * CW, 56), 255); dr = ImageDraw.Draw(row)
    dr.text((2, 20), f'c{c} n{len(mem)}', fill=0)
    for j, it in enumerate(mem[:14]):
        x0, y0, x1, y1 = it['box']; cr = Image.fromarray(a[y0:y1, x0:x1])
        row.paste(cr, (60 + j * CW + 2, 2))
    sheet_rows.append(row)
per = 14
for s in range(0, len(sheet_rows), per):
    H = Image.new('L', (sheet_rows[0].width, 56 * len(sheet_rows[s:s + per])), 255)
    for i, r in enumerate(sheet_rows[s:s + per]): H.paste(r, (0, 56 * i))
    H.save(f'seg/clu_{k}_{s // per}.png')
print(len(items), 'items', k, 'clusters')
