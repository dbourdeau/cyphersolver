"""Homophonic annealer (symbol -> Latin letter, optional nulls), Latin n-gram from lang/ plus a
letter-frequency (chi-square) term, because the shared 'la' model scores runs like 'iiii' too well."""
import sys, os, numpy as np, numba
sys.path.insert(0, r'C:\Users\dbour\cypher')
from lang import lm

ORDER = int(os.environ.get('ORDER', '5'))
M = lm.load('la', order=ORDER, spaces=False)
LP = M.lp.astype(np.float32); A = M.A; ALPHA = M.alpha
_c = lm.norm(open(r'C:\Users\dbour\cypher\lang\corpora\la-gutenberg.txt', encoding='latin-1').read()[:3000000],
             'latin', spaces=False)
FREQ = np.array([_c.count(a) for a in ALPHA], float); FREQ /= FREQ.sum()


@numba.njit(cache=True)
def score(seq, key, LP, A, K, buf):
    n = 0; tot = 0.0
    for i in range(seq.shape[0]):
        s = seq[i]
        if s < 0:
            n = 0; continue
        c = key[s]
        if c >= A: continue
        buf[n] = c; n += 1
        if n >= K:
            idx = 0
            for j in range(n - K, n):
                idx = idx * A + buf[j]
            tot += LP[idx]
    return tot


@numba.njit(cache=True)
def fpen(key, cnt, A, freq, w):
    lc = np.zeros(A + 1)
    N = 0.0
    for s in range(key.shape[0]):
        lc[key[s]] += cnt[s]
    for a in range(A):
        N += lc[a]
    p = 0.0
    for a in range(A):
        e = freq[a] * N + 0.5
        p += (lc[a] - e) ** 2 / e
    return -w * p


@numba.njit(cache=True)
def anneal(seq, nsym, LP, A, K, iters, T0, pnull, nullpen, fixed, init, seed, freq, w):
    np.random.seed(seed)
    buf = np.zeros(seq.shape[0] + 5, np.int64)
    key = np.random.randint(0, A, nsym)
    for s in range(nsym):
        if init[s] >= 0: key[s] = init[s]
        if fixed[s] >= 0: key[s] = fixed[s]
    cnt = np.zeros(nsym, np.int64)
    for s in seq:
        if s >= 0: cnt[s] += 1

    def total(key):
        t = score(seq, key, LP, A, K, buf) + fpen(key, cnt, A, freq, w)
        for s in range(nsym):
            if key[s] == A: t -= nullpen * cnt[s]
        return t
    cur = total(key)
    best = cur; bkey = key.copy()
    for it in range(iters):
        T = T0 * (1.0 - it / iters) + 0.05
        s = np.random.randint(0, nsym)
        if fixed[s] >= 0: continue
        old = key[s]
        if np.random.random() < pnull:
            new = A
        else:
            new = np.random.randint(0, A)
        if new == old: continue
        key[s] = new
        sc = total(key)
        d = sc - cur
        if d > 0 or np.random.random() < np.exp(d / T):
            cur = sc
            if cur > best:
                best = cur; bkey = key.copy()
        else:
            key[s] = old
    return best, bkey


def decode(seq, key):
    out = []
    for s in seq:
        if s < 0: out.append('|'); continue
        c = key[s]; out.append('_' if c >= A else ALPHA[c])
    return ''.join(out)
