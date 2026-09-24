"""Round 63 (saturation loop 5): the commodity sign written once and understood. BH at 5% across the seven.

S1  On single-commodity tablets the commodity sign stands in the first entry more often than in later entries.
S2  Linear B single-commodity lists write the logogram on a larger share of entries than Linear A lists do.
S3  On multi-commodity tablets, an entry without a commodity sign has an amount closer (in log) to the median amount
    of the preceding commodity on that tablet than to the median of the tablet's other commodities.
S4  Within commodity blocks on multi-commodity tablets, entries run largest-first beyond chance.
S5  On single-commodity tablets, entries without the sign are name-slot entries more often than entries with it.
S7  Entries with a fraction carry the commodity sign more often than entries without a fraction.
S8  On the same tablet, entries with the commodity sign have larger amounts than entries without it.
"""
from collections import defaultdict
from math import log
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round59 as N  # noqa: E402
import round43 as FF  # noqa: E402
import vigorous2 as W2  # noqa: E402

B, X = R.B, R.X
WORD = N.WORD
com_of = N.com_of


def recs():
    out = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        ents = defaultdict(list)
        for t in r['tokens']:
            if t['cls'] != 'apparatus':
                ents[t['entry']].append(t)
        rows = []
        for e, toks in sorted(ents.items()):
            q = sum(t['value'] for t in toks if t['cls'] == 'number')
            if not q and not any(t['cls'].startswith('fraction') for t in toks):
                continue
            if any(t['label'] in ('KU-RO', 'KI-RO', 'PO-TO-KU-RO') for t in toks):
                continue
            coms = [com_of(t) for t in toks if t['cls'] == 'commodity' and com_of(t)]
            name = any(toks[i]['cls'] in WORD and toks[i + 1]['cls'] == 'number' for i in range(len(toks) - 1))
            rows.append({'q': q, 'com': coms[0] if coms else None, 'frac': any(t['cls'].startswith('fraction') for t in toks), 'name': name})
        ncom = len({x['com'] for x in rows if x['com']})
        if rows:
            out.append({'rows': rows, 'ncom': ncom})
    return out


RECS = recs()
SINGLE = [r for r in RECS if r['ncom'] == 1 and len(r['rows']) >= 3]
MULTI = [r for r in RECS if r['ncom'] >= 2]


def S1():
    items = [(i == 0, x['com'] is not None) for r in SINGLE for i, x in enumerate(r['rows'])]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'The commodity sign stands in the first entry more often', {'first_entry': a, 'later_entries': b, 'p': round(p, 4)}, {}


def lb_single_share():
    import round55 as C
    shares = []
    for _, r in B.LB_RECS:
        if r.get('site') not in ('Knossos', 'Pylos'):
            continue
        tw = [('\n' if t.strip() == '' else t.strip()) for t in r.get('transliteratedWords', [])]
        lines, cur = [], []
        for t in tw + ['\n']:
            if t == '\n':
                if any(re.fullmatch(r'\d+', x) for x in cur):
                    lines.append(cur)
                cur = []
            else:
                cur.append(t)
        logos = {C.LOGO.match(x).group(1) for ln in lines for x in ln if C.LOGO.match(x)}
        if len(lines) >= 3 and len(logos) == 1:
            shares.append(sum(1 for ln in lines if any(C.LOGO.match(x) for x in ln)) / len(lines))
    return shares


def S2():
    la = [sum(1 for x in r['rows'] if x['com']) / len(r['rows']) for r in SINGLE]
    lb = lb_single_share()
    r, p, nm = R.compare(lb, la, lambda v: sum(v) / len(v))
    return p, 'Linear B writes the logogram on more entries than Linear A', {'LB_share': round(sum(lb) / len(lb), 3), 'LA_share': round(sum(la) / len(la), 3), 'p': round(p, 4), 'n': [len(lb), len(la)]}, {}


def S3():
    hits = n = 0
    items = []
    for r in MULTI:
        by = defaultdict(list)
        for x in r['rows']:
            if x['com'] and x['q'] > 0:
                by[x['com']].append(log(x['q']))
        med = {c: sorted(v)[len(v) // 2] for c, v in by.items()}
        prev = None
        for x in r['rows']:
            if x['com']:
                prev = x['com']
            elif prev in med and x['q'] > 0 and len(med) >= 2:
                others = [m for c, m in med.items() if c != prev]
                items.append(abs(log(x['q']) - med[prev]) < min(abs(log(x['q']) - m) for m in others))
    k, n = sum(items), len(items)
    from math import comb
    p = sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n if n else 1.0
    return p, 'Sign-less entries match the preceding commodity\'s scale', {'closer_to_preceding': f'{k}/{n}', 'sign_test_p': round(p, 4)}, {}


def S4():
    lists = []
    for r in MULTI:
        cur, com = [], None
        for x in r['rows']:
            if x['com'] and x['com'] != com:
                if len(cur) >= 3:
                    lists.append(cur)
                cur, com = [], x['com']
            if x['q'] > 0:
                cur.append(x['q'])
        if len(cur) >= 3:
            lists.append(cur)
    real, p, nm = FF.shuffle_within(lists, lambda ls: sum(W2.tau(q) for q in ls) / max(1, len(ls)))
    return p, 'Commodity blocks run largest-first', {'mean_tau': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'blocks': len(lists)}, {}


def S5():
    items = [x for r in SINGLE for x in r['rows']]
    r_, p, a, b = R.flag_compare(items, lambda x: x['com'] is None, lambda x: x['name'])
    return p, 'Sign-less entries are name entries more often', {'signless_name': a, 'signed_name': b, 'p': round(p, 4)}, {}


def S7():
    items = [x for r in RECS for x in r['rows'] if r['ncom'] >= 1]
    r_, p, a, b = R.flag_compare(items, lambda x: x['frac'], lambda x: x['com'] is not None)
    return p, 'Fraction entries carry the commodity sign more often', {'with_fraction': a, 'without': b, 'p': round(p, 4)}, {}


def S8():
    wins = n = 0
    for r in RECS:
        s = [log(x['q']) for x in r['rows'] if x['com'] and x['q'] > 0]
        u = [log(x['q']) for x in r['rows'] if not x['com'] and x['q'] > 0]
        if s and u:
            ms, mu = sum(s) / len(s), sum(u) / len(u)
            if ms != mu:
                n += 1
                wins += ms > mu
    from math import comb
    p = sum(comb(n, i) for i in range(wins, n + 1)) / 2 ** n if n else 1.0
    return p, 'Signed entries are larger than sign-less entries on the same tablet', {'signed_larger': f'{wins}/{n}', 'sign_test_p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round63', 'the commodity sign written once and understood', __doc__, [S1, S2, S3, S4, S5, S7, S8])
