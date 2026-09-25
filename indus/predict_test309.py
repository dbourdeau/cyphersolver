"""Three-hundred-and-ninth registered prediction set (PREDICTIONS.md, SL1-SL3): decipherment loop 134, which referent
configuration survives a split-half check. Configurations C0-C7 (sets 233-307, in the order adopted); five random
half-splits of each pool's texts (seeds 3091-3095), both directions; per configuration the real matches (held-out
objects carrying the unit's picture) summed over the ten split-directions against 200 shuffles of the held-out pictures
(all split-directions shuffled together). A configuration is confirmed if p < 0.05. Writes results/predict_test309.md."""
import random

import rtools as R
import referents as X
from predict_test304 import fam
from predict_test305 import both as c5
from predict_test306 import more as c6
from predict_test307 import mid as c7
from predict_test308 import matches, split
from progress import data
from prizebench import referent_fixed


def c0(P):
    return X.units(P, 3, 0.8, (2,))


def c1(P):
    return X.units(P, 2, 0.67, (2,))


def c2(P):
    return X.units(P, 2, 0.67, (2, 3))


def c3(P):
    u = c2(P)
    for lab, (clean, b) in P.items():
        u[(lab, 1)] = X.q_pairs(b, 3, 0.8, 1)
    return u


def c4(P):
    u = c3(P)
    for lab, (clean, b) in P.items():
        fb = [(fam(t), m) for t, m in b]
        for n in (2, 3):
            u[('F' + lab, n)] = X.q_pairs(fb, 3, 0.8, n)
    return u


CONFIGS = [('C0 set 233', c0), ('C1 set 287', c1), ('C2 set 288', c2), ('C3 set 303', c3), ('C4 set 304', c4), ('C5 set 305', c5), ('C6 set 306', c6), ('C7 set 307', c7)]


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-ninth registered predictions: decipherment loop 134, which referent configuration survives a split-half check', 'predict_test309')
    DL, tr, te = data()
    P = X.pools(F, recs)
    halves = [split(P, seed) for seed in range(3091, 3096)]
    rnd = random.Random(309)
    confirmed = []
    for name, build in CONFIGS:
        allm = []
        for H1, H2 in halves:
            for learn, test in ((H1, H2), (H2, H1)):
                allm.append(matches(build(learn), test))
        real = sum(a == b for ms in allm for a, b, t in ms)
        tot = sum(len(ms) for ms in allm)
        ge = 0
        for _ in range(200):
            s = 0
            for ms in allm:
                objs = sorted({(t, b) for a, b, t in ms})
                pics = [b for t, b in objs]
                rnd.shuffle(pics)
                idx = {t: i for i, (t, b) in enumerate(objs)}
                s += sum(a == pics[idx[t]] for a, b, t in ms)
            ge += s >= real
        p = (ge + 1) / 201
        if p < 0.05:
            confirmed.append(name)
        rd.say('- %s: %d of %d held-out matches right (%.0f%%); p = %.3f.' % (name, real, tot, 100 * real / max(1, tot), p))
    rd.say()
    best = confirmed[-1] if confirmed else None
    rd.rec('SL1', 'C0 (the original criterion) is confirmed', 'confirmed: %s' % (', '.join(confirmed) or 'none'), 'C0 set 233' in confirmed)
    rd.rec('SL2', 'C7 (the tuned configuration) is confirmed', 'C7 %s' % ('C7 set 307' in confirmed), 'C7 set 307' in confirmed)
    rd.rec('SL3', 'progress rule: none (the referent line is set to the largest confirmed configuration)', 'largest confirmed: %s' % best, False)
    rd.finish()


if __name__ == '__main__':
    main()
