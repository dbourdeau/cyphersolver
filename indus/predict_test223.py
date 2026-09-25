"""Two-hundred-and-twenty-third registered prediction set (PREDICTIONS.md, SU1-SU4): decipherment loop 48, is the tail after
a mid-line ending a second name (last sign with high head propensity)? Writes results/predict_test223.md."""
import random
from collections import Counter

import rtools as R
from predict_test103 import CL
from signs import load


def tail(t):
    k = next((i for i, g in enumerate(t) if g in R.END), None)
    if k is None or k == len(t) - 1:
        return None
    r = [g for g in t[k + 1:] if g not in ('400', '90') and g not in R.NUMS]
    if not r or all(g in CL for g in r):
        return None
    return r


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-twenty-third registered predictions: decipherment loop 48, a second unit after a mid-line ending', 'predict_test223')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    occ = Counter(g for t in DA for g in t)
    hd = Counter(t[i - 1] for t in DA for i, g in enumerate(t) if g in R.END and i > 0)
    prop = lambda g: hd[g] / occ[g] if occ[g] else 0.0
    tok = Counter(g for t in DA + DB for g in t)
    ranked = sorted(tok, key=tok.get)
    band = {g: ranked[max(0, i - 10):i + 11] for i, g in enumerate(ranked)}

    def test(lines, seed):
        ts = [x for x in (tail(t) for t in lines) if x]
        last = [x[-1] for x in ts]
        obs = sum(map(prop, last)) / max(1, len(last))
        rnd = random.Random(seed)
        ge = sum(sum(prop(rnd.choice(band[g])) for g in last) / max(1, len(last)) >= obs for _ in range(1000))
        return ts, obs, (ge + 1) / 1001
    ta, oa, pa = test(DA, 223)
    rd.rec('SU1', 'the tail ends in a likely head (A)', '%d tails; mean head propensity of the last sign %.3f; frequency-matched p = %.4f' % (len(ta), oa, pa), pa < 0.05)
    tb, ob, pb = test(DB, 224)
    rd.rec('SU2', 'and in B', '%d tails; %.3f; p = %.4f' % (len(tb), ob, pb), pb < 0.05)
    other = [prop(g) for x in tb for g in x[:-1]]
    lastb = [prop(x[-1]) for x in tb]
    mo, ml = sum(other) / max(1, len(other)), sum(lastb) / max(1, len(lastb))
    rd.rec('SU3', 'other tail signs less head-like than the last (B)', 'other %.3f (%d), last %.3f' % (mo, len(other), ml), mo < ml)
    rd.rec('SU4', 'progress rule', 'SU1 %s, SU2 %s' % (pa < 0.05, pb < 0.05), pa < 0.05 and pb < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
