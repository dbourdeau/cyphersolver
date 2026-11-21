"""Apply the reviewers' decisions (decisions_s1.json, decisions_s2.json) to the T-S NS J479 CTTS project and write the
files CTTS restores a project from.

Per band, in this order: delete, merge, split, set, add. Boxes with an entry in "uncertain" get their type marked with a
leading `?` so that they sit together in CTTS's symbol-type view. Output: boxes_corrected.json, labels_corrected.json,
corrections.tsv (every operation, one line each) and, through to_ctts.py, ctts/positions + colors.txt.

  python apply_decisions_j479.py
"""
import json, subprocess, sys
from pathlib import Path

P = Path(__file__).parent / 'projects' / 'tsnsj479'
boxes = json.load(open(P / 'boxes_final.json', encoding='utf-8'))
labels = json.load(open(P / 'labels_final.json', encoding='utf-8'))
dec = {}
for f in ('decisions_s1.json', 'decisions_s2.json'):
    dec.update(json.load(open(P / f, encoding='utf-8')))
log = []
out_b, out_l = {}, {}
tot = dict(set=0, delete=0, merge=0, split=0, add=0, uncertain=0, bands_without_decisions=0)
for img, bx in boxes.items():
    d = dec.get(img)
    rows = {b['n']: dict(x=b['x'], y=b['y'], w=b['w'], h=b['h'], label=labels[img][str(b['n'])], tag='') for b in bx}
    if d is None:
        tot['bands_without_decisions'] += 1; d = {}
    for n in d.get('delete', []):
        if rows.pop(int(n), None) is not None:
            tot['delete'] += 1; log.append((img, 'delete', n, ''))
    nxt = max(rows, default=0) + 1000
    for m in d.get('merge', []):
        ns = [int(n) for n in m['ns'] if int(n) in rows]
        if len(ns) < 2:
            continue
        x0 = min(rows[n]['x'] for n in ns); y0 = min(rows[n]['y'] for n in ns)
        x1 = max(rows[n]['x'] + rows[n]['w'] for n in ns); y1 = max(rows[n]['y'] + rows[n]['h'] for n in ns)
        for n in ns: rows.pop(n)
        nxt += 1; rows[nxt] = dict(x=x0, y=y0, w=x1 - x0, h=y1 - y0, label=m['label'], tag='')
        tot['merge'] += 1; log.append((img, 'merge', ns, m['label']))
    for s in d.get('split', []):
        n = int(s['n'])
        if n not in rows: continue
        b = rows.pop(n); k = len(s['labels'])
        for j, lab in enumerate(s['labels']):
            nxt += 1; rows[nxt] = dict(x=b['x'] + b['w'] * j / k, y=b['y'], w=b['w'] / k, h=b['h'], label=lab, tag='')
        tot['split'] += 1; log.append((img, 'split', n, ' '.join(s['labels'])))
    for n, lab in d.get('set', {}).items():
        n = int(n)
        if n in rows:
            log.append((img, 'set', n, f"{rows[n]['label']} -> {lab}")); rows[n]['label'] = lab; tot['set'] += 1
    for a in d.get('add', []):
        nxt += 1; rows[nxt] = dict(x=a['x'], y=a['y'], w=a['w'], h=a['h'], label=a['label'], tag='added')
        tot['add'] += 1; log.append((img, 'add', f"{a['x']},{a['y']}", a['label']))
    unc = d.get('uncertain', {})
    for key in unc:
        if str(key).isdigit() and int(key) in rows:
            lab = rows[int(key)]['label']
            if not lab.startswith('?'): rows[int(key)]['label'] = '?' + lab
            tot['uncertain'] += 1; log.append((img, 'uncertain', key, unc[key]))
    for r in rows.values():                      # a box still carrying the alignment's '?' (unmatched) stays marked
        pass
    order = sorted(rows.values(), key=lambda r: r['x'])
    out_b[img] = [dict(line=1, x=round(r['x']), y=round(r['y']), w=max(round(r['w']), 4), h=round(r['h']), n=i + 1) for i, r in enumerate(order)]
    out_l[img] = {str(i + 1): r['label'] for i, r in enumerate(order)}
json.dump(out_b, open(P / 'boxes_corrected.json', 'w', encoding='utf-8'), indent=1)
json.dump(out_l, open(P / 'labels_corrected.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
with open(P / 'corrections.tsv', 'w', encoding='utf-8') as fh:
    fh.write('band\top\twhere\twhat\n')
    for r in log: fh.write('\t'.join(map(str, r)) + '\n')
print(tot)
subprocess.run([sys.executable, str(Path(__file__).parent / 'to_ctts.py'), str(P), str(P / 'labels_corrected.json'), '--boxes', 'boxes_corrected.json'], check=True)
