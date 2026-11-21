"""Apply the second-round decisions (recheck3_s1.json, recheck3_s2.json) on top of boxes_corrected2.json / labels_corrected2.json
of the T-S NS J479 CTTS project and write boxes_corrected3.json, labels_corrected3.json, corrections3.tsv and the CTTS files.
Ops: relabel, delete, split (equal-width cut), uncertain (type name gets a leading ?). Ids are <band>_<n> of the corrected boxes.
"""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).parent / 'projects' / 'tsnsj479'
boxes = json.load(open(P / 'boxes_corrected2.json', encoding='utf-8'))
labels = json.load(open(P / 'labels_corrected2.json', encoding='utf-8'))
dec = dict(relabel={}, delete=[], split={}, uncertain={})
for f in ('recheck3_s1.json', 'recheck3_s2.json'):
    d = json.load(open(P / f, encoding='utf-8'))
    dec['relabel'].update(d.get('relabel', {})); dec['delete'] += d.get('delete', [])
    dec['split'].update(d.get('split', {})); dec['uncertain'].update(d.get('uncertain', {}))
log = []; out_b, out_l = {}, {}; tot = dict(relabel=0, delete=0, split=0, uncertain=0)
for img, bx in boxes.items():
    rows = []
    for b in bx:
        rid = f"{img[:-4]}_{b['n']}"; lab = labels[img][str(b['n'])]
        if rid in dec['delete']:
            tot['delete'] += 1; log.append((rid, 'delete', lab)); continue
        if rid in dec['split']:
            ls = dec['split'][rid]; k = len(ls); tot['split'] += 1; log.append((rid, 'split', lab + ' -> ' + ' '.join(ls)))
            for j, l in enumerate(ls):
                rows.append(dict(x=b['x'] + b['w'] * j / k, y=b['y'], w=b['w'] / k, h=b['h'], label=l))
            continue
        if rid in dec['relabel'] and dec['relabel'][rid] != lab:
            log.append((rid, 'relabel', lab + ' -> ' + dec['relabel'][rid])); lab = dec['relabel'][rid]; tot['relabel'] += 1
        if rid in dec['uncertain'] and not lab.startswith('?'):
            log.append((rid, 'uncertain', dec['uncertain'][rid])); lab = '?' + lab; tot['uncertain'] += 1
        rows.append(dict(x=b['x'], y=b['y'], w=b['w'], h=b['h'], label=lab))
    rows.sort(key=lambda r: r['x'])
    out_b[img] = [dict(line=1, x=round(r['x']), y=round(r['y']), w=max(round(r['w']), 4), h=round(r['h']), n=i + 1) for i, r in enumerate(rows)]
    out_l[img] = {str(i + 1): r['label'] for i, r in enumerate(rows)}
json.dump(out_b, open(P / 'boxes_corrected3.json', 'w', encoding='utf-8'), indent=1)
json.dump(out_l, open(P / 'labels_corrected3.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
with open(P / 'corrections3.tsv', 'w', encoding='utf-8') as fh:
    fh.write('id\top\twhat\n')
    for r in log: fh.write('\t'.join(map(str, r)) + '\n')
print(tot)
subprocess.run([sys.executable, str(Path(__file__).parent / 'to_ctts.py'), str(P), str(P / 'labels_corrected3.json'), '--boxes', 'boxes_corrected3.json'], check=True)
