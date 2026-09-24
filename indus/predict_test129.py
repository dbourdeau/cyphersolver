"""Hundred-and-twenty-ninth registered prediction set (PREDICTIONS.md, CW1-CW10): the strong pairs as compounds.
Writes results/predict_test129.md."""
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test61 import units
from predict_test108 import genre
from predict_test128 import adj, gaps_excess

CITY = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-twenty-ninth registered predictions: the strong pairs as compounds', 'predict_test129')
    DL = sorted({tuple(t) for t in AB})
    tc = Counter(g for t in DL for g in t)
    cm = sorted(g for g in tc if tc[g] >= 20 and g not in R.NUMS)
    g, E = gaps_excess(DL, cm)
    a = adj(DL)
    rd.say('- excess pairs %d.' % len(E))
    rd.say()
    rd.thr('CW1', 'the order is fixed', 'pairs with under 5% reverse', sum(a[(y, x)] < 0.05 * (a[(x, y)] + a[(y, x)]) for x, y in E), len(E), 0.8)
    rd.thr('CW2', 'the left member calls the right', 'pairs where the right follows the left in 50%+ of its tokens', sum(a[(x, y)] >= 0.5 * tc[x] for x, y in E), len(E), 0.5)
    gen = defaultdict(set)
    for t in DL:
        for p in zip(t, t[1:]):
            gen[p].add(genre(t))
    rd.thr('CW3', 'compounds cross genres', 'pairs in 2+ genres', sum(len(gen[p] - {'other'}) >= 2 for p in E), len(E), 0.6)
    Fn = [r for r in F if r['type'] != 'TAB:C']
    site = defaultdict(set)
    FL = set()
    for r in Fn:
        for ln in r['seq']:
            if ln:
                FL.add(tuple(ln))
                for p in zip(ln, ln[1:]):
                    site[p].add(r['site'].strip())
    rd.thr('CW4', 'compounds are shared by the cities', 'pairs at both cities', sum(set(CITY) <= site[p] for p in E), len(E), 0.6)
    ab = adj(sorted({tuple(t) for t in B}))
    rd.thr('CW5', 'compounds hold in B', 'pairs occurring 2+ times in B', sum(ab[p] >= 2 for p in E), len(E), 0.6 + 0.1)
    fr1 = set()
    for t in DL:
        s = ['#'] + list(t) + ['#']
        for i in range(1, len(s) - 1):
            if s[i] in cm:
                fr1.add((s[i - 1], s[i + 1]))
    frp = defaultdict(set)
    for t in DL:
        s = ['#'] + list(t) + ['#']
        for i in range(1, len(s) - 2):
            frp[(s[i], s[i + 1])].add((s[i - 1], s[i + 2]))
    rd.thr('CW6', 'a compound fills a one-sign slot', 'pairs sharing a frame with a single sign', sum(bool(frp[p] & fr1) for p in E), len(E), 0.5)
    U = units(sorted({b for b, e in T.names(AB) if len(b) >= 2}))
    rd.thr('CW7', 'compounds are the name units', 'pairs that are units', sum(p in U for p in E), len(E), 0.6)
    rd.thr('CW8', 'compounds are not name + ending', 'pairs with 740 or 520', sum(x in R.END or y in R.END for x, y in E), len(E), 0.2, above=False)
    lefts = {x for x, y in E}
    rights = {y for x, y in E}
    rd.thr('CW9', 'compounds chain', 'pairs chaining with another', sum(y in lefts or x in rights for x, y in E), len(E), 0.2)
    new = FL - set(DL)
    an = adj(sorted(new))
    rd.thr('CW10', 'compounds recur in new lines', "pairs in F' lines absent from A + B", sum(an[p] >= 1 for p in E), len(E), 0.6)
    rd.finish()


if __name__ == '__main__':
    main()
