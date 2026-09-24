"""Round 66 (saturation loop 8): fixed allocations, and what the fraction signs and final signs go with. BH at 5%
across the nine.

W1  A name-slot word on 2+ tablets gets similar amounts each time: the mean within-word variance of log amount
    (one mean per tablet) is lower than when amounts are shuffled among name-slot entries of the same site.
W2  The same for descriptor-slot words.
W3  A name-slot word on 2+ tablets gets exactly the same amount on two tablets more often than chance (same shuffle).
W4  Fraction signs are associated with the commodity of their tablet (single-commodity tablets).
W5  Fraction signs are associated with site.
W6  At Haghia Triada, fraction signs are associated with scribe.
W7  The final sign of name-slot words is associated with the commodity of the tablet.
W8  The final sign of descriptor-slot words is associated with the commodity they stand before.
W9  Name-slot words on 2+ tablets stand on tablets of the same commodity more often than chance (commodities of
    single-commodity tablets shuffled among the word's tablets' site).
"""
from collections import Counter, defaultdict
from math import log
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round59 as N  # noqa: E402
import round61 as QQ  # noqa: E402

B, X = R.B, R.X
TOK, DESC, NAME = N.TOK, N.DESC, N.NAME
TCOM = {k: next(iter(v['com'])) for k, v in QQ.ST.items() if len(v['com']) == 1}
MAIN_FR = ['¹⁄2', '¹⁄4', '≈ ¹⁄6', '³⁄4', '¹⁄16', '¹⁄3', '¹⁄5', '¹⁄8']


def per_word(items):
    """word -> {tablet: mean log amount} for words on 2+ tablets."""
    d = defaultdict(lambda: defaultdict(list))
    for x in items:
        d[x['label']][X.whole(x['rec'])].append(log(x['q']))
    return {w: {t: sum(v) / len(v) for t, v in tabs.items()} for w, tabs in d.items() if len(tabs) >= 2}


def var(v):
    m = sum(v) / len(v)
    return sum((a - m) ** 2 for a in v) / len(v)


def consistency(pool, stat):
    items = [x for x in pool if x['q'] > 0]
    real = stat(per_word(items))
    by = defaultdict(list)
    for i, x in enumerate(items):
        by[x['site']].append(i)
    null = []
    for _ in range(R.REPS):
        qs = [x['q'] for x in items]
        for idx in by.values():
            v = [qs[i] for i in idx]
            R.rng.shuffle(v)
            for i, a in zip(idx, v):
                qs[i] = a
        null.append(stat(per_word([dict(x, q=q) for x, q in zip(items, qs)])))
    return real, null


def mean_var(pw):
    return sum(var(list(t.values())) for t in pw.values()) / max(1, len(pw))


def exact(pw):
    return sum(1 for t in pw.values() if len(set(round(v, 6) for v in t.values())) < len(t))


def W1():
    real, null = consistency(NAME, mean_var)
    p = R.pv_lo(null, real)
    return p, 'A recurring name gets similar amounts', {'mean_var': round(real, 3), 'null': round(sum(null) / len(null), 3), 'p': round(p, 4), 'words': len(per_word([x for x in NAME if x['q'] > 0]))}, {}


def W2():
    real, null = consistency(DESC, mean_var)
    p = R.pv_lo(null, real)
    return p, 'A recurring descriptor gets similar amounts', {'mean_var': round(real, 3), 'null': round(sum(null) / len(null), 3), 'p': round(p, 4), 'words': len(per_word([x for x in DESC if x['q'] > 0]))}, {}


def W3():
    real, null = consistency(NAME, exact)
    p = R.pv_hi(null, real)
    return p, 'A recurring name gets exactly the same amount on two tablets', {'words_with_repeat': real, 'null': round(sum(null) / len(null), 2), 'p': round(p, 4)}, {}


def fractions():
    out = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        k = X.whole(r['name'])
        for t in r['tokens']:
            if t['cls'] == 'fraction' and t['label'] in MAIN_FR:
                out.append({'fr': t['label'], 'site': r['site'], 'com': TCOM.get(k), 'scribe': X.SCRIBE_W.get(k)})
    return out


FR = fractions()


def chi(pairs, min_a=5):
    c = Counter(a for a, _ in pairs)
    pairs = [x for x in pairs if c[x[0]] >= min_a]
    real, p, nm = R.assoc(pairs)
    return p, {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'n': len(pairs), 'groups': dict(Counter(a for a, _ in pairs))}


def W4():
    p, d = chi([(x['com'], x['fr']) for x in FR if x['com']])
    return p, 'Fraction signs go with the commodity', d, {}


def W5():
    p, d = chi([(x['site'], x['fr']) for x in FR])
    return p, 'Fraction signs differ by site', d, {}


def W6():
    p, d = chi([(x['scribe'], x['fr']) for x in FR if x['site'] == 'Haghia Triada' and x['scribe']])
    return p, 'Fraction signs differ by Haghia Triada scribe', d, {}


def W7():
    p, d = chi([(TCOM[X.whole(x['rec'])], x['label'].split('-')[-1]) for x in NAME if X.whole(x['rec']) in TCOM and '-' in x['label']])
    return p, 'Final sign of name words goes with the tablet commodity', d, {}


def W8():
    p, d = chi([(x['com'], x['label'].split('-')[-1]) for x in DESC if x['com'] and '-' in x['label']])
    return p, 'Final sign of descriptor words goes with the commodity', d, {}


def W9():
    tabs = defaultdict(set)
    for x in NAME:
        k = X.whole(x['rec'])
        if k in TCOM:
            tabs[x['label']].add(k)
    words = {w: sorted(t) for w, t in tabs.items() if len(t) >= 2}
    alltabs = sorted({t for ts in words.values() for t in ts})
    coms = [TCOM[t] for t in alltabs]

    def stat(cm):
        m = dict(zip(alltabs, cm))
        return sum(1 for ts in words.values() if len({m[t] for t in ts}) == 1)
    real = stat(coms)
    null = []
    for _ in range(R.REPS):
        c2 = list(coms)
        R.rng.shuffle(c2)
        null.append(stat(c2))
    p = R.pv_hi(null, real)
    return p, 'A recurring name stays with one commodity', {'single_commodity_words': f'{real}/{len(words)}', 'null': round(sum(null) / len(null), 2), 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round66', 'fixed allocations, fraction signs and final signs', __doc__, [W1, W2, W3, W4, W5, W6, W7, W8, W9])
