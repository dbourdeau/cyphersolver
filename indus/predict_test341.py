"""Three-hundred-and-forty-first registered prediction set (PREDICTIONS.md, VD1-VD3): decipherment loop 166, the picture
vault of set 298 with mould copies counted once: in the moulded pool, tablets with the same text (copies of one mould,
part-texts merged) become one observation with their majority picture, both as held-out targets and as training
support; hand-made tablets stay separate. Correct predictions, excess over the shuffle median (set 298: +64 on objects).
A correction: the lower figure replaces the vault line. Writes results/predict_test341.md."""
import random
from collections import Counter, defaultdict

import predict_test298 as V
import rtools as R
import referents as X


def once(objs):
    g = defaultdict(list)
    for t, m in objs:
        g[t].append(m)
    return [(t, Counter(ms).most_common(1)[0][0]) for t, ms in g.items()]


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-forty-first registered predictions: decipherment loop 166, the picture vault with mould copies counted once', 'predict_test341')
    P = X.pools(F, recs)
    pools = {'made': P['made'][1], 'moulded': once(P['moulded'][1])}
    h, n = V.vault2(pools)
    rnd = random.Random(341)
    null = []
    for _ in range(200):
        Q = {}
        for lab, objs in pools.items():
            pics = [m for t, m in objs]
            rnd.shuffle(pics)
            Q[lab] = list(zip([t for t, m in objs], pics))
        null.append(V.vault2(Q)[0])
    med = sorted(null)[100]
    p = (1 + sum(x >= h for x in null)) / 201
    rd.say('- moulded pool %d objects -> %d designs; %d correct of %d predicted (%.1f%%); shuffles median %d, 95th percentile %d; p = %.3f; excess %+d (set 298: +64 on objects).' % (len(P['moulded'][1]), len(pools['moulded']), h, n, 100 * h / max(1, n), med, sorted(null)[189], p, h - med))
    rd.say()
    rd.rec('VD1', 'the vault stays above chance with mould copies counted once (p < 0.05)', 'p = %.3f' % p, p < 0.05)
    rd.rec('VD2', 'its excess is at least set 298\'s +64', 'excess %+d' % (h - med), h - med >= 64)
    rd.rec('VD3', 'progress rule: none (a correction; the lower excess replaces the vault line)', 'VD1 %s' % (p < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
