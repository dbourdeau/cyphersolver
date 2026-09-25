"""Three-hundred-and-third registered prediction set (PREDICTIONS.md, SS1-SS3): decipherment loop 128, single signs as
referent units under a stricter criterion (3+ objects in 2+ texts, 80%+ one picture) beside pairs and 3-sign runs at
set 287's (2+, 67%+). Combined FDR against 100 picture shuffles. Writes results/predict_test303.md."""
import random

import rtools as R
import referents as X
from progress import data


def mixed(P):
    u = X.units(P, 2, 0.67, (2, 3))
    for lab, (clean, both) in P.items():
        u[(lab, 1)] = X.q_pairs(both, 3, 0.8, 1)
    return u


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-third registered predictions: decipherment loop 128, single signs under a stricter criterion', 'predict_test303')
    DL, tr, te = data()
    P = X.pools(F, recs)
    base = X.units(P, 2, 0.67, (2, 3))
    u = mixed(P)
    rnd = random.Random(303)
    tot = 0
    for _ in range(100):
        Q = {}
        for lab, (clean, both) in P.items():
            pics = [m for t, m in both]
            rnd.shuffle(pics)
            cp = [m for t, m in clean]
            rnd.shuffle(cp)
            Q[lab] = (list(zip([t for t, m in clean], cp)), list(zip([t for t, m in both], pics)))
        tot += X.count(mixed(Q))
    null = tot / 100
    real = X.count(u)
    fdr = null / max(1, real)
    b_cov, cov = X.coverage(DL, P, base), X.coverage(DL, P, u)
    singles = sorted((k[0], g[0], m) for k, qq in u.items() if k != 'texts' and k[1] == 1 for g, m in qq.items())
    rd.say('- units %d (single signs %d), shuffled mean %.1f, FDR %.1f%%; coverage %.2f%% -> %.2f%%.' % (real, len(singles), null, 100 * fdr, 100 * b_cov, 100 * cov))
    rd.say('- single signs: %s.' % ('; '.join('%s %s -> %s' % x for x in singles) or 'none'))
    rd.say()
    rd.rec('SS1', 'combined FDR <= 10%', '%.1f%%' % (100 * fdr), fdr <= 0.10)
    rd.rec('SS2', 'coverage rises above 1.46%', '%.2f%%' % (100 * cov), cov > b_cov)
    rd.rec('SS3', 'progress rule: SS1 and SS2 (strict single signs join the referent units)', 'SS1 %s, SS2 %s' % (fdr <= 0.10, cov > b_cov), fdr <= 0.10 and cov > b_cov)
    rd.finish()


if __name__ == '__main__':
    main()
