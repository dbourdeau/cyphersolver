"""Descriptive companion to predict_test18 (not a test): the N700 tablet formula and the signs before 33-520.

Usage: python describe18.py path/to/icit_full_records_indusscript_net.csv
Writes results/describe18.md.
"""
import os, sys
from collections import Counter
import icit_full
import predict_test13 as T
from numerals import NUMS
from predict_test18 import n700
OUT = []
def say(s=''):
    OUT.append(s); print(s)
path = sys.argv[1]
intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
    ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
tabs = [r for r in intact if r['type'].startswith('TAB') and n700(r)]
say('# The N700 tablet formula and the signs before 33-520 (descriptive)')
say()
say('- N700 tablets: %d; types %s; sites %s.' % (len(tabs), dict(Counter(r['type'] for r in tabs)), dict(Counter(r['site'] for r in tabs).most_common(5))))
say('- commonest full texts (reading order, lines joined): %s.' % '; '.join('%s x%d' % (' '.join(t), n) for t, n in Counter(tuple(r['flat']) for r in tabs).most_common(15)))
shape = Counter(tuple('N' if g in NUMS else ('U' if g == '700' else 'X') for g in r['flat']) for r in tabs)
say('- text shapes (N numeral, U 700, X other): %s.' % '; '.join('%s x%d' % (''.join(s), n) for s, n in shape.most_common(8)))
other = Counter(g for r in tabs for g in r['flat'] if g not in NUMS and g != '700')
say('- other signs on N700 tablets: %s.' % ', '.join('%s x%d' % kv for kv in other.most_common(12)))
b = Counter(t[i - 2] for t in T.sample('A') + T.sample('B') for i, g in enumerate(t) if g == '520' and i >= 2 and t[i - 1] == '33')
say('- signs before 33-520 (A + B): %s.' % ', '.join('%s x%d' % kv for kv in b.most_common(10)))
open(os.path.join(T.HERE, 'results', 'describe18.md'), 'w', encoding='utf-8').write('\n'.join(OUT) + '\n')
