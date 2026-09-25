"""Three-hundred-and-eighth registered prediction set (PREDICTIONS.md, SH1-SH3): decipherment loop 133, a split-half
check of the tuned referent configuration (set 307). Each pool's distinct texts are split at random into halves (seed
308); the units are learned on one half with set 307's configuration and scored on the other: the share of (unit,
held-out object) matches whose picture is the unit's label, against 1,000 shuffles of the held-out pictures. Both
directions. Validation only. Writes results/predict_test308.md."""
import random

import rtools as R
import referents as X
from predict_test304 import fam
from predict_test307 import mid


def split(P, seed=308):
    rnd = random.Random(seed)
    H1, H2 = {}, {}
    for lab, (clean, both) in P.items():
        texts = sorted({t for t, m in both})
        rnd.shuffle(texts)
        a = set(texts[:len(texts) // 2])
        H1[lab] = ([o for o in clean if o[0] in a], [o for o in both if o[0] in a])
        H2[lab] = ([o for o in clean if o[0] not in a], [o for o in both if o[0] not in a])
    return H1, H2


def matches(u, H):
    """(unit label, object picture) for every unit found in a held-out object."""
    out = []
    for key, qq in u.items():
        if key == 'texts':
            for t, m in sum((b for c, b in H.values()), []):
                if t in qq:
                    out.append((qq[t], m, t))
            continue
        lab, n = key
        fl = lab.startswith('F')
        dl = lab.startswith('D')  # decade-family units (set 349); no effect on earlier runs
        pool = lab[1:] if (fl or dl) else lab
        for t, m in H[pool][1]:
            tt = fam(t) if fl else tuple(g if g == '|' else ('f%d' % (int(g) // 10) if g.isdigit() else g) for g in t) if dl else t
            for g in X.grams_of(tt, n):
                if g in qq:
                    out.append((qq[g], m, t))
    return out


def score(ms, rnd, n=1000):
    real = sum(a == b for a, b, t in ms)
    objs = sorted({(t, b) for a, b, t in ms})
    pics = [b for t, b in objs]
    idx = {t: i for i, (t, b) in enumerate(objs)}
    ge = 0
    for _ in range(n):
        rnd.shuffle(pics)
        ge += sum(a == pics[idx[t]] for a, b, t in ms) >= real
    return real, len(ms), (ge + 1) / (n + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-eighth registered predictions: decipherment loop 133, a split-half check of the tuned referent configuration', 'predict_test308')
    P = X.pools(F, recs)
    H1, H2 = split(P)
    rnd = random.Random(3081)
    res = []
    for name, learn, test in (('half 1 -> half 2', H1, H2), ('half 2 -> half 1', H2, H1)):
        u = mid(learn)
        r = score(matches(u, test), rnd)
        res.append(r)
        rd.say('- %s: %d units learned; %d of %d held-out matches carry the unit\'s picture (%.0f%%); p = %.4f.' % (name, X.count(u), r[0], r[1], 100 * r[0] / max(1, r[1]), r[2]))
    rd.say()
    rd.rec('SH1', 'half 1 -> half 2: matches above the shuffles (p < 0.05)', 'p = %.4f' % res[0][2], res[0][2] < 0.05)
    rd.rec('SH2', 'half 2 -> half 1: the same', 'p = %.4f' % res[1][2], res[1][2] < 0.05)
    rd.rec('SH3', 'progress rule: none (validation; failure of SH1 or SH2 downgrades the tuned line)', 'SH1 %s, SH2 %s' % (res[0][2] < 0.05, res[1][2] < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
