"""Round 43 (second loop, round 5 of 10): the bookkeeping, second pass.

Lists are the entry sequences of round33.RECS (one record = one side of a tablet; entry order kept).

FF1  At Haghia Triada, lists on tablets with a total are more strictly largest-first (Kendall tau) than others.
FF2  Lists on tablets with a total are single-commodity more often.
FF3  KI-RO stands on tablets that also have KU-RO more often than chance (tablet sides merged).
FF4  The first entry is the unique largest more often than chance in lists of goods (no VIR).
FF5  Tablets with fractions carry a total more often.
FF6  Lists of men (VIR) are longer than lists of goods.
FF7  Entries with fractions stand on neighbouring lines more often than chance.
FF8  Lists that open with a heading word are longer.
FF9  Multi-commodity tablets list their commodities in a consistent order across tablets.
FF10 Entries of the same commodity stand in blocks more often than chance.
"""
from collections import Counter, defaultdict
from math import log
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round33 as VV  # noqa: E402

B, X = R.B, R.X
import vigorous2 as W2  # noqa: E402

RECS = VV.RECS
SITE = {r['name']: r['site'] for r in B.READ['records']}
FIRST_HEAD = {}
for _r in B.READ['records']:
    for _t in _r['tokens']:
        if _t['cls'] in ('word', 'term'):
            FIRST_HEAD[_r['name']] = _t.get('function') == 'heading'
            break


def shuffle_within(lists, stat, reps=R.REPS):
    real = stat(lists)
    null = []
    for _ in range(reps):
        sh = []
        for q in lists:
            q2 = list(q)
            R.rng.shuffle(q2)
            sh.append(q2)
        null.append(stat(sh))
    return real, R.pv_hi(null, real), sum(null) / len(null)


def FF1():
    items = [rec for rec in RECS if SITE[rec['name']] == 'Haghia Triada' and len(rec['rows']) >= 4]
    r_, p, a, b = R.flag_compare(items, lambda r: r['total'], lambda r: W2.tau([x['q'] for x in r['rows']]))
    return p, 'At HT, lists with a total are more strictly largest-first', {'with_total_tau': a, 'without': b, 'p': round(p, 4)}, {}


def FF2():
    items = [rec for rec in RECS if len(rec['rows']) >= 2 and any(x['com'] for x in rec['rows'])]
    r_, p, a, b = R.flag_compare(items, lambda r: r['total'], lambda r: len({x['com'] for x in r['rows'] if x['com']}) == 1)
    return p, 'Lists with a total are single-commodity more often', {'with_total': a, 'without': b, 'p': round(p, 4)}, {}


def FF3():
    tabs = defaultdict(lambda: [False, False])
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        k = X.whole(r['name'])
        for t in r['tokens']:
            if t['label'] == 'KI-RO':
                tabs[k][0] = True
            if t['label'] in ('KU-RO', 'PO-TO-KU-RO'):
                tabs[k][1] = True
    items = list(tabs.values())
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'KI-RO stands on tablets with KU-RO more often than chance', {'kiro_tablets_with_kuro': a, 'others_with_kuro': b, 'p': round(p, 4)}, {}


def FF4():
    lists = [[x['q'] for x in rec['rows']] for rec in RECS if len(rec['rows']) >= 3 and all(x['q'] > 0 for x in rec['rows'])
             and not any(x['com'] == 'VIR' for x in rec['rows'])]
    real, p, nm = shuffle_within(lists, lambda ls: sum(q[0] == max(q) and q.count(max(q)) == 1 for q in ls))
    return p, 'The first entry is the unique largest in lists of goods', {'first_is_max': f'{real}/{len(lists)}', 'null': round(nm, 1), 'p': round(p, 4)}, {}


def FF5():
    items = [rec for rec in RECS if len(rec['rows']) >= 2]
    r_, p, a, b = R.flag_compare(items, lambda r: any(x['frac'] for x in r['rows']), lambda r: r['total'])
    return p, 'Tablets with fractions carry a total more often', {'with_fractions': a, 'without': b, 'p': round(p, 4)}, {}


def FF6():
    items = [rec for rec in RECS if any(x['com'] for x in rec['rows'])]
    r_, p, a, b = R.flag_compare(items, lambda r: any(x['com'] == 'VIR' for x in r['rows']), lambda r: len(r['rows']))
    return p, 'Lists of men are longer than lists of goods', {'VIR_lists': a, 'goods_lists': b, 'p': round(p, 4)}, {}


def FF7():
    lists = [[x['frac'] for x in rec['rows']] for rec in RECS if len(rec['rows']) >= 3 and any(x['frac'] for x in rec['rows'])]
    real, p, nm = shuffle_within(lists, lambda ls: sum(1 for q in ls for i in range(len(q) - 1) if q[i] and q[i + 1]))
    return p, 'Fraction entries stand on neighbouring lines more often than chance', {'adjacent': real, 'null': round(nm, 1), 'p': round(p, 4)}, {}


def FF8():
    items = [rec for rec in RECS if rec['name'] in FIRST_HEAD]
    r_, p, a, b = R.flag_compare(items, lambda r: FIRST_HEAD[r['name']], lambda r: len(r['rows']))
    return p, 'Lists that open with a heading are longer', {'with_heading': a, 'without': b, 'p': round(p, 4)}, {}


def FF9():
    seqs = []
    for rec in RECS:
        order = list(dict.fromkeys(x['com'] for x in rec['rows'] if x['com']))
        if len(order) >= 2:
            seqs.append(order)

    def stat(ss):
        c = Counter()
        for s in ss:
            for i in range(len(s)):
                for j in range(i + 1, len(s)):
                    c[(s[i], s[j])] += 1
        return sum(abs(c[(a, b)] - c[(b, a)]) for (a, b) in {tuple(sorted(k)) for k in c})
    real, p, nm = shuffle_within(seqs, stat)
    c = Counter()
    for s in seqs:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                c[f'{s[i]}<{s[j]}'] += 1
    return p, 'Multi-commodity tablets list commodities in a consistent order', {'order_asymmetry': real, 'null': round(nm, 1), 'p': round(p, 4), 'tablets': len(seqs)}, {'commonest orders': c.most_common(10)}


def FF10():
    lists = [[x['com'] for x in rec['rows'] if x['com']] for rec in RECS]
    lists = [l for l in lists if len(set(l)) >= 2 and len(l) >= 3]
    real, p, nm = shuffle_within(lists, lambda ls: sum(1 for q in ls for i in range(len(q) - 1) if q[i] == q[i + 1]))
    return p, 'Same-commodity entries stand in blocks more often than chance', {'adjacent_same': real, 'null': round(nm, 1), 'p': round(p, 4), 'lists': len(lists)}, {}


if __name__ == '__main__':
    R.run('round43', 'the bookkeeping, second pass', __doc__, [FF1, FF2, FF3, FF4, FF5, FF6, FF7, FF8, FF9, FF10])
