"""Apply the owner's marks on the printed sign table (21 Nov 2026) to the T-S NS J479 CTTS project.

The owner went through the table with red circles (a cut-out is wrong), check marks (the row is right), a long circle with
an arrow over the right-hand half of row J (those boxes belong in row `-`), question marks beside h, m, n, o and "d" beside
o. The cut-outs were mapped to box ids from table_drawn.json (key_table_j479.py records which box each cut-out is). Reads
boxes_corrected3.json / labels_corrected3.json, writes boxes_corrected4.json / labels_corrected4.json, marks_applied.tsv
and the CTTS files. Circled boxes become uncertain (type name gets a leading ?), so they leave the table.
"""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).parent / 'projects' / 'tsnsj479'
MARKS = dict(
    relabel={'S1V01_5': '-', 'S2L05_13': '-', 'S2L06_9': '-', 'S2L09_8': '-', 'S2L17_1': '-',   # long circle over the right half of J
             'S2L22_9': 'd'},                                                                      # "? d" beside the o row; the alphabet row S2L22 puts t-et here
    circled=['S1L08_7', 'S2L04_1', 'S1L10_1', 'S1L12_27', 'S2L13_7', 'S2L13_1', 'S2L13_5', 'S2V01_20', 'S2V02_14',
             'S1L04_11', 'S1L10_22', 'S1L10_13', 'S1L06_2', 'S2V01_11', 'S2V02_9', 'S2L19_7', 'S1L13_15', 'S1L14_26',
             'S1L05_8', 'S1L14_3', 'S1L14_5', 'S1L14_23', 'S2L07_4', 'S2V02_11', 'S1L15_2', 'S2U02_4', 'S2V02_2',
             'S2L02_14', 'S2L03_1', 'S2L05_4', 'S2L05_18', 'S2L05_21', 'S2L05_25'],
    questioned=['S1L03_7', 'S2V01_22', 'S2V02_3', 'S1L06_1', 'S2V01_8', 'S1L10_4', 'S1L11_18', 'S2U02_23', 'S2U03_9'],  # rows h, m, n
    checked_rows=['I', 'U', 'p', 'q', 'O', '6', 'S', 'X'])
boxes = json.load(open(P / 'boxes_corrected3.json', encoding='utf-8'))
labels = json.load(open(P / 'labels_corrected3.json', encoding='utf-8'))
out_l = {}; log = []
unc = set(MARKS['circled']) | set(MARKS['questioned'])
for img, bx in boxes.items():
    d = {}
    for b in bx:
        rid = f"{img[:-4]}_{b['n']}"; lab = labels[img][str(b['n'])]
        if rid in MARKS['relabel']:
            log.append((rid, 'relabel', lab + ' -> ' + MARKS['relabel'][rid])); lab = MARKS['relabel'][rid]
        elif rid in unc and not lab.startswith('?'):
            log.append((rid, 'circled' if rid in MARKS['circled'] else 'questioned', 'marked uncertain, was ' + lab)); lab = '?' + lab
        d[str(b['n'])] = lab
    out_l[img] = d
json.dump(boxes, open(P / 'boxes_corrected4.json', 'w', encoding='utf-8'), indent=1)
json.dump(out_l, open(P / 'labels_corrected4.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
with open(P / 'marks_applied.tsv', 'w', encoding='utf-8') as fh:
    fh.write('id\top\twhat\n')
    for r in log: fh.write('\t'.join(r) + '\n')
print(len(log), 'changes;', 'checked rows:', ' '.join(MARKS['checked_rows']))
subprocess.run([sys.executable, str(Path(__file__).parent / 'to_ctts.py'), str(P), str(P / 'labels_corrected4.json'), '--boxes', 'boxes_corrected4.json'], check=True)
