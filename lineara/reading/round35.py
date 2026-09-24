"""Round 35 (loop round 7 of 10): variation between sites (tablet sides merged; sites with five or more tablets
unless stated).

X1  List length differs by site.
X2  Use of KU-RO totals differs by site.
X3  Use of word dividers (per word) differs by site.
X5  Fractions per entry differ by site within the same commodity (site labels shuffled within commodity).
X6  The share of entries equal to 1 differs by site within the same commodity.
X9  Word length (signs per word type) differs by site.
X10 Use of single signs (per token) differs by site.
X11 The word-initial preference of Q-row signs (round 29 P6) holds both at Haghia Triada and outside it.
X12 Khania uses the consonant rows in different proportions from Haghia Triada.
X14 Tablets that open with a heading word are commoner at some sites than others.
"""
from collections import Counter, defaultdict
from math import log
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round34 as W  # noqa: E402

B, X, D = R.B, R.X, R.D
grid = R.grid
whole = X.whole


def tablets():
    tabs = defaultdict(lambda: {'site': None, 'n': 0, 'kuro': False, 'div': 0, 'words': 0, 'single': 0, 'tokens': 0, 'first_heading': None})
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        t = tabs[whole(r['name'])]
        t['site'] = r['site']
        t['n'] += len({tok['entry'] for tok in r['tokens']})
        for tok in r['tokens']:
            t['tokens'] += 1
            if tok['label'] in ('KU-RO', 'PO-TO-KU-RO'):
                t['kuro'] = True
            if tok['cls'] == 'apparatus' and tok['label'] == '𐄁':
                t['div'] += 1
            if tok['cls'] in ('word', 'term'):
                t['words'] += 1
                if t['first_heading'] is None:
                    t['first_heading'] = tok.get('function') == 'heading'
            if tok['cls'] == 'single-sign':
                t['single'] += 1
    by = Counter(t['site'] for t in tabs.values())
    return {k: v for k, v in tabs.items() if by[v['site']] >= 5}


TABS = tablets()
KEYS = sorted(TABS)


def site_ss(value, text):
    keys = [k for k in KEYS if value(TABS[k]) is not None]
    vals = [value(TABS[k]) for k in keys]
    st = [TABS[k]['site'] for k in keys]
    real, p, nm = X.shuffle_test(lambda s: W.between(vals, s), st, reps=R.REPS)
    g = defaultdict(list)
    for s, v in zip(st, vals):
        g[s].append(v)
    return p, text, {'between_SS': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'tablets': len(keys)}, {'means': {s: round(sum(v) / len(v), 3) for s, v in g.items()}}


def X1():
    return site_ss(lambda t: log(t['n']) if t['n'] else None, 'List length differs by site')


def X2():
    return site_ss(lambda t: float(t['kuro']), 'Use of KU-RO totals differs by site')


def X3():
    return site_ss(lambda t: t['div'] / t['words'] if t['words'] else None, 'Use of word dividers differs by site')


def entry_rows():
    import round33 as V
    site = {r['name']: r['site'] for r in B.READ['records']}
    rows = []
    for rec in V.RECS:
        for x in rec['rows']:
            if x['com']:
                rows.append((site[rec['name']], x['com'], x))
    c = Counter(s for s, _, _ in rows)
    return [r for r in rows if c[r[0]] >= 10]


def within_commodity(value, text):
    rows = entry_rows()
    vals = [value(x) for _, _, x in rows]
    by_c = defaultdict(list)
    for i, (s, c, x) in enumerate(rows):
        by_c[c].append(i)

    def stat(sites):
        return sum(W.between([vals[i] for i in idx], [sites[i] for i in idx]) for idx in by_c.values())
    st = [s for s, _, _ in rows]
    real = stat(st)
    null = []
    for _ in range(R.REPS):
        sh = list(st)
        for idx in by_c.values():
            v = [st[i] for i in idx]
            R.rng.shuffle(v)
            for i, x in zip(idx, v):
                sh[i] = x
        null.append(stat(sh))
    p = R.pv_hi(null, real)
    return p, text, {'between_SS': round(real, 3), 'null': round(sum(null) / len(null), 3), 'p': round(p, 4), 'entries': len(rows)}, {}


def X5():
    return within_commodity(lambda x: float(x['frac']), 'Fractions per entry differ by site within commodity')


def X6():
    return within_commodity(lambda x: float(x['q'] == 1), 'The share of entries equal to 1 differs by site within commodity')


def site_types():
    sw = defaultdict(set)
    for r, t, w in B.words_of():
        sw[r['site']].add(w)
    return {s: sorted(v) for s, v in sw.items() if len(v) >= 30}


def X9():
    sw = site_types()
    items = [(s, len(w)) for s, ws in sw.items() for w in ws]
    vals = [v for _, v in items]
    real, p, nm = X.shuffle_test(lambda st: W.between(vals, st), [s for s, _ in items], reps=R.REPS)
    return p, 'Word length differs by site', {'between_SS': round(real, 2), 'null': round(nm, 2), 'p': round(p, 4), 'words': len(items)}, {}


def X10():
    return site_ss(lambda t: t['single'] / t['tokens'] if t['tokens'] else None, 'Use of single signs differs by site')


def q_initial(ws):
    occ = [(i == 0) for w in ws for i, x in enumerate(w) if grid(x) and grid(x)[0] == 'q']
    return sum(occ) / max(1, len(occ)), len(occ)


def X11():
    ht = D.site_words(lambda s: s == 'Haghia Triada')
    oth = D.site_words(lambda s: s != 'Haghia Triada')
    lb = q_initial(R.LB)[0]
    res = {}
    ps = []
    for name, ws in (('HT', ht), ('other', oth)):
        r, p, nm = R.compare(ws, R.LB, lambda x: q_initial(x)[0])
        res[name] = {'share': round(q_initial(ws)[0], 3), 'n': q_initial(ws)[1], 'p': round(p, 4)}
        ps.append(p)
    return max(ps), 'Q-row signs are word-initial at HT and outside HT, each more than in Linear B', {**res, 'LB': round(lb, 3), 'p (larger)': round(max(ps), 4)}, {}


def X12():
    kh = D.site_words(lambda s: s == 'Khania')
    ht = D.site_words(lambda s: s == 'Haghia Triada')
    pairs = [(site, grid(x)[0] or 'V') for site, ws in (('KH', kh), ('HT', ht)) for w in ws for x in w if grid(x)]
    real, p, nm = R.assoc(pairs)
    return p, 'Khania uses the consonant rows in different proportions from Haghia Triada', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'syllables': len(pairs)}, {}


def X14():
    return site_ss(lambda t: float(t['first_heading']) if t['first_heading'] is not None else None, 'Tablets opening with a heading word differ by site')


if __name__ == '__main__':
    R.run('round35', 'variation between sites', __doc__, [X1, X2, X3, X5, X6, X9, X10, X11, X12, X14])
