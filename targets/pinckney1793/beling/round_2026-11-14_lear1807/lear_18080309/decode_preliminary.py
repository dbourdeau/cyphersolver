"""Decode the 9 Mar 1808 passage (reconciled.txt) with key v5 as it stands; groups read differently by the two readers
(a/b) or with a doubtful digit (?) get no value. Run from this folder: python decode_preliminary.py  (writes decode_v5_preliminary.txt)"""
import csv, re
from pathlib import Path
H = Path(__file__).resolve().parent
key = {r['group']: r['value'] for r in csv.DictReader(open(H.parents[1] / 'round_2026-11-11' / 'code16_key_v5.tsv', encoding='utf-8'), delimiter='\t')}
out, n, k = [], 0, 0
for line in open(H / 'reconciled.txt', encoding='utf-8'):
    if not re.match(r'^L\d+ ', line): continue
    lab, rest = line.split(' ', 1)
    toks = []
    for t in rest.split():
        if t in ('(', ')', '--'): continue
        n += 1
        if re.fullmatch(r'\d+', t) and t in key: toks.append(f'{t}={key[t]}'); k += 1
        else: toks.append(f'{t}=?')
    out.append(f'{lab} ' + ' '.join(toks))
head = (f'# Lear to Madison, 9 Mar 1808 (M23 roll 10 frame 0014), PRELIMINARY decode with key v5 unaltered: {n} groups, {k} with a value '
        f'({k / n:.3f}).\n# group=value from the key; group=? no value (unknown, doubtful digit or the readers differ). Not a reading.\n')
(H / 'decode_v5_preliminary.txt').write_text(head + '\n'.join(out) + '\n', encoding='utf-8', newline='\n')
print(head)
