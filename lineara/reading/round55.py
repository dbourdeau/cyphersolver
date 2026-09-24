"""Round 55: which Linear A bookkeeping habits did Linear B keep? Each test repeats a Linear A finding on the Linear B
tablets of Knossos and Pylos (NI read as the fig logogram FIC). Benjamini-Hochberg at 5% across the ten.

C1  Cyperus comes before figs (Linear A: 19 of 19).
C2  Oil comes before figs (Linear A: 11 of 16).
C3  Figs stand on grain tablets beyond chance (Linear A: 19 vs 9).
C4  Fig entries carry sub-units more often than entries of men.
C5  Grain amounts exceed oil amounts on tablets with both (Linear A: 13 of 16).
C6  The first commodity carries the tablet's largest amount beyond chance (Linear A: 30 of 53).
C7  Wine is the last commodity beyond chance (Linear A: 13 of 17).
C8  Oil and olives stand on the same tablets beyond chance (Linear A: 11 vs 4).
C9  Grain is the first commodity on tablets with several commodities beyond chance.
C10 Lists of goods (not men, not sheep) are largest-first beyond chance.
"""
from collections import Counter
from math import comb
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round43 as FF  # noqa: E402
import vigorous2 as W2  # noqa: E402

B = R.B
LOGO = re.compile(r'^\*?([A-Z]{3,})')
SUB = {'T', 'V', 'Z', 'S'}


def parse():
    tabs = []
    for _, r in B.LB_RECS:
        if r.get('site') not in ('Knossos', 'Pylos'):
            continue
        tw = [t.strip() for t in r.get('transliteratedWords', [])]
        ents = []
        for i, t in enumerate(tw[:-1]):
            g = None
            m = LOGO.match(t)
            if m:
                g = {'HORD': 'GRA'}.get(m.group(1), m.group(1))
            elif t == 'NI':
                g = 'FIC'
            if g and re.fullmatch(r'\d+', tw[i + 1]):
                sub = i + 2 < len(tw) and tw[i + 2] in SUB
                ents.append((g, int(tw[i + 1]), sub))
        if ents:
            tabs.append({'site': r['site'], 'ents': ents, 'seq': list(dict.fromkeys(g for g, _, _ in ents))})
    return tabs


TABS = parse()


def order_sign(a, b):
    ss = [t['seq'] for t in TABS if a in t['seq'] and b in t['seq']]
    k = sum(s.index(a) < s.index(b) for s in ss)
    n = len(ss)
    p = sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n if n else 1.0
    return p, f'{k}/{n}'


def C1():
    p, s = order_sign('CYP', 'FIC')
    return p, 'Cyperus before figs', {'cyperus_first': s, 'p': round(p, 5)}, {}


def C2():
    p, s = order_sign('OLE', 'FIC')
    return p, 'Oil before figs', {'oil_first': s, 'p': round(p, 5)}, {}


def cooc(a, b):
    has_a = [a in t['seq'] for t in TABS]
    has_b = [b in t['seq'] for t in TABS]
    real = sum(x and y for x, y in zip(has_a, has_b))
    null = []
    for _ in range(R.REPS):
        R.rng.shuffle(has_b)
        null.append(sum(x and y for x, y in zip(has_a, has_b)))
    return R.pv_hi(null, real), real, sum(null) / len(null)


def C3():
    p, r, nm = cooc('FIC', 'GRA')
    return p, 'Figs stand on grain tablets beyond chance', {'together': r, 'null': round(nm, 1), 'p': round(p, 4)}, {}


def C4():
    items = [(g, sub) for t in TABS for g, _, sub in t['ents'] if g in ('FIC', 'VIR')]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0] == 'FIC', lambda x: x[1])
    return p, 'Fig entries carry sub-units more often than entries of men', {'FIC': a, 'VIR': b, 'p': round(p, 4)}, {}


def C5():
    wins = n = 0
    for t in TABS:
        g = [q for c, q, _ in t['ents'] if c == 'GRA']
        o = [q for c, q, _ in t['ents'] if c == 'OLE']
        if g and o and max(g) != max(o):
            n += 1
            wins += max(g) > max(o)
    p = sum(comb(n, i) for i in range(wins, n + 1)) / 2 ** n if n else 1.0
    return p, 'Grain amounts exceed oil amounts on tablets with both', {'grain_larger': f'{wins}/{n}', 'p': round(p, 4)}, {}


def C6():
    items = []
    for t in TABS:
        if len(t['seq']) >= 2:
            mx = max(t['ents'], key=lambda e: e[1])
            items.append((t['seq'], mx[0]))
    real = sum(s[0] == c for s, c in items)
    null = [sum(R.rng.choice(s) == c for s, c in items) for _ in range(R.REPS)]
    p = R.pv_hi(null, real)
    return p, 'The first commodity carries the largest amount', {'first_has_max': f'{real}/{len(items)}', 'null': round(sum(null) / len(null), 1), 'p': round(p, 4)}, {}


def C7():
    ss = [t['seq'] for t in TABS if 'VIN' in t['seq'] and len(t['seq']) >= 2]
    real = sum(s[-1] == 'VIN' for s in ss)
    null = [sum(R.rng.choice(s) == 'VIN' for s in ss) for _ in range(R.REPS)]
    p = R.pv_hi(null, real)
    return p, 'Wine is the last commodity', {'VIN_last': f'{real}/{len(ss)}', 'null': round(sum(null) / len(null), 1), 'p': round(p, 4)}, {}


def C8():
    p, r, nm = cooc('OLE', 'OLIV')
    return p, 'Oil and olives stand on the same tablets beyond chance', {'together': r, 'null': round(nm, 1), 'p': round(p, 4)}, {}


def C9():
    ss = [t['seq'] for t in TABS if 'GRA' in t['seq'] and len(t['seq']) >= 2]
    real = sum(s[0] == 'GRA' for s in ss)
    null = [sum(R.rng.choice(s) == 'GRA' for s in ss) for _ in range(R.REPS)]
    p = R.pv_hi(null, real)
    return p, 'Grain is the first commodity', {'GRA_first': f'{real}/{len(ss)}', 'null': round(sum(null) / len(null), 1), 'p': round(p, 4)}, {}


def C10():
    lists = [[q for _, q, _ in t['ents']] for t in TABS if len(t['ents']) >= 3 and not any(g in ('VIR', 'MUL', 'OVIS') or g.startswith('OVIS') for g, _, _ in t['ents'])]
    real, p, nm = FF.shuffle_within(lists, lambda ls: sum(W2.tau(q) for q in ls) / max(1, len(ls)))
    return p, 'Lists of goods (not men, not sheep) are largest-first', {'mean_tau': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'lists': len(lists)}, {}


if __name__ == '__main__':
    R.run('round55', 'Linear A bookkeeping habits kept in Linear B', __doc__, [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10])
