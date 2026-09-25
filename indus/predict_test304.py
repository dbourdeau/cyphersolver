"""Three-hundred-and-fourth registered prediction set (PREDICTIONS.md, SF1-SF3): decipherment loop 129, skip-pairs and
sign-family units (pairs, 3-sign runs over Parpola's description families) under the stricter criterion (3+ objects in
2+ texts, 80%+) added to set 303's units. Combined FDR against 100 picture shuffles; coverage on the real tokens.
Writes results/predict_test304.md."""
import random

import rtools as R
import referents as X
from descfam import families
from progress import data

FM = families()


def fam(t):
    return tuple(g if g == '|' else FM.get(g, g) for g in t)


def current(P):
    u = X.units(P, 2, 0.67, (2, 3))
    for lab, (clean, both) in P.items():
        u[(lab, 1)] = X.q_pairs(both, 3, 0.8, 1)
    return u


def with_skip(P):
    u = current(P)
    for lab, (clean, both) in P.items():
        u[(lab, -2)] = X.q_pairs(both, 3, 0.8, -2)
    return u


def with_fam(P):
    u = current(P)
    for lab, (clean, both) in P.items():
        fb = [(fam(t), m) for t, m in both]
        for n in (2, 3):
            u[('F' + lab, n)] = X.q_pairs(fb, 3, 0.8, n)
    return u


def fdr(P, build, seed):
    rnd = random.Random(seed)
    tot = 0
    for _ in range(100):
        Q = {}
        for lab, (clean, both) in P.items():
            pics = [m for t, m in both]
            rnd.shuffle(pics)
            cp = [m for t, m in clean]
            rnd.shuffle(cp)
            Q[lab] = (list(zip([t for t, m in clean], cp)), list(zip([t for t, m in both], pics)))
        tot += X.count(build(Q))
    return tot / 100 / max(1, X.count(build(P)))


def coverage(DL, P, u):
    used = {lab: {t for t, m in P[lab][0]} for lab in P}
    cov = 0
    for t in DL:
        if t in u['texts']:
            cov += len(t)
            continue
        mark = set()
        for key, qq in u.items():
            if key == 'texts':
                continue
            lab, n = key
            fl = lab.startswith('F')
            dl = lab.startswith('D')  # set 348: decade-family units
            pool = lab[1:] if (fl or dl) else lab
            if t not in used[pool]:
                continue
            tt = fam(t) if fl else tuple(g if g == '|' else ('f%d' % (int(g) // 10) if g.isdigit() else g) for g in t) if dl else t
            if n == -2:
                mark |= {j for i in range(len(tt) - 2) if (tt[i], '_', tt[i + 2]) in qq for j in (i, i + 2)}
            elif n == -3:
                mark |= {j for i in range(len(tt) - 3) if (tt[i], '_', '_', tt[i + 3]) in qq for j in (i, i + 3)}
            if n > 0:
                mark |= {j for i in range(len(tt) - n + 1) if tt[i:i + n] in qq for j in range(i, i + n)}
        cov += len(mark)
    return cov / sum(len(t) for t in DL)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-fourth registered predictions: decipherment loop 129, skip-pairs and family units under the stricter criterion', 'predict_test304')
    DL, tr, te = data()
    P = X.pools(F, recs)
    c0 = coverage(DL, P, current(P))
    res = {}
    for name, build, seed in (('skip-pairs', with_skip, 3041), ('family units', with_fam, 3042)):
        u = build(P)
        res[name] = (X.count(u), fdr(P, build, seed), coverage(DL, P, u))
        rd.say('- + %s: %d units, FDR %.1f%%, coverage %.2f%% (now %.2f%%).' % (name, res[name][0], 100 * res[name][1], 100 * res[name][2], 100 * c0))
    rd.say()
    a, b = res['skip-pairs'], res['family units']
    rd.rec('SF1', 'strict skip-pairs: FDR <= 10% and coverage rises', 'FDR %.1f%%, %.2f%%' % (100 * a[1], 100 * a[2]), a[1] <= 0.10 and a[2] > c0)
    rd.rec('SF2', 'strict family units: FDR <= 10% and coverage rises', 'FDR %.1f%%, %.2f%%' % (100 * b[1], 100 * b[2]), b[1] <= 0.10 and b[2] > c0)
    ok = (a[1] <= 0.10 and a[2] > c0) or (b[1] <= 0.10 and b[2] > c0)
    rd.rec('SF3', 'progress rule: SF1 or SF2 (the passing kind joins the referent units)', 'SF1 %s, SF2 %s' % (a[1] <= 0.10 and a[2] > c0, b[1] <= 0.10 and b[2] > c0), ok)
    rd.finish()


if __name__ == '__main__':
    main()
