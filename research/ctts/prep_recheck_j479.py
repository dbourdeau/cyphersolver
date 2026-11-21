"""Worklist for the second correction round of the T-S NS J479 CTTS project (21 Nov 2026), from the line-by-line review of
the sign table (targets/tsnsj479/ctts_table_review.md).

A box is rechecked when (a) it is one of the cut-outs flagged in the review (cut-out numbers count left to right within a
table row, in the table's own order), or (b) it sits in a row the review found systematically confused: U, a, 7, P, p, q, d
and the resh rows (9, s, 8, y, 5), plus S, f, e, h, K, z, g, m, t, b, n, o, y, 2. Writes recheck/<band>_<n>.png (the band
around the box at 3x with the box outlined, the whole band height) and recheck.json (id, band, n, current label, why).
"""
import json
from pathlib import Path
from PIL import Image, ImageDraw

P = Path(__file__).parent / 'projects' / 'tsnsj479'
boxes = json.load(open(P / 'boxes_corrected.json', encoding='utf-8'))
labels = json.load(open(P / 'labels_corrected.json', encoding='utf-8'))
FLAG = {'I': [2, 5, 14], 'E': [1, 3, 4, 5, 10, 11, 14], 'A': [14, 17], 'N': [2, 11, 12, 13, 14, 15], '4': [5, 13, 16],
        'c': [3, 4, 5], 'B': [8, 9], 'd': [1, 2], '-': [5, 9, 15], '<': [4, 5, 10], 'p': [11], 'w': [4],
        'O': [3, 7, 14, 15, 16], '6': [9, 10, 12], 'X': [7], 'C': [2], 'U': [10, 11, 12], 'q': [3, 5, 6, 8], '9': [1, 2, 3, 8, 14]}
WHOLE = set('U a 7 P p q d S f e h K z g m t b n o y 2 5 8 s 9'.split())
byt = {}
for img, bx in boxes.items():
    for b in bx:
        lab = labels[img][str(b['n'])]
        if lab[0] in '?_#':
            continue
        byt.setdefault(lab.rstrip('.?'), []).append((img, b, lab))
work = {}
for t, items in byt.items():
    for k, (img, b, lab) in enumerate(items, 1):
        why = []
        if k in FLAG.get(t, []) and k <= 16:
            why.append(f'flagged in the review: row {t}, cut-out {k}')
        if t in WHOLE:
            why.append(f'row {t} is systematically confused')
        if why:
            work[f"{img[:-4]}_{b['n']}"] = dict(id=f"{img[:-4]}_{b['n']}", band=img, n=b['n'], label=lab, row=t, why='; '.join(why),
                                                  x=b['x'], y=b['y'], w=b['w'], h=b['h'])
# also the 103 uncertain boxes are NOT included (already marked)
(P / 'recheck').mkdir(exist_ok=True)
S = 3
for rid, w in work.items():
    im = Image.open(P / 'images' / w['band']).convert('RGB')
    x0 = max(0, w['x'] - 170); x1 = min(im.width, w['x'] + w['w'] + 170)
    c = im.crop((x0, 0, x1, im.height)).resize(((x1 - x0) * S, im.height * S), Image.LANCZOS)
    d = ImageDraw.Draw(c)
    d.rectangle(((w['x'] - x0) * S, w['y'] * S, (w['x'] - x0 + w['w']) * S, (w['y'] + w['h']) * S), outline=(220, 0, 0), width=3)
    c.save(P / 'recheck' / f'{rid}.png')
json.dump(work, open(P / 'recheck.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
s1 = sum(1 for w in work.values() if w['band'].startswith('S1')); print(len(work), 'boxes;', s1, 'side 1,', len(work) - s1, 'side 2')
