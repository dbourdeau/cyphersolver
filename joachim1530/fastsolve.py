"""Incremental permutation search for the Passano cryptogram.

Each manuscript sign maps to one period Italian letter. Only 4-gram windows
touching the two swapped signs are rescored, so long searches are practical.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lang import lm
from joachim1530.solve import PLAIN, load


def run(windows, touch, tlen, lp, power, letters, restarts, iterations, seed):
    rng = np.random.default_rng(seed)
    nsym = len(letters)
    best_key = letters.copy()
    overall = -1e20
    counts = np.zeros(restarts, dtype=np.float64)
    for restart in range(restarts):
        key = rng.permutation(letters)
        current = float(lp[(key[windows] * power).sum(axis=1)].sum())
        local = current
        for step in range(iterations):
            a = rng.integers(nsym)
            b = rng.integers(nsym - 1)
            if b >= a: b += 1
            ids = touch[a,b,:tlen[a,b]]
            win = windows[ids]
            old = float(lp[(key[win] * power).sum(axis=1)].sum())
            key[a], key[b] = key[b], key[a]
            new = float(lp[(key[win] * power).sum(axis=1)].sum())
            candidate = current - old + new
            x = 1.0 - step / iterations
            temperature = max(.04, 8.0 * x * x * x)
            if candidate >= current or rng.random() < np.exp((candidate - current) / temperature):
                current = candidate
                if current > local:
                    local = current
                if current > overall:
                    overall = current
                    best_key[:] = key
            else:
                key[a], key[b] = key[b], key[a]
        counts[restart] = local
    return overall, best_key, counts


def main(path: str, restarts: int, iterations: int, seed: int, model_name: str, order: int,
         drop: set[str] | None = None):
    model = lm.load(model_name, order=order, spaces=False)
    if any(c not in model.alpha for c in PLAIN):
        raise ValueError("plaintext alphabet is not in the selected language model")
    items = load(path)
    if drop:
        items = [[x for x in z if x not in drop] for z in items]
    signs = sorted(set(x for z in items for x in z))
    if len(signs) > len(PLAIN):
        raise ValueError(f"at most {len(PLAIN)} signs, got {len(signs)}")
    index = {s: i for i, s in enumerate(signs)}
    encoded = [[index[s] for s in item] for item in items]
    windows = np.array([item[i:i+order] for item in encoded for i in range(len(item)-order+1)], dtype=np.int64)
    max_touch = len(windows)
    touch = np.zeros((len(PLAIN),len(PLAIN),max_touch),dtype=np.int64)
    tlen = np.zeros((len(PLAIN),len(PLAIN)),dtype=np.int64)
    for a in range(len(PLAIN)):
        for b in range(len(PLAIN)):
            ids = np.flatnonzero(np.any((windows==a)|(windows==b),axis=1))
            touch[a,b,:len(ids)] = ids
            tlen[a,b] = len(ids)
    power = np.array([model.A ** (order-1-i) for i in range(order)],dtype=np.int64)
    letters = np.array([model.index[c] for c in PLAIN],dtype=np.int64)
    score, key, local = run(windows,touch,tlen,model.lp,power,letters,restarts,iterations,seed)
    mapping = {s:model.alpha[int(key[i])] for i,s in enumerate(signs)}
    print("windows",len(windows),"scores",round(float(local.min()),1),round(float(np.median(local)),1),round(float(local.max()),1))
    print("BEST",round(score,3))
    print("KEY"," ".join(f"{s}={mapping[s]}" for s in signs))
    for item in items:
        print("".join(mapping[s] for s in item))


if __name__ == "__main__":
    main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),
         sys.argv[5] if len(sys.argv)>5 else "it-cinquecento",int(sys.argv[6]) if len(sys.argv)>6 else 4,
         set(sys.argv[7].split(",")) if len(sys.argv)>7 else None)
