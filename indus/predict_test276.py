"""Two-hundred-and-seventy-sixth registered prediction set (PREDICTIONS.md, CC1-CC3): decipherment loop 101, the slot
after the counted sign. In count lines (genre 'count'), the lexical sign right after the counted sign (numeral run +
counted sign + X) is X. Is that slot restricted, as the count-label slot before the count is (set 215)? Entropy of X
against 1,000 random same-size samples of the lexical tokens of the same lines. Writes results/predict_test276.md."""
import math
import random
from collections import Counter

import rtools as R
from grammar import lexical
from predict_test108 import genre
from signs import load


def slot(lines):
    xs, pool = [], []
    for t in lines:
        t = tuple(t)
        if genre(t) != 'count':
            continue
        pool += [g for g in t if lexical(g)]
        for i in range(len(t) - 2):
            if t[i] in R.NUMS and t[i + 1] not in R.NUMS and lexical(t[i + 1]) and lexical(t[i + 2]):
                xs.append(t[i + 2])
    return xs, pool


def H(xs):
    c = Counter(xs)
    n = len(xs)
    return -sum(v / n * math.log2(v / n) for v in c.values())


def test(xs, pool, seed=276):
    rnd = random.Random(seed)
    h = H(xs)
    null = [H(rnd.sample(pool, len(xs))) for _ in range(1000)]
    p = (1 + sum(x <= h for x in null)) / 1001
    return h, sorted(null)[500], p, len(xs)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-seventy-sixth registered predictions: decipherment loop 101, the slot after the counted sign', 'predict_test276')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    ra = test(*slot(DA))
    rb = test(*slot(DB))
    for nm, r in (('A', ra), ('B', rb)):
        rd.say('- %s: slot entropy %.2f bits (%d tokens) against null median %.2f; p = %.3f.' % (nm, r[0], r[3], r[1], r[2]))
    rd.say()
    rd.rec('CC1', 'A: the slot is restricted (entropy below 95% of random samples)', 'H %.2f vs %.2f, p = %.3f' % (ra[0], ra[1], ra[2]), ra[2] < 0.05)
    rd.rec('CC2', 'B: the same', 'H %.2f vs %.2f, p = %.3f' % (rb[0], rb[1], rb[2]), rb[2] < 0.05)
    rd.rec('CC3', 'progress rule: CC1 and CC2 (role count complement; R rises)', 'CC1 %s, CC2 %s' % (ra[2] < 0.05, rb[2] < 0.05), ra[2] < 0.05 and rb[2] < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
