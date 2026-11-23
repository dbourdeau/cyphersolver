"""Round 6 of the T-S NS J479 CTTS project (21 Nov 2026): (a) the owner's note that the circled P cut-outs are probably f:
the six circled in the second pass and the six circled in the first pass (all look like f: a stem with a loop at top
right crossing into a lower-left loop) become `f`; (b) the 7 / dash / J sorting (recheck4_decisions.json: long `>`-shaped
strokes are 7, the small flat dash with a hook stays `-`, 5 round J hooks go to `-`, 14 boxes marked uncertain).
Reads boxes/labels_corrected5.json, writes ...6, corrections6.tsv and the CTTS files.
"""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).parent / 'projects' / 'tsnsj479'
P_TO_F = ['S2L06_11', 'S2L06_20', 'S2L07_7', 'S2L07_13', 'S2L07_15', 'S2L09_17',
          'S2L02_14', 'S2L03_1', 'S2L05_4', 'S2L05_18', 'S2L05_21', 'S2L05_25']
boxes = json.load(open(P / 'boxes_corrected5.json', encoding='utf-8'))
labels = json.load(open(P / 'labels_corrected5.json', encoding='utf-8'))
dec = json.load(open(P / 'recheck4_decisions.json', encoding='utf-8'))
log = []; out_b = {}; out_l = {}
for img, bx in boxes.items():
    nb = []; nl = {}
    for b in bx:
        rid = f"{img[:-4]}_{b['n']}"; lab = labels[img][str(b['n'])]
        if rid in dec.get('delete', []):
            log.append((rid, 'delete', lab)); continue
        new = lab
        if rid in P_TO_F:
            new = 'f'; log.append((rid, 'P->f (owner)', lab + ' -> f'))
        elif rid in dec.get('relabel', {}):
            new = dec['relabel'][rid]
            if new != lab: log.append((rid, 'relabel', lab + ' -> ' + new))
        if rid in dec.get('uncertain', {}) and not new.startswith('?'):
            log.append((rid, 'uncertain', dec['uncertain'][rid])); new = '?' + new
        nb.append(dict(b, n=len(nb) + 1)); nl[str(len(nb))] = new
    out_b[img] = nb; out_l[img] = nl
json.dump(out_b, open(P / 'boxes_corrected6.json', 'w', encoding='utf-8'), indent=1)
json.dump(out_l, open(P / 'labels_corrected6.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
with open(P / 'corrections6.tsv', 'w', encoding='utf-8') as fh:
    fh.write('id\top\twhat\n')
    for r in log: fh.write('\t'.join(r) + '\n')
print(len(log), 'changes')
subprocess.run([sys.executable, str(Path(__file__).parent / 'to_ctts.py'), str(P), str(P / 'labels_corrected6.json'), '--boxes', 'boxes_corrected6.json'], check=True)
