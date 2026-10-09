"""Homophonic annealer on the letter runs of Trevor 1645 (R8433), optional cribs. Exploratory: 54 letter groups only."""
import os, sys, random, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
M = lm.load('en-1640s', order=4, spaces=False)
RUNS = [[25,45,5,15,22,41,4,11,57,32], [75], [76,33,44,32,21], [26,50,30,12,45,7,32,67,5], [6,22,45,4,54],
        [67,24,43,9,31,52,39], [27,37,25], [22,45,8,32,46,69], [45,39,37,45,17,16,44,12,67]]
SYM = sorted({s for r in RUNS for s in r})
AL = 'abcdefghiklmnopqrstuwxy'
FREQ = 'eeeeeeettttttaaaaaooooooiiiinnnnnssssshhhhhrrrrrddddlllcccuuummwwfggyypbbk'
def score(K):
    return sum(M.score(''.join(K[s] for s in r)) for r in RUNS)
def solve(fixed, iters=60000, seed=0):
    rnd = random.Random(seed)
    K = {s: rnd.choice(FREQ) for s in SYM}; K.update(fixed)
    free = [s for s in SYM if s not in fixed]
    cur = score(K); best = (cur, dict(K)); T = 3.0
    for i in range(iters):
        s = rnd.choice(free); old = K[s]; K[s] = rnd.choice(AL)
        n = score(K)
        if n > cur or rnd.random() < math.exp((n-cur)/T): cur = n
        else: K[s] = old
        if cur > best[0]: best = (cur, dict(K))
        T = max(0.2, 3.0*(1-i/iters))
    return best
if __name__ == '__main__':
    crib = sys.argv[1] if len(sys.argv) > 1 else ''
    fixed = {}
    if crib: fixed = dict(zip(RUNS[5], crib))
    for seed in range(4):
        sc, K = solve(fixed, seed=seed)
        print(round(sc,1), ' | '.join(''.join(K[s] for s in r) for r in RUNS))
