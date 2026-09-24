"""Test of the third prediction set in PREDICTIONS.md (R1, R2; registered and committed before this script).
Held-out texts only: the M77 additions and the fuller corpus's texts not in the ICIT-derived dump.

Usage: python predict_test3.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test3.md.
"""
import math
import os
import sys
from collections import Counter

import icit_full
from numerals import NUMS
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
OPEN = ('817', '820', '861')
ENDS = ('740', '520')


def say(s=''):
    OUT.append(s)
    print(s)


def fisher_right(a, b, c, d):
    n1, n2, k = a + b, c + d, a + c
    tot = n1 + n2

    def lc(n, r):
        return math.lgamma(n + 1) - math.lgamma(r + 1) - math.lgamma(n - r + 1)
    return min(1.0, sum(math.exp(lc(n1, x) + lc(n2, k - x) - lc(tot, k)) for x in range(a, min(n1, k) + 1)))


def main(path):
    have = {tuple(tuple(ln) for ln in r['seq']) for r in load()}
    held_rows = [r for r in load(only_m77=True) if r['flat']]
    held_rows += [r for r in icit_full.objects(path, intact_only=True)
                  if r['seq'] and tuple(tuple(ln) for ln in r['seq']) not in have]
    lines = [[g for g in ln if g != '?'] for r in held_rows for ln in r['seq']]
    lines = [t for t in lines if len(t) >= 2]
    say('# Third prediction set (R1, R2): results on held-out texts (%d lines)' % len(lines))
    say()
    last = foll = tot = 0
    for t in lines:
        s = t
        if len(s) >= 3 and s[0] in OPEN and s[1] in ('2', '60', '1'):
            s = s[2:]
        if len(s) >= 3 and s[-1] in ('400', '90', '151') and s[-2] in ENDS:
            s = s[:-2]
        elif s and s[-1] in ENDS:
            s = s[:-1]
        else:
            continue
        for i, g in enumerate(s):
            if g in NUMS and g not in ('2', '32'):
                tot += 1
                if i == len(s) - 1:
                    last += 1
                elif s[i + 1] not in NUMS:
                    foll += 1
    r1 = tot and last / tot < 0.10 and foll / tot >= 0.90
    say('## R1 Numerals inside names')
    say()
    say('- stroke numerals inside names (pairs left out): %d; standing last, right before the ending: %d (%.1f%%); '
        'followed by a non-numeral sign: %d (%.1f%%). **R1 %s.**' % (
            tot, last, 100 * last / max(tot, 1), foll, 100 * foll / max(tot, 1), 'holds' if r1 else 'fails'))
    say()

    def closed(t):
        return t[-1] in ENDS or (t[-1] in ('90', '400', '151') and len(t) >= 2 and t[-2] in ENDS) or t[-1] == '90'
    internal = [t for t in lines if any(g == '740' for g in t[:-1]) and not (len(t) >= 2 and t[-2] == '740' and t[-1] in ('400', '90', '151') and '740' not in t[:-2])]
    internal = [t for t in internal if '740' in t[:-2] or (t[-1] != '740' and '740' in t[:-1] and t[t.index('740') + 1:t.index('740') + 2] not in (['400'], ['90'], ['151']))]
    lens = Counter(len(t) for t in internal)
    pool = [t for t in lines if '740' not in t[:-2] and not ('740' in t[:-1] and t[-1] not in ('400', '90', '151'))]
    by_len = {}
    for t in pool:
        by_len.setdefault(len(t), []).append(t)
    ctrl = []
    for L, k in lens.items():
        ctrl += by_len.get(L, [])
    a = sum(1 for t in internal if closed(t))
    c = sum(1 for t in ctrl if closed(t))
    p = fisher_right(a, len(internal) - a, c, len(ctrl) - c)
    r2 = bool(internal) and a / len(internal) > c / max(len(ctrl), 1) and p < 0.05
    say('## R2 Stacked possessives')
    say()
    say('- texts with an internal 740 (not the final ending slot): %d; closing with an ending or the man sign: %d '
        '(%.0f%%). Texts of the same lengths without one: %d; closing so: %d (%.0f%%). Fisher p = %.3g. **R2 %s.**' % (
            len(internal), a, 100 * a / max(len(internal), 1), len(ctrl), c, 100 * c / max(len(ctrl), 1), p,
            'holds' if r2 else 'fails'))
    say('- examples: %s.' % '; '.join(' '.join(t) for t in internal[:10]))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test3.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
