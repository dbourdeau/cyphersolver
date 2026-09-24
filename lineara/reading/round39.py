"""Round 39 (second loop, round 1 of 10): word-shape follow-ups, each against Linear B.

BB1  The Q-initial pattern holds counting each word-initial sign pair (first two signs) once.
BB2  J-row signs are word-initial less often in Linear A than in Linear B.
BB3  W-row signs are word-final less often in Linear A than in Linear B.
BB5  Special signs (pa3, ra2, ta2, pu2) are word-internal more often in Linear A than in Linear B.
BB6  Neighbouring syllables repeat the same consonant more often in Linear A than in Linear B.
BB7  Initial and final consonant distributions differ more in Linear A than in Linear B (JSD).
BB8  Z-row signs are word-final more often in Linear A than in Linear B.
BB9  First syllables favour a over later syllables more in Linear A than in Linear B.
BB10 Linear A words that begin with a Q-row sign are entry labels more often than other words.
BB11 Word-final consonants are more restricted (lower entropy relative to initial) in Linear A than in Linear B.
"""
from collections import Counter, defaultdict
from math import log, log2
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round29 as P  # noqa: E402

grid, LA, LB, B = R.grid, R.LA, R.LB, R.B
cons = P.cons
SPECIAL = {'pa3', 'ra2', 'ta2', 'pu2'}


def cmp(f, text, lower=False, a=LA, b=LB):
    r, p, nm = R.compare(a, b, f, lower=lower)
    return p, text, {'LA': round(f(a), 4), 'LB': round(f(b), 4), 'p': round(p, 4)}, {}


def BB1():
    uniq = lambda ws: sorted({w[:2] for w in ws if len(w) >= 2})
    f = lambda ws: P.initial_share(uniq(ws), lambda x: cons(x) == 'q')
    return cmp(f, 'Q-initial share counting each initial sign pair once')


def pos_share(ws, pred, where):
    occ = [(i == 0) if where == 'initial' else (i == len(w) - 1) for w in ws for i, x in enumerate(w) if pred(x)]
    return sum(occ) / max(1, len(occ))


def BB2():
    return cmp(lambda ws: pos_share(ws, lambda x: cons(x) == 'j', 'initial'), 'J-row signs word-initial less often', lower=True)


def BB3():
    return cmp(lambda ws: pos_share(ws, lambda x: cons(x) == 'w', 'final'), 'W-row signs word-final less often', lower=True)


def BB5():
    f = lambda ws: sum(1 for w in ws for i, x in enumerate(w) if x in SPECIAL and 0 < i < len(w) - 1) / max(1, sum(1 for w in ws for x in w if x in SPECIAL))
    return cmp(f, 'Special signs word-internal more often')


def BB6():
    f = lambda ws: sum(1 for w in ws for i in range(len(w) - 1) if cons(w[i]) and cons(w[i]) == cons(w[i + 1])) / max(1, sum(len(w) - 1 for w in ws))
    return cmp(f, 'Neighbouring syllables repeat the consonant more often')


def dist(ws, idx):
    c = Counter(cons(w[idx]) or 'V' for w in ws if grid(w[idx]))
    n = sum(c.values())
    return {k: v / n for k, v in c.items()}


def jsd(p, q):
    keys = set(p) | set(q)
    m = {k: (p.get(k, 0) + q.get(k, 0)) / 2 for k in keys}
    kl = lambda a: sum(a[k] * log2(a[k] / m[k]) for k in keys if a.get(k, 0) > 0)
    return (kl(p) + kl(q)) / 2


def BB7():
    return cmp(lambda ws: jsd(dist(ws, 0), dist(ws, -1)), 'Initial and final consonant distributions differ more')


def BB8():
    return cmp(lambda ws: pos_share(ws, lambda x: cons(x) == 'z', 'final'), 'Z-row signs word-final more often')


def BB9():
    def f(ws):
        first = [grid(w[0])[1] == 'a' for w in ws if grid(w[0])]
        rest = [grid(x)[1] == 'a' for w in ws for x in w[1:] if grid(x)]
        return sum(first) / len(first) - sum(rest) / len(rest)
    return cmp(f, 'First syllables favour a over later syllables more')


def BB10():
    fn = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        fn[w][t.get('function')] += 1
    words = sorted(fn)
    r_, p, a, b = R.flag_compare(words, lambda w: cons(w[0]) == 'q', lambda w: fn[w].most_common(1)[0][0] == 'entry label')
    return p, 'Q-initial words are entry labels more often', {'Q_initial': a, 'other': b, 'p': round(p, 4)}, {}


def ent(d):
    return -sum(v * log(v) for v in d.values() if v > 0)


def BB11():
    return cmp(lambda ws: ent(dist(ws, -1)) - ent(dist(ws, 0)), 'Final consonants more restricted than initial ones', lower=True)


if __name__ == '__main__':
    R.run('round39', 'word-shape follow-ups', __doc__, [BB1, BB2, BB3, BB5, BB6, BB7, BB8, BB9, BB10, BB11])
