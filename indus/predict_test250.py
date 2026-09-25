"""Two-hundred-and-fiftieth registered prediction set (PREDICTIONS.md, LP1-LP3): decipherment loop 75, grammar rule LOW-POST
(1-2 lexical signs + 400, the sign before 400 of low head propensity). Writes results/predict_test250.md."""
from collections import Counter

import grammar as G
import rtools as R
from predict_test108 import genre
from predict_test215 import slots
from progress import data
from signs import load


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-fiftieth registered predictions: decipherment loop 75, a rule for 400 after a non-head', 'predict_test250')
    DL, tr, te = data()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    DF = sorted({tuple(ln) for r in F for ln in r['seq'] if ln} - set(DA) - set(DB))
    H = G.heads_from(DL)
    hc, mc = G.head_stats(DL)
    labels = {g for g, v in Counter(s[0] for s in (slots(t) for t in DA if genre(t) == 'count') if s).most_common(10)}
    occ = Counter(g for t in DA for g in t)
    hd = Counter(t[i - 1] for t in DA for i, g in enumerate(t) if g in R.END and i > 0)
    low = {g for g in occ if occ[g] >= 3 and hd[g] / occ[g] < 0.05 and G.lexical(g)}
    f0 = lambda t: G.parse5(t, H, hc, mc, labels) is not None

    def f1(t):
        if f0(t):
            return True
        t = tuple(t)
        return 2 <= len(t) <= 3 and t[-1] == '400' and t[-2] in low and all(G.lexical(g) for g in t[:-1])
    b0, b1 = G.margin(DB, f0), G.margin(DB, f1)
    SB = G.shuffled(DB)
    r0, r1 = sum(map(f0, DB)) / len(DB), sum(map(f1, DB)) / len(DB)
    s0, s1 = sum(map(f0, SB)) / len(SB), sum(map(f1, SB)) / len(SB)
    ok1 = b1 > b0 and (r1 - r0) > (s1 - s0)
    rd.rec('LP1', 'B margin rises, real more than shuffled', 'margin %.2f -> %.2f; real %+.2f, shuffled %+.2f points' % (100 * b0, 100 * b1, 100 * (r1 - r0), 100 * (s1 - s0)), ok1)
    f0m, f1m = G.margin(DF, f0), G.margin(DF, f1)
    rd.rec('LP2', 'F margin rises', '%.2f -> %.2f' % (100 * f0m, 100 * f1m), f1m > f0m)
    rd.rec('LP3', 'progress rule', 'LP1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
