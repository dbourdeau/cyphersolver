"""Two-hundred-and-ninetieth registered prediction set (PREDICTIONS.md, VH1-VH3): decipherment loop 115, the picture
vault (set 289) scored by the number of correct predictions against 200 shuffles, with a Linear B control: each DAMOS
line's ideogram predicted from its words, units learned from the other lines without copies of the same word list
(same criterion: 2+ lines, 2+ distinct word lists, 67%+ one ideogram). Writes results/predict_test290.md."""
import random
from collections import Counter, defaultdict

import rtools as R
import referents as X
from predict_test234 import lines
from predict_test289 import vault


def lb_vault(ls):
    occ = defaultdict(list)
    for ws, i in ls:
        for w in set(ws):
            occ[w].append((ws, i))
    hits = 0
    for ws, i in ls:
        votes = Counter()
        for w in set(ws):
            rest = [(u, x) for u, x in occ[w] if u != ws]
            if len(rest) < 2 or len({tuple(u) for u, x in rest}) < 2:
                continue
            lab = X.ok([x for u, x in rest], 2, 0.67)
            if lab:
                votes[lab] += 1
        if votes:
            hits += sorted(votes.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] == i
    return hits


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-ninetieth registered predictions: decipherment loop 115, the picture vault by correct predictions, with a Linear B control', 'predict_test290')
    P = X.pools(F, recs)
    real = sum(vault(both)[0] for clean, both in P.values())
    rnd = random.Random(290)
    null = []
    for _ in range(200):
        tot = 0
        for clean, both in P.values():
            pics = [m for t, m in both]
            rnd.shuffle(pics)
            tot += vault(list(zip([t for t, m in both], pics)))[0]
        null.append(tot)
    p = (1 + sum(x >= real for x in null)) / 201
    rd.say('- Indus: %d correct predictions; shuffles median %d, 95th percentile %d; p = %.3f.' % (real, sorted(null)[100], sorted(null)[189], p))
    ls = [(tuple(ws), i) for ws, i in lines()]
    lreal = lb_vault(ls)
    lnull = []
    for _ in range(20):
        ids = [i for ws, i in ls]
        rnd.shuffle(ids)
        lnull.append(lb_vault(list(zip([ws for ws, i in ls], ids))))
    lp = (1 + sum(x >= lreal for x in lnull)) / 21
    rd.say('- Linear B: %d of %d lines right; shuffles median %d, max %d; p = %.3f.' % (lreal, len(ls), sorted(lnull)[10], max(lnull), lp))
    rd.say()
    rd.rec('VH1', 'Indus: correct predictions above the 95th percentile of 200 shuffles', 'p = %.3f' % p, p < 0.05)
    rd.rec('VH2', 'Linear B control: correct predictions above all 20 shuffles', 'p = %.3f' % lp, lreal > max(lnull))
    rd.rec('VH3', 'progress rule: VH1 and VH2 (tier 3 picture-vault line)', 'VH1 %s, VH2 %s' % (p < 0.05, lreal > max(lnull)), p < 0.05 and lreal > max(lnull))
    rd.finish()


if __name__ == '__main__':
    main()
