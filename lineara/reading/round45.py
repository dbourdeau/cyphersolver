"""Round 45 (second loop, round 7 of 10): the signs.

HH1  Unread signs are word-initial more often than known signs.
HH3  The single signs used on tablets are the commonest syllables of Linear A words (Spearman over signs).
HH4  Single signs on sealings differ in repertoire from single signs on tablets.
HH5  *301 is word-internal (neither first nor last) more often than other signs.
HH6  Unread signs stand next to other unread signs more often than chance (signs shuffled within words).
HH7  Unread signs are confined to fewer word types per occurrence than known signs.
HH8  The single sign ZE is followed directly by a number more often than other single signs.
HH11 The single sign NI is followed directly by a number more often than other single signs.
HH15 Syllable signs are associated with register (religious against administrative), whole inventory.
HH16 Signs that Linear B uses word-finally are relatively rarer in Linear A (Spearman of Linear B final share
     against log(LA frequency / LB frequency), predicted negative).
"""
from collections import Counter, defaultdict
from math import log
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402

B, X, D = R.B, R.X, R.D
UNREAD = re.compile(r'^\*\d+[A-Z]?$')
KNOWN = re.compile(r'^[A-Z]+[0-9]?$')


def word_tokens(pred=lambda r: True):
    out = []
    for r in B.READ['records']:
        if not pred(r):
            continue
        for t in r['tokens']:
            if t['cls'] in ('word', 'word-with-unknown-sign', 'term') and '-' in t['label']:
                parts = t['label'].split('-')
                if all(UNREAD.match(x) or KNOWN.match(x) for x in parts):
                    out.append(parts)
    return out


WT = word_tokens()
WTYPES = sorted({tuple(w) for w in WT})


def HH1():
    occ = [(bool(UNREAD.match(x)), i == 0) for w in WTYPES for i, x in enumerate(w)]
    r_, p, a, b = R.flag_compare(occ, lambda o: o[0], lambda o: o[1])
    return p, 'Unread signs are word-initial more often than known signs', {'unread_initial': a, 'known_initial': b, 'p': round(p, 4)}, {}


def singles(pred=lambda r: True):
    out = []
    for r in B.READ['records']:
        if not pred(r):
            continue
        toks = r['tokens']
        for i, t in enumerate(toks):
            if t['cls'] == 'single-sign' and KNOWN.match(t['label']):
                nxt = toks[i + 1] if i + 1 < len(toks) else None
                out.append((t['label'], bool(nxt) and nxt['cls'] in ('number', 'fraction')))
    return out


def HH3():
    sc = Counter(s for s, _ in singles(lambda r: r['support'] in B.ADMIN))
    wc = Counter(x for w in WT for x in w if KNOWN.match(x))
    signs = sorted(set(sc) & set(wc))
    xs, ys = [sc[s] for s in signs], [wc[s] for s in signs]
    real = B.spearman(xs, ys)
    null = []
    for _ in range(5000):
        y2 = list(ys)
        R.rng.shuffle(y2)
        null.append(B.spearman(xs, y2))
    p = R.pv_hi(null, real)
    return p, 'Tablet single signs are the commonest word syllables', {'spearman': round(real, 3), 'p': round(p, 4), 'signs': len(signs)}, {}


def HH4():
    pairs = [(s, 'seal') for s, _ in singles(lambda r: r['support'] in B.SEAL)] + [(s, 'tablet') for s, _ in singles(lambda r: r['support'] in B.ADMIN)]
    c = Counter(s for s, _ in pairs)
    pairs = [x for x in pairs if c[x[0]] >= 5]
    real, p, nm = R.assoc(pairs)
    return p, 'Single signs on sealings differ in repertoire from those on tablets', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'tokens': len(pairs)}, {}


def HH5():
    occ = [(x == '*301', 0 < i < len(w) - 1) for w in WTYPES for i, x in enumerate(w)]
    r_, p, a, b = R.flag_compare(occ, lambda o: o[0], lambda o: o[1])
    return p, '*301 is word-internal more often than other signs', {'301_internal': a, 'other_internal': b, 'p': round(p, 4)}, {}


def HH6():
    ws = [list(w) for w in WTYPES if len(w) >= 2]
    stat = lambda wl: sum(1 for w in wl for i in range(len(w) - 1) if UNREAD.match(w[i]) and UNREAD.match(w[i + 1]))
    real = stat(ws)
    null = []
    for _ in range(R.REPS):
        sh = []
        for w in ws:
            w2 = list(w)
            R.rng.shuffle(w2)
            sh.append(w2)
        null.append(stat(sh))
    p = R.pv_hi(null, real)
    return p, 'Unread signs stand next to other unread signs more than chance', {'adjacent_unread_pairs': real, 'null': round(sum(null) / len(null), 2), 'p': round(p, 4)}, {}


def HH7():
    occ, types = Counter(), defaultdict(set)
    for w in WT:
        for x in w:
            occ[x] += 1
            types[x].add(tuple(w))
    signs = [s for s in occ if occ[s] >= 3]
    xs = {s: log(occ[s]) for s in signs}
    ys = {s: log(len(types[s])) for s in signs}
    n = len(signs)
    mx, my = sum(xs.values()) / n, sum(ys.values()) / n
    b = sum((xs[s] - mx) * (ys[s] - my) for s in signs) / sum((xs[s] - mx) ** 2 for s in signs)
    resid = {s: ys[s] - (my + b * (xs[s] - mx)) for s in signs}
    r_, p, a, bb = R.flag_compare(signs, lambda s: bool(UNREAD.match(s)), lambda s: resid[s], lower=True)
    return p, 'Unread signs are confined to fewer word types per occurrence', {'unread_resid': a, 'known_resid': bb, 'p': round(p, 4)}, {}


def number_after(sign):
    items = singles(lambda r: r['support'] in B.ADMIN)
    r_, p, a, b = R.flag_compare(items, lambda x: x[0] == sign, lambda x: x[1])
    return p, a, b


def HH8():
    p, a, b = number_after('ZE')
    return p, 'ZE is followed directly by a number more often than other single signs', {'ZE': a, 'other': b, 'p': round(p, 4)}, {}


def HH11():
    p, a, b = number_after('NI')
    return p, 'NI is followed directly by a number more often than other single signs', {'NI': a, 'other': b, 'p': round(p, 4)}, {}


def HH15():
    rel = word_tokens(lambda r: r['support'] not in B.ADMIN and r['support'] not in B.SEAL)
    adm = word_tokens(lambda r: r['support'] in B.ADMIN)
    pairs = [(x, 'rel') for w in {tuple(w) for w in rel} for x in w if KNOWN.match(x)] + \
            [(x, 'adm') for w in {tuple(w) for w in adm} for x in w if KNOWN.match(x)]
    c = Counter(s for s, _ in pairs)
    pairs = [x for x in pairs if c[x[0]] >= 10]
    real, p, nm = R.assoc(pairs)
    return p, 'Syllable signs are associated with register', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'tokens': len(pairs)}, {}


def HH16():
    la = Counter(x.lower() for w in WT for x in w if KNOWN.match(x))
    lbc = Counter(x for w in R.LB for x in w)
    lbf = Counter(w[-1] for w in R.LB)
    signs = [s for s in la if lbc.get(s, 0) >= 20 and la[s] >= 5]
    xs = [lbf[s] / lbc[s] for s in signs]
    ys = [log((la[s] / sum(la.values())) / (lbc[s] / sum(lbc.values()))) for s in signs]
    real = B.spearman(xs, ys)
    null = []
    for _ in range(5000):
        y2 = list(ys)
        R.rng.shuffle(y2)
        null.append(B.spearman(xs, y2))
    p = R.pv_lo(null, real)
    return p, 'Signs Linear B uses word-finally are relatively rarer in Linear A', {'spearman': round(real, 3), 'p': round(p, 4), 'signs': len(signs)}, {}


if __name__ == '__main__':
    R.run('round45', 'the signs', __doc__, [HH1, HH3, HH4, HH5, HH6, HH7, HH8, HH11, HH15, HH16])
