"""Three-hundred-and-forty-eighth registered prediction set (PREDICTIONS.md, DF1-DF3): decipherment loop 173, units over
ICIT decade families (the S model's graphic families, set 194) added to set 347's referent units (true-duplicate pool,
alpha 0.002): single, pair, 3-sign run, skip-pair and wide skip-pair over decade families, tagged apart. Combined FDR
against 100 within-stratum shuffles; Linear B control. Writes results/predict_test348.md."""
import random
from collections import defaultdict

import predict_test334 as S
import rtools as R
import referents as X
from predict_test234 import lines
from predict_test235 import KEY
from predict_test304 import coverage
from predict_test325 import lb_q
from predict_test338 import collapse, objects_typed
from progress import data


def dec(t):
    return tuple(g if g == '|' else ('f%d' % (int(g) // 10) if g.isdigit() else g) for g in t)


def build(cc, cb):
    u = S.units(cc, cb)
    fam_on, sign = S.FAMILIES, S.SIGN
    S.FAMILIES, S.SIGN = False, (1, 2, 3, -2, -3)
    ud = S.units([(dec(t), m, s) for t, m, s in cc], [(dec(t), m, s) for t, m, s in cb])
    S.FAMILIES, S.SIGN = fam_on, sign
    for (lab, n), q in ((k, v) for k, v in ud.items() if k != 'texts'):
        u[('D' + lab, n)] = q
    return u


def fdr(cc, cb, seed):
    rnd = random.Random(seed)
    real = X.count(build(cc, cb))
    tot = 0
    for _ in range(100):
        def shuf(obs):
            by = defaultdict(list)
            for i, (t, m, s) in enumerate(obs):
                by[s].append(i)
            pics = [m for t, m, s in obs]
            for s, idx in by.items():
                vals = [pics[i] for i in idx]
                rnd.shuffle(vals)
                for i, v in zip(idx, vals):
                    pics[i] = v
            return [(t, p, s) for (t, m, s), p in zip(obs, pics)]
        tot += X.count(build(shuf(cc), shuf(cb)))
    return real, tot / 100 / max(1, real)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-forty-eighth registered predictions: decipherment loop 173, decade-family referent units', 'predict_test348')
    DL, tr, te = data()
    clean, both = objects_typed(F, recs)
    P = {'made': ([(o[0], o[1]) for o in clean], [(o[0], o[1]) for o in both])}
    cc, cb = collapse(clean), collapse(both)
    S.ALPHA = 0.002
    S.SIGN = tuple(S.SIGN) + (-3, 5)
    S.FAM = tuple(S.FAM) + (-3,)
    u = build(cc, cb)
    n, f = fdr(cc, cb, 348)
    c = coverage(DL, P, u)
    rd.say('- %d units (%d decade-family), FDR %.1f%%, coverage %.2f%% (set 347: 3.04%%).' % (n, sum(len(v) for k, v in u.items() if k != 'texts' and k[0].startswith('D')), 100 * f, 100 * c))
    q = lb_q(lines(), 0.002)
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rd.say()
    ok = f <= 0.10 and c > 0.0304
    rd.rec('DF1', 'FDR <= 10% and coverage above 3.04%', 'FDR %.1f%%, %.2f%%' % (100 * f, 100 * c), ok)
    rd.rec('DF2', 'Linear B at alpha 0.002: 2+ of 4 control words, none wrong', 'recovered %d, wrong %d' % (len(rec), len(wrong)), len(rec) >= 2 and not wrong)
    rd.rec('DF3', 'progress rule: DF1 and DF2 (decade-family units join)', 'DF1 %s, DF2 %s' % (ok, len(rec) >= 2 and not wrong), ok and len(rec) >= 2 and not wrong)
    rd.finish()


if __name__ == '__main__':
    main()
