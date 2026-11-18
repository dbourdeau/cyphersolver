"""Collate the two cipher witnesses of Carleton, 25 Sep 1782 (post-test material, 14 Nov 2026).

    python targets/carleton1782/followup_2026-11-14/duplicate_fo125/collate.py

Witness A: B.148 pp. 123-125 = BL fo. 124 (../../carleton_1782-09-25/transcription.txt, the post-test text of the frozen
transcript). Witness B: B.148 pp. 126-128 = BL fo. 125 (transcription_fo125.txt, read 14 Nov 2026). Both are reduced to a
stream of tokens (number pairs and clear words, struck figures and copyist notes dropped) and aligned with difflib.
Every difference is printed and written to collation.tsv. The frozen files are only read.
"""
import difflib, re, sys
from pathlib import Path

H = Path(__file__).resolve().parent
T = H.parents[1]

def tokens(path):
    out = []
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('#') or '\t' not in line:
            continue
        loc, body = line.split('\t', 1)
        body = re.sub(r'\{[^}]*\}', ' ', body)            # struck figures, blanks, copyist notes
        body = re.sub(r'\[The L\'Aigle[^\]]*\]', ' [NAVALNEWS] ', body)
        for m in re.finditer(r'x\(|\)|\[[^\]]*\]|\d+-\d+', body):
            t = m.group(0)
            if t in ('x(', ')'):
                continue
            out.append((t.strip('[]').lower() if t.startswith('[') else t, loc.split('→')[0]))
    return out

A = tokens(T / 'carleton_1782-09-25/transcription.txt')
B = tokens(H / 'transcription_fo125.txt')
a, b = [t for t, _ in A], [t for t, _ in B]
# the main witness's naval-news line carries the signature and dateline differently; compare from the first pair on
sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
rows, same = [], 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal':
        same += i2 - i1
        continue
    rows.append((op, ' '.join(a[i1:i2]), A[i1][1] if i1 < len(A) else '', ' '.join(b[j1:j2]), B[j1][1] if j1 < len(B) else '',
                 ' '.join(a[max(0, i1 - 3):i1])))
print(f'witness A (fo. 124, pp. 123-125): {len(a)} tokens; witness B (fo. 125, pp. 126-128): {len(b)} tokens; {same} aligned equal')
with (H / 'collation.tsv').open('w', encoding='utf-8') as f:
    f.write('op\tfo124_pp123-125\tloc_A\tfo125_pp126-128\tloc_B\tpreceded_by\n')
    for r in rows:
        f.write('\t'.join(r) + '\n')
        print('\t'.join(r))
