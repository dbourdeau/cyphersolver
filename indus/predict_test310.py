"""Three-hundred-and-tenth registered prediction set (PREDICTIONS.md, LP1-LP3): decipherment loop 135, the split-half
precision of the referent method on Linear B, as a yardstick for the Indus figure (set 309: C0 44%, C7 23%). DAMOS lines
(words, first ideogram); five random half-splits of the distinct word lists (seeds 3101-3105), both directions; units =
words qualifying at 3+ lines / 80%+ (C0-like) and at 2+ lines / 67%+ (C1-like), 2+ distinct word lists; held-out
precision = share of (word, held-out line) matches whose ideogram is the word's label. Writes results/predict_test310.md."""
import random
from collections import defaultdict

import rtools as R
import referents as X
from predict_test234 import lines


def learn(ls, k, s):
    occ, texts = defaultdict(list), defaultdict(set)
    for ws, i in ls:
        for w in set(ws):
            occ[w].append(i)
            texts[w].add(ws)
    return {w: m for w, ii in occ.items() if len(texts[w]) >= 2 for m in [X.ok(ii, k, s)] if m}


def main():
    rd = R.Round('Three-hundred-and-tenth registered predictions: decipherment loop 135, split-half precision of the referent method on Linear B', 'predict_test310')
    ls = [(tuple(ws), i) for ws, i in lines()]
    res = {}
    for name, k, s in (('C0-like (3+, 80%)', 3, 0.8), ('C1-like (2+, 67%)', 2, 0.67)):
        right = tot = 0
        for seed in range(3101, 3106):
            rnd = random.Random(seed)
            wl = sorted({ws for ws, i in ls})
            rnd.shuffle(wl)
            a = set(wl[:len(wl) // 2])
            H1 = [x for x in ls if x[0] in a]
            H2 = [x for x in ls if x[0] not in a]
            for L, T in ((H1, H2), (H2, H1)):
                u = learn(L, k, s)
                for ws, i in T:
                    for w in set(ws):
                        if w in u:
                            tot += 1
                            right += u[w] == i
        res[name] = (right, tot)
        rd.say('- %s: %d of %d held-out matches right (%.0f%%).' % (name, right, tot, 100 * right / max(1, tot)))
    rd.say()
    a, b = res['C0-like (3+, 80%)'], res['C1-like (2+, 67%)']
    pa, pb = a[0] / max(1, a[1]), b[0] / max(1, b[1])
    rd.rec('LP1', 'Linear B C0-like held-out precision is above the Indus C0 figure (44%)', '%.0f%%' % (100 * pa), pa > 0.44)
    rd.rec('LP2', 'Linear B C1-like precision is above the Indus C1 figure (28%)', '%.0f%%' % (100 * pb), pb > 0.28)
    rd.rec('LP3', 'progress rule: none (a yardstick for the Indus precision)', 'LB %.0f%% / %.0f%% against Indus 44%% / 28%%' % (100 * pa, 100 * pb), False)
    rd.finish()


if __name__ == '__main__':
    main()
