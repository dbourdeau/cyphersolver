"""Test of the seventh registered prediction set (PREDICTIONS.md, Hypothesis X): where do seal texts break lines?

X1  share of line breaks on segment-boundary gaps (after the heading, before the ending) against breaks placed at
    random among each text's gaps.
X2  gaps inside bound pairs (top 30 PMI pairs with count 10+, from single-line seal texts) against other gaps of the
    multi-line texts: break rate, Fisher exact test.

Usage: python predict_test7.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test7.md.
"""
import math
import os
import random
import sys
from collections import Counter

import icit_full

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
OPEN = ('817', '820', '861')
N_PERM = 10000
random.seed(27)


def say(s=''):
    OUT.append(s)
    print(s)


def boundaries(t):
    b = set()
    if len(t) >= 3 and t[0] in OPEN and t[1] in ('2', '60', '1'):
        b.add(2)
    if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
        b.add(len(t) - 2)
    elif len(t) >= 2 and t[-1] in ('740', '520'):
        b.add(len(t) - 1)
    return b


def fisher_less(a, b, c, d):
    """One-sided p that the first row's rate a/(a+b) is this low or lower, rows (a, b) and (c, d)."""
    n1, n2, k = a + b, c + d, a + c
    tot = n1 + n2

    def h(x):
        return math.exp(math.lgamma(n1 + 1) - math.lgamma(x + 1) - math.lgamma(n1 - x + 1) + math.lgamma(n2 + 1)
                        - math.lgamma(k - x + 1) - math.lgamma(n2 - k + x + 1) - math.lgamma(tot + 1)
                        + math.lgamma(k + 1) + math.lgamma(tot - k + 1))
    return sum(h(x) for x in range(max(0, k - n2), a + 1))


def main(path):
    single, multi = [], []
    for r in icit_full.objects(path):
        if not r['type'].startswith('SEAL') or not r['flat'] or '?' in r['flat']:
            continue
        if any(ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw']):
            continue
        if len(r['seq']) == 1:
            single.append(r['flat'])
        elif len(r['seq']) >= 2:
            t, brk = [], set()
            for ln in r['seq']:
                if t:
                    brk.add(len(t))
                t.extend(ln)
            multi.append((t, brk))
    say('# Seventh registered predictions: where do seal texts break lines?')
    say()
    say('- intact seal texts: %d single-line, %d with 2+ lines (%d breaks, %d gaps).' % (
        len(single), len(multi), sum(len(b) for _, b in multi), sum(len(t) - 1 for t, _ in multi)))
    say()

    # X1
    breaks_on = sum(len(b & boundaries(t)) for t, b in multi)
    nb = sum(len(b) for _, b in multi)
    obs = breaks_on / nb
    null = []
    for _ in range(N_PERM):
        on = 0
        for t, b in multi:
            gaps = list(range(1, len(t)))
            on += len(set(random.sample(gaps, len(b))) & boundaries(t))
        null.append(on / nb)
    p1 = (sum(1 for x in null if x >= obs) + 1) / (N_PERM + 1)
    say('## X1 segment boundaries')
    say()
    say('- texts with a boundary gap: %d of %d. Breaks on a boundary: %.1f%% (%d of %d); random placement: %.1f%%; '
        'p = %.4f. **X1 %s.**' % (sum(1 for t, _ in multi if boundaries(t)), len(multi), 100 * obs, breaks_on, nb,
                                  100 * sum(null) / N_PERM, p1, 'holds' if p1 < 0.05 else 'fails'))
    pos = Counter()
    for t, b in multi:
        for g in b:
            bd = boundaries(t)
            if g in bd and g == 2 and t[0] in OPEN:
                pos['after the heading'] += 1
            elif g in bd:
                pos['before the ending'] += 1
            elif g == len(t) - 1:
                pos['before the last sign (not an ending)'] += 1
            else:
                pos['inside'] += 1
    say('- where the breaks fall: %s.' % ', '.join('%s %d' % kv for kv in pos.most_common()))
    say()

    # X2
    uni = Counter(g for t in single for g in t)
    bi = Counter((a, b) for t in single for a, b in zip(t, t[1:]))
    N1, N2 = sum(uni.values()), sum(bi.values())
    pmi = {p: math.log((c / N2) / ((uni[p[0]] / N1) * (uni[p[1]] / N1))) for p, c in bi.items() if c >= 10}
    bound = set(sorted(pmi, key=lambda p: -pmi[p])[:30])
    a = b = c = d = 0
    for t, brk in multi:
        for g in range(1, len(t)):
            inb = (t[g - 1], t[g]) in bound
            isb = g in brk
            if inb:
                a += isb
                b += not isb
            else:
                c += isb
                d += not isb
    p2 = fisher_less(a, b, c, d)
    say('## X2 bound pairs')
    say()
    say('- bound pairs (top 30 PMI, count 10+): %s.' % ', '.join('%s-%s (%d)' % (x, y, bi[(x, y)])
                                                              for x, y in sorted(bound, key=lambda p: -pmi[p])))
    say('- in multi-line texts, gaps inside a bound pair broken: %d of %d (%.1f%%); other gaps: %d of %d (%.1f%%); '
        'Fisher one-sided p = %.4f. **X2 %s.**' % (a, a + b, 100 * a / max(1, a + b), c, c + d, 100 * c / (c + d), p2,
                                                   'holds' if p2 < 0.05 and a / max(1, a + b) < c / (c + d) else 'fails'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test7.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    # line order in the fuller corpus is ambiguous (icit_full.lines_of): run with lines as listed, then reversed
    main(sys.argv[1])
    say()
    say('# Second run: lines in reversed order (as data/corpus.tsv)')
    say()
    icit_full.LINES_REVERSED = True
    random.seed(27)
    main(sys.argv[1])
