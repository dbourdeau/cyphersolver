"""Two-hundred-and-forty-ninth registered prediction set (PREDICTIONS.md, ZF1-ZF3): decipherment loop 74, is the sign
directly before a 400 that follows no ending head-like? Writes results/predict_test249.md."""
import random
from collections import Counter

import grammar as G
import rtools as R
from signs import load


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-forty-ninth registered predictions: decipherment loop 74, the marker 400 without an ending', 'predict_test249')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    occ = Counter(g for t in DA for g in t)
    hd = Counter(t[i - 1] for t in DA for i, g in enumerate(t) if g in R.END and i > 0)
    prop = lambda g: hd[g] / occ[g] if occ[g] else 0.0
    tok = Counter(g for t in DA + DB for g in t)
    ranked = sorted(tok, key=tok.get)
    band = {g: ranked[max(0, i - 10):i + 11] for i, g in enumerate(ranked)}
    pre = lambda D: [t[i - 1] for t in D for i, g in enumerate(t) if g == '400' and i > 0 and G.lexical(t[i - 1])]

    def hi(signs, seed):
        obs = sum(map(prop, signs)) / max(1, len(signs))
        rnd = random.Random(seed)
        ge = sum(sum(prop(rnd.choice(band[g])) for g in signs) / max(1, len(signs)) >= obs for _ in range(1000))
        return obs, (ge + 1) / 1001, len(signs)
    oa, pa, na = hi(pre(DA), 249)
    ob, pb, nb = hi(pre(DB), 250)
    rd.rec('ZF1', 'the sign before a bare 400 is head-like (A)', '%d tokens; mean propensity %.3f; p = %.4f' % (na, oa, pa), pa < 0.05)
    rd.rec('ZF2', 'and in B', '%d tokens; %.3f; p = %.4f' % (nb, ob, pb), pb < 0.05)
    rd.rec('ZF3', 'progress rule', 'ZF1 %s, ZF2 %s' % (pa < 0.05, pb < 0.05), pa < 0.05 and pb < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
