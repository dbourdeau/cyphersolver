"""Monotone-table annealer for the 1759 van Swieten key (R956/R957).

The 1757 letter (R955) shows the table is an alphabetical list of letters and short syllables
(a 203, ab 205, an 216 ... c 250, d 279, da 280, de 282 ... u 511, ur 512), a few with homophones.
So every observed code maps to an entry of a sorted inventory, and the map is non-decreasing in the code.
State: one inventory index per distinct observed code, non-decreasing. Score: LM log-prob of the
decrypt + BONUS per character + a small cost per rarely used unit.
usage: python msolve.py [seed] [iters]
"""
import sys, os, json, random, math, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.stdout.reconfigure(encoding='utf-8')
from lang import lm
import numpy as np

HERE = os.path.dirname(__file__)
M = lm.load('fr-1750-nospace')

def load_runs():
    runs = []
    for line in open(os.path.join(HERE, os.environ.get('RUNS','runs.txt')), encoding='utf-8'):
        line = line.split('#')[0].strip()
        if not line: continue
        tag, g = line.split(':', 1)
        runs.append((tag.strip(), g.split()))
    return runs

V = 'aeiou'
C = 'bcdfghjlmnpqrstvxyz'
def inventory():
    s = set(V) | set(C) | {'y'}
    for c in C:
        for v in V: s.add(c + v)
    for a in 'bcfgpt':
        s.add(a + 'l'); s.add(a + 'r')
    s |= {'dr', 'vr', 'ch', 'ph', 'gn', 'qu', 'st', 'sp', 'sc', 'ns', 'nt', 'nd', 'nc', 'rs', 'rt', 'ss', 'mm', 'll', 'tt'}
    for v in V:
        for c in 'bcdfglmnprstvx': s.add(v + c)
    s |= {'ai', 'au', 'ei', 'eu', 'oi', 'ou', 'ui', 'ie', 'ue', 'ay', 'oy', 'ey', 'ay'}
    s |= {'les', 'des', 'que', 'qui', 'ent', 'ont', 'ment', 'tion', 'est', 'mes', 'ces', 'ses', 'par', 'pour',
          'con', 'com', 'dans', 'sur', 'nous', 'vous', 'roi', 'ons', 'ais', 'ait', 'eur', 'eux', 'oit', 'ant'}
    s |= {'ex', 'z', 'zi', 'ya', 'ye', 'yo', 'ez', 'ag', 'eg', 'ic', 'ig', 'il', 'im', 'in', 'is', 'it', 'iv',
          'ob', 'oc', 'of', 'ol', 'om', 'on', 'op', 'or', 'os', 'ot', 'ov', 'up', 'us', 'ut', 'um', 'un', 'ur',
          'bs', 'ab', 'ad', 'ap', 'mes', 'nous', 'vous', 'pour', 'oit', 'ait', 'ais', 'que', 'ces', 'des', 'les'}
    return sorted(s)

INV = inventory()
PRI = {1: 0.0, 2: 0.3, 3: 1.2, 4: 2.0}

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 400000
    BONUS = float(sys.argv[3]) if len(sys.argv) > 3 else 2.2
    rnd = random.Random(seed)
    runs = load_runs()
    codes = sorted({int(x) for _, g in runs for x in g})
    ci = {c: i for i, c in enumerate(codes)}
    seqs = [[ci[int(x)] for x in g] for _, g in runs]
    n = len(codes); K = len(INV)
    lo, hi = codes[0], codes[-1]
    FREE = int(os.environ.get('FREE', '0'))
    free = [c < FREE for c in codes]
    ordi = [i for i in range(n) if not free[i]]
    pos = {i: k for k, i in enumerate(ordi)}
    g = sorted(rnd.sample(range(K), len(ordi)))
    gg = [0] * n
    for k, i in enumerate(ordi): gg[i] = g[k]
    for i in range(n):
        if free[i]: gg[i] = rnd.randrange(K)
    g = gg
    cnt = [0] * n
    for s in seqs:
        for t in s: cnt[t] += 1

    def text_of(g):
        return ''.join(''.join(INV[g[t]] for t in s) + ' ' for s in seqs)

    def score(g):
        tot = 0.0; L = 0
        for s in seqs:
            t = ''.join(INV[g[x]] for x in s)
            idx = M.encode(t)
            tot += M.score_idx(idx); L += len(idx)
        pen = sum(PRI[len(INV[g[i]])] * 0.5 for i in range(n))
        return tot + BONUS * L - pen

    MAXM = int(os.environ.get('MAXM', '2'))
    def multok(v):
        run = 1
        for k in range(1, len(ordi)):
            run = run + 1 if v[ordi[k]] == v[ordi[k - 1]] else 1
            if run > MAXM: return False
        return True
    if os.environ.get('INIT'):
        ik = json.load(open(os.path.join(HERE, os.environ['INIT'])))
        for i, c in enumerate(codes):
            if str(c) in ik and ik[str(c)] in INV: g[i] = INV.index(ik[str(c)])
        # repair order
        for k in range(1, len(ordi)):
            if g[ordi[k]] < g[ordi[k - 1]]: g[ordi[k]] = g[ordi[k - 1]]
    cur = score(g); best = cur; bestg = g[:]
    T0, T1 = float(os.environ.get('T0', '8')), 0.2
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        ng = g[:]
        r = rnd.random()
        if r < 0.7:
            i = rnd.randrange(n)
            if free[i]:
                ng[i] = rnd.randrange(K)
            else:
                k = pos[i]
                a = ng[ordi[k - 1]] if k > 0 else 0
                b = ng[ordi[k + 1]] if k < len(ordi) - 1 else K - 1
                ng[i] = rnd.randint(a, b)
        else:
            m = len(ordi); i = rnd.randrange(m); j = min(m, i + rnd.randint(2, 20)); d = rnd.choice((-1, 1)) * rnd.randint(1, 4)
            for k in range(i, j): ng[ordi[k]] += d
            ok = all(0 <= ng[ordi[k]] < K for k in range(i, j)) and (i == 0 or ng[ordi[i - 1]] <= ng[ordi[i]]) and (j == m or ng[ordi[j - 1]] <= ng[ordi[j]])
            if not ok: continue
        if not multok(ng): continue
        s = score(ng)
        if s >= cur or rnd.random() < math.exp((s - cur) / T):
            g, cur = ng, s
            if cur > best: best, bestg = cur, g[:]
    print('seed', seed, 'best', round(best, 1))
    print(text_of(bestg))
    json.dump({str(c): INV[bestg[i]] for i, c in enumerate(codes)}, open(os.path.join(HERE, f'mkey_{seed}.json'), 'w'))

if __name__ == '__main__':
    main()
