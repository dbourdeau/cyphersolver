"""Faster homophonic annealer (incremental n-gram deltas) for the Rangone cipher.

python solve2.py RESTARTS ITERS [fixed.json] ; env CHIW (freq penalty weight), NULLS=1 allows '.' for rare signs,
OUT=result file. fixed.json maps sign -> letter (or '.' for null) and pins it.
"""
import os, sys, json, math, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
from solve import load_segments

HERE = os.path.dirname(os.path.abspath(__file__))
LETTERS = 'abcdefghilmnopqrstuz'
FREQ = dict(a=.117, b=.009, c=.045, d=.037, e=.118, f=.011, g=.016, h=.015, i=.113, l=.065, m=.025, n=.069,
            o=.098, p=.030, q=.005, r=.064, s=.050, t=.056, u=.030, z=.008)


def build(segs, m):
    types = sorted({t for s in segs for t in s})
    ti = {t: i for i, t in enumerate(types)}
    K = m.order
    wins = []          # each window: K type indices
    for s in segs:
        x = [ti[t] for t in s]
        for a in range(len(x) - K + 1):
            wins.append(x[a:a + K])
    wins = np.array(wins, dtype=np.int64)
    per = [np.where((wins == i).any(1))[0] for i in range(len(types))]
    cnt = np.bincount(np.array([ti[t] for s in segs for t in s]), minlength=len(types))
    return types, ti, wins, per, cnt


def main():
    R = int(sys.argv[1]); IT = int(sys.argv[2])
    fixed = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else {}
    m = lm.load('it-cinquecento', order=5, spaces=False)
    A, K = m.A, m.order
    segs = load_segments()
    types, ti, wins, per, cnt = build(segs, m)
    nT = len(types)
    powv = A ** np.arange(K - 1, -1, -1)
    lp = m.lp.astype(np.float64)
    W = float(os.environ.get('CHIW', '1.0'))
    N = cnt.sum()
    E = np.full(A, 0.3)
    for c, f in FREQ.items():
        E[m.index[c]] = f * N
    Lidx = [m.index[c] for c in LETTERS]

    def lmscore(key, idx=None):
        w = wins if idx is None else wins[idx]
        return lp[(key[w] * powv).sum(1)].sum()

    def chi(n):
        return W * (((n - E) ** 2) / (E + 2)).sum()

    free = [i for i, t in enumerate(types) if t not in fixed]
    out = []
    for r in range(R):
        seed = json.load(open(os.environ['SEED'])) if os.environ.get('SEED') else None
        if seed:
            key = np.array([m.index[fixed.get(t, seed.get(t, 'e'))] for t in types], dtype=np.int64)
            for _ in range(int(os.environ.get('PERT', '5'))):
                i = free[random.randrange(len(free))]; key[i] = random.choice(Lidx)
        else:
            key = np.array([m.index[fixed[t]] if t in fixed else random.choice(Lidx) for t in types], dtype=np.int64)
        n = np.bincount(key, weights=cnt, minlength=A)
        cur_lm = lmscore(key); cur = cur_lm - chi(n)
        best = cur; bk = key.copy()
        T0, T1 = float(os.environ.get('T0','3.0')), 0.1
        for it in range(IT):
            T = T0 * (T1 / T0) ** (it / IT)
            i = free[random.randrange(len(free))]
            old = key[i]; new = Lidx[random.randrange(20)]
            if new == old:
                continue
            idx = per[i]
            before = lmscore(key, idx)
            key[i] = new
            after = lmscore(key, idx)
            n2 = n.copy(); n2[old] -= cnt[i]; n2[new] += cnt[i]
            cand = cur_lm - before + after - chi(n2)
            if cand >= cur or random.random() < math.exp((cand - cur) / T):
                cur_lm += after - before; cur = cand; n = n2
                if cur > best:
                    best = cur; bk = key.copy()
            else:
                key[i] = old
        nw = len(wins)
        dec = ' | '.join(''.join(m.alpha[c] for c in bk[[ti[t] for t in s]]) for s in segs)
        out.append((best / nw, lmscore(bk) / nw, dec, {t: m.alpha[bk[ti[t]]] for t in types}))
        print('%3d %.3f lm %.3f %s' % (r, best / nw, lmscore(bk) / nw, dec), flush=True)
    out.sort(key=lambda z: -z[0])
    json.dump(out, open(os.path.join(HERE, os.environ.get('OUT', 'sa2_best.json')), 'w'), indent=0)


if __name__ == '__main__':
    main()
