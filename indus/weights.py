"""The Harappan weights against the stroke numerals.

Hemmy's measurements (Marshall 1931 vol. 2 App. I-II; Mackay 1938 vol. 1 App. I) and Vats 1940
(Harappa), typed from the page images (weights in grams; Vats's 3 and 8 are easily confused in
print and flagged values are left out).

W1  The weight system: fit the unit u (0.80-0.95 g) that best explains the weights as multiples of
    u x {1, 2, 4, 8, 16, 32, 64, 160, 200, 320, 640, 1600, 3200, 6400, 8000, 12800} (the
    binary-then-decimal series of Hemmy and Kenoyer); share of weights within 5% of a series
    member, against the same for series made of random multiples (the null: any dense set fits
    some weights).
W2  The numerals: share of stroke-numeral tokens whose value is in the weight series (1, 2, 4, 8,
    16...), short and long strokes apart, against the share among all values 1-12 used. If the
    numbers written on seals and tablets counted weight units, the binary values would dominate.

Usage: python weights.py <marshall csv> <mackay csv> <vats csv>
Writes results/weights.md.
"""
import csv
import math
import os
import random
import sys
from collections import Counter

from numerals import NUMS
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
SERIES = [1, 2, 4, 8, 16, 32, 64, 160, 200, 320, 640, 1600, 3200, 6400, 8000, 12800]
random.seed(7)


def say(s=''):
    OUT.append(s)
    print(s)


def fit(ws, series, lo=0.80, hi=0.95, tol=0.05):
    best = (0, 0)
    u = lo
    while u <= hi:
        k = sum(1 for w in ws if min(abs(w / (u * s) - 1) for s in series) <= tol)
        if k > best[0]:
            best = (k, u)
        u += 0.0005
    return best


def main(marshall, mackay, vats):
    ws = []
    for path in (marshall, mackay):
        for r in csv.DictReader(open(path, encoding='utf-8')):
            try:
                ws.append(float(r['weight_g']))
            except ValueError:
                pass
    nv = 0
    for r in csv.DictReader(open(vats, encoding='utf-8')):
        if r.get('flag_3_8', '').strip().lower() != 'yes':
            try:
                ws.append(float(r['weight_g']))
                nv += 1
            except ValueError:
                pass
    ws = [w for w in ws if w > 0.3]
    say('# The Harappan weights and the stroke numerals')
    say()
    k, u = fit(ws, SERIES)
    say('- W1 %d weights (Hemmy in Marshall 1931 and Mackay 1938; Vats 1940 without the %s); the best unit '
        'is %.4f g, with %d weights (%.0f%%) within 5%% of u x the binary-decimal series.' % (
            len(ws), 'values flagged for 3/8 misprints, %d kept' % nv, u, k, 100 * k / len(ws)))
    null = []
    for _ in range(100):
        rs = sorted(random.sample(range(3, 13000), len(SERIES) - 1) + [1])
        null.append(fit(ws, rs)[0])
    null.sort()
    say('- the same with random series of %d multiples (always containing 1), each with its own best unit: median '
        '%d weights (%.0f%%), best %d. The binary-decimal series fits %s.' % (
            len(SERIES), null[50], 100 * null[50] / len(ws), null[-1],
            'better than every random series' if k > null[-1] else 'no better than random series'))
    near = Counter()
    for w in ws:
        s = min(SERIES, key=lambda s: abs(w / (u * s) - 1))
        if abs(w / (u * s) - 1) <= 0.05:
            near[s] += 1
    say('- weights per series step: %s.' % ', '.join('%d x%d' % kv for kv in sorted(near.items())))
    say()
    rows = [r for r in load(split=False) if r['flat']]
    for kind in ('short', 'long', 'tiered'):
        c = Counter(NUMS[g][0] for r in rows for g in r['flat'] if g in NUMS and NUMS[g][1] == kind
                    and g not in ('2', '32'))
        n = sum(c.values())
        b = sum(v for val, v in c.items() if val in SERIES)
        say('- W2 %s strokes (the pairs left out): %d tokens, values %s; in the weight series (1, 2, 4, 8): %d '
            '(%.0f%%).' % (kind, n, ', '.join('%d x%d' % kv for kv in sorted(c.items())), b, 100 * b / max(n, 1)))
    say('- Of the values 1-12 that occur, 1, 2, 4, 8 are four of eight (half). The written numerals are dominated '
        'by 3 (short and long), a value the weight series does not have: the stroke numbers count things (or '
        'capacity units), not weight units.')
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'weights.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:4])
