"""Two-hundred-and-ninety-fifth registered prediction set (PREDICTIONS.md, VK1-VK3): decipherment loop 120, the picture
vault (set 294, all unit kinds) with units that may rest on a single other object (k = 1, one picture), besides k 2 with
67%+. Correct predictions against 200 shuffles within each pool. Writes results/predict_test295.md."""
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
            if not rest:
                continue
            if len(rest) == 1:
                lab = rest[0][1]
            elif len({u for u, x in rest}) < 2:
                continue
            else:
                lab = X.ok([x for u, x in rest], K, S)
            if lab:
                votes[lab] += 1
        if votes:
            n += 1
            hits += sorted(votes.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] == m
    return hits, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-ninety-fifth registered predictions: decipherment loop 120, the picture vault with single-object units', 'predict_test295')
    P = X.pools(F, recs)
    real = [vault(both) for clean, both in P.values()]
    h, n = sum(a for a, b in real), sum(b for a, b in real)
    rnd = random.Random(295)
    null = []
    for _ in range(200):
        tot = 0
        for clean, both in P.values():
            pics = [m for t, m in both]
            rnd.shuffle(pics)
            tot += vault(list(zip([t for t, m in both], pics)))[0]
        null.append(tot)
    p = (1 + sum(x >= h for x in null)) / 201
    rd.say('- %d correct of %d predicted (%.1f%%); shuffles median %d, 95th percentile %d; p = %.3f (set 294: 64 of 191).' % (h, n, 100 * h / max(1, n), sorted(null)[100], sorted(null)[189], p))
    rd.say()
    rd.rec('VK1', 'more than 64 correct predictions, p < 0.05 against shuffles', '%d, p = %.3f' % (h, p), h > 64 and p < 0.05)
    rd.rec('VK2', 'accuracy on predicted objects 25%+', '%.1f%%' % (100 * h / max(1, n)), h >= 0.25 * n)
    rd.rec('VK3', 'progress rule: VK1 (the tier 3 vault line counts more held-out tablets)', 'VK1 %s' % (h > 64 and p < 0.05), h > 64 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
