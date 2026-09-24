"""Test of the second prediction set in PREDICTIONS.md (Q1, Q2; registered and committed before this script).

Usage: python predict_test2.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test2.md.
"""
import math
import os
import random
import sys
from collections import Counter

import icit_full
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def names(rows):
    out = []
    for r in rows:
        for t in r['seq']:
            t = [g for g in t if g != '?']
            if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
                s, e = t[:-2], t[-2]
            elif len(t) >= 2 and t[-1] in ('740', '520'):
                s, e = t[:-1], t[-1]
            else:
                continue
            if len(s) >= 2:
                out.append((tuple(s), e))
    return out


def mi(pairs):
    n = len(pairs)
    a = Counter(x for x, _ in pairs)
    b = Counter(y for _, y in pairs)
    ab = Counter(pairs)
    return sum(c / n * math.log2(c * n / (a[x] * b[y])) for (x, y), c in ab.items())


def mi_excess(pairs, rng, k=500):
    obs = mi(pairs)
    xs = [x for x, _ in pairs]
    ys = [y for _, y in pairs]
    sims = []
    for _ in range(k):
        rng.shuffle(ys)
        sims.append(mi(list(zip(xs, ys))))
    m = sum(sims) / k
    return obs, obs - m, sum(1 for s in sims if s >= obs) / k


def agree(ns, pos):
    by = {}
    for s, e in ns:
        by.setdefault(s[pos], []).append(e)
    same = tot = 0
    for es in by.values():
        c = Counter(es)
        n = len(es)
        same += sum(v * (v - 1) for v in c.values())
        tot += n * (n - 1)
    return same / tot if tot else 0


def run(label, ns, rng):
    say('## %s (%d names of 2+ signs with an ending)' % (label, len(ns)))
    say()
    last = mi_excess([(s[-1], e) for s, e in ns], rng)
    first = mi_excess([(s[0], e) for s, e in ns], rng)
    say('- Q1 mutual information with the ending: last sign %.3f bits (excess over permutations %.3f, p %.3f); first '
        'sign %.3f (excess %.3f, p %.3f). Pairs of names agreeing in ending: sharing the last sign %.1f%%, sharing the '
        'first sign %.1f%%.' % (last[0], last[1], last[2], first[0], first[1], first[2],
                                100 * agree(ns, -1), 100 * agree(ns, 0)))
    q1 = last[1] > first[1] and last[2] < 0.01 and agree(ns, -1) > agree(ns, 0)
    ff = [e for s, e in ns if s[-1] in FISH]
    fn = [e for s, e in ns if s[-1] not in FISH and any(g in FISH for g in s)]
    no = [e for s, e in ns if not any(g in FISH for g in s)]

    def rate(v):
        return 100 * v.count('520') / len(v) if v else float('nan')
    say('- Q2 share taking 520: fish-final names %.1f%% (%d), fish inside but not last %.1f%% (%d), no fish %.1f%% (%d).' % (
        rate(ff), len(ff), rate(fn), len(fn), rate(no), len(no)))
    q2 = bool(fn) and rate(fn) < rate(ff) / 2 and abs(rate(fn) - rate(no)) < 10
    say('- Q1 %s; Q2 %s.' % ('holds' if q1 else 'fails', 'holds' if q2 else 'fails'))
    say()
    return q1, q2


def main(path):
    rng = random.Random(151)
    disc = names(load())
    have = {tuple(tuple(ln) for ln in r['seq']) for r in load()}
    full_new = [r for r in icit_full.objects(path, intact_only=True)
                if r['seq'] and tuple(tuple(ln) for ln in r['seq']) not in have]
    held = names(load(only_m77=True)) + names(full_new)
    say('# Second prediction set (Q1, Q2): results')
    say()
    a = run('Discovery: ICIT-derived corpus', disc, rng)
    b = run('Held out: M77 additions + texts of the fuller corpus not in the dump', held, rng)
    say('**Verdict as registered:** Q1 %s, Q2 %s (both samples required).' % (
        'holds' if a[0] and b[0] else 'fails', 'holds' if a[1] and b[1] else 'fails'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test2.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
