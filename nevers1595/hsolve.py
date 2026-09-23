"""Fast homophonic-substitution annealer with incremental n-gram scoring.

usage: python hsolve.py MODE [restarts] [iters]      (MODE as in anneal.py: glyph, pair, pairall, prefix1, n65 ...)
env:   CTFILES=a.txt,b.txt   ORDER=5   T0=...   SEED=...

Each unit type gets one plaintext letter; a move reassigns one unit (or swaps two), and only the n-gram windows that
touch that unit's occurrences are rescored.  Runs are scored separately (no n-gram spans a run boundary).
Prints the best decryption of every run and the key.
"""
import os, sys, math, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
from anneal import runs

mode = sys.argv[1] if len(sys.argv) > 1 else 'glyph'
restarts = int(sys.argv[2]) if len(sys.argv) > 2 else 4
iters = int(sys.argv[3]) if len(sys.argv) > 3 else 400000
K = int(os.environ.get('ORDER', '5'))
random.seed(int(os.environ.get('SEED', '1')))
m = lm.load('fr-1600-letters', order=K, spaces=False)
A = m.A; lp = m.lp
R = runs(mode)
units = sorted({u for r in R for u in r}); ui = {u: i for i, u in enumerate(units)}; U = len(units)
# concatenated stream; window starts valid only inside a run
seq = []; valid = []
for r in R:
    for j, u in enumerate(r):
        seq.append(ui[u]); valid.append(j <= len(r) - K)
seq = np.array(seq); valid = np.array(valid); N = len(seq)
starts_all = np.nonzero(valid)[0]
occ = [np.nonzero(seq == u)[0] for u in range(U)]
aff = []
for u in range(U):
    s = set()
    for p in occ[u]:
        for st in range(p - K + 1, p + 1):
            if 0 <= st < N and valid[st]: s.add(st)
    aff.append(np.array(sorted(s), dtype=np.int64))
powers = A ** np.arange(K - 1, -1, -1)
offs = np.arange(K)
letters = [c for c in m.alpha]
common = [m.index[c] for c in 'eeeeaaiinnssttrruuoolldcmp']

FR = {'a': .08, 'b': .01, 'c': .033, 'd': .038, 'e': .16, 'f': .012, 'g': .009, 'h': .008, 'i': .07, 'l': .055,
      'm': .03, 'n': .072, 'o': .052, 'p': .028, 'q': .014, 'r': .065, 's': .082, 't': .07, 'u': .068, 'x': .004,
      'y': .004, 'z': .002}
exp = np.full(A, 0.0005)
for c, f in FR.items(): exp[m.index[c]] = f
exp = exp / exp.sum() * N
W = float(os.environ.get('W', '1.0'))
cnt_u = np.array([len(o) for o in occ])
def penalty(counts):
    return W * float((((counts - exp) ** 2) / (exp + 2)).sum())

def wscore(pt, st):
    if len(st) == 0: return 0.0
    idx = pt[st[:, None] + offs[None, :]] @ powers
    return float(lp[idx].sum())

best_all = None
for rs in range(restarts):
    key = np.array([random.choice(common) for _ in range(U)])
    pt = key[seq]
    counts = np.bincount(pt, minlength=A).astype(float)
    cur = wscore(pt, starts_all) - penalty(counts)
    best = (cur, key.copy())
    T0 = float(os.environ.get('T0', '12'))
    for it in range(iters):
        T = T0 * (1 - it / iters) + 0.2
        if random.random() < 0.8:
            u = random.randrange(U); old = key[u]; new = random.randrange(A)
            if new == old: continue
            st = aff[u]
            before = wscore(pt, st) - penalty(counts)
            key[u] = new; pt[occ[u]] = new
            counts[old] -= cnt_u[u]; counts[new] += cnt_u[u]
            d = wscore(pt, st) - penalty(counts) - before
            if d >= 0 or random.random() < math.exp(d / T):
                cur += d
            else:
                key[u] = old; pt[occ[u]] = old
                counts[new] -= cnt_u[u]; counts[old] += cnt_u[u]
        else:
            u, v = random.randrange(U), random.randrange(U)
            if key[u] == key[v]: continue
            st = np.union1d(aff[u], aff[v])
            before = wscore(pt, st) - penalty(counts)
            a, b = key[u], key[v]
            key[u], key[v] = b, a; pt[occ[u]] = b; pt[occ[v]] = a
            counts[a] += cnt_u[v] - cnt_u[u]; counts[b] += cnt_u[u] - cnt_u[v]
            d = wscore(pt, st) - penalty(counts) - before
            if d >= 0 or random.random() < math.exp(d / T):
                cur += d
            else:
                key[u], key[v] = a, b; pt[occ[u]] = a; pt[occ[v]] = b
                counts[a] -= cnt_u[v] - cnt_u[u]; counts[b] -= cnt_u[u] - cnt_u[v]
        if cur > best[0]: best = (cur, key.copy())
    print(f'restart {rs}: {best[0] / len(starts_all):.3f}/window', flush=True)
    if best_all is None or best[0] > best_all[0]: best_all = best
key = best_all[1]
print('best', best_all[0] / len(starts_all))
for r in R:
    print(''.join(letters[key[ui[u]]] for u in r))
from collections import Counter
c = Counter(u for r in R for u in r)
print(' '.join(f'{u}={letters[key[ui[u]]]}({c[u]})' for u in sorted(units, key=lambda u: -c[u])))
