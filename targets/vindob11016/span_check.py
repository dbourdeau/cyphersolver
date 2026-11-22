"""Longest exact corpus span within a line, allowing reader 9b's sign options.

Remove the manuscript dividers and all corpus spaces. Index seven-sign
substrings as a starting point, then grow each hit. The flattened APD stream
can include artificial joins, so even an exact hit requires checking its source.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
from random import Random
from phrase_order import fold, lines, normalize

text = normalize("".join(Path("tr/apd_letters.txt").read_text(encoding="utf-8").split()))
minimum = 7
index = {text[i:i + minimum] for i in range(len(text) - minimum + 1)}


@lru_cache(maxsize=None)
def options(token):
    return tuple({normalize(fold.get(s, s)) for s in token.split("/")})


def longest(tokens):
    best = ""
    for i in range(len(tokens) - minimum + 1):
        active = {"".join(p) for p in product(*tokens[i:i + minimum])}
        active.intersection_update(index)
        end = i + minimum
        while active:
            hit = min(active)
            if len(hit) > len(best):
                best = hit
            if end == len(tokens):
                break
            active = {a + b for a in active for b in tokens[end] if a + b in text}
            end += 1
    return best


if __name__ == "__main__":
    sample = [[options(t) for t in line if t != "|"] for line in lines]
    assert longest([(c,) for c in text[:15]]) == text[:15]
    hits = [longest(row) for row in sample]
    print("Line maxima (blank = below seven):", hits)
    observed = max(map(len, hits))
    rng = Random(844)
    maxima = []
    for _ in range(999):
        shuffled = []
        for line in sample:
            pool = [t for t in line if t != ("*",)]
            rng.shuffle(pool)
            draw = iter(pool)
            shuffled.append([next(draw) if t != ("*",) else t for t in line])
        maxima.append(max(len(longest(row)) for row in shuffled))
    print("Observed", observed, "controls at least seven", sum(m >= minimum for m in maxima),
          "of", len(maxima), "controls equal or exceed", sum(m >= observed for m in maxima))
