"""Faster homophonic annealer with incremental n-gram scoring (R8499)."""
import os, sys, re, random, collections, json, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
from solve import runs, FIXED

HERE = os.path.dirname(os.path.abspath(__file__))
_M = {}


def model(order):
    if order not in _M:
        m = lm.load('en-1640s', order=order, spaces=False)
        txt0 = lm.norm(open(os.path.join(HERE, '..', 'lang', 'corpora', 'en-1640s-history.txt'), encoding='utf8',
                            errors='replace').read()[:3000000], 'early', spaces=False)
        fx = m.encode(txt0)
        _M[order] = (m, np.bincount(fx, minlength=m.A) / len(fx))
    return _M[order]


def build(R, m, fixed=FIXED, pinned=None):
    types = sorted({t for r in R for t in r if t not in fixed})
    ti = {t: i for i, t in enumerate(types)}
    x, owner, seg = [], [], []
    for si, r in enumerate(R):
        for t in r:
            if t in fixed:
                for ch in fixed[t]:
                    x.append(m.index[ch]); owner.append(-1); seg.append(si)
            else:
                x.append(0); owner.append(ti[t]); seg.append(si)
    return types, ti, np.array(x), np.array(owner), np.array(seg)


def anneal(R, seed=0, iters=300000, order=4, W=0.5, T0=None, T1=None, init=None, pinned=None, quiet=True):
    m, fexp = model(order)
    A, lp, k = m.A, m.lp, order
    types, ti, x, owner, seg = build(R, m)
    n = len(x)
    # windows: start positions s such that s..s+k-1 in same segment
    starts = np.array([s for s in range(n - k + 1) if seg[s] == seg[s + k - 1]])
    wmask = np.zeros(n, bool); wmask[starts] = True
    # per type: affected window starts
    occ = [np.where(owner == i)[0] for i in range(len(types))]
    aff = []
    for p in occ:
        s = set()
        for q in p:
            for d in range(k):
                if q - d >= 0 and wmask[q - d]: s.add(q - d)
        aff.append(np.array(sorted(s), dtype=np.int64))
    pw = A ** np.arange(k - 1, -1, -1)
    offs = np.arange(k)
    rng = random.Random(seed)
    key = np.array([rng.randrange(A) for _ in types]) if init is None else np.array(init)
    if pinned:
        for t, ch in pinned.items():
            if t in ti: key[ti[t]] = m.index[ch]
    free = [i for i, t in enumerate(types) if not pinned or t not in pinned]
    mask = owner >= 0
    x[mask] = key[owner[mask]]
    N = n
    cnt = np.bincount(x, minlength=A).astype(float)
    E = N * fexp + 1e-3
    def pen(c): return float(((c - E) ** 2 / E).sum())
    def win(a): return lp[(x[a[:, None] + offs] * pw).sum(1)].sum()
    lm_total = float(lp[(x[starts[:, None] + offs] * pw).sum(1)].sum())
    cur = lm_total - W * pen(cnt)
    best = (cur, key.copy())
    nch = len(starts)
    T0 = T0 if T0 is not None else 0.02 * nch / 100 * 10
    T1 = T1 if T1 is not None else 0.05
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        i = free[rng.randrange(len(free))]
        old = key[i]; new = rng.randrange(A - 1); new += new >= old
        a = aff[i]; p = occ[i]
        before = win(a)
        x[p] = new
        after = win(a)
        c2 = cnt.copy(); c2[old] -= len(p); c2[new] += len(p)
        d = (after - before) - W * (pen(c2) - pen(cnt))
        if d >= 0 or rng.random() < math.exp(d / T):
            key[i] = new; cnt = c2; cur += d
            if cur > best[0]: best = (cur, key.copy())
        else:
            x[p] = old
    key = best[1]
    x[mask] = key[owner[mask]]
    out, last = [], None
    for v, s in zip(x, seg):
        if last is not None and s != last: out.append(' ')
        out.append(m.alpha[v]); last = s
    return best[0], {t: m.alpha[key[ti[t]]] for t in types}, ''.join(out)


if __name__ == '__main__':
    seed = int(sys.argv[1]); it = int(sys.argv[2])
    s, key, txt = anneal(runs(), seed, it)
    print(s); print(txt[:2000])
    json.dump({'score': float(s), 'key': key, 'text': txt}, open(os.path.join(HERE, f'run2_{seed}.json'), 'w'))
