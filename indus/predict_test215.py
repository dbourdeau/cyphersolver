"""Two-hundred-and-fifteenth registered prediction set (PREDICTIONS.md, CT1-CT5): decipherment loop 40, is the slot before
a count filled from a restricted set (a count label)? Writes results/predict_test215.md."""
import random
from collections import Counter

import rtools as R
from predict_test108 import genre
from signs import load


def slots(t):
    """(sign before the first numeral run, first sign after it) or None."""
    i = next((i for i, g in enumerate(t) if g in R.NUMS), None)
    if i is None or i == 0 or t[i - 1] in R.NUMS:
        return None
    j = i
    while j < len(t) and t[j] in R.NUMS:
        j += 1
    return t[i - 1], (t[j] if j < len(t) else None)


def conc(lines):
    pre = [s[0] for s in (slots(t) for t in lines) if s]
    return sum(v for k, v in Counter(pre).most_common(10)) / max(1, len(pre)), pre


def shuffled(lines, rnd):
    out = []
    for t in lines:
        idx = [i for i, g in enumerate(t) if g not in R.NUMS]
        vals = [t[i] for i in idx]
        rnd.shuffle(vals)
        u = list(t)
        for i, v in zip(idx, vals):
            u[i] = v
        out.append(tuple(u))
    return out


def test(lines, seed, n=1000):
    obs, pre = conc(lines)
    rnd = random.Random(seed)
    ge = sum(conc(shuffled(lines, rnd))[0] >= obs for _ in range(n))
    return obs, len(pre), (ge + 1) / (n + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-fifteenth registered predictions: decipherment loop 40, the sign before a count', 'predict_test215')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    ca = [t for t in DA if genre(t) == 'count']
    cb = [t for t in DB if genre(t) == 'count']
    oa, na, pa = test(ca, 215)
    rd.rec('CT1', 'the pre-count slot is concentrated (A)', 'top-ten share %.1f%% of %d pre-count tokens; shuffles p = %.4f' % (100 * oa, na, pa), pa < 0.01)
    ob, nb, pb = test(cb, 216)
    rd.rec('CT2', 'and in B', 'top-ten share %.1f%% of %d; p = %.4f' % (100 * ob, nb, pb), pb < 0.05)
    topA = [g for g, v in Counter(s[0] for s in (slots(t) for t in ca) if s).most_common(10)]
    preB = [s[0] for s in (slots(t) for t in cb) if s]
    cov = sum(g in topA for g in preB) / max(1, len(preB))
    rd.rec('CT3', "A's ten commonest pre-count signs cover 40% of B's", '%.1f%% (%s)' % (100 * cov, ', '.join(topA)), cov >= 0.4)
    heads = {t[i - 1] for t in DA for i, g in enumerate(t) if g in R.END and i > 0}
    sb = [s for s in (slots(t) for t in cb) if s]
    ph = [s[0] in heads for s in sb]
    ah = [s[1] in heads for s in sb if s[1]]
    rd.ltl('CT4', 'the label slot is not the counted-thing slot (B)', 'name heads, pre-count sign', ph, ah)
    rd.rec('CT5', 'progress rule', 'CT1 %s, CT2 %s' % (pa < 0.01, pb < 0.05), pa < 0.01 and pb < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
