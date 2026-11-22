"""Test fixed reader-9b options against adjacent words in documentary letters.

Run in the target directory. Each control shuffles whole sign tokens inside
each line while retaining divider positions, damage and all sign frequencies.
"""
from collections import defaultdict
from itertools import product
from pathlib import Path
from random import Random
import sys

greek = "αβγδεϛζηθικλμνξοπϙρστυφχψωϡ"
abjad = "ابجدهوزحطيكلمنسعفصقرشتثخذضظ"
fold = dict(zip(greek, "".join(abjad[i:i + 9][::-1] for i in (0, 9, 18))))
# Conservative: merge only families with the same skeleton in every position.
skeleton = str.maketrans("تثخجذزشضظغ", "ببححدرسصطع")


def normalize(s):
    return s.translate(skeleton) if "--rasm" in sys.argv else s


letters = defaultdict(set)
for line in Path("tr/apd_letters.txt").read_text(encoding="utf-8").splitlines():
    words = normalize(line).split()
    for left, right in zip(words, words[1:]):
        letters[left].add(right)

variant = next((arg for arg in sys.argv[1:] if arg in ("a", "b", "c", "d")), "b")
lines = [line.partition(":")[2].split() for line in
         Path(f"tr/reader9_{variant}.txt").read_text(encoding="utf-8").splitlines() if line.startswith("L")]


def phrases(line):
    groups = []
    options = []
    for token in line + ["|"]:
        if token != "|":
            options.append({normalize(fold.get(s, s)) for s in token.split("/")})
        elif options:
            groups.append({"".join(p) for p in product(*options)})
            options = []
    return sorted({(a, b) for left, right in zip(groups, groups[1:])
                   for a in left for b in right.intersection(letters.get(a, ()))})


if __name__ == "__main__":
    rng = Random(11016)
    observed = sum(bool(phrases(line)) for line in lines)
    for i, line in enumerate(lines, 1):
        print(f"L{i:02}", phrases(line))
    above = positive = 0
    for _ in range(999):
        hits = 0
        for line in lines:
            movable = [t for t in line if t not in {"|", "*"}]
            rng.shuffle(movable)
            draw = iter(movable)
            hits += bool(phrases([t if t in {"|", "*"} else next(draw) for t in line]))
        above += hits >= observed
        positive += hits > 0
    print(f"{observed} lines with matches; {positive}/999 controls with matches; {above}/999 equal or exceed; p={(above+1)/1000:g}")
