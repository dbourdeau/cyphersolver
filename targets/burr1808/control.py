"""Control for the period-6 break: encipher a period English text of the same length as
section A with a random 6-place key (a=1..z=26 numbering, key running through the letters),
then run the same column chi-square solver used on the letter and check it recovers the key."""
import random
from collections import Counter

E = [8.17, 1.49, 2.78, 4.25, 12.7, 2.23, 2.02, 6.09, 6.97, .15, .77, 4.03, 2.41, 6.75, 7.51,
     1.93, .1, 5.99, 6.33, 9.06, 2.76, .98, 2.36, .15, 1.97, .07]

# Burr to Alston, New York, 18 July 1804, as printed by Davis, Memoirs, vol. 2 (1837) (clear text).
TEXT = ("The event of which you have been advised has driven me into a sort of exile and may terminate "
        "in an actual and permanent ostracism Our most unprincipled Jacobins are the loudest in their "
        "lamentations for the death of General Hamilton whom for many years they have uniformly "
        "represented as the most detestable and unprincipled of men the motives are obvious Every sort "
        "of persecution is to be exercised against me A coroners jury will sit this evening being the "
        "fourth time The object of this unexampled measure is to obtain an inquest of murder")


def solve(nums, p):
    key = []
    for i in range(p):
        c = Counter(nums[i::p])
        key.append(max(range(26), key=lambda k: sum(c[(j + k) % 26 + 1] * E[j] for j in range(26))))
    return key


if __name__ == '__main__':
    letters = [ch for ch in TEXT.lower() if ch.isalpha()][:341]   # section A has 341 numbers
    hits = 0
    for trial in range(20):
        rng = random.Random(trial)
        key = [rng.randrange(26) for _ in range(6)]
        nums = [((ord(ch) - 97) + key[i % 6]) % 26 + 1 for i, ch in enumerate(letters)]
        got = solve(nums, 6)
        ok = got == key
        hits += ok
        if trial < 3 or not ok:
            plain = ''.join(chr(97 + (n - 1 - got[i % 6]) % 26) for i, n in enumerate(nums))
            print(trial, key, got, ok, plain[:60])
    print(f'{len(letters)} letters: key recovered in {hits}/20 trials')
