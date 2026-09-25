"""Two-hundred-and-twenty-fifth registered prediction set (PREDICTIONS.md, TL1-TL3): decipherment loop 50, do tails after a
mid-line ending avoid the head slot in F's extra lines (set 223's A finding)? Writes results/predict_test225.md."""
import random
from collections import Counter

import rtools as R
from predict_test223 import tail
from signs import load


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-twenty-fifth registered predictions: decipherment loop 50, the post-name tail on F', 'predict_test225')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    DF = sorted({tuple(ln) for r in F for ln in r['seq'] if ln} - set(DA) - set(DB))
    occ = Counter(g for t in DA for g in t)
    hd = Counter(t[i - 1] for t in DA for i, g in enumerate(t) if g in R.END and i > 0)
    prop = lambda g: hd[g] / occ[g] if occ[g] else 0.0
    tok = Counter(g for t in DA + DB + DF for g in t)
    ranked = sorted(tok, key=tok.get)
    band = {g: ranked[max(0, i - 10):i + 11] for i, g in enumerate(ranked)}
    ts = [x for x in (tail(t) for t in DF) if x]
    rd.say('- F extra lines %d; tails %d.' % (len(DF), len(ts)))
    rd.say()

    def low(signs, seed):
        obs = sum(map(prop, signs)) / max(1, len(signs))
        rnd = random.Random(seed)
        le = sum(sum(prop(rnd.choice(band[g])) for g in signs) / max(1, len(signs)) <= obs for _ in range(1000))
        return obs, (le + 1) / 1001
    o1, p1 = low([x[-1] for x in ts], 225)
    rd.rec('TL1', 'tail last signs avoid the head slot (F)', 'mean head propensity %.3f of %d; lower-tail p = %.4f' % (o1, len(ts), p1), p1 < 0.05)
    o2, p2 = low([g for x in ts for g in x], 226)
    rd.rec('TL2', 'all tail signs (F)', 'mean %.3f; p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('TL3', 'progress rule', 'TL1 %s' % (p1 < 0.05), p1 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
