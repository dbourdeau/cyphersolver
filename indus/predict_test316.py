"""Three-hundred-and-sixteenth registered prediction set (PREDICTIONS.md, OW1-OW3): decipherment loop 141, one word per
referent? Within each pool, the referent units (pairs and 3-sign runs at 2+ / 67%+, single signs at 3+ / 67%+; sign
units only): the share of unit pairs sharing at least one sign among pairs with the same picture, minus the same share
among pairs with different pictures; against 1,000 shuffles of the unit labels. Writes results/predict_test316.md."""
import random
from itertools import combinations

import rtools as R
import referents as X


def units(both):
    u = {}
    for n in (2, 3):
        u.update(X.q_pairs(both, 2, 0.67, n))
    u.update(X.q_pairs(both, 3, 0.67, 1))
    return list(u.items())


def stat(items, labels):
    same = [0, 0]
    diff = [0, 0]
    for (i, (g1, _)), (j, (g2, _)) in combinations(enumerate(items), 2):
        share = bool(set(g1) & set(g2))
        (same if labels[i] == labels[j] else diff)[0] += share
        (same if labels[i] == labels[j] else diff)[1] += 1
    return same[0] / max(1, same[1]) - diff[0] / max(1, diff[1]), same, diff


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-sixteenth registered predictions: decipherment loop 141, one word per referent', 'predict_test316')
    P = X.pools(F, recs)
    rnd = random.Random(316)
    res = {}
    for lab, (clean, both) in P.items():
        items = units(both)
        labels = [m for g, m in items]
        d, same, diff = stat(items, labels)
        null = []
        for _ in range(1000):
            sh = labels[:]
            rnd.shuffle(sh)
            null.append(stat(items, sh)[0])
        p = (1 + sum(x >= d for x in null)) / 1001
        res[lab] = p
        rd.say('- %s: %d units; same-picture pairs sharing a sign %d of %d, different-picture %d of %d; difference %.3f; p = %.3f.' % (lab, len(items), same[0], same[1], diff[0], diff[1], d, p))
    rd.say()
    rd.rec('OW1', 'individually made tablets: same-picture units share signs more (p < 0.05)', 'p = %.3f' % res['made'], res['made'] < 0.05)
    rd.rec('OW2', 'moulded tablets: the same', 'p = %.3f' % res['moulded'], res['moulded'] < 0.05)
    rd.rec('OW3', 'progress rule: OW1 and OW2 (a new finding replicated across pools)', 'OW1 %s, OW2 %s' % (res['made'] < 0.05, res['moulded'] < 0.05), res['made'] < 0.05 and res['moulded'] < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
