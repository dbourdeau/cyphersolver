"""Three-hundred-and-thirteenth registered prediction set (PREDICTIONS.md, RE1-RE3): decipherment loop 138, referent
units before an ending. For each pool, the share of occurrences of qualifying referent units (pairs, 3-sign runs at set
287-288's criterion) directly followed by 740 / 520 against the same share for other units recurring on 2+ objects in 2+
texts; Fisher, two-sided. Writes results/predict_test313.md."""
from collections import defaultdict

from scipy.stats import fisher_exact

import rtools as R
import referents as X

NS = (2, 3)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-thirteenth registered predictions: decipherment loop 138, referent units before an ending', 'predict_test313')
    P = X.pools(F, recs)
    res = {}
    for lab, (clean, both) in P.items():
        units = set()
        for n in NS:
            units |= set(X.q_pairs(both, 2, 0.67, n))
        occ, texts = defaultdict(int), defaultdict(set)
        for t, m in both:
            for n in NS:
                for g in X.grams_of(t, n):
                    if '|' not in g:
                        occ[g] += 1
                        texts[g].add(t)
        recur = {g for g in occ if occ[g] >= 2 and len(texts[g]) >= 2}
        c = {True: [0, 0], False: [0, 0]}
        for t in {t for t, m in both}:
            for n in NS:
                for i in range(len(t) - n + 1):
                    g = t[i:i + n]
                    if '|' in g or g not in recur or any(x in R.END for x in g):
                        continue
                    nxt = t[i + n] in R.END if i + n < len(t) else False
                    c[g in units][0 if nxt else 1] += 1
        p = fisher_exact([c[True], c[False]])[1]
        r1, r0 = c[True][0] / max(1, sum(c[True])), c[False][0] / max(1, sum(c[False]))
        res[lab] = (r1, r0, p)
        rd.say('- %s: referent units followed by 740 / 520 %.0f%% (%d), other recurring units %.0f%% (%d); p = %.2g.' % (lab, 100 * r1, sum(c[True]), 100 * r0, sum(c[False]), p))
    rd.say()
    a, b = res['made'], res['moulded']
    same = (a[0] - a[1]) * (b[0] - b[1]) > 0
    rd.rec('RE1', 'individually made tablets: the shares differ (p < 0.05)', 'p = %.2g' % a[2], a[2] < 0.05)
    rd.rec('RE2', 'moulded tablets: they differ in the same direction', 'p = %.2g, same direction %s' % (b[2], same), b[2] < 0.05 and same)
    rd.rec('RE3', 'progress rule: RE1 and RE2 (a new finding replicated across pools)', 'RE1 %s, RE2 %s' % (a[2] < 0.05, b[2] < 0.05 and same), a[2] < 0.05 and b[2] < 0.05 and same)
    rd.finish()


if __name__ == '__main__':
    main()
