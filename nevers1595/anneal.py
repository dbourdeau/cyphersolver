"""Homophonic substitution annealer for the Nevers -> Villeroy runs (fr. 3993 ff. 148-149).

usage: python anneal.py MODE [restarts] [iters]
  MODE = glyph  : every transcribed sign is one unit
         pair   : '1'/'2' followed by a figure or o -> one two-digit unit; everything else single
         pair4  : as pair, and '4' followed by '1' -> 41
Each run is scored separately with fr-1600-letters (order 5, no spaces).  Units occurring once are free.
"""
import os, sys, random, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
from seg import load

D = set('0123456789o')
def segment(toks, mode):
    if mode == 'glyph': return list(toks)
    if mode == 'decade':
        return [u[0] + 'x' if len(u) == 2 and u[0].isdigit() and u[1].isdigit() else u for u in segment(toks, 'pairall')]
    if mode.startswith('prefix'):
        lead = mode[6:] or '1'
        out = []; i = 0
        while i < len(toks):
            if toks[i] in lead and i + 1 < len(toks):
                out.append(toks[i] + toks[i+1]); i += 2
            else:
                out.append(toks[i]); i += 1
        return out
    lead = {'pair': '12', 'pair4': '124', 'pairall': '123456789'}[mode]
    out = []; i = 0
    while i < len(toks):
        t = toks[i]
        if t in lead and i + 1 < len(toks) and toks[i+1] in D and not (mode == 'pair4' and t == '4' and toks[i+1] != '1'):
            out.append(t + toks[i+1].replace('o', '0')); i += 2
        else:
            out.append(t); i += 1
    return out

def runs(mode):
    here = os.path.dirname(os.path.abspath(__file__))
    R = []
    for f in os.environ.get('CTFILES', 'ct_f148r.txt,ct_f148v_149r.txt').split(','):
        for l in load(os.path.join(here, f)):
            if mode == 'n65':
                cur = []
                for u in segment(l, 'pairall'):
                    if len(u) == 2 and u.isdigit():
                        v = int(u)
                        if v % 10 == 0: continue            # nulls 10, 20 ... 90
                        if v >= 65:                          # name/word code: break the run
                            if cur: R.append(cur)
                            cur = []; continue
                    cur.append(u)
                if cur: R.append(cur)
            else:
                R.append(segment(l, mode))
    return R

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'pair'
    restarts = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else 60000
    global W
    W = float(os.environ.get('W', '1.0'))
    m = lm.load('fr-1600-letters', order=5, spaces=False)
    R = runs(mode)
    units = sorted({u for r in R for u in r})
    ui = {u: i for i, u in enumerate(units)}
    Ri = [[ui[u] for u in r] for r in R]
    letters = 'abcdefghilmnopqrstuxyz'
    alpha = [m.encode(c)[0] for c in letters]
    freq = [0.08, 0.01, 0.035, 0.04, 0.16, 0.012, 0.01, 0.01, 0.07, 0.055, 0.03, 0.075, 0.055, 0.03, 0.012, 0.065, 0.08,
            0.07, 0.06, 0.004, 0.003, 0.002]
    import numpy as np
    MAXNULL = int(os.environ.get('MAXNULL', '0'))
    from collections import Counter as _C0
    _c0 = _C0(u for r in Ri for u in r); cnt = [_c0[u] for u in range(len(units))]
    fr = dict(zip(alpha, freq)); tot = sum(freq)
    N = sum(len(r) for r in Ri)
    from collections import Counter as _C
    def score(key):
        s = 0.0
        for r in Ri:
            x = np.array([key[u] for u in r if key[u] >= 0], dtype=np.int64)
            if len(x) > 1: s += m.score_idx(x)
        c = _C(key[u] for r in Ri for u in r if key[u] >= 0)
        nn = sum(cnt[u] for u in range(len(units)) if key[u] < 0)
        if sum(1 for u in range(len(units)) if key[u] < 0) > MAXNULL: return -1e9
        # chi-square-like penalty on letter frequencies
        pen = sum((c.get(a, 0) - N * fr[a] / tot) ** 2 / (N * fr[a] / tot + 1) for a in alpha)
        return s - W * pen
    best_all = None
    for rs in range(restarts):
        key = [alpha[random.choices(range(len(letters)), freq)[0]] for _ in units]
        cur = score(key); best = (cur, key[:])
        T0 = 3.0
        for it in range(iters):
            T = T0 * (1 - it / iters) + 0.05
            u = random.randrange(len(units)); old = key[u]
            key[u] = -1 if random.random() < 0.03 else random.choice(alpha)
            new = score(key)
            if new >= cur or random.random() < math.exp((new - cur) / T):
                cur = new
                if cur > best[0]: best = (cur, key[:])
            else:
                key[u] = old
        n = sum(1 for r in Ri for u in r if best[1][u] >= 0)
        print(f'restart {rs}: {best[0]/n:.3f}/unit', flush=True)
        if best_all is None or best[0] > best_all[0]: best_all = best
    key = best_all[1]
    inv = {a: c for a, c in zip(alpha, letters)}; inv[-1] = '_'
    print('best', best_all[0] / sum(len(r) for r in Ri))
    for r, ri in zip(R, Ri):
        print(''.join(inv[key[u]] for u in ri))
    from collections import Counter
    c = Counter(u for r in R for u in r)
    print(' '.join(f'{u}={inv[key[ui[u]]]}({c[u]})' for u in sorted(units, key=lambda u: -c[u])))

if __name__ == '__main__':
    main()
