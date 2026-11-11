"""Write key.tsv: Code No. 16 values attested by a contemporary decoding in Pinckney's London letters.

Code No. 16: George Taylor's interlinear decodings and the 25 Nov 1793 Explication aligned by hand, on NARA M30 roll 2
(transcription/pinckney_m30.tsv), frame 0140 itself excluded. This is the Code No. 16 half of
targets/legation1788/make_key.py, moved here when the code was split out on 11 Nov 2026; the Code No. 10 half stayed there.
Andrew Beling's larger key is beling/key/code16_key_v4.tsv.
"""
import csv, os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
vals = defaultdict(Counter)
where = defaultdict(set)
for r in csv.DictReader(open(os.path.join(HERE, 'transcription', 'pinckney_m30.tsv'), encoding='utf-8'), delimiter='\t'):
    if r['frame'] == '0140':
        continue
    w = (r.get('interlinear_word') or '').strip()
    src = 'T'
    if not w and 'aligned:' in (r.get('note') or ''):
        w, src = r['note'].split('aligned:')[1].strip(), 'A'
    g = r['group'].strip()
    if w and not w.startswith('(') and '?' not in g:
        vals[('16', g)][w.lower()] += 1
        where[('16', g)].add('M30-002-' + r['frame'] + ('' if src == 'T' else ' (explication)'))
with open(os.path.join(HERE, 'key.tsv'), 'w', encoding='utf-8', newline='') as f:
    f.write('code\tgroup\tvalue\tn\tother_readings\tsource\n')
    for (code, g) in sorted(vals, key=lambda k: (int(k[0]), int(''.join(c for c in k[1] if c.isdigit()) or 0), k[1])):
        c = vals[(code, g)]
        (top, n), rest = c.most_common(1)[0], c.most_common()[1:]
        f.write(f"{code}\t{g}\t{top}\t{sum(c.values())}\t{'; '.join(f'{w} x{k}' for w, k in rest)}\t{' '.join(sorted(where[(code, g)]))}\n")
print(sum(1 for k in vals if k[0] == '16'), 'Code No. 16 values')
