"""Homophonic substitution solver: simulated annealing over sign->letter maps, scored by a lang/ n-gram model
plus a letter-frequency penalty (HW env, default 1). usage: hsolve.py <tokens file> [restarts] [iters] [model] [order]"""
import sys, os, math, random, collections, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'cyphersolver'))
from lang import lm

def load_tokens(path):
    toks = []
    for line in open(path):
        if not line.strip(): continue
        if ':' in line.split()[0]: line = line.split(':', 1)[1]
        if ']' in line: line = line.split(']')[-1]
        toks += [t.rstrip('?') for t in line.split() if t != '??']
    return toks

def solve(toks, restarts=8, iters=60000, model='la', order=4, seed=0, fixed=None, verbose=True, init=None, T0=3.0):
    M = lm.load(model, order=order, spaces=False)
    A, k = M.A, M.order
    labels = sorted(set(toks)); L = len(labels); li = {s: i for i, s in enumerate(labels)}
    c = np.array([li[t] for t in toks], dtype=np.int64); n = len(c)
    base = os.path.join(HERE, 'cyphersolver/lang')
    spec = json.load(open(os.path.join(base, 'models.json')))[model]
    raw = ''.join(open(os.path.join(base, 'corpora', s + '.txt'), errors='ignore').read()[:2000000] for s in spec['sources'])
    corp = lm.norm(raw, spec['norm'], spaces=False)
    pexp = np.bincount(M.encode(corp), minlength=A) / len(corp) + 1e-4
    W = float(os.environ.get('HW', '1.0'))
    rng = random.Random(seed)
    def score(key):
        x = key[c]
        ctx = np.zeros(n - k + 1, dtype=np.int64)
        for j in range(k): ctx = ctx * A + x[j:n - k + 1 + j]
        po = np.bincount(x, minlength=A) / n + 1e-6
        return float(M.lp[ctx].sum()) - W * n * float((po * np.log(po / pexp)).sum())
    best_all = (-1e18, None)
    common = [M.index[ch] for ch in 'eiatusnromclpdqbfghx' if ch in M.index]
    for r in range(restarts):
        key = np.array([M.index[init[l]] if init and l in init else rng.choice(common) for l in labels], dtype=np.int64)
        if fixed:
            for s, ch in fixed.items():
                if s in li: key[li[s]] = M.index[ch]
        cur = score(key); best = (cur, key.copy())
        for it in range(iters):
            T = T0 * (1 - it / iters) + 0.05
            s = rng.randrange(L)
            if fixed and labels[s] in fixed: continue
            old = key[s]
            if rng.random() < 0.15:
                s2 = rng.randrange(L)
                if fixed and labels[s2] in fixed: continue
                old2 = key[s2]; key[s], key[s2] = old2, old
                new = score(key)
                if new >= cur or rng.random() < math.exp((new - cur) / T): cur = new
                else: key[s], key[s2] = old, old2
            else:
                key[s] = rng.randrange(A); new = score(key)
                if new >= cur or rng.random() < math.exp((new - cur) / T): cur = new
                else: key[s] = old
            if cur > best[0]: best = (cur, key.copy())
        if verbose: print(f'restart {r}: {best[0]/(n-k+1):.3f}', file=sys.stderr)
        if best[0] > best_all[0]: best_all = best
    key = best_all[1]
    return best_all[0] / (n - k + 1), {labels[i]: M.alpha[key[i]] for i in range(L)}, ''.join(M.alpha[i] for i in key[c])

if __name__ == '__main__':
    toks = load_tokens(sys.argv[1]); a = sys.argv[2:]
    sc, key, text = solve(toks, int(a[0]) if a else 8, int(a[1]) if len(a) > 1 else 60000,
                          a[2] if len(a) > 2 else 'la', int(a[3]) if len(a) > 3 else 4)
    print('tokens', len(toks), 'labels', len(key), 'score/char', round(sc, 3)); print(text)
    inv = collections.defaultdict(list)
    for s, ch in key.items(): inv[ch].append(s)
    for ch in sorted(inv): print(ch, ' '.join(sorted(inv[ch])))
