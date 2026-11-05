"""Write texts/f139_seg.txt: per text line, the cluster id of every narrow glyph group (seg/items.json), W for a wide group
(clear word or linked signs), left to right. Clear-text clusters are written lower-case 'x<id>'.
usage: python seqs.py"""
import json
d = json.load(open('seg/groups.json')); L = d['lines']; items = json.load(open('seg/items.json'))
CLEAR = {21, 6, 49, 30, 38, 45, 61, 84, 68, 17, 73, 27, 3, 40, 43, 16, 37}
by = {(i['line'], tuple(i['box'])): i['c'] for i in items}
out = []
for n, gs in d['groups'].items():
    n = int(n); c = L[n - 1]; toks = []
    for x0, y0, x1, y1, ink in gs:
        cy = (y0 + y1) / 2
        if not (c - 22 <= cy <= c + 14): continue
        k = by.get((n, (x0, y0, x1, y1)))
        if k is None:
            if x1 - x0 > 62: toks.append('W')
            continue
        toks.append(f'x{k}' if k in CLEAR else f'c{k}')
    out.append(f'L{n} ' + ' '.join(toks))
open('texts/f139_seg.txt', 'w').write('\n'.join(out) + '\n')
print('\n'.join(out[:6]))
