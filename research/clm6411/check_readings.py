"""Test fixed letter values for the 10/8/8 segmentation in Bischoff, p. 24."""

import argparse
import itertools
import re
from pathlib import Path


# IDs denote shapes. Give the damaged first triangle, unclear right ends,
# and the two uncertain signs at the start of line 3 independent IDs.
# This deliberately drops doubtful equalities and permits homophones.
ROWS = ("XABCDEFGHJ", "EGFKLKMN", "QROPYGYG")
WORDS = "alocus ceroficon domus dominicus dei cella".split()


def windows_matching(text, rows):
    cipher = "".join(rows)
    first = {}
    repeats = []
    for position, sign in enumerate(cipher):
        if sign in first:
            repeats.append((first[sign], position))
        else:
            first[sign] = position
    for start in range(len(text) - len(cipher) + 1):
        if all(text[start + i] == text[start + j] for i, j in repeats):
            yield text[start:start + len(cipher)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--latin-text", type=Path, help="UTF-8 plain text")
    args = parser.parse_args()
    words = "".join(WORDS)
    doubles = [words[i:i + 4] for i in range(len(words) - 3)
               if words[i:i + 2] == words[i + 2:i + 4]]
    print(f"Repeated note: {len(words)} letters, repeated pairs: {doubles}")
    length = sum(map(len, ROWS))
    selections = ["".join(s) for n in range(1, len(WORDS) + 1)
                  for s in itertools.permutations(WORDS, n)
                  if len("".join(s)) == length]
    corpus = None
    if args.latin_text:
        raw = args.latin_text.read_text(encoding="utf-8").lower()
        corpus = re.sub("[^a-z]", "", raw).replace("v", "u").replace("j", "i")
    for directions in itertools.product((1, -1), repeat=3):
        rows = [row[::step] for row, step in zip(ROWS, directions)]
        fits = [s for s in selections if list(windows_matching(s, rows))]
        print(directions, len(selections), "selections;", "fits:", fits)
        if corpus is not None:
            print("Corpus:", len(corpus), "letters; fits:",
                  list(windows_matching(corpus, rows)))


if __name__ == "__main__":
    main()
