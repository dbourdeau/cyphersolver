"""How much of the corpus fits the established templates (descriptive, not a test).

Each intact line of the fuller corpus is parsed as a count token (numeral + 700), count + other signs, name + ending,
name + closing formula (705 / 706 + 33 + 520), numbers only, or no template; each sign token gets the role it has
there (number, measure sign after a number, ending, clitic after an ending, heading, formula sign, human figure, other).

Usage: python readable.py path/to/icit_full_records_indusscript_net.csv
Writes results/readable.md.
"""
import os
import sys
from collections import Counter

import icit_full
from numerals import NUMS
from predict_test4 import name_of
from predict_test14 import cat_of

HERE = os.path.dirname(os.path.abspath(__file__))
OPEN = ('817', '820', '861')
POST = ('90', '400', '151')
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def parse(t):
    if len(t) == 2 and t[0] in NUMS and t[1] == '700':
        return 'count token'
    if any(x in NUMS and y == '700' for x, y in zip(t, t[1:])):
        return 'count + other signs'
    nm = name_of(t)
    if nm:
        b = nm[0]
        if nm[1] == '520' and len(b) >= 2 and b[-1] == '33' and b[-2] in ('705', '706'):
            return 'name + closing formula'
        return 'name + ending'
    if all(g in NUMS for g in t):
        return 'numbers only'
    return 'no template'


def role(ln, i, cat):
    g = ln[i]
    if g in NUMS:
        return 'number (value known)'
    if g == '700' and i > 0 and ln[i - 1] in NUMS:
        return 'measure sign after a number'
    if g in ('740', '520'):
        return 'ending (class known)'
    if g in POST and i > 0 and ln[i - 1] in ('740', '520'):
        return 'clitic after an ending'
    if i == 0 and g in OPEN:
        return 'heading'
    if g in ('705', '706', '33'):
        return 'formula sign'
    if cat.get(g) == 'A':
        return 'human figure (picture known)'
    return 'other sign (meaning unknown)'


def main(path):
    cat = cat_of()
    intact = [r for r in icit_full.objects(path) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    kinds, bytype, tok = Counter(), Counter(), Counter()
    for r in intact:
        k = r['type'].split(':')[0]
        for ln in r['seq']:
            p = parse(ln)
            kinds[p] += 1
            bytype[(k, p)] += 1
            for i in range(len(ln)):
                tok[role(ln, i, cat)] += 1
    n, T = sum(kinds.values()), sum(tok.values())
    say('# How much of the corpus fits the templates (descriptive)')
    say()
    say('| line template | lines | share |')
    say('|---|---|---|')
    for k, v in kinds.most_common():
        say('| %s | %d | %.1f%% |' % (k, v, 100 * v / n))
    say()
    say('| sign role | tokens | share |')
    say('|---|---|---|')
    for k, v in tok.most_common():
        say('| %s | %d | %.1f%% |' % (k, v, 100 * v / T))
    say()
    for k in ('SEAL', 'TAB', 'TAG', 'POT'):
        tot = sum(v for (kk, _), v in bytype.items() if kk == k)
        say('- %s (%d lines): %s.' % (k, tot, ', '.join('%s %.0f%%' % (p, 100 * v / tot) for (kk, p), v in
                                                      sorted(bytype.items(), key=lambda x: -x[1]) if kk == k)))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'readable.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
