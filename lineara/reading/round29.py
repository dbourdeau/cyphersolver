"""Round 29 (loop round 1 of 10): spelling and sound patterns of Linear A words, each against Linear B.

P1  Linear A words begin with a pure vowel sign more often than Linear B words.
P2  Linear A writes two pure vowel signs in succession (hiatus) more often than Linear B.
P3  o-signs stand word-initially more often than other signs in Linear A, more so than in Linear B.
P4  After an a-syllable, Linear A has an i or u vowel sign (a diphthong such as A-I, TA-I) more often than Linear B.
P5  Linear A words begin with a repeated syllable (KI-KI-, QA-QA-) more often than Linear B words.
P6  Q-row signs stand word-initially more often in Linear A than in Linear B.
P7  R-row signs stand word-initially less often in Linear A than in Linear B.
P8  In Linear A the final syllable has vowel a more often than internal syllables do, more so than in Linear B.
P9  Linear A words end in a pure vowel sign more often than Linear B words.
P10 The next sign is more predictable from the current one in Linear A than in Linear B (conditional entropy,
    Linear B subsampled to Linear A's size).
"""
from collections import Counter
from math import log
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402

grid, LA, LB = R.grid, R.LA, R.LB
vow = lambda x: bool(grid(x)) and grid(x)[0] == ''
cons = lambda x: grid(x)[0] if grid(x) else None


def share(ws, pred):
    return sum(1 for w in ws if pred(w)) / len(ws)


def P1():
    f = lambda ws: share(ws, lambda w: vow(w[0]))
    r, p, nm = R.compare(LA, LB, f)
    return p, 'Linear A words begin with a pure vowel more often than Linear B words', {'LA': round(f(LA), 3), 'LB': round(f(LB), 3), 'p': round(p, 4)}, {}


def P2():
    f = lambda ws: share(ws, lambda w: any(vow(w[i]) and vow(w[i + 1]) for i in range(len(w) - 1)))
    r, p, nm = R.compare(LA, LB, f)
    return p, 'Linear A writes two pure vowel signs in succession more often', {'LA': round(f(LA), 3), 'LB': round(f(LB), 3), 'p': round(p, 4)}, {}


def initial_share(ws, pred):
    occ = [(i == 0) for w in ws for i, x in enumerate(w) if pred(x)]
    return sum(occ) / max(1, len(occ))


def P3():
    o = lambda x: bool(grid(x)) and grid(x)[1] == 'o'
    f = lambda ws: initial_share(ws, o) - initial_share(ws, lambda x: bool(grid(x)) and grid(x)[1] != 'o')
    r, p, nm = R.compare(LA, LB, f)
    return p, 'o-signs are word-initial more than other signs, more so than in Linear B', {'LA_gap': round(f(LA), 3), 'LB_gap': round(f(LB), 3), 'p': round(p, 4)}, {}


def P4():
    def f(ws):
        pairs = [(w[i], w[i + 1]) for w in ws for i in range(len(w) - 1) if grid(w[i]) and grid(w[i])[1] == 'a']
        return sum(1 for a, b in pairs if b in ('i', 'u')) / max(1, len(pairs))
    r, p, nm = R.compare(LA, LB, f)
    return p, 'After an a-syllable, Linear A has I or U more often (diphthongs)', {'LA': round(f(LA), 4), 'LB': round(f(LB), 4), 'p': round(p, 4)}, {}


def P5():
    f = lambda ws: share(ws, lambda w: len(w) >= 3 and w[0] == w[1])
    r, p, nm = R.compare(LA, LB, f)
    return p, 'Linear A words begin with a repeated syllable more often', {'LA': round(f(LA), 4), 'LB': round(f(LB), 4), 'p': round(p, 4)}, {}


def P6():
    f = lambda ws: initial_share(ws, lambda x: cons(x) == 'q')
    r, p, nm = R.compare(LA, LB, f)
    return p, 'Q-row signs are word-initial more often in Linear A', {'LA': round(f(LA), 3), 'LB': round(f(LB), 3), 'p': round(p, 4)}, {}


def P7():
    f = lambda ws: initial_share(ws, lambda x: cons(x) == 'r')
    r, p, nm = R.compare(LA, LB, f, lower=True)
    return p, 'R-row signs are word-initial less often in Linear A', {'LA': round(f(LA), 3), 'LB': round(f(LB), 3), 'p': round(p, 4)}, {}


def P8():
    def f(ws):
        fin = [grid(w[-1])[1] == 'a' for w in ws if grid(w[-1])]
        inn = [grid(x)[1] == 'a' for w in ws for x in w[:-1] if grid(x)]
        return sum(fin) / len(fin) - sum(inn) / len(inn)
    r, p, nm = R.compare(LA, LB, f)
    return p, 'Final syllables favour a over internal ones more in Linear A', {'LA_gap': round(f(LA), 3), 'LB_gap': round(f(LB), 3), 'p': round(p, 4)}, {}


def P9():
    f = lambda ws: share(ws, lambda w: vow(w[-1]))
    r, p, nm = R.compare(LA, LB, f)
    return p, 'Linear A words end in a pure vowel sign more often', {'LA': round(f(LA), 3), 'LB': round(f(LB), 3), 'p': round(p, 4)}, {}


def cond_entropy(ws):
    pairs = Counter((w[i], w[i + 1]) for w in ws for i in range(len(w) - 1))
    first = Counter()
    for (a, b), n in pairs.items():
        first[a] += n
    tot = sum(pairs.values())
    return -sum(n / tot * log(n / first[a]) for (a, b), n in pairs.items())


def P10():
    real = cond_entropy(LA)
    n = sum(len(w) - 1 for w in LA)
    null = []
    for _ in range(500):
        smp, k = [], 0
        while k < n:
            w = R.rng.choice(LB)
            smp.append(w)
            k += len(w) - 1
        null.append(cond_entropy(smp))
    p = R.pv_lo(null, real)
    return p, 'The next sign is more predictable in Linear A than in size-matched Linear B', {'LA_H': round(real, 3), 'LB_H_subsampled': round(sum(null) / len(null), 3), 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round29', 'spelling and sound patterns', __doc__, [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10])
