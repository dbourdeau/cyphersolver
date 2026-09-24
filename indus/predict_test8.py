"""Test of the eighth registered prediction set (PREDICTIONS.md, Hypothesis Y): are foreign names spelled with free
(sound) signs rather than bound (word) pairs?

Y1  share of adjacent pairs that are bound pairs (seventh set), West Asian lines against length-matched home draws.
Y2  mean freedom of sign tokens (residual of log distinct neighbours on log tokens, home lines; 740, 520, 817, 820,
    861 left out), West Asian against length-matched home draws.

Usage: python predict_test8.py path/to/icit_full_records_indusscript_net.csv
Writes results/predict_test8.md.
"""
import math
import os
import random
import sys
from collections import Counter, defaultdict

import icit_full
from gulf import IRAN_WEST, WEST

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N_PERM = 10000
LEAVE = {'740', '520', '817', '820', '861'}
random.seed(28)


def say(s=''):
    OUT.append(s)
    print(s)


def bound_pairs(path):
    """As predict_test7: the 30 highest-PMI pairs with count 10+ in single-line intact seal texts."""
    single = []
    for r in icit_full.objects(path):
        if not r['type'].startswith('SEAL') or not r['flat'] or '?' in r['flat']:
            continue
        if any(ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw']):
            continue
        if len(r['seq']) == 1:
            single.append(r['flat'])
    uni = Counter(g for t in single for g in t)
    bi = Counter((a, b) for t in single for a, b in zip(t, t[1:]))
    N1, N2 = sum(uni.values()), sum(bi.values())
    pmi = {p: math.log((c / N2) / ((uni[p[0]] / N1) * (uni[p[1]] / N1))) for p, c in bi.items() if c >= 10}
    return set(sorted(pmi, key=lambda p: -pmi[p])[:30])


def main(path):
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = [r for r in icit_full.objects(path, intact_only=True) if r['seq']]
    west = [r for r in rows if recs[r['sealid']][2] in WEST or r['site'] in IRAN_WEST]
    wids = {r['sealid'] for r in west}
    home = [r for r in rows if r['sealid'] not in wids and recs[r['sealid']][2] not in ('Other',)]
    wl = [ln for r in west for ln in r['seq'] if len(ln) >= 2]
    hl = [ln for r in home for ln in r['seq'] if len(ln) >= 2]
    bylen = defaultdict(list)
    for ln in hl:
        bylen[len(ln)].append(ln)

    def draw(n):
        while n not in bylen:
            n -= 1
        return random.choice(bylen[n])
    say('# Eighth registered predictions: foreign names, bound pairs and free signs')
    say()
    say('- West Asian lines of 2+ signs: %d (%d signs); home lines: %d.' % (len(wl), sum(map(len, wl)), len(hl)))
    for ln in wl:
        say('  - %s' % ' '.join(ln))
    say()

    # Y1
    bound = bound_pairs(path)

    def bshare(lines):
        pr = [(a, b) for t in lines for a, b in zip(t, t[1:])]
        return sum(p in bound for p in pr) / len(pr), sum(p in bound for p in pr), len(pr)
    obs, k, n = bshare(wl)
    null = [bshare([draw(len(t)) for t in wl])[0] for _ in range(N_PERM)]
    p1 = (sum(1 for x in null if x <= obs) + 1) / (N_PERM + 1)
    say('## Y1 bound pairs')
    say()
    say('- West Asian adjacent pairs that are bound pairs: %d of %d (%.1f%%); length-matched home draws: %.1f%% '
        '(5-95%%: %.1f-%.1f%%); p = %.4f. **Y1 %s.**' % (
            k, n, 100 * obs, 100 * sum(null) / N_PERM, 100 * sorted(null)[N_PERM // 20],
            100 * sorted(null)[-N_PERM // 20], p1, 'holds' if p1 < 0.05 else 'fails'))
    say()

    # Y2
    tok = Counter(g for t in hl for g in t)
    nb = defaultdict(set)
    for t in hl:
        for a, b in zip(t, t[1:]):
            nb[a].add(('R', b))
            nb[b].add(('L', a))
    sg = [g for g in tok if tok[g] >= 5]
    xs = [math.log(tok[g]) for g in sg]
    ys = [math.log(max(1, len(nb[g]))) for g in sg]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    free = {g: y - (my + slope * (x - mx)) for g, x, y in zip(sg, xs, ys)}

    def fmean(lines):
        v = [free[g] for t in lines for g in t if g in free and g not in LEAVE]
        return sum(v) / len(v) if v else float('nan'), len(v)
    obs2, nw = fmean(wl)
    null2 = [fmean([draw(len(t)) for t in wl])[0] for _ in range(N_PERM)]
    p2 = (sum(1 for x in null2 if x >= obs2) + 1) / (N_PERM + 1)
    wtoks = [g for t in wl for g in t if g not in LEAVE]
    say('## Y2 free signs')
    say()
    say('- freedom: log(distinct neighbours) = %.2f + %.2f log(tokens) over %d home signs; residual = freedom.' % (
        my - slope * mx, slope, len(sg)))
    say('- West Asian tokens scored: %d of %d (the rest have under 5 home tokens: %s).' % (
        nw, len(wtoks), ', '.join(sorted({g for g in wtoks if g not in free})) or 'none'))
    say('- mean freedom, West Asian: %+.3f; length-matched home draws: %+.3f (5-95%%: %+.3f to %+.3f); p = %.4f. '
        '**Y2 %s.**' % (obs2, sum(null2) / N_PERM, sorted(null2)[N_PERM // 20], sorted(null2)[-N_PERM // 20], p2,
                        'holds' if p2 < 0.05 else 'fails'))
    say()
    say('**Hypothesis Y %s.**' % ('holds' if p1 < 0.05 and p2 < 0.05 else 'fails'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test8.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
