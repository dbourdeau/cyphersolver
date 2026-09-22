"""Homophonic simulated annealing for the Rangone cipher against it-cinquecento (5-gram, no spaces).

Usage: python solve.py [restarts] [iters] [fixed.json]
Each sign type maps to one letter (or '.' = null when --nulls). Segments are scored separately
(clear text interrupts the cipher). Prints the best few keys and decrypts.
"""
import os, sys, json, math, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))


def load_segments(path=os.path.join(HERE, 'cipher.txt')):
    lines = {}
    for l in open(path, encoding='utf-8'):
        if l[:1] in 'AB' and l[1].isdigit():
            k, v = l.split(':', 1)
            lines[k] = v.split()
    segs = []
    # A: A1..A5 up to '|' is one run, the rest of A5 plus A6 another
    run = []
    for k in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']:
        for t in lines[k]:
            if t == '|':
                segs.append(run); run = []
            else:
                run.append(t)
    segs.append(run)
    segs.append(lines['B1'])
    segs.append(lines['B2'] + lines['B3'] + lines['B4'] + lines['B5'])
    return segs


LETTERS = 'abcdefghilmnopqrstuz'


def main():
    restarts = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 60000
    fixed = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else {}
    m = lm.load('it-cinquecento', order=5, spaces=False)
    segs = load_segments()
    types = sorted({t for s in segs for t in s})
    ti = {t: i for i, t in enumerate(types)}
    segi = [np.array([ti[t] for t in s]) for s in segs]
    L = np.array([m.index[c] for c in LETTERS])
    A, K = m.A, m.order
    lp = m.lp

    def score(key):
        tot = 0.0
        for s in segi:
            x = key[s]
            if len(x) < K:
                # score short runs with lower-order proxy: pad nothing, use unigram-ish via full-order on repeats
                continue
            ctx = np.zeros(len(x) - K + 1, dtype=np.int64)
            for j in range(K):
                ctx = ctx * A + x[j:len(x) - K + 1 + j]
            tot += lp[ctx].sum()
        return float(tot)

    # expected letter frequencies (Italian, early norm)
    FREQ = dict(a=.117,b=.009,c=.045,d=.037,e=.118,f=.011,g=.016,h=.015,i=.113,l=.065,m=.025,n=.069,o=.098,
                p=.030,q=.005,r=.064,s=.050,t=.056,u=.030,z=.008)
    W = float(os.environ.get('CHIW', '1.0'))
    N = sum(len(s) for s in segi)
    cnt = np.bincount(np.concatenate(segi), minlength=len(types))
    E = np.zeros(A); 
    for c, f in FREQ.items(): E[m.index[c]] = f * N
    E[E == 0] = 0.3
    base_score = score

    def score(key):
        n = np.bincount(key, weights=cnt, minlength=A)
        return base_score(key) - W * float((((n - E) ** 2) / (E + 2)).sum())

    free = [i for i, t in enumerate(types) if t not in fixed]
    results = []
    for r in range(restarts):
        key = np.array([m.index[fixed[t]] if t in fixed else random.choice(L) for t in types])
        cur = score(key); best = cur; bestkey = key.copy()
        T0, T1 = 4.0, 0.05
        for it in range(iters):
            T = T0 * (T1 / T0) ** (it / iters)
            i = random.choice(free)
            old = key[i]
            if random.random() < 0.2:
                j = random.choice(free)
                key[i], key[j] = key[j], key[i]
                new = score(key)
                if new >= cur or random.random() < math.exp((new - cur) / T):
                    cur = new
                else:
                    key[i], key[j] = key[j], key[i]
            else:
                key[i] = random.choice(L)
                new = score(key)
                if new >= cur or random.random() < math.exp((new - cur) / T):
                    cur = new
                else:
                    key[i] = old
            if cur > best:
                best = cur; bestkey = key.copy()
        n = sum(max(0, len(s) - K + 1) for s in segi)
        dec = ' | '.join(''.join(m.alpha[c] for c in bestkey[s]) for s in segi)
        results.append((best / n, dec, {t: m.alpha[bestkey[ti[t]]] for t in types}))
        print('%3d %.3f %s' % (r, best / n, dec), flush=True)
    results.sort(key=lambda z: -z[0])
    json.dump(results[:30], open(os.path.join(HERE, os.environ.get('OUT','sa_best.json')), 'w'), indent=0)


if __name__ == '__main__':
    main()
