"""Conservative tests of Bohak's printed consonantal transcription, pp. 13–14.

Reading order is right to left. Rows contain interior cells only. A trailing
question mark denotes a doubtful reading, '-' an unidentified sign and '.'
an absent cell. All three are wildcards in the tests. The web text layer
has 23 interior tokens for line 2; try every possible one-token omission
when a model requires 22. No particular omission is endorsed.
"""

from collections import Counter
from math import gcd


TRANSCRIPTION = (
    "ו ד ו ה מ כ ח ג ט - כ - ז ה? צ ע? ב . . . . .",
    "ט ו י ח ג מ ב נ ד - ו ס כ ז ש ע נ - ז? צ? - י -",
    "כ מ ב - ה ד ו ע? ח ש? - ו א - - ט ג י ז ה - -",
    "ט ו י ח ג מ ב - ד נ ו ע ש כ ו ק ת ס? נ? צ ר? -",
)


def secure(token):
    return token not in ("-", ".") and "?" not in token


def compatible(a, b):
    return a == b or not (secure(a) and secure(b))


def maximum_matching(edges):
    """Maximum number of target columns assignable to distinct source columns."""
    owners = {}

    def assign(target, visited):
        for source in edges[target]:
            if source in visited:
                continue
            visited.add(source)
            if source not in owners or assign(owners[source], visited):
                owners[source] = target
                return True
        return False

    return sum(assign(i, set()) for i in range(len(edges)))


def suffix_test(second, fourth):
    # Full-row signs 1–13 have matching inventories, including the frame
    # and the reversed triplet. The two far-end frame signs are excluded.
    tails = [second[11:], fourth[11:]]
    assert list(map(len, tails)) == [12, 11]
    readings = [[t.removesuffix("?") for t in tail] for tail in tails]

    def match_count():
        return maximum_matching([
            [j for j, a in enumerate(readings[0]) if compatible(a, b)]
            for b in readings[1]
        ])

    print("Suffix matches retaining tentative readings:", match_count(), "of 11")
    alphabet = "אבגדהוזחטיכלמנסעפצקרשת"
    for row, tail in enumerate(tails):
        for i, token in enumerate(tail):
            if not token.endswith("?"):
                continue
            fits = []
            for candidate in alphabet:
                readings[row][i] = candidate
                if match_count() == 11:
                    fits.append(candidate)
            readings[row][i] = token[:-1]
            if fits:
                print("Single-reading alternatives, row", (2, 4)[row],
                      "full sign", i+14, "alphabet ranks",
                      [alphabet.index(letter)+1 for letter in fits])


def main():
    first, second, third, fourth = rows = [r.split() for r in TRANSCRIPTION]
    assert list(map(len, rows)) == [22, 23, 22, 22]
    # X carries the same angular lower mark in these three photographed cells.
    # A shared next sign, even with row-specific reversal, must have an upper
    # consonant in every pair of immediate neighbors.
    neighbors = []
    for row, full_pos in ((second, 12), (third, 6), (fourth, 10)):
        i = full_pos - 3  # strip the two right-frame cells and index from zero
        assert row[i] == "-"
        pair = {row[i-1], row[i+1]}
        assert all(secure(token) for token in pair)
        neighbors.append(pair)
    print("Common possible successor consonants of marked X:",
          len(set.intersection(*neighbors)))
    # Photo readings in interior coordinates. Descriptions are shape labels.
    # This count excludes row 2 and does not require a reading for sign X.
    marks = [(1, 1, "ו", "bent"), (3, 7, "ו", "angular"), (4, 11, "ו", "ring"),
             (1, 6, "כ", "ring"), (1, 11, "כ", "three dots"),
             (3, 1, "כ", "bent"), (4, 14, "כ", "angular")]
    known = {t for row in (first, third, fourth) for t in row if secure(t)}
    variants = {}
    for r, i, consonant, mark in marks:
        assert rows[r-1][i-1] == consonant
        variants.setdefault(consonant, set()).add(mark)
    print("Rows 1, 3, 4: distinct secure consonants", len(known),
          "minimum visibly distinguished combinations",
          len(known) + sum(len(forms)-1 for forms in variants.values()))
    # Try the vertical frame as input, using only the two distinct, undamaged
    # odd-row seeds. Each column supplies part of one letter transformation.
    columns = [dict((seed, letter) for seed, letter in zip("יו", pair)
                    if secure(letter)) for pair in zip(first, third)]
    conflicts = []
    for i, left in enumerate(columns):
        for j, right in enumerate(columns[:i]):
            for seed in left.keys() & right.keys():
                lr = left.get(right[seed])
                rl = right.get(left[seed])
                if lr is not None and rl is not None and lr != rl:
                    conflicts.append((j+1, i+1))
    print("Noncommuting interior-column pairs from rows 1 and 3:",
          sorted(set(conflicts)))
    suffix_test(second, fourth)
    for row in rows:
        counts = Counter(s for s in row if secure(s))
        print("Duplicate excess among secure readings:", sum(n-1 for n in counts.values()))

    required = Counter()
    for row in (first, third, fourth):
        required |= Counter(s for s in row if secure(s))
    lower_bounds = []
    for drop in range(len(second)):
        shortened = second[:drop] + second[drop+1:]
        counts = Counter(s for s in shortened if secure(s))
        lower_bounds.append(sum((required | counts).values()))
    print("Shortest common inventory, lower bound:", min(lower_bounds))

    for joint in (False, True):
        arbitrary, affine = [], []
        for drop in range(len(second)):
            source = second[:drop] + second[drop+1:]
            edges = [
                [j for j in range(22) if compatible(source[j], fourth[i])
                 and (not joint or compatible(first[j], third[i]))]
                for i in range(22)
            ]
            arbitrary.append(maximum_matching(edges))
            affine.append(max(
                sum((a*i+b) % 22 in edges[i] for i in range(22))
                for a in range(22) if gcd(a, 22) == 1 for b in range(22)
            ))
        print("Joint" if joint else "Even rows only",
              "best matched columns out of 22:",
              "unrestricted", max(arbitrary), "affine", max(affine))


if __name__ == "__main__":
    main()
