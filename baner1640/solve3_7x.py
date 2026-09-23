"""Banded homophonic annealer, after the Swedish chancery keys of the 1630s-40s (R4123, R4325, R4122):
the values fall into bands of W consecutive numbers and each band is a permutation of the alphabet, so every letter
has exactly one value per band. Values outside the bands are free letters.

    python solve3.py --b0 2 --width 24 [--nb 4] [--iters 300000] [--restarts 10] [--fix fix.json]
"""
import argparse, json, math, os, random, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
from lang import lm
from solve_7x import load


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--model', default='de-1640s')
    ap.add_argument('--order', type=int, default=5)
    ap.add_argument('--b0', type=int, required=True)
    ap.add_argument('--width', type=int, default=24)
    ap.add_argument('--nb', type=int, default=4)
    ap.add_argument('--iters', type=int, default=300000)
    ap.add_argument('--restarts', type=int, default=10)
    ap.add_argument('--fix')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--t0', type=float, default=5.0)
    ap.add_argument('--t1', type=float, default=0.2)
    ap.add_argument('--ct', default=os.path.join(HERE, 'ct_neal.txt'))
    ap.add_argument('--out', default=os.path.join(HERE, 'runs3.jsonl'))
    ap.add_argument('--quiet', action='store_true')
    ap.add_argument('--pglob', type=float, default=0.2)
    ap.add_argument('--cycles', type=int, default=1)
    ap.add_argument('--finit', type=float, default=0.0)
    ap.add_argument('--start')
    ap.add_argument('--copies', type=int, default=1)
    ap.add_argument('--ils', type=int, default=0)
    ap.add_argument('--ilsfrac', type=float, default=0.4)
    ap.add_argument('--ilst0', type=float, default=3.0)
    ap.add_argument('--scramble', type=float, default=0.0)
    a = ap.parse_args()
    m = lm.load(a.model, order=a.order, spaces=False)
    A, k, lp = m.A, m.order, m.lp
    segs = load(a.ct)
    # symbol space: every value in the bands (used or not) + used values outside bands
    used = sorted({int(t) for s in segs for t in s})
    band_vals = [list(range(a.b0 + b * a.width, a.b0 + (b + 1) * a.width)) for b in range(a.nb)]
    inband = {v for bv in band_vals for v in bv}
    extra = [v for v in used if v not in inband]
    vals = [v for bv in band_vals for v in bv] + extra
    vi = {v: i for i, v in enumerate(vals)}
    V = len(vals)
    flat, wins = [], []
    for s in segs:
        base = len(flat)
        flat += [vi[int(t)] for t in s]
        wins += [base + j for j in range(len(s) - k + 1)]
    flat = np.array(flat); wins = np.array(wins, dtype=np.int64)
    W = len(wins)
    win_pos = wins[:, None] + np.arange(k)[None, :]
    touch = [np.nonzero((flat[win_pos] == i).any(1))[0] for i in range(V)]
    powk = A ** np.arange(k - 1, -1, -1)
    # band membership as index lists into vals
    bands = [[vi[v] for v in bv] for bv in band_vals]
    ext = [vi[v] for v in extra]
    rng = random.Random(a.seed)
    fix = json.load(open(a.fix, encoding='utf-8')) if a.fix else {}

    def wscore(key, idx):
        return lp[(key[flat[win_pos[idx]]] * powk).sum(1)]

    width_letters = a.width
    results = []
    for r in range(a.restarts):
        key = np.zeros(V, dtype=np.int64)
        cnt = np.bincount(flat, minlength=V)
        for b in bands:
            if a.finit:
                # frequency init: rank values in the band, assign letters by German frequency, then jitter
                order = sorted(b, key=lambda i: -cnt[i] + rng.random() * a.finit)
                freqorder = [m.index[c] for c in 'enrisatdhulcgmobwfkzpyxq' if c in m.index]
                freqorder = [x for x in freqorder for _ in range(a.copies)] if a.copies > 1 else freqorder
                if a.copies > 1:
                    # interleave so that the most frequent values get e,e,n,e,n,r... roughly
                    fo = []
                    for rep in range(a.copies):
                        fo += [m.index[c] for c in 'enrisatdhulcgmobwfkzpyxq' if c in m.index]
                    freqorder = sorted(fo, key=lambda x: 'enrisatdhulcgmobwfkzpyxq'.index(m.alpha[x]) + rng.random() * 3)
                for j, i in enumerate(order):
                    key[i] = freqorder[j] if j < len(freqorder) else rng.randrange(A)
                continue
            perm = list(range(A)) * a.copies; rng.shuffle(perm)
            # width may exceed A (umlauts, nulls): extra cells get random letters
            for j, i in enumerate(b):
                key[i] = perm[j] if j < len(perm) else rng.randrange(A)
        for i in ext: key[i] = rng.randrange(A)
        if a.start:
            st = json.load(open(a.start, encoding='utf-8'))
            for v, c in st.items():
                if int(v) in vi: key[vi[int(v)]] = m.index[c]
            for b in bands:  # scramble a fraction of each band
                sel = [i for i in b if rng.random() < a.scramble]
                vv = [key[i] for i in sel]; rng.shuffle(vv)
                for i, x in zip(sel, vv): key[i] = x
        for s, v in fix.items():
            if int(s) in vi: key[vi[int(s)]] = m.index[v]
        fixed = {vi[int(s)] for s in fix if int(s) in vi}
        ws = wscore(key, np.arange(W)); cur = ws.sum(); best = (cur, key.copy())
        gbest = None
        for rnd in range(a.ils + 1):
          if rnd:
            key = gbest[1].copy()
            for b in bands:
                sel = [i for i in b if rng.random() < a.ilsfrac and i not in fixed]
                vv = [key[i] for i in sel]; rng.shuffle(vv)
                for i, x in zip(sel, vv): key[i] = x
            ws = wscore(key, np.arange(W)); cur = ws.sum(); best = (cur, key.copy())
          t0 = a.t0 if rnd == 0 else a.ilst0
          for it in range(a.iters * a.cycles):
              if it and it % a.iters == 0:
                  key = best[1].copy(); ws = wscore(key, np.arange(W)); cur = ws.sum()
              T = (t0 if it < a.iters else t0 / 3) * (a.t1 / t0) ** ((it % a.iters) / a.iters)
              u = rng.random()
              if u < a.pglob:
                  # swap two letters in every band at once (and in the free values)
                  x, y = rng.sample(range(A), 2)
                  ix = [i for i in range(V) if key[i] == x and i not in fixed]
                  iy = [i for i in range(V) if key[i] == y and i not in fixed]
                  ch = ix + iy
                  if not ch: continue
                  idx = np.unique(np.concatenate([touch[i] for i in ch]))
                  if not len(idx): continue
                  for i in ix: key[i] = y
                  for i in iy: key[i] = x
                  nw = wscore(key, idx); d = nw.sum() - ws[idx].sum()
                  if d >= 0 or rng.random() < math.exp(d / T):
                      ws[idx] = nw; cur += d
                  else:
                      for i in ix: key[i] = x
                      for i in iy: key[i] = y
              elif ext and u < a.pglob + 0.1:
                  i = ext[rng.randrange(len(ext))]
                  if i in fixed: continue
                  old = key[i]; key[i] = rng.randrange(A)
                  idx = touch[i]
                  if not len(idx): continue
                  nw = wscore(key, idx); d = nw.sum() - ws[idx].sum()
                  if d >= 0 or rng.random() < math.exp(d / T):
                      ws[idx] = nw; cur += d
                  else:
                      key[i] = old
              else:
                  b = bands[rng.randrange(len(bands))]
                  i, j = rng.sample(b, 2)
                  if key[i] == key[j] or i in fixed or j in fixed: continue
                  key[i], key[j] = key[j], key[i]
                  idx = np.union1d(touch[i], touch[j])
                  if not len(idx): continue
                  nw = wscore(key, idx); d = nw.sum() - ws[idx].sum()
                  if d >= 0 or rng.random() < math.exp(d / T):
                      ws[idx] = nw; cur += d
                  else:
                      key[i], key[j] = key[j], key[i]
              if cur > best[0]: best = (cur, key.copy())
          if gbest is None or best[0] > gbest[0]: gbest = (best[0], best[1].copy())
        best = gbest
        sc, bk = best
        txt = [''.join(m.alpha[bk[vi[int(t)]]] for t in s) for s in segs]
        results.append(sc)
        if not a.quiet:
            print(f'b0={a.b0} w={a.width} restart {r}: {sc:.1f}  ' + ' | '.join(txt)); sys.stdout.flush()
        with open(a.out, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'b0': a.b0, 'width': a.width, 'nb': a.nb, 'seed': a.seed, 'score': float(sc),
                                'key': {str(v): m.alpha[bk[vi[v]]] for v in vals}, 'text': txt}) + '\n')
    print(f'b0={a.b0} w={a.width} best {max(results):.1f} mean {np.mean(results):.1f}')


if __name__ == '__main__':
    main()
