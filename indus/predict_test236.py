"""Two-hundred-and-thirty-sixth registered prediction set (PREDICTIONS.md, OB1-OB4): decipherment loop 61, are the short
all-lexical lines of genre 'other' bare names (last sign head-like)? Writes results/predict_test236.md."""
import random
from collections import Counter

import grammar as G
import rtools as R
from predict_test108 import genre
from signs import load


def short_other(lines):
    return [t for t in lines if genre(t) == 'other' and 2 <= len(t) <= 3 and all(G.lexical(g) for g in t)]


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-thirty-sixth registered predictions: decipherment loop 61, the short lines of no genre', 'predict_test236')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    occ = Counter(g for t in DA for g in t)
    hd = Counter(t[i - 1] for t in DA for i, g in enumerate(t) if g in R.END and i > 0)
    prop = lambda g: hd[g] / occ[g] if occ[g] else 0.0
    tok = Counter(g for t in DA + DB for g in t)
    ranked = sorted(tok, key=tok.get)
    band = {g: ranked[max(0, i - 10):i + 11] for i, g in enumerate(ranked)}

    def hi(signs, seed):
        obs = sum(map(prop, signs)) / max(1, len(signs))
        rnd = random.Random(seed)
        ge = sum(sum(prop(rnd.choice(band[g])) for g in signs) / max(1, len(signs)) >= obs for _ in range(1000))
        return obs, (ge + 1) / 1001
    sa, sb = short_other(DA), short_other(DB)
    oa, pa = hi([t[-1] for t in sa], 236)
    ob, pb = hi([t[-1] for t in sb], 237)
    rd.rec('OB1', 'the last sign is head-like (A)', '%d lines; mean propensity %.3f; p = %.4f' % (len(sa), oa, pa), pa < 0.05)
    rd.rec('OB2', 'and in B', '%d lines; %.3f; p = %.4f' % (len(sb), ob, pb), pb < 0.05)
    fa = sum(prop(t[0]) for t in sa) / max(1, len(sa))
    fb = sum(prop(t[0]) for t in sb) / max(1, len(sb))
    rd.rec('OB3', 'first sign less head-like than last', 'A first %.3f / last %.3f; B %.3f / %.3f' % (fa, oa, fb, ob), fa < oa and fb < ob)
    rd.rec('OB4', 'progress rule', 'OB1 %s, OB2 %s' % (pa < 0.05, pb < 0.05), pa < 0.05 and pb < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
