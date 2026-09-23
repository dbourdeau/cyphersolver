"""Homophonic key fit for R2276 under the shared French 5-gram (no spaces).
Every sign maps to one letter (or null); '1' = de and 'n' = et are fixed (Nevers-Piles key)."""
import sys, os, random, math, json, collections
import numpy as np
sys.path.insert(0, '..')
from lang import lm
from decode import load
FIXED = {'1': 'de', 'n': 'et'}
M = lm.load('fr-1530-despatches', spaces=False)
AL = M.alpha            # early alphabet, no j/v
LET = list(AL)

def build(files):
    L = load(files); segs = []
    for name, toks in L:
        cur = []
        for t in toks:
            if t == '...':
                if cur: segs.append(cur); cur = []
            else: cur.append(t)
        if cur: segs.append(cur)
    return L, segs

def plain(segs, k):
    return [''.join(FIXED.get(t) or k[t] for t in s) for s in segs]

def score(segs, k):
    return sum(M.score_idx(M.encode(p)) for p in plain(segs, k) if len(p) > 5)

def anneal(segs, k, free, iters, seed, T0=1.5):
    rnd = random.Random(seed); cur = score(segs, k); best = (cur, dict(k))
    for i in range(iters):
        T = T0 * (1 - i / iters) + 0.05
        s = rnd.choice(free); old = k[s]
        k[s] = rnd.choice(LET)
        new = score(segs, k)
        if new >= cur or rnd.random() < math.exp((new - cur) / T): cur = new
        else: k[s] = old
        if cur > best[0]: best = (cur, dict(k))
    return best

if __name__ == '__main__':
    files = sys.argv[1].split(','); iters = int(sys.argv[2]); runs = int(sys.argv[3])
    init = json.load(open(sys.argv[4], encoding='utf8')) if len(sys.argv) > 4 else {}
    L, segs = build(files)
    syms = sorted({t for s in segs for t in s if t not in FIXED})
    frz = sys.argv[5] if len(sys.argv) > 5 else ''
    free = [s for s in syms if s not in frz.split(',')]
    print('free', free)
    res = []
    for r in range(runs):
        k = {s: init.get(s) if init.get(s) is not None else 'e' for s in syms}
        res.append(anneal(segs, k, free, iters, r))
        print('run', r, round(res[-1][0]), flush=True)
    res.sort(key=lambda x: -x[0]); best = res[0][1]
    n = sum(len(p) for p in plain(segs, best))
    print('best', round(res[0][0]), 'per char', res[0][0] / n)
    for s in syms: print(s, best[s], end=' | ')
    print()
    json.dump(best, open('key_fit.json', 'w'), ensure_ascii=False, indent=0)
    for name, toks in L:
        print(name, ''.join('…' if t == '...' else (FIXED.get(t) or best[t] or '·') for t in toks))
