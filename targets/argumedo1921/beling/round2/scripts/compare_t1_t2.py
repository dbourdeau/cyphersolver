"""Round 2: compare T1 and the blind T2 of DCXXI.4.425.2 digit for digit, run by run (no decoding).
Usage (from targets/argumedo1921/beling/round2/): python3 -I scripts/compare_t1_t2.py"""
import re
from pathlib import Path

def runs(path, col):
    out = []
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        f = line.split('\t')
        if f[0] != 'DCXXI.4.425.2' or len(f) <= col or f[2] == '0': continue
        out.append(f[col])
    return out

def norm(s):
    return re.sub(r'[^0-9\[\]|]', '', s.replace('|', ''))

t1 = runs('transcription_T1.tsv', 3); t2 = runs('transcription_T2_blind.tsv', 4)
same = 0
for i, (a, b) in enumerate(zip(t1, t2), 1):
    if norm(a) == norm(b): same += 1
    else: print(f'run {i}: T1 {a}  T2 {b}')
print(f'{same} of {len(t1)} runs agree digit for digit (T1 {len(t1)} runs, T2 {len(t2)} runs)')
