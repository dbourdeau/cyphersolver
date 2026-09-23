"""Fast homophonic annealer: incremental n-gram deltas (only windows touching the changed symbol are rescored).

    python solve2.py [--model de-1640s] [--iters 2000000] [--restarts 20] [--fix fix.json] [--seed 0]
"""
import argparse, json, math, os, random, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
from lang import lm
from solve import load


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--model', default='de-1640s')
    ap.add_argument('--order', type=int, default=5)
    ap.add_argument('--iters', type=int, default=2000000)
    ap.add_argument('--restarts', type=int, default=20)
    ap.add_argument('--fix')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--t0', type=float, default=6.0)
    ap.add_argument('--t1', type=float, default=0.3)
    ap.add_argument('--ct', default=os.path.join(HERE, 'ct_neal.txt'))
    ap.add_argument('--out', default=os.path.join(HERE, 'runs2.jsonl'))
    a = ap.parse_args()
    m = lm.load(a.model, order=a.order, spaces=False)
    A, k, lp = m.A, m.order, m.lp
    segs = [s for s in load(a.ct) if len(s) >= 1]
    syms = sorted({t for s in segs for t in s}, key=int)
    si = {s: i for i, s in enumerate(syms)}
    S = len(syms)
    # flatten segments long enough to score; windows = start positions of k-grams
    flat, wins = [], []
    for s in segs:
        base = len(flat)
        flat += [si[t] for t in s]
        for j in range(len(s) - k + 1):
            wins.append(base + j)
    flat = np.array(flat); wins = np.array(wins, dtype=np.int64)
    W = len(wins)
    offs = np.arange(k)
    win_pos = wins[:, None] + offs[None, :]            # W x k positions
    # windows touching each symbol
    touch = [np.unique(np.nonzero(np.isin(flat[win_pos], [i]).any(1))[0]) for i in range(S)]
    powk = A ** np.arange(k - 1, -1, -1)
    fix = json.load(open(a.fix, encoding='utf-8')) if a.fix else {}
    fixi = {si[s]: m.index[v] for s, v in fix.items() if s in si}
    free = [i for i in range(S) if i not in fixi and len(touch[i])]
    rng = random.Random(a.seed)
    # letter prior for proposals: unigram frequencies of the model
    uni = np.exp(lm.load(a.model, order=1, spaces=False).lp[:A]) if False else None

    def wscore(key, idx):
        return lp[(key[flat[win_pos[idx]]] * powk).sum(1)]

    for r in range(a.restarts):
        key = np.array([rng.randrange(A) for _ in range(S)], dtype=np.int64)
        for i, v in fixi.items(): key[i] = v
        ws = wscore(key, np.arange(W)); cur = ws.sum()
        best = (cur, key.copy())
        for it in range(a.iters):
            T = a.t0 * (a.t1 / a.t0) ** (it / a.iters)
            i = free[rng.randrange(len(free))]
            old = key[i]; new = rng.randrange(A)
            if new == old: continue
            idx = touch[i]
            key[i] = new
            nw = wscore(key, idx)
            d = nw.sum() - ws[idx].sum()
            if d >= 0 or rng.random() < math.exp(d / T):
                ws[idx] = nw; cur += d
                if cur > best[0]: best = (cur, key.copy())
            else:
                key[i] = old
        sc, bk = best
        txt = [''.join(m.alpha[bk[si[t]]] for t in s) for s in segs]
        print(f'restart {r}: {sc:.1f}  ' + ' | '.join(txt)); sys.stdout.flush()
        with open(a.out, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'model': a.model, 'seed': a.seed, 'fix': a.fix, 'score': float(sc),
                                'key': {s: m.alpha[bk[si[s]]] for s in syms}, 'text': txt}) + '\n')


if __name__ == '__main__':
    main()
