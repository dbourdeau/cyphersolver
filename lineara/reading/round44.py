"""Round 44 (second loop, round 6 of 10): the canonical commodity order, and persons and commodities.

GG1  The commodity order of round 43 FF9 holds at Haghia Triada alone.
GG2  It holds outside Haghia Triada.
GG3  Linear A's commodity order agrees with Linear B's order for the same commodities more than chance.
GG4  It holds with the two sides of a tablet read as one sequence (side a, then b).
GG5  Same-commodity tablets share entry labels beyond chance (sides merged, shuffling within site).
GG8  On tablets with both grain and oil, grain amounts exceed oil amounts more often than not.
GG9  The first commodity on a multi-commodity tablet carries the tablet's largest amount more often than chance.
GG10 Wine stands last among a tablet's commodities more often than chance.
GG11 Cyperus and wine stand on the same tablets beyond chance.
GG12 Oil and olives stand on the same tablets beyond chance.
"""
from collections import Counter, defaultdict
from math import comb
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round33 as VV  # noqa: E402
import round43 as FF  # noqa: E402

B, X = R.B, R.X
SITE = FF.SITE
GOODS = {'GRA', 'OLE', 'OLIV', 'VIN', 'CYP', 'FIC'}


def seq_of(rec):
    return list(dict.fromkeys(x['com'] for x in rec['rows'] if x['com']))


def order_test(seqs):
    real, p, nm = FF.shuffle_within(seqs, FF.FF9.__globals__['FF9'].__code__ and (lambda ss: _asym(ss)))
    return real, p, nm


def _asym(ss):
    c = Counter()
    for s in ss:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                c[(s[i], s[j])] += 1
    return sum(abs(c[(a, b)] - c[(b, a)]) for (a, b) in {tuple(sorted(k)) for k in c})


def seqs_where(pred):
    return [s for rec in VV.RECS if pred(rec) for s in [seq_of(rec)] if len(s) >= 2]


def GG1():
    ss = seqs_where(lambda r: SITE[r['name']] == 'Haghia Triada')
    real, p, nm = FF.shuffle_within(ss, _asym)
    return p, 'The commodity order holds at Haghia Triada', {'asymmetry': real, 'null': round(nm, 1), 'p': round(p, 4), 'tablets': len(ss)}, {}


def GG2():
    ss = seqs_where(lambda r: SITE[r['name']] != 'Haghia Triada')
    real, p, nm = FF.shuffle_within(ss, _asym)
    return p, 'The commodity order holds outside Haghia Triada', {'asymmetry': real, 'null': round(nm, 1), 'p': round(p, 4), 'tablets': len(ss)}, {}


def lb_pairs():
    c = Counter()
    for _, r in B.LB_RECS:
        seq = []
        for t in r.get('transliteratedWords', []):
            m = re.match(r'^\*?([A-Z]{3,})', t.strip())
            if m:
                g = {'HORD': 'GRA'}.get(m.group(1), m.group(1))
                if g in GOODS and g not in seq:
                    seq.append(g)
        for i in range(len(seq)):
            for j in range(i + 1, len(seq)):
                c[(seq[i], seq[j])] += 1
    return c


def GG3():
    lb = lb_pairs()
    major = {}
    for (a, b), n in lb.items():
        if n + lb[(b, a)] >= 3 and n > lb[(b, a)]:
            major[frozenset((a, b))] = (a, b)
    ss = [[g for g in s if g in GOODS] for s in seqs_where(lambda r: True)]
    ss = [s for s in ss if len(s) >= 2]

    def agree(seqs):
        hit = tot = 0
        for s in seqs:
            for i in range(len(s)):
                for j in range(i + 1, len(s)):
                    k = frozenset((s[i], s[j]))
                    if k in major:
                        tot += 1
                        hit += (s[i], s[j]) == major[k]
        return hit / max(1, tot), tot
    real, n = agree(ss)
    real_, p, nm = FF.shuffle_within(ss, lambda x: agree(x)[0])
    return p, 'Linear A commodity order agrees with Linear B order', {'agreement': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'pairs': n},\
        {'Linear B majority orders': ['<'.join(v) for v in major.values()]}


def GG4():
    merged = defaultdict(list)
    for rec in VV.RECS:
        merged[X.whole(rec['name'])].append((rec['name'], seq_of(rec)))
    ss = []
    for k, parts in merged.items():
        s = []
        for _, sq in sorted(parts):
            for g in sq:
                if g not in s:
                    s.append(g)
        if len(s) >= 2:
            ss.append(s)
    real, p, nm = FF.shuffle_within(ss, _asym)
    return p, 'The commodity order holds with tablet sides merged', {'asymmetry': real, 'null': round(nm, 1), 'p': round(p, 4), 'tablets': len(ss)}, {}


def GG5():
    import decipher9i as I9
    tabs = [(k, t) for k, t in I9.TF.items() if len(t['com']) == 1 and t['ent']]
    site = {X.whole(r['name']): r['site'] for r in B.READ['records']}
    names = [k for k, _ in tabs]
    sets = {k: t['ent'] for k, t in tabs}
    share = {(a, b): bool(sets[a] & sets[b]) for i, a in enumerate(names) for b in names[i + 1:]}
    com = [next(iter(t['com'])) for _, t in tabs]

    def stat(labs):
        cm = dict(zip(names, labs))
        same = [v for (a, b), v in share.items() if cm[a] == cm[b]]
        diff = [v for (a, b), v in share.items() if cm[a] != cm[b]]
        return sum(same) / max(1, len(same)) - sum(diff) / max(1, len(diff))
    real = stat(com)
    idx = defaultdict(list)
    for i, k in enumerate(names):
        idx[site.get(k)].append(i)
    null = []
    for _ in range(R.REPS):
        sh = list(com)
        for ii in idx.values():
            v = [com[i] for i in ii]
            R.rng.shuffle(v)
            for i, x in zip(ii, v):
                sh[i] = x
        null.append(stat(sh))
    p = R.pv_hi(null, real)
    return p, 'Same-commodity tablets share entry labels (within-site shuffle)', {'diff': round(real, 4), 'null': round(sum(null) / len(null), 4), 'p': round(p, 4), 'tablets': len(names)}, {}


def GG8():
    wins = n = 0
    for rec in VV.RECS:
        g = [x['q'] for x in rec['rows'] if x['com'] == 'GRA' and x['q'] > 0]
        o = [x['q'] for x in rec['rows'] if x['com'] == 'OLE' and x['q'] > 0]
        if g and o and max(g) != max(o):
            n += 1
            wins += max(g) > max(o)
    p = sum(comb(n, k) for k in range(wins, n + 1)) / 2 ** n if n else 1.0
    return p, 'On tablets with both, grain amounts exceed oil amounts', {'grain_larger': f'{wins}/{n}', 'sign_test_p': round(p, 4)}, {}


def GG9():
    items = []
    for rec in VV.RECS:
        s = seq_of(rec)
        if len(s) >= 2:
            mx = max(rec['rows'], key=lambda x: x['q'])
            items.append((s, mx['com']))
    real = sum(s[0] == c for s, c in items)
    exp = sum(1 / len(s) for s, _ in items)
    null = []
    for _ in range(R.REPS):
        null.append(sum(R.rng.choice(s) == c for s, c in items))
    p = R.pv_hi(null, real)
    return p, 'The first commodity carries the largest amount more often than chance', {'first_has_max': f'{real}/{len(items)}', 'null': round(sum(null) / len(null), 1), 'p': round(p, 4)}, {}


def GG10():
    ss = [s for s in seqs_where(lambda r: True) if 'VIN' in s]
    real = sum(s[-1] == 'VIN' for s in ss)
    null = [sum(R.rng.choice(s) == 'VIN' for s in ss) for _ in range(R.REPS)]
    p = R.pv_hi(null, real)
    return p, 'Wine stands last more often than chance', {'VIN_last': f'{real}/{len(ss)}', 'null': round(sum(null) / len(null), 1), 'p': round(p, 4)}, {}


def cooc(a, b):
    tabs = defaultdict(set)
    for rec in VV.RECS:
        for x in rec['rows']:
            if x['com']:
                tabs[X.whole(rec['name'])].add(x['com'])
    sets = [s for s in tabs.values() if s]
    real = sum(a in s and b in s for s in sets)
    has_a = [a in s for s in sets]
    has_b = [b in s for s in sets]
    null = []
    for _ in range(R.REPS):
        R.rng.shuffle(has_b)
        null.append(sum(x and y for x, y in zip(has_a, has_b)))
    return real, R.pv_hi(null, real), sum(null) / len(null)


def GG11():
    r, p, nm = cooc('CYP', 'VIN')
    return p, 'Cyperus and wine stand on the same tablets beyond chance', {'together': r, 'null': round(nm, 2), 'p': round(p, 4)}, {}


def GG12():
    r, p, nm = cooc('OLE', 'OLIV')
    return p, 'Oil and olives stand on the same tablets beyond chance', {'together': r, 'null': round(nm, 2), 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round44', 'commodity order, persons and commodities', __doc__, [GG1, GG2, GG3, GG4, GG5, GG8, GG9, GG10, GG11, GG12])
