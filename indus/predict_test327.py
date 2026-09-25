"""Three-hundred-and-twenty-seventh registered prediction set (PREDICTIONS.md, TY1-TY2): decipherment loop 152, the
base-rate referent configuration (set 325, alpha 0.01) with the individually made pool split by tablet type: copper
(TAB:C) and incised (TAB:I) as separate pools beside the moulded pool; whole texts per individually made pool. Combined
FDR against 100 picture shuffles; coverage on the real tokens. Writes results/predict_test327.md."""
from collections import Counter, defaultdict

from scipy.stats import binom

import rtools as R
import referents as X
from predict_test200 import objects
from predict_test237 import merged
from predict_test254 import frag_objects
from predict_test304 import coverage, fam, fdr
from predict_test325 import FAM, SIGN, build, qb
from progress import data

POOLS3 = {'copper': ('TAB:C',), 'incised': ('TAB:I',), 'moulded': ('TAB:B',)}


def build3(alpha):
    def f(P):
        u = {'texts': {}}
        for lab in ('copper', 'incised'):
            g = defaultdict(list)
            for t, m in P[lab][0]:
                g[t].append(m)
            bm = Counter(m for t, m in P[lab][1])
            tot = sum(bm.values())
            for t, ms in g.items():
                m, v = Counter(ms).most_common(1)[0]
                if len(ms) >= 2 and binom.sf(v - 1, len(ms), bm[m] / tot) < alpha:
                    u['texts'][t] = m
        for lab, (clean, both) in P.items():
            c = Counter(m for t, m in both)
            base = {m: c[m] / len(both) for m in c}
            for n in SIGN:
                u[(lab, n)] = qb(both, n, alpha, base)
            fb = [(fam(t), m) for t, m in both]
            for n in FAM:
                u[('F' + lab, n)] = qb(fb, n, alpha, base)
        return u
    return f


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-twenty-seventh registered predictions: decipherment loop 152, referent pools by tablet type', 'predict_test327')
    DL, tr, te = data()
    P = X.pools(F, recs)
    c0 = coverage(DL, P, build(0.01)(P))
    P3 = {}
    for lab, types in POOLS3.items():
        clean = objects(F, recs, types)
        P3[lab] = (clean, merged(clean + frag_objects(types)))
    f = build3(0.01)
    u = f(P3)
    fd = fdr(P3, f, 327)
    c1 = coverage(DL, P3, u)
    rd.say('- pools %s; %d units, FDR %.1f%%, coverage %.2f%% -> %.2f%%.' % (', '.join('%s %d' % (k, len(v[1])) for k, v in P3.items()), X.count(u), 100 * fd, 100 * c0, 100 * c1))
    rd.say()
    rd.rec('TY1', 'combined FDR <= 10% and coverage above 4.79%', 'FDR %.1f%%, %.2f%% -> %.2f%%' % (100 * fd, 100 * c0, 100 * c1), fd <= 0.10 and c1 > c0)
    rd.rec('TY2', 'progress rule: TY1 (the referent pools split by tablet type)', 'TY1 %s' % (fd <= 0.10 and c1 > c0), fd <= 0.10 and c1 > c0)
    rd.finish()


if __name__ == '__main__':
    main()
