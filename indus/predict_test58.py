"""Fifty-eighth registered prediction set (PREDICTIONS.md, FS1-FS10): the fish signs. Writes
results/predict_test58.md."""
import random

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test50 import ent
from predict_test53 import lab_perm
from signs import FISH

random.seed(78)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Fifty-eighth registered predictions: the fish signs', 'predict_test58')
    nm = T.names(AB)
    bs = [b for b, _ in nm if len(b) >= 2]
    ff = lambda b: sum(x in FISH and y in FISH and x != y for x, y in zip(b, b[1:]))
    obs = sum(map(ff, bs))
    ge = 0
    for _ in range(R.N // 10):
        k = 0
        for b in bs:
            s = list(b)
            random.shuffle(s)
            k += ff(s)
        ge += k >= obs
    p = (ge + 1) / (R.N // 10 + 1)
    rd.rec('FS1', 'fish cluster', 'adjacent different-fish pairs %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    prs = [(x, y) for b in bs for x, y in zip(b, b[1:]) if x in FISH and y in FISH and x != y]
    sec, fst = sum(y == '220' for x, y in prs), sum(x == '220' for x, y in prs)
    p = R.binom_ge(sec, sec + fst)
    rd.rec('FS2', 'the plain fish comes second', '220 second %d, first %d; p = %.4f' % (sec, fst, p), sec > fst and p < 0.05)
    fm = [t for t in AB if nonname(t)]
    rd.gtl('FS3', 'fish belong to names', 'fish, body tokens', [g in FISH for b, _ in nm for g in b], [g in FISH for t in fm for g in t])
    fe = [e for b, e in nm if b and b[-1] in FISH]
    oe = [e for b, e in nm if b and b[-1] not in FISH]
    o, p = lab_perm(fe, oe, lambda a, b: ent(a) - ent(b), R.N)
    rd.rec('FS4', 'fish heads take either ending', 'ending entropy fish-headed %.3f, others %.3f; p = %.4f' % (ent(fe), ent(oe), p), o > 0 and p < 0.05)
    pre = lambda b, i: i > 0 and b[i - 1] in R.NUMS
    rd.gtl('FS5', 'fish are counted', 'after a numeral, fish body tokens', [pre(b, i) for b, _ in nm for i, g in enumerate(b) if g in FISH],
           [pre(b, i) for b, _ in nm for i, g in enumerate(b) if g not in FISH])
    pv = [(b[i - 1], g) for b, _ in nm for i, g in enumerate(b) if g in FISH and i > 0]
    rd.mi('FS6', 'the preceding sign picks the fish', 'fish tokens with a preceding sign', [a for a, _ in pv], [g for _, g in pv])
    nx = [(b[i + 1], g) for b, _ in nm for i, g in enumerate(b) if g in FISH and i + 1 < len(b)]
    rd.mi('FS7', 'the following sign picks the fish', 'fish tokens with a following sign', [a for a, _ in nx], [g for _, g in nx])
    fs = [(r['site'].strip(), g) for r in F if r['site'].strip() in ('Harappa', 'Mohenjo-daro') for b, _ in R.names_in(r) for g in b if g in FISH]
    rd.mi('FS8', 'each city has its fish', 'F fish tokens', [a for a, _ in fs], [g for _, g in fs])
    st = lambda site: [g in FISH for r in F if r['site'].strip() == site for b, _ in R.names_in(r) for g in b]
    rd.ltl('FS9', 'Harappa uses fewer fish', 'fish, Harappa body tokens', st('Harappa'), st('Mohenjo-daro'))
    rd.gtl('FS10', 'fish close formulas', 'last, fish formula tokens', [i == len(t) - 1 for t in fm for i, g in enumerate(t) if g in FISH],
           [i == len(t) - 1 for t in fm for i, g in enumerate(t) if g not in FISH])
    rd.finish()


if __name__ == '__main__':
    main()
