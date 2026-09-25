"""Three-hundred-and-fiftieth registered prediction set (PREDICTIONS.md, LC1-LC3): decipherment loop 175, units over 50
learned distributional sign classes (famlm.learned_classes on the distinct training lines, seed 0; set 201) added to
set 348's referent units, tagged apart. Combined FDR against 100 within-stratum shuffles; Linear B control.
Writes results/predict_test350.md."""
import random
from collections import defaultdict

import predict_test304 as C
import predict_test334 as S
import rtools as R
import referents as X
from famlm import learned_classes
from predict_test234 import lines
from predict_test235 import KEY
from predict_test325 import lb_q
from predict_test338 import collapse, objects_typed
from predict_test348 import build as b348
from progress import data

LM = {}


def lc(t):
    return tuple(g if g == '|' else LM.get(g, g) for g in t)


def build(cc, cb):
    u = b348(cc, cb)
    fam_on, sign = S.FAMILIES, S.SIGN
    S.FAMILIES, S.SIGN = False, (1, 2, 3, -2, -3)
    ul = S.units([(lc(t), m, s) for t, m, s in cc], [(lc(t), m, s) for t, m, s in cb])
    S.FAMILIES, S.SIGN = fam_on, sign
    for (lab, n), q in ((k, v) for k, v in ul.items() if k != 'texts'):
        u[('L' + lab, n)] = q
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
    rd = R.Round('Three-hundred-and-fiftieth registered predictions: decipherment loop 175, learned-class referent units', 'predict_test350')
    DL, tr, te = data()
    LM.update(learned_classes(DL, 50, seed=0))
    C.LMAP.update(LM)
    clean, both = objects_typed(F, recs)
    P = {'made': ([(o[0], o[1]) for o in clean], [(o[0], o[1]) for o in both])}
    cc, cb = collapse(clean), collapse(both)
    S.ALPHA = 0.002
    S.SIGN = tuple(S.SIGN) + (-3, 5)
    S.FAM = tuple(S.FAM) + (-3,)
    u = build(cc, cb)
    n, f = fdr(cc, cb, 350)
    c = C.coverage(DL, P, u)
    rd.say('- %d units (%d learned-class), FDR %.1f%%, coverage %.2f%% (set 348: 4.57%%).' % (n, sum(len(v) for k, v in u.items() if k != 'texts' and k[0].startswith('L')), 100 * f, 100 * c))
    q = lb_q(lines(), 0.002)
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rd.say()
    ok = f <= 0.10 and c > 0.0457
    rd.rec('LC1', 'FDR <= 10% and coverage above 4.57%', 'FDR %.1f%%, %.2f%%' % (100 * f, 100 * c), ok)
    rd.rec('LC2', 'Linear B at alpha 0.002: 2+ of 4 control words, none wrong', 'recovered %d, wrong %d' % (len(rec), len(wrong)), len(rec) >= 2 and not wrong)
    rd.rec('LC3', 'progress rule: LC1 and LC2 (learned-class units join)', 'LC1 %s, LC2 %s' % (ok, len(rec) >= 2 and not wrong), ok and len(rec) >= 2 and not wrong)
    rd.finish()


if __name__ == '__main__':
    main()
