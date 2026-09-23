"""Homophonic annealer for the Banér letter: every two-digit number is one letter (or a null), the
three-digit numbers are nomenclator words and break the text. Scored with a German no-space n-gram model.

    python solve.py [--model de-1500s] [--iters 300000] [--restarts 8] [--fix fix.json] [--nulls]
"""
import argparse, json, math, os, random, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
from lang import lm


def load(path=os.path.join(HERE, 'ct_neal.txt')):
    segs = []
    for l in open(path, encoding='utf-8'):
        if l.startswith('S'):
            toks = [t for t in l.split()[1:]]
            cur = []
            for t in toks:
                if '?' in t:
                    if cur: segs.append(cur)
                    cur = []
                else:
                    cur.append(t)
            if cur: segs.append(cur)
    return segs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--model', default='de-1500s')
    ap.add_argument('--order', type=int, default=5)
    ap.add_argument('--iters', type=int, default=300000)
    ap.add_argument('--restarts', type=int, default=6)
    ap.add_argument('--fix')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--ct', default=os.path.join(HERE, 'ct_neal.txt'))
    ap.add_argument('--adj', type=float, default=0.0)
    ap.add_argument('--out', default=os.path.join(HERE, 'runs.jsonl'))
    a = ap.parse_args()
    m = lm.load(a.model, order=a.order, spaces=False)
    A, k, lp = m.A, m.order, m.lp
    segs = load(a.ct)
    syms = sorted({t for s in segs for t in s}, key=int)
    si = {s: i for i, s in enumerate(syms)}
    S = len(syms)
    fix = json.load(open(a.fix, encoding='utf-8')) if a.fix else {}
    fixi = {si[s]: m.index[v] for s, v in fix.items() if s in si}
    # concatenate segments with a boundary: score each segment separately via index arrays
    xs = [np.array([si[t] for t in s]) for s in segs if len(s) >= k]
    # unigram prior from the corpus for proposals
    rng = random.Random(a.seed)
    letters = list(range(A))

    ALPH = 'abcdefghiklmnopqrstuwxyz'
    aidx = np.array([ALPH.find(c) if c in ALPH else -9 for c in m.alpha])
    pairs = [(si[s], si[str(int(s) + 1)]) for s in syms if str(int(s) + 1) in si]
    pa = np.array([p[0] for p in pairs]); pb = np.array([p[1] for p in pairs])

    def score(key):
        tot = 0.0
        if a.adj and len(pa):
            d = np.abs(aidx[key[pa]] - aidx[key[pb]])
            tot += a.adj * np.sum(d == 1)
        for x in xs:
            y = key[x]
            ctx = np.zeros(len(y) - k + 1, dtype=np.int64)
            for j in range(k):
                ctx = ctx * A + y[j:len(y) - k + 1 + j]
            tot += lp[ctx].sum()
        return tot

    best_all = None
    for r in range(a.restarts):
        key = np.array([rng.randrange(A) for _ in range(S)], dtype=np.int64)
        for i, v in fixi.items(): key[i] = v
        free = [i for i in range(S) if i not in fixi]
        cur = score(key); best = (cur, key.copy())
        T0, T1 = 12.0, 0.5
        for it in range(a.iters):
            T = T0 * (T1 / T0) ** (it / a.iters)
            i = rng.choice(free)
            old = key[i]
            key[i] = rng.randrange(A)
            if key[i] == old: continue
            new = score(key)
            if new >= cur or rng.random() < math.exp((new - cur) / T):
                cur = new
                if cur > best[0]: best = (cur, key.copy())
            else:
                key[i] = old
        sc, key = best
        txt = [''.join(m.alpha[key[si[t]]] for t in s) for s in segs]
        print(f'restart {r}: {sc:.1f}')
        print(' | '.join(txt)); sys.stdout.flush()
        with open(a.out, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'model': a.model, 'score': float(sc), 'key': {s: m.alpha[key[si[s]]] for s in syms}, 'text': txt}) + '\n')
        if best_all is None or sc > best_all[0]: best_all = (sc, key)


if __name__ == '__main__':
    main()
