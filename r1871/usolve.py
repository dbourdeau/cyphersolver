"""Free (non-monotone) nomenclator annealer for R1871: each 3-digit code -> one unit (letter, syllable or short word).
Score: clean Italian 4-gram (q4.npy) sum + BONUS per char - length prior. usage: python usolve.py seed iters bonus [runs]"""
import sys, os, random, math, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
LP = np.load(os.path.join(HERE, 'q4.npy'))
A = 'abcdefghilmnopqrstuz'; IX = {c: i for i, c in enumerate(A)}

def inventory():
    V = 'aeiou'; C = 'bcdfghlmnpqrstuz'
    s = set(A)
    for c in C:
        for v in V: s.add(c + v)
    for v in V:
        for c in 'lnrs': s.add(v + c)
    s |= {'che', 'chi', 'per', 'non', 'con', 'il', 'et', 'del', 'gli', 'qu', 'st', 'tt', 'll', 'ss', 'nt', 'mente', 'sua', 'suo'}
    return sorted(s)
INV = inventory(); K = len(INV)
ENC = [np.array([IX[c] for c in u]) for u in INV]
PRI = [0.0 if len(u) == 1 else 0.4 * (len(u) - 1) for u in INV]

def main():
    seed = int(sys.argv[1]); iters = int(sys.argv[2]); BONUS = float(sys.argv[3])
    runs = sys.argv[4] if len(sys.argv) > 4 else 'runs.txt'
    rnd = random.Random(seed)
    lines = [l.split(':')[1].split() for l in open(os.path.join(HERE, runs)) if ':' in l]
    toks = [x for l in lines for x in l]
    codes = sorted(set(toks)); ci = {c: i for i, c in enumerate(codes)}
    seq = [ci[x] for x in toks]; n = len(codes)
    g = [rnd.randrange(26) if False else IX[rnd.choice('eaiontlrs')] for _ in range(n)]
    g = [INV.index(A[x]) for x in g]

    def score(g):
        y = np.concatenate([ENC[g[t]] for t in seq])
        lp = LP[((y[:-3] * 20 + y[1:-2]) * 20 + y[2:-1]) * 20 + y[3:]].sum()
        return lp + BONUS * len(y) - sum(PRI[g[i]] for i in range(n))
    cur = score(g); best, bestg = cur, g[:]
    T0, T1 = 6.0, 0.15
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        i = rnd.randrange(n); old = g[i]
        g[i] = rnd.randrange(K) if rnd.random() < 0.3 else INV.index(rnd.choice(A))
        s = score(g)
        if s >= cur or rnd.random() < math.exp((s - cur) / T):
            cur = s
            if cur > best: best, bestg = cur, g[:]
        else:
            g[i] = old
    txt = ' '.join(''.join(INV[bestg[ci[x]]] for x in l) for l in lines)
    print('seed', seed, 'best', round(best, 1)); print(txt)
    json.dump({c: INV[bestg[i]] for i, c in enumerate(codes)}, open(os.path.join(HERE, f'ukey_{seed}.json'), 'w'))

if __name__ == '__main__':
    main()
