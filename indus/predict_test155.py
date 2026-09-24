"""Hundred-and-fifty-fifth registered prediction set (PREDICTIONS.md, DT1-DT4): names from two interchangeable elements?
Writes results/predict_test155.md."""
import random
from collections import Counter

import predict_test13 as T
import rtools as R

random.seed(175)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-fifty-fifth registered predictions: names from two interchangeable elements?', 'predict_test155')
    ns = sorted({(b, e) for b, e in T.names(A + B) if b})
    two = sorted({b for b, e in ns if len(b) == 2})
    three = sorted({b for b, e in ns if len(b) == 3})
    rd.say('- distinct two-sign bodies %d, three-sign bodies %d.' % (len(two), len(three)))
    rd.say()
    hc = Counter(b[1] for b in two)
    ops = {b[0] for b in two}
    hs = [h for h, n in hc.items() if n >= 3]
    rd.thr('DT1', 'heads also open names', 'heads with 3+ two-sign names also attested as openers', sum(h in ops for h in hs), len(hs), 0.5)
    rev = lambda bs: sum(1 for a, b in set(bs) if a != b and (b, a) in set(bs)) // 2
    obs = rev(two)
    heads = [b[1] for b in two]
    draws = []
    for _ in range(1000):
        random.shuffle(heads)
        draws.append(rev([(b[0], h) for b, h in zip(two, heads)]))
    med = sorted(draws)[500]
    rd.rec('DT2', 'reversed pairs as often as chance', 'reversed pairs %d; shuffled median %d (range %d-%d); examples %s' % (
        obs, med, min(draws), max(draws), ', '.join('%s %s' % (a, b) for a, b in two if (b, a) in set(two) and a < b)[:200]), obs >= med)
    o, p = R.mi_perm([b[0] for b in two], [b[1] for b in two])
    rd.rec('DT3', 'opener and head combine freely', 'two-sign bodies %d; MI %.4f bits; p = %.4f (holds if p >= 0.05)' % (len(two), o, p), p >= 0.05)
    edge = {b[0] for b in two + three} | {b[-1] for b in two + three}
    mid = {b[1] for b in three}
    rd.thr('DT4', 'middle signs come from the same pool', 'middle-sign types attested as opener or head', sum(m in edge for m in mid), len(mid), 0.7)
    rd.finish()


if __name__ == '__main__':
    main()
