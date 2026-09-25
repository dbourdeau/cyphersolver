"""Three-hundredth registered prediction set (PREDICTIONS.md, FV1-FV3): decipherment loop 125, referent units over sign
families. Texts are mapped to Parpola's description families (descfam, set 208; signs without a family keep their own
id) before units (pairs, 3-sign runs) are formed, so graphic variants of one sign count together; set 287's criterion and
FDR rule (100 picture shuffles). Coverage: tokens of the real texts under a qualifying family unit.
Writes results/predict_test300.md."""
import rtools as R
import referents as X
from descfam import families
from progress import data

K, S, NS = 2, 0.67, (2, 3)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundredth registered predictions: decipherment loop 125, referent units over sign families', 'predict_test300')
    DL, tr, te = data()
    fm = families()
    f = lambda t: tuple(g if g == '|' else fm.get(g, g) for g in t)
    P = X.pools(F, recs)
    base = X.units(P, K, S, NS)
    b_cov = X.coverage(DL, P, base)
    PF = {lab: ([(f(t), m) for t, m in clean], [(f(t), m) for t, m in both]) for lab, (clean, both) in P.items()}
    u = X.units(PF, K, S, NS)
    real, null = X.count(u), X.null_count(PF, K, S, ns=NS)
    fdr = null / max(1, real)
    used = {lab: {t for t, m in P[lab][0]} for lab in P}
    cov = 0
    for t in DL:
        ft = f(t)
        if ft in u['texts']:
            cov += len(t)
            continue
        mark = set()
        for key, qq in u.items():
            if key == 'texts' or t not in used[key[0]]:
                continue
            n = key[1]
            for i in range(len(ft) - n + 1):
                if ft[i:i + n] in qq:
                    mark |= set(range(i, i + n))
        cov += len(mark)
    cov /= sum(len(t) for t in DL)
    rd.say('- family units: %d, shuffled mean %.1f, FDR %.1f%%, coverage %.2f%% (sign units %d, %.2f%%).' % (real, null, 100 * fdr, 100 * cov, X.count(base), 100 * b_cov))
    rd.say()
    rd.rec('FV1', 'family units keep FDR <= 10%', 'FDR %.1f%%' % (100 * fdr), fdr <= 0.10)
    rd.rec('FV2', 'coverage above the sign units\' %.2f%%' % (100 * b_cov), '%.2f%%' % (100 * cov), cov > b_cov)
    rd.rec('FV3', 'progress rule: FV1 and FV2 (the referent line uses family units)', 'FV1 %s, FV2 %s' % (fdr <= 0.10, cov > b_cov), fdr <= 0.10 and cov > b_cov)
    rd.finish()


if __name__ == '__main__':
    main()
