"""Round 34 (loop round 6 of 10): scribes and archives (Haghia Triada hands; tablet sides merged).

Each test asks whether a recording habit depends on the scribe beyond chance (scribe labels shuffled among tablets,
or among entries/tokens where stated). Only scribes with at least three tablets are used.

W1  List length (entries per tablet) differs by scribe.
W2  Use of a KU-RO total differs by scribe.
W3  Use of word dividers (per word) differs by scribe.
W4  The fraction values used differ by scribe.
W5  Syllable use differs by scribe (transaction terms removed).
W6  Scribes with more tablets balance their totals more often (Spearman over scribes).
W7  Amount size differs by scribe within the same commodity.
W8  Strictness of largest-first order (Kendall tau per list) differs by scribe.
W9  Oil ligature adjuncts differ by scribe.
W11 Use of single signs (per token) differs by scribe.
"""
from collections import Counter, defaultdict
from math import log
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402

B, X = R.B, R.X
whole, SCRIBE = X.whole, X.SCRIBE_W


def tablets():
    tabs = defaultdict(lambda: {'n': 0, 'kuro': False, 'div': 0, 'words': 0, 'fracs': [], 'syl': [], 'q': [], 'lig': [], 'single': 0, 'tokens': 0})
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        k = whole(r['name'])
        if k not in SCRIBE:
            continue
        t = tabs[k]
        ents = {tok['entry'] for tok in r['tokens']}
        t['n'] += len(ents)
        com = None
        for tok in r['tokens']:
            t['tokens'] += 1
            if tok['label'] in ('KU-RO', 'PO-TO-KU-RO'):
                t['kuro'] = True
            if tok['cls'] == 'apparatus' and tok['label'] == '𐄁':
                t['div'] += 1
            if tok['cls'] in ('word', 'term'):
                t['words'] += 1
                if tok['label'] not in X.TERMS:
                    t['syl'] += [x for x in tok['label'].split('-') if re.fullmatch(r'[A-Z]+[0-9]?', x)]
            if tok['cls'] == 'fraction':
                t['fracs'].append(tok['value'])
            if tok['cls'] == 'commodity':
                m = re.findall(r'[A-Z]{3,}', tok['label'])
                if m:
                    com = m[0]
                if tok['label'].startswith('OLE+'):
                    t['lig'].append(tok['label'].split('-')[-1])
            if tok['cls'] == 'single-sign':
                t['single'] += 1
        for x in R.T.ENTRIES:
            pass
    for x in R.T.ENTRIES:
        k = whole(x['record'])
        if k in tabs and x['q'] > 0 and x['com']:
            tabs[k]['q'].append((x['com'], log(x['q'])))
    by = Counter(SCRIBE[k] for k in tabs)
    return {k: v for k, v in tabs.items() if by[SCRIBE[k]] >= 3}


TABS = tablets()
KEYS = sorted(TABS)
SC = [SCRIBE[k] for k in KEYS]


def between(vals, groups):
    mu = sum(vals) / len(vals)
    g = defaultdict(list)
    for s, v in zip(groups, vals):
        g[s].append(v)
    return sum(len(x) * (sum(x) / len(x) - mu) ** 2 for x in g.values())


def tablet_ss(value, text):
    keys = [k for k in KEYS if value(TABS[k]) is not None]
    vals = [value(TABS[k]) for k in keys]
    sc = [SCRIBE[k] for k in keys]
    real, p, nm = R.X.shuffle_test(lambda s: between(vals, s), sc, reps=R.REPS)
    return p, text, {'between_SS': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'tablets': len(keys)}, {}


def W1():
    return tablet_ss(lambda t: log(t['n']) if t['n'] else None, 'List length differs by scribe')


def W2():
    return tablet_ss(lambda t: float(t['kuro']), 'Use of KU-RO totals differs by scribe')


def W3():
    return tablet_ss(lambda t: t['div'] / t['words'] if t['words'] else None, 'Use of word dividers differs by scribe')


def pair_test(pairs_of, text):
    pairs = [(SCRIBE[k], x) for k in KEYS for x in pairs_of(TABS[k])]
    c = Counter(x for _, x in pairs)
    pairs = [p_ for p_ in pairs if c[p_[1]] >= 3]
    real, p, nm = R.assoc(pairs)
    return p, text, {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'tokens': len(pairs)}, {}


def W4():
    return pair_test(lambda t: t['fracs'], 'The fraction values used differ by scribe')


def W5():
    return pair_test(lambda t: t['syl'], 'Syllable use differs by scribe (transaction terms removed)')


def W6():
    tot = defaultdict(list)
    for c in B.READ['totals']:
        k = whole(c['record'])
        if k in TABS and not c['stated_damaged'] and not c['stated_has_unvalued']:
            tot[SCRIBE[k]].append(c['balances_in_some_window'])
    n_tab = Counter(SC)
    rows = [(n_tab[s], sum(v) / len(v)) for s, v in tot.items() if len(v) >= 2]
    xs, ys = [a for a, _ in rows], [b for _, b in rows]
    real = R.B.spearman(xs, ys)
    null = []
    for _ in range(5000):
        y2 = list(ys)
        R.rng.shuffle(y2)
        null.append(R.B.spearman(xs, y2))
    p = R.pv_hi(null, real)
    return p, 'Scribes with more tablets balance their totals more often', {'rho': round(real, 3), 'p': round(p, 4), 'scribes': len(rows)}, {}


def W7():
    rows = [(SCRIBE[k], c, v) for k in KEYS for c, v in TABS[k]['q']]
    by_c = defaultdict(list)
    for i, (s, c, v) in enumerate(rows):
        by_c[c].append(i)

    def stat(sc):
        tot = 0.0
        for c, idx in by_c.items():
            tot += between([rows[i][2] for i in idx], [sc[i] for i in idx])
        return tot
    sc = [s for s, _, _ in rows]
    real = stat(sc)
    null = []
    for _ in range(R.REPS):
        sh = list(sc)
        for c, idx in by_c.items():
            v = [sc[i] for i in idx]
            R.rng.shuffle(v)
            for i, x in zip(idx, v):
                sh[i] = x
        null.append(stat(sh))
    p = R.pv_hi(null, real)
    return p, 'Amount size differs by scribe within the same commodity', {'between_SS': round(real, 2), 'null': round(sum(null) / len(null), 2), 'p': round(p, 4), 'entries': len(rows)}, {}


def W8():
    by = R.I.H.G.F.X.T  # placeholder to keep module references uniform
    import decipher25 as _  # noqa: F401
    import vigorous2 as W
    lists = W.ht_lists()
    rows = [(s, W.tau(v)) for s, vs in lists.items() for v in vs]
    c = Counter(s for s, _ in rows)
    rows = [r for r in rows if c[r[0]] >= 3]
    vals = [v for _, v in rows]
    real, p, nm = R.X.shuffle_test(lambda s: between(vals, s), [s for s, _ in rows], reps=R.REPS)
    return p, 'Strictness of largest-first order differs by scribe', {'between_SS': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'lists': len(rows)}, {}


def W9():
    return pair_test(lambda t: t['lig'], 'Oil ligature adjuncts differ by scribe')


def W11():
    return tablet_ss(lambda t: t['single'] / t['tokens'] if t['tokens'] else None, 'Use of single signs differs by scribe')


if __name__ == '__main__':
    R.run('round34', 'scribes and archives', __doc__, [W1, W2, W3, W4, W5, W6, W7, W8, W9, W11])
