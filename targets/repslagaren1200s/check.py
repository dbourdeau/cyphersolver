"""Repeat-pattern, branch-coordinate and coverage checks for KM 61277:331."""
import csv
from itertools import permutations, product
from pathlib import Path

root = Path(__file__).resolve().parent
with (root / "transcription.tsv").open(encoding="utf-8") as stream:
    rows = list(csv.DictReader(stream, delimiter="\t"))

a, b = ([row for row in rows if row["face"] == face] for face in "AB")
assert all([int(row["position"]) for row in face] == list(range(1, 11)) for face in (a, b))
crib = "".join(row["edition"] for row in a)
signs = [row["sign"] for row in b]
for direction in (crib, crib[::-1]):
    pairs = list(zip(direction, signs, strict=True))
    repeats = [(i + 1, j + 1) for i, (x, s) in enumerate(pairs)
               for j, (y, t) in enumerate(pairs[:i]) if x == y and s != t]
    print(direction, "same rune, different whole sign:", repeats)

groups = ("fuþork", "hnias", "tbmlR")
def decode(coords, order, swap, backward):
    result = []
    for left, right in coords:
        group, pos = (right, left) if swap else (left, right)
        if not 1 <= group <= len(order):
            return None
        letters = order[group - 1][::-1] if backward else order[group - 1]
        if not 1 <= pos <= len(letters):
            return None
        result.append(letters[pos - 1])
    return "".join(result)

def candidates(coords):
    return {value for order in permutations(groups)
            for swap, backward in product((False, True), repeat=2)
            if (value := decode(coords, order, swap, backward)) is not None}

control = "raþþurunar"  # Ten runes, word spaces removed.
key = {letter: (g, p) for g, group in enumerate(groups[::-1], 1)
       for p, letter in enumerate(group, 1)}
assert control in candidates([key[letter] for letter in control])
assert not candidates([(1, 0)])  # B07 alone blocks a uniform paired decoder.
print("Control recovered among candidates. B07 admits no paired decode.")
last_values = candidates([(2, 2)])
assert last_values.isdisjoint({crib[0], crib[-1], "i"})  # Also allow e to use the i-rune.
print("B10 alone, across all 24 conventions:", sorted(last_values))
line = next(line for line in (root / "reading.txt").read_text(encoding="utf-8").splitlines()
            if line.startswith("B1 "))
tokens = line.split()[1:]
assert tokens == [f"[{sign}]" for sign in signs]
print(f"B: 0/{len(tokens)} tokens in established words.")
