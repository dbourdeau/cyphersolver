"""Test two restricted families against the reported first recto crib."""

from itertools import product
from math import gcd

HEBREW = "אבגדהוזחטיכלמנסעפצקרשת"
VALUES = list(range(1, 10)) + list(range(10, 100, 10)) + [100, 200, 300, 400]
R11 = [400, 70, 300, 3, 40]  # Start at the physical right edge.
R12 = [10, 40, 70, 8]  # Four visible forms. 10 follows the Hebrew gloss.
V5 = [1, 60, 100, 400, 40, 1, 100, 1, None, 8, 8]  # Friedman's list.


def lookup(values):
    return "".join(HEBREW[VALUES.index(v)] if v in VALUES else "?" for v in values)


def pattern(values):
    alphabet = list(dict.fromkeys(values))
    return "".join(chr(65 + alphabet.index(v)) for v in values)


if __name__ == "__main__":
    for label, values in [("r11", R11), ("r12", R12), ("v5", V5)]:
        print(label, values, lookup(values), pattern(values))
    crib = "מרשעת"
    for label, values in [("physical RTL", R11), ("physical LTR", R11[::-1])]:
        indexes = [VALUES.index(v) for v in values]
        matches = []
        for a, b in product(range(22), repeat=2):
            if gcd(a, 22) == 1:
                candidate = "".join(HEBREW[(a*i+b) % 22] for i in indexes)
                if candidate == crib:
                    matches.append((a, b))
        print(label, "affine matches:", matches)
    # Train a general one-to-one substitution on the five-letter crib.
    # Show exactly which held-out positions it predicts before fitting r12 or v5.
    for label, reverse in [("RTL", False), ("LTR", True)]:
        orient = lambda seq: seq[::-1] if reverse else seq
        key = dict(zip(orient(R11), crib))
        print(label, "crib predictions", *("".join(key.get(n, "?") for n in orient(seq))
                                           for seq in (R12, V5)))
