"""Many-to-one substitution test for the Passano account."""
from __future__ import annotations

import math
import random
import sys

from solve import load
from lang import lm

ALPHA = "abcdefghilmnopqrstuz"
FREQ = dict(zip(ALPHA, [11.7, 1.0, 4.5, 3.7, 11.8, 1.1, 1.6, 10.1, 6.9,
                        6.5, 2.5, 9.8, 3.0, 0.9, 0.9, 5.0, 5.6, 6.4, 3.0, 2.1, 0.9]))
z = sum(FREQ.values())
FREQ = {c: v / z for c, v in FREQ.items()}


def main(path: str, restarts: int, iterations: int, seed: int, order: int):
    items = load(path)
    symbols = sorted({t for item in items for t in item})
    si = {s: i for i, s in enumerate(symbols)}
    enc = [[si[t] for t in item] for item in items]
    counts = [0] * len(symbols)
    for item in enc:
        for x in item:
            counts[x] += 1
    n = sum(counts)
    model = lm.load("it-cinquecento", order=order, spaces=False)
    rng = random.Random(seed)

    def score(key):
        total = sum(model.score_idx(model.encode("".join(key[x] for x in item))) for item in enc)
        obs = {c: 0 for c in ALPHA}
        for j, c in enumerate(key):
            obs[c] += counts[j]
        kl = sum((v / n) * math.log((v / n) / FREQ[c]) for c, v in obs.items() if v)
        return total - 2.0 * n * kl

    best = (-math.inf, None)
    for restart in range(restarts):
        key = [rng.choice("eaoinlrtscdpumghfbqz") for _ in symbols]
        current = score(key)
        local = (current, key[:])
        for step in range(iterations):
            a = rng.randrange(len(key)); old = key[a]
            key[a] = key[rng.randrange(len(key))] if rng.random() < .45 else rng.choice(ALPHA)
            candidate = score(key)
            temp = max(.25, 10 * (1 - step / iterations) ** 2)
            if candidate >= current or rng.random() < math.exp((candidate - current) / temp):
                current = candidate
                if current > local[0]: local = (current, key[:])
            else:
                key[a] = old
        if local[0] > best[0]: best = local
        print(restart, round(local[0], 1), "".join(local[1][x] for x in enc[0]), flush=True)
    sc, key = best
    print("BEST", sc)
    print("KEY", " ".join(f"{s}={c}" for s, c in zip(symbols, key)))
    for item in enc: print("".join(key[x] for x in item))


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
