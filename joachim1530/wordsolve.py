"""Dictionary-segmentation annealer for the unspaced Passano substitution."""
from __future__ import annotations

import collections
import glob
import math
import random
import re
import sys
import unicodedata

from solve import PLAIN, load


def norm(text: str) -> list[str]:
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.replace("j", "i").replace("v", "u").replace("y", "i")
    return [w for w in re.findall(r"[a-z]+", text) if not re.search(r"[kwx]", w)]


def vocabulary():
    counts = collections.Counter()
    for path in glob.glob("lang/corpora/it-*.txt"):
        counts.update(norm(open(path, encoding="utf-8", errors="ignore").read()))
    # Diplomatic/account vocabulary and historical spellings relevant here.
    for word in "item scuti ducati denari donati pagati spesi dato data signor signore cardinale duca duchessa secretario ambasciatore pensione provisione presente promesso servitii servitio maesta inghilterra francia".split():
        counts[word] += 100
    total = sum(counts.values())
    return {w: math.log(c / total) for w, c in counts.items() if c >= 3 and len(w) <= 18}


def main(path: str, restarts: int, iterations: int, seed: int):
    items = load(path); vocab = vocabulary()
    symbols = sorted({x for item in items for x in item}); si = {x: i for i, x in enumerate(symbols)}
    encoded = [[si[x] for x in item] for item in items]
    rng = random.Random(seed); maxword = 18; unknown = -10.0; boundary_cost = 1.5

    def segscore(text: str):
        n = len(text); best = [0.0] + [-1e30] * n
        for end in range(1, n + 1):
            val = best[end - 1] + unknown
            for start in range(max(0, end - maxword), end):
                lp = vocab.get(text[start:end])
                if lp is not None:
                    val = max(val, best[start] + lp - boundary_cost)
            best[end] = val
        return best[n]

    def total(key):
        return sum(segscore("".join(key[x] for x in item)) for item in encoded)

    overall = (-math.inf, None)
    for restart in range(restarts):
        key = list(PLAIN); rng.shuffle(key)
        cur = total(key); local = (cur, key[:])
        for step in range(iterations):
            a, b = rng.sample(range(len(key)), 2); key[a], key[b] = key[b], key[a]
            cand = total(key); temp = max(.25, 12 * (1 - step / iterations) ** 2)
            if cand >= cur or rng.random() < math.exp((cand - cur) / temp):
                cur = cand
                if cur > local[0]: local = (cur, key[:])
            else: key[a], key[b] = key[b], key[a]
        if local[0] > overall[0]: overall = local
        print(restart, round(local[0], 1), "".join(local[1][x] for x in encoded[0]), flush=True)
    score, key = overall
    print("BEST", score, "KEY", " ".join(f"{s}={c}" for s, c in zip(symbols, key)))
    for item in encoded: print("".join(key[x] for x in item))


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
