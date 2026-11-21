"""Second round of the owner's marks on the printed sign table (21 Nov 2026, table of 528 boxes in 34 rows).

Ticks (rows confirmed): I U E A 4 c B Bc d < p q 6 S X 9 C 7 5 b e f y z (one tick sits between rows E and A and one
between N and 4: taken for E and A, and for 4). Red circles: 13 cut-outs in rows N (1), J (1), P (6), O (1), 8 (1), a (3).
Not marked: -, <5, w, 2. Reads boxes_corrected4/labels_corrected4, writes ...5, marks2_applied.tsv and the CTTS files.
Circled boxes become uncertain (leading ?), so they leave the table.
"""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).parent / 'projects' / 'tsnsj479'
CIRCLED = ['S2L15_6', 'S2L17_4', 'S1L05_1', 'S2L17_25', 'S1L08_6', 'S1L14_24', 'S2L01_3',
           'S2L06_11', 'S2L06_20', 'S2L07_7', 'S2L07_13', 'S2L07_15', 'S2L09_17']
CHECKED = 'I U E A 4 c B Bc d < p q 6 S X 9 C 7 5 b e f y z'.split()
boxes = json.load(open(P / 'boxes_corrected4.json', encoding='utf-8'))
labels = json.load(open(P / 'labels_corrected4.json', encoding='utf-8'))
out = {}; log = []
for img, bx in boxes.items():
    d = {}
    for b in bx:
        rid = f"{img[:-4]}_{b['n']}"; lab = labels[img][str(b['n'])]
        if rid in CIRCLED and not lab.startswith('?'):
            log.append((rid, 'circled', 'marked uncertain, was ' + lab)); lab = '?' + lab
        d[str(b['n'])] = lab
    out[img] = d
json.dump(boxes, open(P / 'boxes_corrected5.json', 'w', encoding='utf-8'), indent=1)
json.dump(out, open(P / 'labels_corrected5.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
with open(P / 'marks2_applied.tsv', 'w', encoding='utf-8') as fh:
    fh.write('id\top\twhat\n')
    for r in log: fh.write('\t'.join(r) + '\n')
print(len(log), 'circled boxes made uncertain; rows ticked:', ' '.join(CHECKED))
subprocess.run([sys.executable, str(Path(__file__).parent / 'to_ctts.py'), str(P), str(P / 'labels_corrected5.json'), '--boxes', 'boxes_corrected5.json'], check=True)
