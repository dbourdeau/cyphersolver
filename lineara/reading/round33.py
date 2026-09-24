"""Round 33 (loop round 5 of 10): amounts, totals and fractions.

V1  Grain amounts are multiples of 5 more often than other commodities' amounts.
V3  Entries with the half sign J (1/2) have odd whole numbers more often than entries without fractions.
V7  Lists that carry a KU-RO total are longer than lists that do not.
V8  Totals balance less often on longer lists.
V9  Totals that do not balance fall short of the entries' sum more often than they exceed it.
V10 Fractions stand on the later half of a list more often than on the earlier half.
V12 Entries with a fraction have smaller whole-number parts than entries without.
V15 Oil amounts differ in size by ligature adjunct (OLE+KI, OLE+U, OLE+MI, OLE+DI ...).
V16 The first entry of a list is its largest more often than chance (order shuffled within the list).
V17 Equal amounts stand on neighbouring lines more often than chance.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import log
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402

B = R.B


def entry_table():
    recs = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        ents = defaultdict(list)
        for t in r['tokens']:
            ents[t['entry']].append(t)
        rows = []
        for e, toks in sorted(ents.items()):
            if any(t['label'] in ('KU-RO', 'KI-RO', 'PO-TO-KU-RO') for t in toks):
                continue
            q = sum(t['value'] for t in toks if t['cls'] == 'number')
            fr = [t for t in toks if t['cls'] == 'fraction']
            com = [re.findall(r'[A-Z]{3,}', t['label'])[0] for t in toks if t['cls'] == 'commodity' and re.findall(r'[A-Z]{3,}', t['label'])]
            lig = [t['label'].split('-')[-1] for t in toks if t['cls'] == 'commodity' and '+' in t['label']]
            if q or fr:
                rows.append({'q': q, 'frac': bool(fr), 'half': any(t['value'] == '1/2' for t in fr), 'com': com[0] if com else None,
                             'lig': lig[0] if lig else None})
        has_total = any(t['label'] in ('KU-RO', 'PO-TO-KU-RO') for t in r['tokens'])
        if rows:
            recs.append({'name': r['name'], 'rows': rows, 'total': has_total})
    return recs


RECS = entry_table()
ROWS = [x for rec in RECS for x in rec['rows']]


def V1():
    items = [x for x in ROWS if x['q'] > 0 and x['com']]
    r, p, a, b = R.flag_compare(items, lambda x: x['com'] == 'GRA', lambda x: x['q'] % 5 == 0)
    return p, 'Grain amounts are multiples of 5 more often than other commodities\' amounts', {'GRA': a, 'other': b, 'p': round(p, 4)}, {}


def V3():
    items = [x for x in ROWS if x['q'] > 0 and (x['half'] or not x['frac'])]
    r, p, a, b = R.flag_compare(items, lambda x: x['half'], lambda x: x['q'] % 2 == 1)
    return p, 'Entries with J (1/2) have odd whole numbers more often', {'with_J': a, 'no_fraction': b, 'p': round(p, 4)}, {}


def V7():
    items = [rec for rec in RECS if len(rec['rows']) >= 2]
    r, p, a, b = R.flag_compare(items, lambda x: x['total'], lambda x: len(x['rows']))
    return p, 'Lists with a KU-RO total are longer', {'with_total': a, 'without': b, 'p': round(p, 4)}, {}


def totals():
    out = []
    n_rows = {rec['name']: len(rec['rows']) for rec in RECS}
    for c in B.READ['totals']:
        if c['stated_damaged'] or c['stated_has_unvalued'] or c['record'] not in n_rows:
            continue
        stated = Fraction(c['stated'])
        sums = [Fraction(w['sum']) for w in c['windows'].values()]
        best = min(sums, key=lambda s_: abs(s_ - stated)) if sums else None
        out.append({'ok': c['balances_in_some_window'], 'n': n_rows[c['record']], 'diff': (stated - best) if best is not None else None})
    return out


def V8():
    t = totals()
    r, p, a, b = R.flag_compare(t, lambda x: x['n'] >= 6, lambda x: x['ok'], lower=True)
    return p, 'Totals balance less often on longer lists (6+ entries)', {'long_ok': a, 'short_ok': b, 'p': round(p, 4)}, {}


def V9():
    bad = [x['diff'] for x in totals() if not x['ok'] and x['diff'] is not None and x['diff'] != 0]
    low = sum(d < 0 for d in bad)
    from math import comb
    n = len(bad)
    p = sum(comb(n, k) for k in range(low, n + 1)) / 2 ** n
    return p, 'Totals that do not balance fall short of the entries more often than they exceed them', {'short': f'{low}/{n}', 'sign_test_p': round(p, 4)}, {}


def V10():
    items = [(i / (len(rec['rows']) - 1) >= 0.5, x['frac']) for rec in RECS if len(rec['rows']) >= 4 for i, x in enumerate(rec['rows'])]
    r, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'Fractions stand on the later half of a list more often', {'later_half': a, 'earlier_half': b, 'p': round(p, 4)}, {}


def V12():
    items = [x for x in ROWS if x['q'] > 0]
    r, p, a, b = R.flag_compare(items, lambda x: x['frac'], lambda x: log(x['q']), lower=True)
    return p, 'Entries with a fraction have smaller whole-number parts', {'with_fraction_mean_log': a, 'without': b, 'p': round(p, 4)}, {}


def V15():
    items = [(x['lig'], log(x['q'])) for x in ROWS if x['com'] == 'OLE' and x['lig'] and x['q'] > 0]
    c = Counter(l for l, _ in items)
    items = [x for x in items if c[x[0]] >= 3]
    vals = [v for _, v in items]
    mu = sum(vals) / len(vals)

    def ss(labs):
        g = defaultdict(list)
        for l, v in zip(labs, vals):
            g[l].append(v)
        return sum(len(x) * (sum(x) / len(x) - mu) ** 2 for x in g.values())
    real, p, nm = R.X.shuffle_test(ss, [l for l, _ in items], reps=R.REPS)
    means = {l: round(2.718281828 ** (sum(v for l2, v in items if l2 == l) / n), 1) for l, n in Counter(l for l, _ in items).items()}
    return p, 'Oil amounts differ in size by ligature adjunct', {'between_SS': round(real, 2), 'null': round(nm, 2), 'p': round(p, 4), 'entries': len(items)}, {'geometric means': means}


def V16():
    lists = [[x['q'] for x in rec['rows']] for rec in RECS if len(rec['rows']) >= 3 and all(x['q'] > 0 for x in rec['rows'])]
    stat = lambda ls: sum(q[0] == max(q) and q.count(max(q)) == 1 for q in ls)
    real = stat(lists)
    null = []
    for _ in range(R.REPS):
        sh = []
        for q in lists:
            q2 = list(q)
            R.rng.shuffle(q2)
            sh.append(q2)
        null.append(stat(sh))
    p = R.pv_hi(null, real)
    return p, 'The first entry is the largest more often than chance', {'first_is_max': f'{real}/{len(lists)}', 'null': round(sum(null) / len(null), 1), 'p': round(p, 4)}, {}


def V17():
    lists = [[x['q'] for x in rec['rows']] for rec in RECS if len(rec['rows']) >= 3]
    stat = lambda ls: sum(1 for q in ls for i in range(len(q) - 1) if q[i] == q[i + 1])
    real = stat(lists)
    null = []
    for _ in range(R.REPS):
        sh = []
        for q in lists:
            q2 = list(q)
            R.rng.shuffle(q2)
            sh.append(q2)
        null.append(stat(sh))
    p = R.pv_hi(null, real)
    return p, 'Equal amounts stand on neighbouring lines more often than chance', {'adjacent_equal': real, 'null': round(sum(null) / len(null), 1), 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round33', 'amounts, totals and fractions', __doc__, [V1, V3, V7, V8, V9, V10, V12, V15, V16, V17])
