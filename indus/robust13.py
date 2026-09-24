"""Post-test robustness checks on the thirteenth set's held results (not registered; reported as checks).

Usage: python robust13.py path/to/icit_full_records_indusscript_net.csv
Writes results/robust13.md.
"""
import sys, os, random
from collections import Counter
import predict_test13 as T
import icit_full
from gulf import IRAN_WEST, WEST
from numerals import NUMS
T.N = 2000
OUT = []
def say(s=''):
    OUT.append(s); print(s)

path = sys.argv[1]
A, B = T.sample('A'), T.sample('B')
recs = {rec[0]: rec for rec in icit_full.records(path)}
rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
west = {r['sealid'] for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST}
home = [r for r in rows if r['sealid'] not in west and recs[r['sealid']][2] not in ('Other',)]
say('# Robustness checks on the thirteenth set (after the test, not registered)')
say()
# H3 without the fish family
fam = dict(T.FAMILIES); fam.pop('fish')
T.FAMILIES = fam
for lab, L in (('A', A), ('B', B)):
    r = T.h3(L)
    say('- H3 without fish: %s: %s' % (lab, 'no pairs' if r is None else '%d pairs, cosine %.3f, p = %.4f' % (r[2], r[0], r[1])))
# H7 excluding names whose first sign is a numeral
orig_names = T.names
T.names = lambda lines: [(b, e) for b, e in orig_names(lines) if b[0] not in NUMS]
for lab, L in (('A', A), ('B', B)):
    b, c, both, nei, p = T.h7(L)
    say('- H7 first sign not a numeral: %s: %d vs %d, p = %.4f' % (lab, b, c, p))
# H10 excluding numerals anywhere in first/last position
for lab, L in (('A', A), ('B', B)):
    o, p, n, hf, hl = T.h10(L)
    say('- H10 first sign not a numeral: %s: %d names, %.2f vs %.2f bits, p = %.4f' % (lab, n, hf, hl, p))
T.names = orig_names
# H8: seals only, distinct (name, site), numerals and grammar signs out of both positions
seals = [r for r in home if r['type'].startswith('SEAL')]
def h8_variant(rs, dedupe):
    seen = set(); keep = []
    for r in rs:
        for ln in r['seq']:
            x = T.name_of(ln)
            if x and len(x[0]) >= 2:
                key = (x, r['site'].strip())
                if dedupe and key in seen: continue
                seen.add(key); keep.append(r)
                break
    return keep
for lab, rs, dd in (('seals only', seals, False), ('distinct name-site, all objects', home, True),
                    ('seals only, distinct name-site', seals, True)):
    o, p, n, mf, ml = T.h8(h8_variant(rs, dd))
    say('- H8 %s: %d names, MI first %.3f, last %.3f, difference %+.3f, p = %.4f' % (lab, n, mf, ml, o, p))
os.makedirs(os.path.join(T.HERE, 'results'), exist_ok=True)
open(os.path.join(T.HERE, 'results', 'robust13.md'), 'w', encoding='utf-8').write('\n'.join(OUT) + '\n')
