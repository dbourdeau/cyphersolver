"""Monotone (alphabetical-range) key search for the 2-digit letter cipher.

Hypothesis: the table gives each letter a block of consecutive numbers in alphabetical order (a lowest).
Search the block boundaries by annealing on a German no-space n-gram model (lang/).
usage: python monotone.py [model] [alphabet] [restarts]
"""
import json, os, sys, random, math
import numpy as np
sys.path.insert(0, r'C:/Users/dbour/cypher')
from lang import lm
from solve import load_runs

def main():
    model = sys.argv[1] if len(sys.argv) > 1 else 'de-1740s'
    ALPH = sys.argv[2] if len(sys.argv) > 2 else 'abcdefghiklmnopqrstuwxyz'
    restarts = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    M = lm.load(model, order=5, spaces=False)
    runs = load_runs()
    LO, HI = 1, 84
    R = [np.array([int(x) for x in r]) for r in runs]
    HI = max(int(x) for r in runs for x in r) + 1
    aidx = np.array([M.index[c] for c in ALPH])
    K = len(ALPH)

    def key_from(bounds):
        # bounds: sorted K-1 cut points; number n -> letter index = count of cuts <= n
        lut = np.searchsorted(np.array(bounds), np.arange(HI + 1), side='right')
        return aidx[lut]

    def score(bounds):
        lut = key_from(bounds)
        return sum(M.score_idx(lut[r]) for r in R)

    best_all = None
    for rs in range(restarts):
        rng = random.Random(rs)
        b = sorted(rng.sample(range(LO + 1, HI), K - 1))
        cur = score(b); best = (cur, b[:])
        iters = 30000
        for it in range(iters):
            T = 15 * (1 - it / iters) + 0.05
            nb = b[:]
            i = rng.randrange(K - 1)
            nb[i] += rng.choice([-3, -2, -1, 1, 2, 3])
            nb.sort()
            if nb[0] <= LO or nb[-1] >= HI or len(set(nb)) < len(nb): continue
            s = score(nb)
            if s >= cur or rng.random() < math.exp((s - cur) / T):
                b, cur = nb, s
                if cur > best[0]: best = (cur, b[:])
        print(rs, round(best[0], 1), list(zip(ALPH[1:], best[1])), flush=True)
        if best_all is None or best[0] > best_all[0]: best_all = best
    lut = key_from(best_all[1])
    print(' | '.join(''.join(M.alpha[c] for c in lut[r]) for r in R))

if __name__ == '__main__':
    main()
