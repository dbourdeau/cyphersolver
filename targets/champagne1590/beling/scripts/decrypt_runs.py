"""Mechanical decryption of the no. 24/60 runs with key no. 25 (letters from key/key25.md, barred names from the sheet)."""
import csv, sys
sys.path.insert(0, 'scripts')
from key25 import load
key = load('key/key25.md')
names = {r[0]: r[1] for r in csv.reader((l for l in open('transcription/key25_noms_propres.tsv') if not l.startswith('#')), delimiter='\t') if r[0] != 'figure'}
NULLS = set('11 12 13 14 15 16 17 18 19 01 02 03 04 05 06 07 08 09 39 49 59 69 79 89 99'.split())
for r in csv.reader((l for l in open('transcription/n24_n60_runs.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] == 'doc': continue
    out = []
    for f in r[3].split():
        if f.endswith('b'): out.append('[' + names.get(f[:-1], f'barred {f[:-1]}?') + ']')
        elif f in key: out.append(key[f])
        elif f in NULLS: out.append('·')
        else: out.append(f'[{f}?]')
    print(f'no. {r[0]} l. {r[1]}\t{r[2]} …\t' + ''.join(out))
