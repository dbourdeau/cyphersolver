"""Reproduce the initial lexicon search, before the folios were reconciled."""

import gzip
import json
import re
import sys
from pathlib import Path

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

LEXICONS = Path(__file__).resolve().parents[2] / "lang" / "lexicons"
INITIAL = ("7T25 3KL2D 96yV 397 3Ty4y 34B B425D4 O424E TyD "
           "34B 85T6V 7V854T 924DV 3TyDT6")
ALPHABET = " abcdefghijklmnopqrstuvwxyz"


def word_model(language):
    with gzip.open(LEXICONS / f"{language}.json.gz") as source:
        words = json.load(source)
    counts = np.zeros(27**4)
    for word, count in words.items():
        if not re.fullmatch("[a-z]+", word):
            continue
        padded = "  " + word + "  "
        for start in range(len(padded) - 3):
            index = 0
            for char in padded[start:start + 4]:
                index = index * 27 + ALPHABET.index(char)
            counts[index] += count
    return np.log(counts + 0.03)


def search(language):
    model = word_model(language)
    symbols = " " + "".join(sorted(set(INITIAL) - {" "}))
    padded = "  " + "  ".join(INITIAL.split()) + "  "
    grams = sliding_window_view(np.array([symbols.index(c) for c in padded]), 4)
    weights = (27**3, 27**2, 27, 1)

    def scores(keys):
        indices = sum(keys[:, grams[:, i]] * weight for i, weight in enumerate(weights))
        return model[indices].sum(axis=1)

    rng = np.random.default_rng(3656)
    rows = np.arange(48)
    keys = np.stack([np.r_[0, rng.permutation(26) + 1] for _ in rows])
    current = scores(keys)
    best = -np.inf
    for _ in range(5):
        for temperature in np.geomspace(15, 0.25, 650):
            left = rng.integers(1, len(symbols), size=len(rows))
            right = rng.integers(1, 27, size=len(rows))
            trial = keys.copy()
            trial[rows, left], trial[rows, right] = keys[rows, right], keys[rows, left]
            candidate = scores(trial)
            accept = np.log(rng.random(len(rows))) * temperature < candidate - current
            keys[accept] = trial[accept]
            current[accept] = candidate[accept]
        winner = current.argmax()
        if current[winner] > best:
            best = current[winner]
            reading = "".join(ALPHABET[keys[winner, symbols.index(c)]] for c in INITIAL)
            print(language, round(best, 1), reading)


if __name__ == "__main__":
    for language in sys.argv[1:] or ["nl", "de", "la", "da", "fr"]:
        search(language)
