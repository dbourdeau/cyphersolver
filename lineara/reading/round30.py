"""Round 30 (loop round 2 of 10): the vowel system in detail.

Q1  e/o follow T (alone) more than non-coronals, more than in Linear B.
Q2  e/o follow S and N more than K, P and M, more than in Linear B.
Q3  e/o follow Q more than K (QE/QO against KE/KO), more than in Linear B.
Q4  In Linear A, o is word-final more often than e is.
Q5  a followed by a (a-harmony) exceeds chance within Linear A words (signs shuffled within words), more than in
    Linear B.
Q6  High vowels (i, u) co-occur within a word beyond chance, more than in Linear B.
Q7  e/o are commoner in Linear A words of 3+ signs than in two-sign words.
Q8  e/o are commoner in entry labels (names) than in headings.
Q9  e/o are commoner in religious words than in administrative words.
Q10 Among pure vowel signs, E and O are rarer relative to CV e/o signs in Linear A than in Linear B.
"""
from collections import Counter, defaultdict
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402

grid, LA, LB, X, B = R.grid, R.LA, R.LB, R.X, R.B
RARE = R.RARE
NONCOR = set('pmwkqj')


def lor(ws, a, b):
    return X.log_or_v(ws, RARE, cons_sets=(set(a), set(b)))


def cmp_lor(a, b, text):
    f = lambda ws: lor(ws, a, b)
    r, p, nm = R.compare(LA, LB, f)
    return p, text, {'logOR_LA': round(f(LA), 3), 'logOR_LB': round(f(LB), 3), 'p': round(p, 4)}, {}


def Q1():
    return cmp_lor('t', NONCOR, 'e/o follow T alone more than non-coronals, more than in Linear B')


def Q2():
    return cmp_lor('sn', 'kpm', 'e/o follow S and N more than K, P, M, more than in Linear B')


def Q3():
    return cmp_lor('q', 'k', 'e/o follow Q more than K, more than in Linear B')


def Q4():
    rows = [(grid(x)[1], i == len(w) - 1) for w in LA for i, x in enumerate(w) if grid(x) and grid(x)[1] in 'eo']
    r, p, a, b = R.flag_compare(rows, lambda x: x[0] == 'o', lambda x: x[1])
    return p, 'In Linear A, o is word-final more often than e', {'o_final': a, 'e_final': b, 'p': round(p, 4)}, {}


def within_shuffle_excess(ws, pair_ok, reps=500):
    def count(wl):
        return sum(1 for w in wl for i in range(len(w) - 1) if pair_ok(w[i], w[i + 1]))
    real = count(ws)
    null = []
    for _ in range(reps):
        sh = []
        for w in ws:
            w2 = list(w)
            R.rng.shuffle(w2)
            sh.append(w2)
        null.append(count(sh))
    return real / (sum(null) / len(null))


def Q5():
    ok = lambda a, b: bool(grid(a)) and bool(grid(b)) and grid(a)[1] == 'a' and grid(b)[1] == 'a'
    la = within_shuffle_excess([w for w in LA if len(w) >= 3], ok)
    lb = within_shuffle_excess([w for w in LB if len(w) >= 3], ok, reps=200)
    boot = []
    L3 = [w for w in LA if len(w) >= 3]
    for _ in range(200):
        smp = [R.rng.choice(L3) for _ in L3]
        boot.append(within_shuffle_excess(smp, ok, reps=50))
    p = R.pv_lo([b_ - lb for b_ in boot], 0.0)
    return p, 'a-a sequences exceed chance within Linear A words more than in Linear B', {'LA_ratio': round(la, 3), 'LB_ratio': round(lb, 3), 'bootstrap p': round(p, 4)}, {}


def cooc(ws, cls):
    def stat(wl):
        return sum(1 for w in wl if sum(1 for x in w if grid(x) and grid(x)[1] in cls) >= 2) / len(wl)
    real = stat(ws)
    flat = [x for w in ws for x in w]
    null = []
    for _ in range(300):
        R.rng.shuffle(flat)
        k, sh = 0, []
        for w in ws:
            sh.append(flat[k:k + len(w)])
            k += len(w)
        null.append(stat(sh))
    return real / (sum(null) / len(null))


def Q6():
    la = cooc(LA, 'iu')
    lb = cooc(LB, 'iu')
    boot = []
    for _ in range(100):
        smp = [R.rng.choice(LA) for _ in LA]
        boot.append(cooc(smp, 'iu'))
    p = R.pv_lo([b_ - lb for b_ in boot], 0.0)
    return p, 'High vowels co-occur within words beyond chance, more than in Linear B', {'LA_ratio': round(la, 3), 'LB_ratio': round(lb, 3), 'bootstrap p': round(p, 4)}, {}


eo_share = lambda ws: sum(1 for w in ws for x in w if grid(x) and grid(x)[1] in RARE) / max(1, sum(1 for w in ws for x in w if grid(x)))


def Q7():
    long_ = [w for w in LA if len(w) >= 3]
    short = [w for w in LA if len(w) == 2]
    r, p, nm = R.compare(long_, short, eo_share)
    return p, 'e/o are commoner in Linear A words of 3+ signs than in two-sign words', {'long': round(eo_share(long_), 3), 'short': round(eo_share(short), 3), 'p': round(p, 4)}, {}


def functions():
    fn = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        fn[w][t.get('function')] += 1
    return {w: c.most_common(1)[0][0] for w, c in fn.items()}


def Q8():
    fn = functions()
    ent = [w for w, f in fn.items() if f == 'entry label']
    head = [w for w, f in fn.items() if f == 'heading']
    r, p, nm = R.compare(ent, head, eo_share)
    return p, 'e/o are commoner in entry labels than in headings', {'entries': round(eo_share(ent), 3), 'headings': round(eo_share(head), 3), 'p': round(p, 4)}, {}


def Q9():
    rel = sorted({w for _, _, w in B.LA_RELIG})
    adm = sorted({w for _, _, w in B.LA_ADMIN} - set(rel))
    r, p, nm = R.compare(rel, adm, eo_share)
    return p, 'e/o are commoner in religious words than in administrative words', {'religious': round(eo_share(rel), 3), 'admin': round(eo_share(adm), 3), 'p': round(p, 4)}, {}


def Q10():
    def ratio(ws):
        pv = [x for w in ws for x in w if grid(x) and grid(x)[0] == '']
        cv = [x for w in ws for x in w if grid(x) and grid(x)[0]]
        pv_eo = sum(grid(x)[1] in RARE for x in pv) / max(1, len(pv))
        cv_eo = sum(grid(x)[1] in RARE for x in cv) / max(1, len(cv))
        return pv_eo - cv_eo
    r, p, nm = R.compare(LA, LB, ratio, lower=True)
    return p, 'E/O are rarer among pure vowel signs, relative to CV e/o, in Linear A than in Linear B', {'LA_gap': round(ratio(LA), 3), 'LB_gap': round(ratio(LB), 3), 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round30', 'the vowel system in detail', __doc__, [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10])
