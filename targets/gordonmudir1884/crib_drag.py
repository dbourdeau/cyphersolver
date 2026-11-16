"""Crib dragging for the last four groups of the note (38 75 34 49), calibrated against random cribs.

    python crib_drag.py [--words N] [--restarts N] [--iters N]

The four groups stand right after the clear words "he did not give them" (closing line 1), so the plaintext there is
probably a noun. For each of the N commonest Arabic four-letter words with four distinct letters (from
lang/corpora/ar-wikipedia-sample.txt) the key entries of 38, 75, 34 and 49 are fixed to that word's letters and the
other 22 symbols are optimised under the trigram model of crib_attack.py. The score is the best total log-probability
over the restarts. The same procedure is run for N random four-letter strings. A real crib helps only if it scores well
above the random cribs, and then only if the rest of the decode begins to read.
"""
import math, os, random, re, sys
from collections import Counter

import numpy as np

import analysis as A
import crib_attack as C

L = A.LETTERS
IDX = C.IDX


def words(minfreq=20):
    t = open(os.path.join(A.ROOT, 'lang', 'corpora', 'ar-wikipedia-sample.txt'), encoding='utf-8').read()
    t = ''.join(A.FOLD.get(c, c) for c in t)
    cnt = Counter(re.findall('[' + L + ']+', t))
    return [(w, k) for w, k in cnt.most_common() if len(w) == 4 and len(set(w)) == 4 and k >= minfreq]


def anneal_locked(cipher, nsym, rng, iters, lock):
    n = len(L)
    locked = set(lock)
    free_syms = [s for s in range(nsym) if s not in locked]
    pool = [x for x in range(n) if x not in set(lock.values())]
    cipher = np.asarray(cipher)
    key = np.zeros(nsym, dtype=int)
    for s, l in lock.items(): key[s] = l
    for s, l in zip(free_syms, rng.sample(pool, len(free_syms))): key[s] = l
    cur = C.seq_score(key[cipher]); best = cur; bestkey = key.copy()
    T0, T1 = 3.0, 0.05
    for it in range(iters):
        temp = T0 * (T1 / T0) ** (it / iters)
        k2 = key.copy()
        if rng.random() < 0.7:
            a, b = rng.sample(free_syms, 2); k2[a], k2[b] = k2[b], k2[a]
        else:
            a = rng.choice(free_syms); used = set(k2.tolist())
            k2[a] = rng.choice([x for x in range(n) if x not in used])
        s = C.seq_score(k2[cipher])
        if s >= cur or rng.random() < math.exp((s - cur) / temp):
            key, cur = k2, s
            if cur > best: best, bestkey = cur, key.copy()
    return best, bestkey


def main():
    nw = int(sys.argv[sys.argv.index('--words') + 1]) if '--words' in sys.argv else 400
    restarts = int(sys.argv[sys.argv.index('--restarts') + 1]) if '--restarts' in sys.argv else 4
    iters = int(sys.argv[sys.argv.index('--iters') + 1]) if '--iters' in sys.argv else 8000
    rng = random.Random(11)
    g = A.groups(); syms = sorted(set(g)); sidx = {s: i for i, s in enumerate(syms)}
    cipher = [sidx[v] for v in g]
    target = [sidx[v] for v in ('38', '75', '34', '49')]
    cands = [w for w, _ in words()][:nw]
    f, _ = A.arabic_freq()
    pl = np.array([f[c] for c in L]); pl = pl / pl.sum()

    def run(word_idx):
        lock = dict(zip(target, word_idx))
        return max(anneal_locked(cipher, len(syms), rng, iters, lock) for _ in range(restarts)), lock

    real = []
    for w in cands:
        (s, k), _ = run([IDX[c] for c in w]); real.append((s, w, k))
    nulls = []
    for _ in range(len(cands)):
        while True:
            ix = list(np.random.default_rng(rng.randrange(10 ** 9)).choice(len(L), 4, replace=False, p=pl))
            if len(set(ix)) == 4: break
        (s, k), _ = run(ix); nulls.append((s, ''.join(L[i] for i in ix), k))
    rs = np.array([x[0] for x in real]); ns = np.array([x[0] for x in nulls])
    print(f'{len(cands)} real cribs: mean {rs.mean():.1f} sd {rs.std():.1f} max {rs.max():.1f}')
    print(f'{len(nulls)} random cribs: mean {ns.mean():.1f} sd {ns.std():.1f} max {ns.max():.1f}')
    print(f'real cribs above the best random crib: {int((rs > ns.max()).sum())}; above the random 95th percentile: '
          f'{int((rs > np.percentile(ns, 95)).sum())} (about {len(rs) // 20} expected by chance)')
    print('\ntop real cribs:')
    for s, w, k in sorted(real, reverse=True)[:12]:
        m = {sy: L[x] for sy, x in zip(syms, k)}
        print(f'  {s:7.1f}  {w}   decode: {"".join(m[v] for v in g)}')


if __name__ == '__main__':
    main()
