"""Settle the alphabet-row boxes by their slot position (21 Nov 2026; alpha_decisions.json from a reviewer who matched every uncertain box
of the 13 alphabet bands to its slot in the Hebrew order and checked that the drawn shape can be that sign). Reads boxes/labels_corrected9,
writes ...10, alpha_applied.tsv and the CTTS files. Settled and relabelled boxes lose their ?; deleted boxes (fragments) go; kept boxes stay
uncertain. Certain here means: the slot fixes the letter and the shape does not contradict it."""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).parent / 'projects' / 'tsnsj479'
B = json.load(open(P / 'boxes_corrected9.json', encoding='utf-8')); L = json.load(open(P / 'labels_corrected9.json', encoding='utf-8'))
D = json.load(open(P / 'alpha_decisions.json', encoding='utf-8'))
settle = set(D.get('settle', [])); relabel = D.get('relabel', {}); delete = set(D.get('delete', []))
log = []; out_b = {}; out_l = {}
for img, bx in B.items():
    nb = []; nl = {}
    for b in bx:
        rid = f"{img[:-4]}_{b['n']}"; lab = L[img][str(b['n'])]
        if rid in delete:
            log.append((rid, 'delete', lab)); continue
        new = lab
        if rid in relabel: new = relabel[rid].lstrip('?'); log.append((rid, 'relabel', lab + ' -> ' + new))
        elif rid in settle and lab.startswith('?'): new = lab[1:]; log.append((rid, 'settle', lab + ' -> ' + new))
        nb.append(dict(b, n=len(nb) + 1)); nl[str(len(nb))] = new
    out_b[img] = nb; out_l[img] = nl
json.dump(out_b, open(P / 'boxes_corrected10.json', 'w', encoding='utf-8'), indent=1)
json.dump(out_l, open(P / 'labels_corrected10.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
with open(P / 'alpha_applied.tsv', 'w', encoding='utf-8') as fh:
    fh.write('id\top\twhat\n'); [fh.write('\t'.join(r) + '\n') for r in log]
print(len(log), 'changes')
subprocess.run([sys.executable, str(Path(__file__).parent / 'to_ctts.py'), str(P), str(P / 'labels_corrected10.json'), '--boxes', 'boxes_corrected10.json'], check=True)
