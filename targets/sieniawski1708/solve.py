"""Homophonic annealer for the 2-digit letter cipher of the Vienna -> Schenck letters.

Each run from runs.json is scored separately with a German no-space n-gram model (lang/), with word-boundary
context: the run is scored as ' ' + text + ' ' using the spaced model, and inner spaces are not allowed (runs may
hold several words, so we also try the no-space model).  Many-to-one key, annealed with a unigram prior so that the
letter distribution stays German-like.

usage: python solve.py [model] [restarts] [iters]   (fixed=sym:letter,... optional env FIX)
"""
import json, os, sys, random, math, collections
import numpy as np
sys.path.insert(0, r'C:/Users/dbour/cypher')
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))
SKIP = {('17', '06'), ('16', '01'), ('16', '04')}

def load_runs():
    R = json.load(open(os.path.join(HERE, 'runs.json'), encoding='utf-8'))
    out = []
    for r in R:
        seq = [x for x in r['nums'] if x != '.' and not x.startswith('0')]
        if len(seq) < 2: continue
        if tuple(seq) in SKIP: continue
        out.append(seq)
    return out

def main():
    model = sys.argv[1] if len(sys.argv) > 1 else 'de-1740s'
    restarts = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else 200000
    M = lm.load(model, order=5, spaces=False)
    alpha = M.alpha
    runs = load_runs()
    syms = sorted({s for r in runs for s in r})
    si = {s: i for i, s in enumerate(syms)}
    R = [np.array([si[s] for s in r]) for r in runs]
    # unigram German frequencies from the model order-1 marginal is not exposed; use fixed table
    freq = dict(e=.165, n=.098, i=.075, r=.07, s=.068, t=.06, a=.058, h=.048, d=.047, u=.04, l=.035, c=.03,
                g=.03, m=.026, o=.025, b=.019, w=.018, f=.016, k=.012, z=.011, p=.008, v=.008, j=.002, y=.002,
                x=.001, q=.0005)
    lf = np.array([math.log(freq.get(c, 1e-4)) for c in alpha])
    counts = collections.Counter(s for r in runs for s in r)
    N = sum(counts.values())
    cnt = np.array([counts[s] for s in syms])
    fix = {}
    for kv in os.environ.get('FIX', '').split(','):
        if ':' in kv:
            a, b = kv.split(':'); fix[si[a]] = M.index[b]

    def score(key):
        tot = 0.0
        for r in R:
            x = key[r]
            tot += M.score_idx(np.concatenate(([0, 0, 0, 0], x))) if False else M.score_idx(x)
        # letter-distribution prior: multinomial log-lik of letter counts under German frequencies
        lc = np.bincount(key, weights=cnt, minlength=len(alpha))
        p = lc / N
        kl = float(np.sum(np.where(lc > 0, lc * np.log(np.maximum(p, 1e-9)), 0)) - np.sum(lc * lf))
        return tot - 1.0 * kl

    best_all = None
    for rs in range(restarts):
        rng = random.Random(rs)
        key = np.array([rng.randrange(len(alpha)) for _ in syms])
        for k, v in fix.items(): key[k] = v
        cur = score(key); best = (cur, key.copy())
        T0 = 20.0
        free = [i for i in range(len(syms)) if i not in fix]
        for it in range(iters):
            T = T0 * (1 - it / iters) + 0.05
            i = rng.choice(free)
            old = key[i]
            key[i] = rng.randrange(len(alpha))
            new = score(key)
            if new >= cur or rng.random() < math.exp((new - cur) / T):
                cur = new
                if cur > best[0]: best = (cur, key.copy())
            else:
                key[i] = old
        print('restart', rs, round(best[0], 1), flush=True)
        if best_all is None or best[0] > best_all[0]: best_all = best
        k = best[1]
        print(' ', ' | '.join(''.join(alpha[k[x]] for x in r) for r in R[:40]))
    k = best_all[1]
    res = {s: alpha[k[si[s]]] for s in syms}
    json.dump(res, open(os.path.join(HERE, 'key_%s.json' % model), 'w'), indent=0)
    inv = collections.defaultdict(list)
    for s, c in res.items(): inv[c].append(s)
    print(sorted(inv.items()))
    print('\n'.join(''.join(alpha[k[x]] for x in r) for r in R))

if __name__ == '__main__':
    main()
