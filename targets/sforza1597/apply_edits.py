"""Apply hand edits (ctts/hand_edits.json) to the R5464 boxes: writes ctts/h_tokens.txt and ctts_proj/R5464_hand/.
Edit keys 'P1:3' (page:line, 1-based). ops: del [i..]; lab {i: 'sN'}; merge [[i,j,'sN']] (adjacent boxes);
split {i: [fraction, 'sA', 'sB']}; add [[after_i, 'sN']] (after_i -1 = line start). Indices refer to the numbered boxes in ctts/hand/*.png."""
import json, os, shutil, sys
proj = 'ctts_proj/R5464'; out = 'ctts_proj/R5464_hand'
edits = json.load(open('ctts/hand_edits.json')) if os.path.exists('ctts/hand_edits.json') else {}
def lines_of(page):
    L = []; cur = []
    for l in open(f'{proj}/positions/R5464_{page}_positions.txt'):
        if l.strip(): cur.append([float(v) for v in l.split()])
        elif cur: L.append(cur); cur = []
    if cur: L.append(cur)
    return L
def apply(boxes, e):
    B = [list(b) for b in boxes]
    for i, s in (e.get('lab') or {}).items(): B[int(i)][4] = float(int(s.lstrip('s')))
    drop = set(e.get('del') or []); ins = collections_default = {}
    new = {}
    for i, j, s in (e.get('merge') or []):
        a, b = B[i], B[j]; x0 = min(a[0], b[0]); y0 = min(a[1], b[1]); x1 = max(a[0] + a[2], b[0] + b[2]); y1 = max(a[1] + a[3], b[1] + b[3])
        new[i] = [[x0, y0, x1 - x0, y1 - y0, float(int(s.lstrip('s')))]]; drop.add(j)
    for i, (fr, sa, sb) in (e.get('split') or {}).items():
        i = int(i); x, y, w, h, c = B[i]; k = w * fr
        new[i] = [[x, y, k, h, float(int(sa.lstrip('s')))], [x + k, y, w - k, h, float(int(sb.lstrip('s')))]]
    after = {}
    for a, s in (e.get('add') or []): after.setdefault(int(a), []).append(s)
    res = []
    for s in after.get(-1, []): res.append([B[0][0] - 20, B[0][1], 18, B[0][3], float(int(s.lstrip('s')))])
    for i, b in enumerate(B):
        if i not in drop: res.extend(new.get(i, [b]))
        for s in after.get(i, []):
            x, y, w, h, c = B[i]; res.append([x + w + 1, y, max(8, 0.5 * w), h, float(int(s.lstrip('s')))])
    return res
os.makedirs(out + '/positions', exist_ok=True)
for f in ('colors.txt', 'key.txt', 'R5464_P1.png', 'R5464_P2.png'):
    if os.path.exists(f'{proj}/{f}') and not os.path.exists(f'{out}/{f}'): shutil.copy(f'{proj}/{f}', f'{out}/{f}')
toks = []; nl = 0; tot0 = 0; tot1 = 0
for page in ('P1', 'P2'):
    txt = []
    for n, L in enumerate(lines_of(page), 1):
        e = edits.get(f'{page}:{n}')
        M = apply(L, e) if e else L
        if e: nl += 1
        tot0 += len(L); tot1 += len(M)
        for b in M: txt.append(f'{b[0]:f} {b[1]:f} {b[2]:f} {b[3]:f} {int(b[4]):3d}')
        txt.append('')
        toks.append(' '.join('s%02d' % int(b[4]) for b in M))
    open(f'{out}/positions/R5464_{page}_positions.txt', 'w', newline=chr(10)).write(chr(10).join(txt) + chr(10))
open('ctts/h_tokens.txt', 'w', newline=chr(10)).write(chr(10).join(toks) + chr(10))
print('lines edited', nl, '| boxes', tot0, '->', tot1)
