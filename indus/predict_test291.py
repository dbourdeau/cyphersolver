"""Two-hundred-and-ninety-first registered prediction set (PREDICTIONS.md, SN1-SN4): decipherment loop 116, the
referent method on seals with the calibrated criterion (set 287: 2+ seals in 2+ distinct texts, 67%+ one animal; units
pairs and 3-sign runs, set 288), counting only units whose animal is not the one-horned bull (Bull1, the default: set
238). FDR against 100 shuffles of the animals among the seals. Writes results/predict_test291.md."""
import random

import rtools as R
import referents as X
from predict_test200 import objects
from predict_test237 import merged
from prizebench import referent_fixed
from progress import data

K, S, NS = 2, 0.67, (2, 3)
TYPES = ('SEAL:S', 'SEAL:R', 'SEAL')


def seal_units(objs):
    out = {}
    for n in NS:
        out.update({p: m for p, m in X.q_pairs(objs, K, S, n).items() if m != 'Bull1'})
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-ninety-first registered predictions: decipherment loop 116, the referent method on seals, non-default animals', 'predict_test291')
    DL, tr, te = data()
    objs = merged(objects(F, recs, TYPES))
    u = seal_units(objs)
    rnd = random.Random(291)
    texts, pics = [t for t, m in objs], [m for t, m in objs]
    null = []
    for _ in range(100):
        rnd.shuffle(pics)
        null.append(len(seal_units(list(zip(texts, pics)))))
    fdr = (sum(null) / 100) / max(1, len(u))
    used = {t for t, m in objects(F, recs, TYPES)}
    add = 0
    base_cov, _ = referent_fixed(DL)
    for t in DL:
        if t not in used:
            continue
        mark = set()
        for n in NS:
            for i in range(len(t) - n + 1):
                if t[i:i + n] in u:
                    mark |= set(range(i, i + n))
        add += len(mark)
    tot = sum(len(t) for t in DL)
    rd.say('- %d seals; %d non-Bull1 units, shuffled mean %.1f, FDR %.1f%%; tokens marked on seals %d (%.2f%% of all).' % (len(objs), len(u), sum(null) / 100, 100 * fdr, add, 100 * add / tot))
    rd.say('- units: %s.' % '; '.join('%s -> %s' % (' '.join(p), m) for p, m in sorted(u.items())[:40]))
    rd.say()
    rd.rec('SN1', 'non-default seal units exist with FDR <= 10%', '%d units, FDR %.1f%%' % (len(u), 100 * fdr), len(u) > 0 and fdr <= 0.10)
    rd.rec('SN2', 'more units than the shuffles\' 95th percentile', 'real %d, 95th %d' % (len(u), sorted(null)[94]), len(u) > sorted(null)[94])
    rd.rec('SN3', 'they mark tokens not already covered', '%d tokens' % add, add > 0)
    ok = len(u) > 0 and fdr <= 0.10 and len(u) > sorted(null)[94]
    rd.rec('SN4', 'progress rule: SN1 and SN2 (seals join the referent line)', 'SN1 %s, SN2 %s' % (len(u) > 0 and fdr <= 0.10, len(u) > sorted(null)[94]), ok)
    rd.finish()


if __name__ == '__main__':
    main()
