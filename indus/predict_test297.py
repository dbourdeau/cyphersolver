"""Two-hundred-and-ninety-seventh registered prediction set (PREDICTIONS.md, VS1-VS3): decipherment loop 122, the picture
vault of set 294 (all unit kinds, 2+ objects, 67%+) with specificity-weighted votes: each qualifying unit votes with
weight 1 / n, n the number of other objects carrying it (rare units count more; set 296 weighted the other way). Scored
by the excess of correct predictions over the shuffle median. Writes results/predict_test297.md."""
import math
import random
from collections import Counter, defaultdict

import rtools as R
import referents as X

K, S = 2, 0.67
NS = (1, 2, 3, -2)


def grams(t):
    out = set()
    for n in NS:
        out |= {g for g in X.grams_of(t, n) if '|' not in g}
    return out


def vault(objs):
    occ = defaultdict(list)
    for t, m in objs:
        for g in grams(t):
            occ[g].append((t, m))
    hits = n = 0
    for t, m in objs:
        votes = Counter()
        for g in grams(t):
            rest = [(u, x) for u, x in occ[g] if u != t]
            if len(rest) < K or len({u for u, x in rest}) < 2:
                continue
            lab = X.ok([x for u, x in rest], K, S)
            if lab:
                votes[lab] += 1 / len(rest)
        if votes:
            n += 1
            hits += sorted(votes.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] == m
    return hits, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-ninety-seventh registered predictions: decipherment loop 122, the picture vault with specificity-weighted votes', 'predict_test297')
    P = X.pools(F, recs)
    real = [vault(both) for clean, both in P.values()]
    h, n = sum(a for a, b in real), sum(b for a, b in real)
    rnd = random.Random(297)
    null = []
    for _ in range(200):
        tot = 0
        for clean, both in P.values():
            pics = [m for t, m in both]
            rnd.shuffle(pics)
            tot += vault(list(zip([t for t, m in both], pics)))[0]
        null.append(tot)
    p = (1 + sum(x >= h for x in null)) / 201
    rd.say('- %d correct of %d predicted (%.1f%%); shuffles median %d, 95th percentile %d; p = %.3f (set 294: 64 of 191, excess +60).' % (h, n, 100 * h / max(1, n), sorted(null)[100], sorted(null)[189], p))
    rd.say()
    ex = h - sorted(null)[100]
    rd.rec('VS1', 'excess of correct predictions over the shuffle median above +60 (set 294), p < 0.05', 'excess %+d, p = %.3f' % (ex, p), ex > 60 and p < 0.05)
    rd.rec('VS2', 'accuracy on predicted objects above 33.5% (set 294)', '%.1f%%' % (100 * h / max(1, n)), h / max(1, n) > 0.335)
    rd.rec('VS3', 'progress rule: VS1 (the tier 3 vault line rises)', 'VS1 %s' % (ex > 60 and p < 0.05), ex > 60 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
