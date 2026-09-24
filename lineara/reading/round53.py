"""Round 53: consonant harmony in depth. Benjamini-Hochberg at 5% across the ten.

"Harmony" = neighbouring syllables with the same consonant and different signs (TA-TI, not SA-SA).

HC1  Non-adjacent harmony (syllables one apart) replicates on SigLA's transcription against Linear B.
HC2  Adjacent harmony with different signs replicates on SigLA against Linear B.
HC3  Harmony holds for obstruents (p t k d q s z) and sonorants (n r m w j) separately (larger p is primary).
HC4  Knossos names show harmony (different signs) more than Pylos names.
HC5  Eteocretan shows harmony (different signs) more than Greek.
HC6  The ratio of same-consonant to same-place-different-consonant neighbours is higher in Linear A than Linear B.
HC7  Harmony holds in three-sign words and in words of four or more signs separately (larger p is primary).
HC8  Harmony holds in Linear A words attested only once.
HC9  Two-sign words share a consonant between their syllables more often than in Linear B.
HC10 Linear A words with harmony are attested at more sites than other words (frequency held within strata).
"""
from collections import Counter, defaultdict
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round29 as P  # noqa: E402
import round37 as Z  # noqa: E402
import round49 as TT  # noqa: E402
import decipher15c as F15  # noqa: E402

B, T, G = R.B, R.T, R.G
cons = P.cons
LA, LB, SIG = R.LA, R.LB, G.SIG
harm = TT.harm
OBS, SON = set('ptkdqsz'), set('nrmwj')
skip1 = lambda ws: sum(1 for w in ws for i in range(len(w) - 2) if cons(w[i]) and cons(w[i]) == cons(w[i + 2])) / max(1, sum(max(0, len(w) - 2) for w in ws))


def cmp(a, b, f, text, lower=False):
    r, p, nm = R.compare(a, b, f, lower=lower)
    return p, text, {'target': round(f(a), 4), 'comparison': round(f(b), 4), 'p': round(p, 4), 'n': [len(a), len(b)]}, {}


def HC1():
    return cmp(SIG, LB, skip1, 'Non-adjacent harmony on SigLA vs Linear B')


def HC2():
    return cmp(SIG, LB, harm, 'Adjacent harmony (different signs) on SigLA vs Linear B')


def harm_class(cls):
    return lambda ws: sum(1 for w in ws for i in range(len(w) - 1) if cons(w[i]) in cls and cons(w[i]) == cons(w[i + 1]) and w[i] != w[i + 1]) / max(1, sum(1 for w in ws for i in range(len(w) - 1) if cons(w[i]) in cls))


def HC3():
    res, ps = {}, []
    for name, cls in (('obstruents', OBS), ('sonorants', SON)):
        f = harm_class(cls)
        r, p, nm = R.compare(LA, LB, f)
        res[name] = {'LA': round(f(LA), 4), 'LB': round(f(LB), 4), 'p': round(p, 4)}
        ps.append(p)
    return max(ps), 'Harmony holds for obstruents and sonorants separately', {**res, 'p (larger)': round(max(ps), 4)}, {}


def HC4():
    return cmp(T.KN_N, T.PY_N, harm, 'Knossos names show harmony more than Pylos names')


def HC5():
    a, b = Z.eteo()
    return cmp(a, b, harm, 'Eteocretan shows harmony more than Greek')


def ident_vs_place(ws):
    same = place = 0
    for w in ws:
        for i in range(len(w) - 1):
            a, b = cons(w[i]), cons(w[i + 1])
            if a in F15.PLACE and b in F15.PLACE:
                if a == b:
                    same += 1
                elif F15.PLACE[a] == F15.PLACE[b]:
                    place += 1
    return same / max(1, place)


def HC6():
    return cmp(LA, LB, ident_vs_place, 'Same consonant preferred over same place more than in Linear B')


def HC7():
    res, ps = {}, []
    for name, pred in (('3 signs', lambda w: len(w) == 3), ('4+ signs', lambda w: len(w) >= 4)):
        a, b = [w for w in LA if pred(w)], [w for w in LB if pred(w)]
        r, p, nm = R.compare(a, b, harm)
        res[name] = {'LA': round(harm(a), 4), 'LB': round(harm(b), 4), 'p': round(p, 4)}
        ps.append(p)
    return max(ps), 'Harmony holds in 3-sign and 4+-sign words separately', {**res, 'p (larger)': round(max(ps), 4)}, {}


def HC8():
    toks = Counter(w for _, _, w in B.words_of())
    hapax = [w for w in LA if toks.get(w, 0) == 1]
    return cmp(hapax, LB, harm, 'Harmony holds in words attested once')


def HC9():
    f = lambda ws: sum(1 for w in ws if cons(w[0]) and cons(w[0]) == cons(w[1])) / max(1, len(ws))
    return cmp([w for w in LA if len(w) == 2], [w for w in LB if len(w) == 2], f, 'Two-sign words share their consonant more often than in Linear B')


def HC10():
    sites = defaultdict(set)
    toks = Counter()
    for r, t, w in B.words_of():
        sites[w].add(r['site'])
        toks[w] += 1
    words = [w for w in sites if len(w) >= 2]
    flag = {w: any(cons(w[i]) and cons(w[i]) == cons(w[i + 1]) and w[i] != w[i + 1] for i in range(len(w) - 1)) for w in words}
    stratum = lambda n: 0 if n == 1 else 1 if n <= 3 else 2
    strata = defaultdict(list)
    for w in words:
        strata[stratum(toks[w])].append(w)

    def stat(fl):
        a = [len(sites[w]) for w in words if fl[w]]
        b = [len(sites[w]) for w in words if not fl[w]]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real = stat(flag)
    null = []
    for _ in range(R.REPS):
        fl = {}
        for ws in strata.values():
            labs = [flag[w] for w in ws]
            R.rng.shuffle(labs)
            fl.update(zip(ws, labs))
        null.append(stat(fl))
    p = R.pv_hi(null, real)
    return p, 'Words with harmony are attested at more sites', {'diff_mean_sites': round(real, 3), 'p': round(p, 4), 'harmonic_words': sum(flag.values())}, {}


if __name__ == '__main__':
    R.run('round53', 'consonant harmony in depth', __doc__, [HC1, HC2, HC3, HC4, HC5, HC6, HC7, HC8, HC9, HC10])
