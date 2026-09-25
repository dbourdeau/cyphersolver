"""Two-hundred-and-eighty-ninth registered prediction set (PREDICTIONS.md, PV1-PV4): decipherment loop 114, the picture
vault with referent units. Leave one text out: for each pictured tablet (both pools, fragments included, part-texts
merged), the referent units (sign pairs and 3-sign runs) are learned from the other objects of its pool, excluding
every object with the same text, with set 287's criterion (2+ objects, 2+ distinct texts, 67%+ one picture); the units
in the held-out text vote for its picture (majority, ties to the first in sort order). Accuracy on the objects that
get a prediction, against 200 shuffles of the pictures within each pool. Writes results/predict_test289.md."""
import random
from collections import Counter, defaultdict

import rtools as R
import referents as X

K, S, NS = 2, 0.67, (2, 3)


def grams(t):
    return {t[i:i + n] for n in NS for i in range(len(t) - n + 1) if '|' not in t[i:i + n]}


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
            best = sorted(votes.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
            n += 1
            hits += best == m
    return hits, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-eighty-ninth registered predictions: decipherment loop 114, the picture vault with referent units', 'predict_test289')
    P = X.pools(F, recs)
    real = {lab: vault(both) for lab, (clean, both) in P.items()}
    h, n = sum(v[0] for v in real.values()), sum(v[1] for v in real.values())
    rnd = random.Random(289)
    null, nullp = [], {lab: [] for lab in P}
    for _ in range(200):
        hh = nn = 0
        for lab, (clean, both) in P.items():
            pics = [m for t, m in both]
            rnd.shuffle(pics)
            a, b = vault(list(zip([t for t, m in both], pics)))
            nullp[lab].append(a / max(1, b))
            hh, nn = hh + a, nn + b
        null.append(hh / max(1, nn))
    acc = h / max(1, n)
    p = (1 + sum(x >= acc for x in null)) / 201
    for lab, (a, b) in real.items():
        rd.say('- %s: %d of %d predicted objects right (%.1f%%); shuffle median %.1f%%; %d objects in the pool.' % (lab, a, b, 100 * a / max(1, b), 100 * sorted(nullp[lab])[100], len(P[lab][1])))
    rd.say('- pooled: %d of %d (%.1f%%); shuffle median %.1f%%, 95th percentile %.1f%%; p = %.3f.' % (h, n, 100 * acc, 100 * sorted(null)[100], 100 * sorted(null)[189], p))
    rd.say()
    rd.rec('PV1', 'pooled accuracy above the 95th percentile of the shuffles', 'p = %.3f' % p, p < 0.05)
    rd.rec('PV2', 'pooled accuracy 30%+ (sign-level vault, sets 201-203: 16.9%)', '%.1f%%' % (100 * acc), acc >= 0.30)
    both_ok = all(real[lab][0] / max(1, real[lab][1]) > sorted(nullp[lab])[100] for lab in P)
    rd.rec('PV3', 'each pool above its shuffle median', ', '.join('%s %.1f%% vs %.1f%%' % (lab, 100 * real[lab][0] / max(1, real[lab][1]), 100 * sorted(nullp[lab])[100]) for lab in P), both_ok)
    rd.rec('PV4', 'progress rule: PV1 and PV2 (tier 3 picture vault line)', 'PV1 %s, PV2 %s' % (p < 0.05, acc >= 0.30), p < 0.05 and acc >= 0.30)
    rd.finish()


if __name__ == '__main__':
    main()
