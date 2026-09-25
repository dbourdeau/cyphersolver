"""Three-hundred-and-twenty-fifth registered prediction set (PREDICTIONS.md, RB1-RB4): decipherment loop 150, a
base-rate criterion for referent units. A unit (on 2+ objects in 2+ distinct texts) takes the picture m most common among
its objects if P(X >= v) < alpha for X ~ Binomial(n, base rate of m in the pool), v of its n objects showing m. Unit
kinds as set 312 (sign single / pair / 3-run / 4-run / skip-pair, family single / pair / 3-run / skip-pair); whole texts
of the individually made pool as before. alpha from 0.001, 0.005, 0.01, 0.02, 0.05: the value with FDR <= 10% (100
picture shuffles) and the largest coverage is chosen; the Linear B control (set 235) is re-run with it.
Writes results/predict_test325.md."""
from collections import Counter, defaultdict

from scipy.stats import binom

import rtools as R
import referents as X
from predict_test234 import lines
from predict_test235 import KEY
from predict_test304 import coverage, fam
from progress import data

ALPHAS = (0.001, 0.005, 0.01, 0.02, 0.05)
SIGN = (1, 2, 3, 4, -2)
FAM = (1, 2, 3, -2)


def qb(objs, n, alpha, base):
    occ, texts = defaultdict(list), defaultdict(set)
    for t, m in objs:
        for g in X.grams_of(t, n):
            if '|' in g:
                continue
            occ[g].append(m)
            texts[g].add(t)
    out = {}
    for g, ms in occ.items():
        if len(ms) < 2 or len(texts[g]) < 2:
            continue
        m, v = Counter(ms).most_common(1)[0]
        if binom.sf(v - 1, len(ms), base[m]) < alpha:
            out[g] = m
    return out


def build(alpha):
    def f(P):
        u = {'texts': {}}
        g = defaultdict(list)
        for t, m in P['made'][0]:
            g[t].append(m)
        bm = Counter(m for t, m in P['made'][1])
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


def lb_q(ls, alpha):
    c = Counter(i for ws, i in ls)
    base = {m: c[m] / len(ls) for m in c}
    occ, texts = defaultdict(list), defaultdict(set)
    for ws, i in ls:
        for w in set(ws):
            occ[w].append(i)
            texts[w].add(tuple(ws))
    out = {}
    for w, ii in occ.items():
        if len(ii) < 2 or len(texts[w]) < 2:
            continue
        m, v = Counter(ii).most_common(1)[0]
        if binom.sf(v - 1, len(ii), base[m]) < alpha:
            out[w] = m
    return out


def main():
    from predict_test304 import fdr
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-twenty-fifth registered predictions: decipherment loop 150, a base-rate criterion for referent units', 'predict_test325')
    DL, tr, te = data()
    P = X.pools(F, recs)
    from predict_test312 import plus4
    c0 = coverage(DL, P, plus4(P))
    res = {}
    for a in ALPHAS:
        f = build(a)
        u = f(P)
        res[a] = (X.count(u), fdr(P, f, 325), coverage(DL, P, u))
        rd.say('- alpha %.3f: %d units, FDR %.1f%%, coverage %.2f%%.' % (a, res[a][0], 100 * res[a][1], 100 * res[a][2]))
    good = [a for a in ALPHAS if res[a][1] <= 0.10]
    best = max(good, key=lambda a: (res[a][2], -a)) if good else None
    rd.say('- current configuration (set 312): %.2f%%.' % (100 * c0))
    q = lb_q(lines(), best or 0.001)
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rd.say('- Linear B with alpha %s: recovered %s; wrong %s.' % (best, ', '.join(rec) or 'none', ', '.join('%s -> %s' % (w, q[w]) for w in wrong) or 'none'))
    rd.say()
    rb1 = best is not None and res[best][2] > c0
    rd.rec('RB1', 'an alpha with FDR <= 10% gives coverage above 2.29%', 'alpha %s: %.2f%%' % (best, 100 * res[best][2] if best else 0), rb1)
    rd.rec('RB2', 'Linear B with that alpha: 2+ of 4 control words, none wrong', 'recovered %d, wrong %d' % (len(rec), len(wrong)), len(rec) >= 2 and not wrong)
    rd.rec('RB3', 'the chosen alpha keeps FDR <= 10%', 'FDR %.1f%%' % (100 * res[best][1] if best else 100), best is not None)
    rd.rec('RB4', 'progress rule: RB1, RB2 and RB3 (the referent line uses the base-rate criterion)', 'RB1 %s, RB2 %s' % (rb1, len(rec) >= 2 and not wrong), rb1 and len(rec) >= 2 and not wrong)
    rd.finish()


if __name__ == '__main__':
    main()
