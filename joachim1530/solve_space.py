"""Test whether one of the twenty signs represents a word boundary."""
from __future__ import annotations

import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lang import lm
from solve import PLAIN, load


def main(path, boundary, restarts, iterations, seed, model_name):
    items = load(path)
    symbols = sorted({x for item in items for x in item})
    assert boundary in symbols
    model = lm.load(model_name, order=4, spaces=True)
    free = [x for x in symbols if x != boundary]
    idx = {x: i for i, x in enumerate(free)}
    seqs = [[-1 if x == boundary else idx[x] for x in item] for item in items]
    rng = random.Random(seed)

    def decode(key, item):
        return "".join(" " if x == -1 else key[x] for x in item)

    def score(key):
        return sum(model.score_idx(model.encode(decode(key, item))) for item in seqs)

    overall = (-math.inf, None)
    for restart in range(restarts):
        key = list(PLAIN)
        rng.shuffle(key)
        cur = score(key); local = (cur, key[:])
        for step in range(iterations):
            a, b = rng.sample(range(len(key)), 2)
            key[a], key[b] = key[b], key[a]
            cand = score(key)
            temp = max(.15, 10 * (1 - step / iterations) ** 2)
            if cand >= cur or rng.random() < math.exp((cand - cur) / temp):
                cur = cand
                if cur > local[0]: local = (cur, key[:])
            else: key[a], key[b] = key[b], key[a]
        if local[0] > overall[0]: overall = local
        print(restart, round(local[0], 1), decode(local[1], seqs[0]), flush=True)
    sc, key = overall
    print("BEST", round(sc, 2), "BOUNDARY", boundary, "KEY", " ".join(f"{s}={c}" for s, c in zip(free,key)))
    for item in seqs: print(decode(key,item))


if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),sys.argv[6] if len(sys.argv)>6 else "it-cinquecento")
