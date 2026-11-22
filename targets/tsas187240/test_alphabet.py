"""Count alphabet keys conditional on the working B1/B2 transcription."""

from itertools import combinations


B1 = (1, 2, 3, 4, 5, 6, 10, 7, 8, 9, 3, 11, 12, 13, 14)
B2 = (15, 16, 17, 18, 19, 20, 21, 21, 16, 22, 23, 24, 25, 27)
C2 = (15, 16, 16, 17, 28, 22, 22, 23, 24, 25, 26, 27)
ALPHABET = "אבגדהוזחטיכךלמםנןסעפףצץקרשת"
FOLD = str.maketrans("ךםןףץ", "כמנפצ")


def fit_keys(signs, letters, omit_letter):
    """Equal signs require equal letters. Different signs may share a letter."""
    keys = set()
    remove_count = len(signs) - len(letters) + int(omit_letter)
    for removed in combinations(range(len(signs)), remove_count):
        remaining = [sign for i, sign in enumerate(signs) if i not in removed]
        for omit in (range(len(letters)) if omit_letter else (-1,)):
            target = [letter for i, letter in enumerate(letters) if i != omit]
            pairs = list(zip(remaining, target, strict=True))
            key = dict(pairs)
            if all(key[sign] == letter for sign, letter in pairs):
                keys.add(tuple(sorted(key.items())))
    return keys


if __name__ == "__main__":
    for direction in (1, -1):
        signs = B1[::direction] + B2[::direction]
        for letters in (ALPHABET, ALPHABET.translate(FOLD)):
            for omit_letter in (False, True):
                keys = fit_keys(signs, letters, omit_letter)
                print(direction, 'folded' if letters != ALPHABET else 'distinct',
                      'omissions', int(omit_letter), 'keys', len(keys))
                if len(keys) == 2:
                    for key in sorted(keys):
                        print('  C2', ''.join(dict(key).get(s, '?') for s in C2[::direction]))
