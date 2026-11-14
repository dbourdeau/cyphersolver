"""Write the part of the decoding key that the three 1759 despatches use, with its source, and count how much of
each despatch rests on the clerk's pairs (M) versus Pusch 2008 only (P).
Usage: python3 -I key_subset.py <key_decode.tsv> <key_manuscript.tsv> <out.tsv> <reconciled transcriptions...>"""
import os, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kcommon import parse
key = {}
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    f = l.rstrip('\n').split('\t'); key[int(f[0])] = (f[1], f[2])
ms = {}
for l in list(open(sys.argv[2], encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t'); ms[int(f[0])] = (f[1], f[2])
use = Counter(); per = {}
for path in sys.argv[4:]:
    name = os.path.basename(path).split('_')[0]
    c = Counter()
    for p in parse(path):
        for L in p['lines']:
            for g in L['codes']:
                if g['kind'] != 'code': c['other'] += 1; continue
                use[g['code']] += 1
                if g['code'] in ms: c['M'] += 1
                elif g['code'] in key: c['P'] += 1
                else: c['none'] += 1
    per[name] = c
with open(sys.argv[3], 'w', encoding='utf-8') as f:
    f.write('# Code values used to decode nos. 206, 207 and 215 of 1759. source M = value attested by the ministry clerk\'s\n')
    f.write('# interlinear decipherments transcribed here (key/key_manuscript.tsv, with folio and line of each pair);\n')
    f.write('# P = taken from Pusch 2008, Table 2 (Louisiana History 49: 477-480) because no pair was transcribed here.\n')
    f.write('code\tvalue\tsource\tuses_in_1759\n')
    for c in sorted(use):
        if c in ms: v, s = ms[c][0], 'M'
        elif c in key: v, s = key[c][0], 'P'
        else: v, s = '', 'none'
        f.write('%d\t%s\t%s\t%d\n' % (c, v, s, use[c]))
for k, c in per.items():
    t = c['M'] + c['P'] + c['none']
    print(k, dict(c), 'code groups', t, 'M share %.1f%%' % (100 * c['M'] / t))
print('distinct codes', len(use), 'M', sum(1 for c in use if c in ms), 'P', sum(1 for c in use if c not in ms and c in key), 'none', sum(1 for c in use if c not in key))
