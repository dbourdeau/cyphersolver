"""Post-test checks on the seventeenth set (not registered).

Usage: python robust17.py path/to/icit_full_records_indusscript_net.csv
Writes results/robust17.md.
"""
import os, sys
from collections import Counter
import icit_full
from numerals import NUMS
from predict_test7 import fisher_less
from predict_test14 import hyper_ge
OUT = []
def say(s=''):
    OUT.append(s); print(s)
path = sys.argv[1]
intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
    ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
kind = lambda r: r['type'].split(':')[0]
say('# Checks on the seventeenth set (after the test, not registered)')
say()
for k in ('TAB', 'SEAL'):
    c = Counter(y for r in intact if kind(r) == k for ln in r['seq'] for x, y in zip(ln, ln[1:]) if x in NUMS and y not in NUMS)
    tot = sum(c.values())
    say('- U3 %s: sign after a numeral (%d tokens): %s.' % (k, tot, ', '.join('%s %.0f%%' % (g, 100 * n / tot) for g, n in c.most_common(8))))
    d = Counter((x, y) for r in intact if kind(r) == k for ln in r['seq'] for x, y in zip(ln, ln[1:]) if x in NUMS and y == '700')
    say('  numerals before 700 on %s: %s.' % (k, ', '.join('%s x%d' % (x, n) for (x, _), n in d.most_common(8))))
# U5 with distinct texts
seen = set(); a = na = c = nc = 0
for r in intact:
    k = kind(r)
    if k not in ('SEAL', 'TAB', 'TAG', 'POT'): continue
    key = (k != 'SEAL', tuple(r['flat']))
    if key in seen: continue
    seen.add(key)
    for ln in r['seq']:
        for x, y in zip(ln, ln[1:]):
            if x in ('740', '520') and y in ('90', '400', '151'):
                if k != 'SEAL':
                    a += y == '400'; na += 1
                else:
                    c += y == '400'; nc += 1
say('- U5 distinct texts: 400 among post-ending signs off seals %d of %d, seals %d of %d; p = %.4f.' % (
    a, na, c, nc, hyper_ge(a, na - a, c, nc - c)))
sites = Counter((r['site'].strip(), r['type']) for r in intact if r['type'] in ('SEAL:C', 'SEAL:CY'))
say('- U24 cylinder seals by site: %s.' % ', '.join('%s %s %d' % (s, t, n) for (s, t), n in sites.most_common()))
home_cyl = [r for r in intact if r['type'] in ('SEAL:C', 'SEAL:CY') and r['site'].strip() in ('Mohenjo-daro', 'Harappa', 'Kalibangan', 'Lothal', 'Dholavira', 'Chanhu-daro')]
say('  cylinder seals at Indus sites: %d; lines without an ending: %s.' % (len(home_cyl), sum(1 for r in home_cyl for ln in r['seq'] if len(ln) >= 2 and not __import__('predict_test4').name_of(ln))))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results', 'robust17.md'), 'w', encoding='utf-8').write('\n'.join(OUT) + '\n')
