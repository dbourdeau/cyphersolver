"""Round 46 (second loop, round 8 of 10): the religious and administrative vocabularies.

II1  Words found in both registers are entry labels (names) in the administrative texts more often than other words.
II2  Religious words begin with a pure vowel sign more often than administrative words.
II3  Religious words repeat the consonant of neighbouring syllables more often.
II4  Religious words contain Z-row signs more often.
II5  Administrative words that also occur in religious texts are attested at more sites.
II6  Religious words are two-sign words less often.
II7  Religious words repeat a whole syllable in succession (SA-SA) more often.
II8  Inked inscriptions are closer in syllable use to administrative texts than to stone-vessel dedications.
II9  Religious inscriptions on the same object type share words more than inscriptions on different types.
II10 Religious words match Knossos Linear B words (exactly or as stem + one syllable) more often than
     administrative words.
"""
from collections import Counter, defaultdict
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round29 as P  # noqa: E402
import round36 as Y  # noqa: E402
import round41 as DD  # noqa: E402

B, X, V = R.B, R.X, R.V
cons = P.cons
REL = sorted({w for _, _, w in B.LA_RELIG})
ADM = sorted({w for _, _, w in B.LA_ADMIN} - set(REL))
BOTH = sorted({w for _, _, w in B.LA_RELIG} & {w for _, _, w in B.LA_ADMIN})


def cmp(a, b, f, text, lower=False):
    r, p, nm = R.compare(a, b, f, lower=lower)
    return p, text, {'religious': round(f(a), 4), 'admin': round(f(b), 4), 'p': round(p, 4), 'n': [len(a), len(b)]}, {}


def II1():
    fn = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        fn[w][t.get('function')] += 1
    words = sorted(fn)
    both = set(BOTH)
    r_, p, a, b = R.flag_compare(words, lambda w: w in both, lambda w: fn[w].most_common(1)[0][0] == 'entry label')
    return p, 'Words in both registers are entry labels more often', {'shared_words_entry': a, 'other_entry': b, 'p': round(p, 4)}, {'shared words': ['-'.join(w).upper() for w in BOTH]}


def II2():
    return cmp(REL, ADM, lambda ws: sum(1 for w in ws if P.vow(w[0])) / len(ws), 'Religious words begin with a pure vowel more often')


def II3():
    f = lambda ws: sum(1 for w in ws for i in range(len(w) - 1) if cons(w[i]) and cons(w[i]) == cons(w[i + 1])) / max(1, sum(len(w) - 1 for w in ws))
    return cmp(REL, ADM, f, 'Religious words repeat neighbouring consonants more often')


def II4():
    return cmp(REL, ADM, lambda ws: sum(1 for w in ws if any(cons(x) == 'z' for x in w)) / len(ws), 'Religious words contain Z-row signs more often')


def II5():
    sites = defaultdict(set)
    for r, t, w in B.LA_ADMIN:
        sites[w].add(r['site'])
    words = sorted(sites)
    both = set(BOTH)
    r_, p, a, b = R.flag_compare(words, lambda w: w in both, lambda w: len(sites[w]))
    return p, 'Administrative words also found in religious texts occur at more sites', {'shared_mean_sites': a, 'other': b, 'p': round(p, 4)}, {}


def II6():
    return cmp(REL, ADM, lambda ws: sum(1 for w in ws if len(w) == 2) / len(ws), 'Religious words are two-sign words less often', lower=True)


def II7():
    return cmp(REL, ADM, lambda ws: sum(1 for w in ws if any(w[i] == w[i + 1] for i in range(len(w) - 1))) / len(ws), 'Religious words repeat a whole syllable more often')


def II8():
    by = defaultdict(list)
    for r in Y.REL:
        for w in r['words']:
            parts = w.split('-')
            if all(re.fullmatch(r'[A-Z]+[0-9]?', x) for x in parts):
                by[r['support']].append(tuple(x.lower() for x in parts))
    inked, stone = by.get('Inked inscription', []), by.get('Stone vessel', [])
    adm = [w for _, _, w in B.LA_ADMIN]
    f = lambda ink: DD.jsd_words(ink, stone) - DD.jsd_words(ink, adm)
    real = f(inked)
    pool, k, null = inked + stone, len(inked), []
    for _ in range(R.REPS):
        R.rng.shuffle(pool)
        null.append(DD.jsd_words(pool[:k], pool[k:]) - DD.jsd_words(pool[:k], adm))
    p = R.pv_hi(null, real)
    return p, 'Inked inscriptions are closer to administrative texts than to stone dedications', {'jsd_to_stone_minus_admin': round(real, 4), 'null': round(sum(null) / len(null), 4), 'p': round(p, 4), 'n': [len(inked), len(stone)]}, {}


def II9():
    items = [(r['support'], set(r['words'])) for r in Y.REL]
    items = [x for x in items if x[1]]
    pairs = [(i, j) for i in range(len(items)) for j in range(i + 1, len(items))]
    share = {(i, j): bool(items[i][1] & items[j][1]) for i, j in pairs}
    labs = [s for s, _ in items]

    def stat(ls):
        same = [v for (i, j), v in share.items() if ls[i] == ls[j]]
        diff = [v for (i, j), v in share.items() if ls[i] != ls[j]]
        return sum(same) / max(1, len(same)) - sum(diff) / max(1, len(diff))
    real, p, nm = X.shuffle_test(stat, labs, reps=R.REPS)
    return p, 'Same object type shares words more than different types', {'diff': round(real, 4), 'null': round(nm, 4), 'p': round(p, 4), 'inscriptions': len(items)}, {}


def II10():
    return cmp(REL, ADM, lambda ws: sum(1 for w in ws if DD.kn_match(w)) / len(ws), 'Religious words match Knossos words more often')


if __name__ == '__main__':
    R.run('round46', 'the religious and administrative vocabularies', __doc__, [II1, II2, II3, II4, II5, II6, II7, II8, II9, II10])
