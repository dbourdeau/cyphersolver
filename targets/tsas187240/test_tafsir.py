"""Compare two glyph rows with the opening of Psalm 45 in BL Or 2375."""

from itertools import accumulate, product

from test_alphabet import B1, B2, FOLD


# The witness alternates the Hebrew and Judeo-Arabic. Only the Arabic is used.
# The first uncertain word is represented by three unknown consonants.
# Vary the uncertain transcription before the final clause, rather
# than using a guessed letter as evidence against a reading.
OPENING = "??? קלבי כלאמא {good} פאנא אקול מא אצפה מן מתל דאך {unknown} "
ENDING = "מא יכון לסאני בה חרכא כקלם כאתב מאהר"


def discrepancies(signs, text):
    key = {}
    failures = []
    for pos, (sign, letter) in enumerate(zip(signs, text, strict=True), 1):
        if letter == "?":
            continue
        oldpos, oldletter = key.setdefault(sign, (pos, letter))
        if oldletter != letter:
            failures.append((sign, oldpos, oldletter, pos, letter))
    return failures


if __name__ == "__main__":
    ending = ENDING.replace(" ", "").translate(FOLD)
    for direction in (1, -1):
        print("29-letter ending", direction,
              discrepancies(B1[::direction] + B2[::direction], ending))
    for single_wave in (False, True):
        second = B2[:7] + B2[8:] if single_wave else B2
        best = 3
        matches = set()
        bounded = set()
        for good, width in product(("גידא", "גיידא"), range(4, 8)):
            words = (OPENING.format(good=good, unknown="?" * width) + ENDING).split()
            text = "".join(words).translate(FOLD)
            boundaries = set(accumulate(map(len, words), initial=0))
            for first, direction in product((B1, B1[1:]), (1, -1)):
                signs = first[::direction] + second[::direction]
                for offset in range(len(text) - len(signs) + 1):
                    excerpt = text[offset:offset+len(signs)]
                    misses = len(discrepancies(signs, excerpt))
                    best = min(best, misses)
                    if misses == 0:
                        matches.add(excerpt)
                        if offset in boundaries and offset+len(signs) in boundaries:
                            bounded.add(excerpt)
        print("single wave", single_wave, "minimum conflicts", best,
              "compatible distinct windows", len(matches),
              "fully transcribed", sum("?" not in s for s in matches),
              "fully transcribed with both boundaries", sum("?" not in s for s in bounded))
        for excerpt in sorted(s for s in matches if "?" not in s):
            print(" ", excerpt)
