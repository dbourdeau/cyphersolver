"""Three-hundred-and-twenty-fourth registered prediction set (PREDICTIONS.md, VB1-VB2): decipherment loop 149, a
back-off picture vault: set 298's loose unit kinds vote first (own pool, then the other pool); a tablet they leave
without a vote takes the votes of set 323's tier 1 configuration (own pool, then the other). Excess of correct
predictions over the shuffle median (set 298: +64). Writes results/predict_test324.md."""
import random

import predict_test298 as L
import predict_test323 as T
import rtools as R
import referents as X


def vault(pools):
    occL = {lab: L.index(objs) for lab, objs in pools.items()}
    occT = {lab: T.index(objs) for lab, objs in pools.items()}
    h = n = 0
    for lab, objs in pools.items():
        other = [o for o in pools if o != lab][0]
        for t, m in objs:
            v = (L.votes_for(t, occL[lab]) or L.votes_for(t, occL[other]) or T.votes(t, occT[lab]) or T.votes(t, occT[other]))
            if v:
                n += 1
                h += sorted(v.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] == m
    return h, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-twenty-fourth registered predictions: decipherment loop 149, a back-off picture vault', 'predict_test324')
    P = {lab: both for lab, (clean, both) in X.pools(F, recs).items()}
    h, n = vault(P)
    rnd = random.Random(324)
    null = []
    for _ in range(200):
        Q = {}
        for lab, objs in P.items():
            pics = [m for t, m in objs]
            rnd.shuffle(pics)
            Q[lab] = list(zip([t for t, m in objs], pics))
        null.append(vault(Q)[0])
    med = sorted(null)[100]
    p = (1 + sum(x >= h for x in null)) / 201
    rd.say('- %d correct of %d predicted (%.1f%%); shuffles median %d, 95th percentile %d; p = %.3f (set 298: 70 of 295, excess +64).' % (h, n, 100 * h / max(1, n), med, sorted(null)[189], p))
    rd.say()
    ex = h - med
    rd.rec('VB1', 'excess over the shuffle median above +64, p < 0.05', 'excess %+d, p = %.3f' % (ex, p), ex > 64 and p < 0.05)
    rd.rec('VB2', 'progress rule: VB1 (the tier 3 vault line rises)', 'VB1 %s' % (ex > 64 and p < 0.05), ex > 64 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
