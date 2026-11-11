"""Write key.tsv: Code No. 10 values attested by a contemporary decoding.

Code No. 10: Jefferson's interlinear over Short's 26 Jul 1792 groups (transcription/short_17920726_full.tsv; a word that
spans several groups is credited to its first group only, the rest are marked "(word)" there and skipped).
Code No. 13 has no attested value. The Code No. 16 half of this script and of key.tsv moved to
targets/pinckney1793/ (make_key.py, key.tsv) when that code was split out on 11 Nov 2026.
"""
import csv, os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
vals = defaultdict(Counter)
where = defaultdict(set)
for r in csv.DictReader(open(os.path.join(HERE, 'transcription', 'short_17920726_full.tsv'), encoding='utf-8'), delimiter='\t'):
    w = (r.get('interlinear') or '').strip()
    if w and not w.startswith('(') and '?' not in r['group']:
        vals[('10', r['group'].strip())][w] += 1
        where[('10', r['group'].strip())].add(r['frame'])
with open(os.path.join(HERE, 'key.tsv'), 'w', encoding='utf-8', newline='') as f:
    f.write('code\tgroup\tvalue\tn\tother_readings\tsource\n')
    for (code, g) in sorted(vals, key=lambda k: (int(k[0]), int(''.join(c for c in k[1] if c.isdigit()) or 0), k[1])):
        c = vals[(code, g)]
        (top, n), rest = c.most_common(1)[0], c.most_common()[1:]
        f.write(f"{code}\t{g}\t{top}\t{sum(c.values())}\t{'; '.join(f'{w} x{k}' for w, k in rest)}\t{' '.join(sorted(where[(code, g)]))}\n")
print(sum(1 for k in vals if k[0] == '10'), 'Code No. 10 values')
