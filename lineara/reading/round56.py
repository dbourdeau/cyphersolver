"""Round 56: more bookkeeping comparisons between Linear A and Linear B. Benjamini-Hochberg at 5% across the nine.

D1  Pylos amounts of goods (not men, women or livestock) of 2 or more are even more often than odd.
D2  Linear A: grain amounts exceed wine amounts on tablets with both.
D3  Linear B: grain amounts exceed wine amounts on tablets with both.
D4  Linear B: grain comes before olives on tablets with both.
D5  Linear B: grain comes before men (VIR) on tablets with both.
D6  Pylos alone: the first entry is the unique largest beyond chance.
D7  Linear A: cyperus and oil stand on the same tablets beyond chance.
D8  Linear B: cyperus and oil stand on the same tablets beyond chance.
D9  Linear B lists of men are ordered largest-first beyond chance.
"""
from math import comb
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round33 as VV  # noqa: E402
import round43 as FF  # noqa: E402
import round44 as GG  # noqa: E402
import round55 as C  # noqa: E402
import vigorous2 as W2  # noqa: E402

LBT = C.TABS
PEOPLE = {'VIR', 'MUL', 'OVIS', 'CAP', 'SUS', 'BOS', 'EQU', 'OVISm', 'OVISf'}


def binom_up(k, n):
    return sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n if n else 1.0


def D1():
    qs = [q for t in LBT if t['site'] == 'Pylos' for g, q, _ in t['ents'] if q >= 2 and not any(g.startswith(x) for x in PEOPLE)]
    k = sum(q % 2 == 0 for q in qs)
    return binom_up(k, len(qs)), 'Pylos goods amounts are even more often than odd', {'even': f'{k}/{len(qs)}', 'p': round(binom_up(k, len(qs)), 5)}, {}


def exceed_la(a, b):
    wins = n = 0
    for rec in VV.RECS:
        x = [r['q'] for r in rec['rows'] if r['com'] == a and r['q'] > 0]
        y = [r['q'] for r in rec['rows'] if r['com'] == b and r['q'] > 0]
        if x and y and max(x) != max(y):
            n += 1
            wins += max(x) > max(y)
    return wins, n


def exceed_lb(a, b):
    wins = n = 0
    for t in LBT:
        x = [q for g, q, _ in t['ents'] if g == a]
        y = [q for g, q, _ in t['ents'] if g == b]
        if x and y and max(x) != max(y):
            n += 1
            wins += max(x) > max(y)
    return wins, n


def D2():
    k, n = exceed_la('GRA', 'VIN')
    return binom_up(k, n), 'Linear A: grain amounts exceed wine amounts', {'grain_larger': f'{k}/{n}', 'p': round(binom_up(k, n), 4)}, {}


def D3():
    k, n = exceed_lb('GRA', 'VIN')
    return binom_up(k, n), 'Linear B: grain amounts exceed wine amounts', {'grain_larger': f'{k}/{n}', 'p': round(binom_up(k, n), 4)}, {}


def D4():
    p, s = C.order_sign('GRA', 'OLIV')
    return p, 'Linear B: grain before olives', {'grain_first': s, 'p': round(p, 5)}, {}


def D5():
    p, s = C.order_sign('GRA', 'VIR')
    return p, 'Linear B: grain before men', {'grain_first': s, 'p': round(p, 5)}, {}


def D6():
    ls = [[q for _, q, _ in t['ents']] for t in LBT if t['site'] == 'Pylos' and len(t['ents']) >= 3]
    real, p, nm = FF.shuffle_within(ls, lambda L: sum(q[0] == max(q) and q.count(max(q)) == 1 for q in L))
    return p, 'Pylos: the first entry is the unique largest beyond chance', {'first_is_max': f'{real}/{len(ls)}', 'null': round(nm, 1), 'p': round(p, 4)}, {}


def D7():
    r, p, nm = GG.cooc('CYP', 'OLE')
    return p, 'Linear A: cyperus and oil on the same tablets beyond chance', {'together': r, 'null': round(nm, 2), 'p': round(p, 4)}, {}


def D8():
    p, r, nm = C.cooc('CYP', 'OLE')
    return p, 'Linear B: cyperus and oil on the same tablets beyond chance', {'together': r, 'null': round(nm, 2), 'p': round(p, 4)}, {}


def D9():
    ls = [[q for g, q, _ in t['ents'] if g == 'VIR'] for t in LBT]
    ls = [q for q in ls if len(q) >= 3]
    real, p, nm = FF.shuffle_within(ls, lambda L: sum(W2.tau(q) for q in L) / max(1, len(L)))
    return p, 'Linear B lists of men are largest-first', {'mean_tau': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'lists': len(ls)}, {}


if __name__ == '__main__':
    R.run('round56', 'more bookkeeping comparisons between Linear A and Linear B', __doc__, [D1, D2, D3, D4, D5, D6, D7, D8, D9])
