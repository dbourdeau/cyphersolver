"""Two-hundred-and-ninety-fourth registered prediction set (PREDICTIONS.md, VX1-VX3): decipherment loop 119, the picture
vault (set 290) with all unit kinds: single signs, pairs, 3-sign runs and skip-pairs. The held-out check itself controls
false units. Correct predictions against 200 shuffles within each pool. Writes results/predict_test294.md."""
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
                votes[lab] += 1
        if votes:
            n += 1
            hits += sorted(votes.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] == m
    return hits, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-ninety-fourth registered predictions: decipherment loop 119, the picture vault with all unit kinds', 'predict_test294')
    P = X.pools(F, recs)
    real = [vault(both) for clean, both in P.values()]
    h, n = sum(a for a, b in real), sum(b for a, b in real)
    rnd = random.Random(294)
    null = []
    for _ in range(200):
        tot = 0
        for clean, both in P.values():
            pics = [m for t, m in both]
            rnd.shuffle(pics)
            tot += vault(list(zip([t for t, m in both], pics)))[0]
        null.append(tot)
    p = (1 + sum(x >= h for x in null)) / 201
    rd.say('- %d correct of %d predicted (%.1f%%); shuffles median %d, 95th percentile %d; p = %.3f (set 290: 26 of 74).' % (h, n, 100 * h / max(1, n), sorted(null)[100], sorted(null)[189], p))
    rd.say()
    rd.rec('VX1', 'more than 26 correct predictions, p < 0.05 against shuffles', '%d, p = %.3f' % (h, p), h > 26 and p < 0.05)
    rd.rec('VX2', 'accuracy on predicted objects 30%+', '%.1f%%' % (100 * h / max(1, n)), h >= 0.3 * n)
    rd.rec('VX3', 'progress rule: VX1 (the tier 3 vault line counts more held-out tablets)', 'VX1 %s' % (h > 26 and p < 0.05), h > 26 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
