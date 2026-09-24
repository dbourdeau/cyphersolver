"""Round 54: did Linear B inherit the Minoan bookkeeping habits? Benjamini-Hochberg at 5% across the ten.

Linear B entries are parsed from linearb.xyz: each logogram followed directly by a whole number gives one entry
(logogram, amount); sub-units (T, V, Z ...) are ignored. A record's list is its entries in order.

LBC1  Knossos lists are largest-first beyond chance (mean Kendall tau; order shuffled within lists).
LBC2  Pylos lists are largest-first beyond chance.
LBC3  Knossos lists are more strictly largest-first than Pylos lists.
LBC4  The first entry is the unique largest beyond chance (Knossos and Pylos pooled).
LBC5  Equal amounts (other than 1) stand next to each other beyond chance.
LBC6  FIC (figs, the NI sign) comes after GRA on tablets with both, more often than not.
LBC7  FIC comes before VIN on tablets with both, more often than not.
LBC8  Commodities appear in a consistent order across tablets (order asymmetry).
LBC9  Amounts of 2 or more are even more often than odd (Knossos).
LBC10 Lists that carry a total word (to-so, to-sa, to-so-de, to-sa-de) are more strictly largest-first.
"""
from collections import Counter
from math import comb
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round43 as FF  # noqa: E402
import round44 as GG  # noqa: E402
import vigorous2 as W2  # noqa: E402

B = R.B
LOGO = re.compile(r'^\*?([A-Z]{3,})')
TOTALS = {'to-so', 'to-sa', 'to-so-de', 'to-sa-de'}


def lb_lists():
    out = []
    for _, r in B.LB_RECS:
        if r.get('site') not in ('Knossos', 'Pylos'):
            continue
        tw = [t.strip() for t in r.get('transliteratedWords', [])]
        ents = []
        for i, t in enumerate(tw[:-1]):
            m = LOGO.match(t)
            if m and re.fullmatch(r'\d+', tw[i + 1]):
                g = {'HORD': 'GRA'}.get(m.group(1), m.group(1))
                ents.append((g, int(tw[i + 1])))
        if ents:
            out.append({'site': r['site'], 'ents': ents, 'total': bool(TOTALS & set(tw))})
    return out


LISTS = lb_lists()
tau_mean = lambda ls: sum(W2.tau(q) for q in ls) / max(1, len(ls))


def qlists(pred, n=3):
    return [[q for _, q in x['ents']] for x in LISTS if pred(x) and len(x['ents']) >= n]


def LBC1():
    ls = qlists(lambda x: x['site'] == 'Knossos')
    real, p, nm = FF.shuffle_within(ls, tau_mean)
    return p, 'Knossos lists are largest-first', {'mean_tau': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'lists': len(ls)}, {}


def LBC2():
    ls = qlists(lambda x: x['site'] == 'Pylos')
    real, p, nm = FF.shuffle_within(ls, tau_mean)
    return p, 'Pylos lists are largest-first', {'mean_tau': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'lists': len(ls)}, {}


def LBC3():
    kn, py = qlists(lambda x: x['site'] == 'Knossos'), qlists(lambda x: x['site'] == 'Pylos')
    r, p, nm = R.compare(kn, py, tau_mean)
    return p, 'Knossos lists are more strictly largest-first than Pylos lists', {'KN': round(tau_mean(kn), 3), 'PY': round(tau_mean(py), 3), 'p': round(p, 4)}, {}


def LBC4():
    ls = [q for q in qlists(lambda x: True) if all(v > 0 for v in q)]
    real, p, nm = FF.shuffle_within(ls, lambda L: sum(q[0] == max(q) and q.count(max(q)) == 1 for q in L))
    return p, 'The first entry is the unique largest', {'first_is_max': f'{real}/{len(ls)}', 'null': round(nm, 1), 'p': round(p, 4)}, {}


def LBC5():
    ls = qlists(lambda x: True)
    real, p, nm = FF.shuffle_within(ls, lambda L: sum(1 for q in L for i in range(len(q) - 1) if q[i] == q[i + 1] and q[i] != 1))
    return p, 'Equal amounts (not 1) stand next to each other beyond chance', {'adjacent_equal': real, 'null': round(nm, 1), 'p': round(p, 4)}, {}


def seqs():
    out = []
    for x in LISTS:
        s = list(dict.fromkeys(g for g, _ in x['ents']))
        if len(s) >= 2:
            out.append(s)
    return out


def sign_test(a, b):
    ss = [s for s in seqs() if a in s and b in s]
    k = sum(s.index(a) < s.index(b) for s in ss)
    n = len(ss)
    return (sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n if n else 1.0), k, n


def LBC6():
    p, k, n = sign_test('GRA', 'FIC')
    return p, 'Figs come after grain', {'grain_first': f'{k}/{n}', 'sign_test_p': round(p, 4)}, {}


def LBC7():
    p, k, n = sign_test('FIC', 'VIN')
    return p, 'Figs come before wine', {'figs_first': f'{k}/{n}', 'sign_test_p': round(p, 4)}, {}


def LBC8():
    ss = seqs()
    real, p, nm = FF.shuffle_within(ss, GG._asym)
    return p, 'Commodities appear in a consistent order', {'asymmetry': real, 'null': round(nm, 1), 'p': round(p, 4), 'tablets': len(ss)}, {}


def LBC9():
    qs = [q for x in LISTS if x['site'] == 'Knossos' for _, q in x['ents'] if q >= 2]
    k = sum(q % 2 == 0 for q in qs)
    n = len(qs)
    p = sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n if n else 1.0
    return p, 'Knossos amounts of 2+ are even more often than odd', {'even': f'{k}/{n}', 'p': round(p, 6)}, {}


def LBC10():
    items = [x for x in LISTS if len(x['ents']) >= 3]
    r_, p, a, b = R.flag_compare(items, lambda x: x['total'], lambda x: W2.tau([q for _, q in x['ents']]))
    return p, 'Lists with a total word are more strictly largest-first', {'with_total': a, 'without': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round54', 'Minoan bookkeeping habits in Linear B', __doc__, [LBC1, LBC2, LBC3, LBC4, LBC5, LBC6, LBC7, LBC8, LBC9, LBC10])
