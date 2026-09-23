"""Monoalphabetic substitution annealer for the Passano account cipher.

The ciphertext is a 21-sign alphabet with no word division.  Each sign maps
one-to-one to the traditional 21-letter Italian alphabet; account-item breaks
are scored separately with the repository's Cinquecento model.
"""
from __future__ import annotations

import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lang import lm


PLAIN = "abcdefghilmnopqrstuz"


def load(path: str) -> list[list[str]]:
    items: list[list[str]] = []
    current: list[str] = []
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            if current:
                items.append(current)
                current = []
            continue
        if line.startswith("#"):
            continue
        current.extend(line.split())
    if current:
        items.append(current)
    return items


def solve(items: list[list[str]], restarts: int, iterations: int, seed: int, order: int = 5,
          model_name: str = "it-cinquecento", drop: set[str] | None = None,
          fixed: dict[str, str] | None = None, plain: str = PLAIN, model_override=None):
    if drop:
        items = [[t for t in item if t not in drop] for item in items]
    model = model_override or lm.load(model_name, order=order, spaces=False)
    if any(c not in model.alpha for c in plain):
        raise ValueError(f"trial alphabet contains symbols absent from {model_name}: {plain}")
    symbols = sorted({token for item in items for token in item})
    if len(symbols) > len(plain):
        raise SystemExit(f"{len(symbols)} cipher signs but only {len(plain)} plaintext letters")
    symbol_index = {s: i for i, s in enumerate(symbols)}
    fixed = fixed or {}
    if any(s not in symbol_index for s in fixed):
        raise ValueError("fixed sign absent from ciphertext")
    if len(set(fixed.values())) != len(fixed):
        raise ValueError("fixed plaintext letters must be distinct")
    if any(c not in plain for c in fixed.values()):
        raise ValueError("fixed plaintext letter absent from trial alphabet")
    free_positions = [i for i, s in enumerate(symbols) if s not in fixed]
    encoded = [[symbol_index[t] for t in item] for item in items]
    rng = random.Random(seed)

    def decipher(key: list[str], item: list[int]) -> str:
        return "".join(key[i] for i in item)

    def score(key: list[str]) -> float:
        total = 0.0
        for item in encoded:
            text = decipher(key, item)
            total += model.score_idx(model.encode(text))
        return total

    best = (-math.inf, None)
    for restart in range(restarts):
        # Keep one dummy slot when the manuscript does not use every Italian
        # letter.  Swapping through it lets the omitted plaintext letter vary;
        # truncating the alphabet here freezes a random omission per restart.
        free_letters = [c for c in plain if c not in fixed.values()]
        rng.shuffle(free_letters)
        key = [fixed[s] if s in fixed else free_letters.pop() for s in symbols]
        key.extend(free_letters)
        current = score(key)
        local_best = (current, key[:])
        for step in range(iterations):
            a, b = rng.sample(free_positions + list(range(len(symbols), len(key))), 2)
            key[a], key[b] = key[b], key[a]
            candidate = score(key)
            temperature = max(0.18, 12.0 * (1.0 - step / iterations) ** 3)
            if candidate >= current or rng.random() < math.exp((candidate - current) / temperature):
                current = candidate
                if current > local_best[0]:
                    local_best = (current, key[:])
            else:
                key[a], key[b] = key[b], key[a]
        if local_best[0] > best[0]:
            best = local_best
        preview = decipher(local_best[1], encoded[0])[:100]
        print(restart, round(local_best[0], 2), preview, flush=True)

    score_best, key_best = best
    assert key_best is not None
    print("BEST", round(score_best, 3))
    print("KEY", " ".join(f"{s}={p}" for s, p in zip(symbols, key_best)))
    if len(key_best) > len(symbols):
        print("UNUSED", "".join(key_best[len(symbols):]))
    for item in encoded:
        print(decipher(key_best, item))


if __name__ == "__main__":
    solve(
        load(sys.argv[1]),
        int(sys.argv[2]) if len(sys.argv) > 2 else 50,
        int(sys.argv[3]) if len(sys.argv) > 3 else 100_000,
        int(sys.argv[4]) if len(sys.argv) > 4 else 0,
        int(sys.argv[5]) if len(sys.argv) > 5 else 5,
        sys.argv[6] if len(sys.argv) > 6 else "it-cinquecento",
        set(sys.argv[7].split(",")) if len(sys.argv) > 7 and sys.argv[7] else None,
        dict(x.split("=") for x in sys.argv[8].split(",")) if len(sys.argv) > 8 and sys.argv[8] else None,
        sys.argv[9] if len(sys.argv) > 9 else PLAIN,
    )
