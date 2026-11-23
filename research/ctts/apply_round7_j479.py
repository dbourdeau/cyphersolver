"""Round 7 (21 Nov 2026): the owner noted that the last three cut-outs of row `a` do not fit. They are S2L06_5 (a long wavy
stroke with a small loop: marked uncertain, perhaps w), S2L06_21 (a narrow strip over the stem of a P, overlapping 22:
deleted) and S2L06_22 (one box over a P and an a: split into P and a). Reads ...6, writes ...7 and the CTTS files.
"""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).parent / 'projects' / 'tsnsj479'
boxes = json.load(open(P / 'boxes_corrected6.json', encoding='utf-8')); labels = json.load(open(P / 'labels_corrected6.json', encoding='utf-8'))
img = 'S2L06.png'; rows = []
for b in boxes[img]:
    lab = labels[img][str(b['n'])]; rid = f"S2L06_{b['n']}"
    if rid == 'S2L06_21': continue
    if rid == 'S2L06_22':
        for j, l in enumerate(['P', 'a']):
            rows.append(dict(line=1, x=round(b['x'] + b['w'] * j / 2), y=b['y'], w=round(b['w'] / 2), h=b['h'], label=l))
        continue
    if rid == 'S2L06_5': lab = '?' + lab.lstrip('?')
    rows.append(dict(line=1, x=b['x'], y=b['y'], w=b['w'], h=b['h'], label=lab))
rows.sort(key=lambda r: r['x'])
nb = [{k: v for k, v in r.items() if k != 'label'} | {'n': i + 1} for i, r in enumerate(rows)]
boxes[img] = nb; labels[img] = {str(i + 1): r['label'] for i, r in enumerate(rows)}
json.dump(boxes, open(P / 'boxes_corrected7.json', 'w', encoding='utf-8'), indent=1)
json.dump(labels, open(P / 'labels_corrected7.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
subprocess.run([sys.executable, str(Path(__file__).parent / 'to_ctts.py'), str(P), str(P / 'labels_corrected7.json'), '--boxes', 'boxes_corrected7.json'], check=True)
