"""Two-hundred-and-ninety-third registered prediction set (PREDICTIONS.md, RP1-RP3): decipherment loop 118, where
referent units sit in a text. For each pool, the relative start position (i / (len - n), 0 = first, 1 = last) of every
occurrence of a qualifying referent unit (pairs, 3-sign runs; set 288's criterion) against every occurrence of the other
units recurring on 2+ objects in 2+ texts. Mann-Whitney, two-sided. Writes results/predict_test293.md."""
from collections import defaultdict

from scipy.stats import mannwhitneyu

import rtools as R
import referents as X

K, S, NS = 2, 0.67, (2, 3)


def positions(objs, units):
    occ, texts = defaultdict(int), defaultdict(set)
    for t, m in objs:
        for n in NS:
            for g in X.grams_of(t, n):
                if '|' not in g:
                    occ[g] += 1
                    texts[g].add(t)
    recur = {g for g in occ if occ[g] >= 2 and len(texts[g]) >= 2}
    ref, oth = [], []
    for t, m in {(t, m) for t, m in objs}:
        for n in NS:
            for i in range(len(t) - n + 1):
                g = t[i:i + n]
                if '|' in g or len(t) == n or g not in recur:
                    continue
                pos = i / (len(t) - n)
                (ref if g in units else oth).append(pos)
    return ref, oth


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-ninety-third registered predictions: decipherment loop 118, where referent units sit in a text', 'predict_test293')
    P = X.pools(F, recs)
    res = {}
    for lab, (clean, both) in P.items():
        units = set()
        for n in NS:
            units |= set(X.q_pairs(both, K, S, n))
        ref, oth = positions(both, units)
        p = mannwhitneyu(ref, oth, alternative='two-sided').pvalue if ref and oth else 1.0
        mr, mo = sum(ref) / max(1, len(ref)), sum(oth) / max(1, len(oth))
        res[lab] = (mr, mo, p, len(ref), len(oth))
        rd.say('- %s: referent units mean position %.2f (%d occurrences), other recurring units %.2f (%d); p = %.2g.' % (lab, mr, len(ref), mo, len(oth), p))
    rd.say()
    a, b = res['made'], res['moulded']
    same = (a[0] - a[1]) * (b[0] - b[1]) > 0
    rd.rec('RP1', 'individually made tablets: referent units sit at a different relative position', 'p = %.2g' % a[2], a[2] < 0.05)
    rd.rec('RP2', 'moulded tablets: the same, same direction', 'p = %.2g, same direction %s' % (b[2], same), b[2] < 0.05 and same)
    rd.rec('RP3', 'progress rule: RP1 and RP2 (a new finding replicated across pools)', 'RP1 %s, RP2 %s' % (a[2] < 0.05, b[2] < 0.05 and same), a[2] < 0.05 and b[2] < 0.05 and same)
    rd.finish()


if __name__ == '__main__':
    main()
