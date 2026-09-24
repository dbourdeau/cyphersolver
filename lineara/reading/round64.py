"""Round 64 (saturation loop 6): who wrote the commodity sign once, and where. BH at 5% across the seven.
"Sign share" = share of a list's entries that carry a commodity sign (single-commodity lists of 3+ entries).

U1 Khania lists have a higher sign share than Haghia Triada lists.
U2 Sign share differs by scribe (Haghia Triada hands with 3+ lists).
U3 Longer lists have a lower sign share (Spearman, predicted negative).
U4 Knossos Linear B single-logogram lists write the logogram on fewer lines than Pylos lists.
U5 Lists of men (VIR) have a lower sign share than lists of goods.
U6 KU-RO total entries carry the commodity sign more often than ordinary later entries.
U7 Lists with a lower sign share are more strictly largest-first (Spearman of sign share against tau, predicted
   negative).
"""
from collections import defaultdict
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round59 as N  # noqa: E402
import round63 as S  # noqa: E402
import round34 as W  # noqa: E402
import vigorous2 as W2  # noqa: E402

B, X = R.B, R.X
com_of = N.com_of


def lists():
    out = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        ents = defaultdict(list)
        for t in r['tokens']:
            if t['cls'] != 'apparatus':
                ents[t['entry']].append(t)
        rows, kuro = [], []
        for e, toks in sorted(ents.items()):
            q = sum(t['value'] for t in toks if t['cls'] == 'number')
            has_com = any(t['cls'] == 'commodity' and com_of(t) for t in toks)
            if any(t['label'] in ('KU-RO', 'PO-TO-KU-RO') for t in toks):
                kuro.append(has_com)
                continue
            if q or any(t['cls'].startswith('fraction') for t in toks):
                rows.append({'q': q, 'com': (com_of(next(t for t in toks if t['cls'] == 'commodity' and com_of(t))) if has_com else None)})
        coms = {x['com'] for x in rows if x['com']}
        if len(rows) >= 3 and len(coms) == 1:
            out.append({'name': r['name'], 'site': r['site'], 'scribe': X.SCRIBE_W.get(X.whole(r['name'])), 'com': next(iter(coms)),
                        'share': sum(1 for x in rows if x['com']) / len(rows), 'n': len(rows), 'q': [x['q'] for x in rows], 'kuro': kuro,
                        'later_signed': [x['com'] is not None for x in rows[1:]]})
    return out


L = lists()


def U1():
    items = [x for x in L if x['site'] in ('Khania', 'Haghia Triada')]
    r_, p, a, b = R.flag_compare(items, lambda x: x['site'] == 'Khania', lambda x: x['share'])
    return p, 'Khania lists repeat the commodity sign more', {'Khania': a, 'HT': b, 'p': round(p, 4)}, {}


def U2():
    from collections import Counter
    c = Counter(x['scribe'] for x in L if x['scribe'])
    items = [x for x in L if x['scribe'] and c[x['scribe']] >= 3]
    vals = [x['share'] for x in items]
    real, p, nm = X.shuffle_test(lambda s: W.between(vals, s), [x['scribe'] for x in items], reps=R.REPS)
    return p, 'Sign share differs by scribe', {'between_SS': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'lists': len(items)}, {}


def spear(xs, ys, lower):
    real = B.spearman(xs, ys)
    null = []
    for _ in range(5000):
        y2 = list(ys)
        R.rng.shuffle(y2)
        null.append(B.spearman(xs, y2))
    return real, (R.pv_lo(null, real) if lower else R.pv_hi(null, real))


def U3():
    real, p = spear([x['n'] for x in L], [x['share'] for x in L], True)
    return p, 'Longer lists write the sign on a smaller share of entries', {'spearman': round(real, 3), 'p': round(p, 4), 'lists': len(L)}, {}


def lb_shares(site):
    import round55 as C
    out = []
    for _, r in B.LB_RECS:
        if r.get('site') != site:
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
            out.append(sum(1 for ln in lines if any(C.LOGO.match(x) for x in ln)) / len(lines))
    return out


def U4():
    kn, py = lb_shares('Knossos'), lb_shares('Pylos')
    r, p, nm = R.compare(kn, py, lambda v: sum(v) / len(v), lower=True)
    return p, 'Knossos writes the logogram on fewer lines than Pylos', {'KN': round(sum(kn) / len(kn), 3), 'PY': round(sum(py) / len(py), 3), 'p': round(p, 4), 'n': [len(kn), len(py)]}, {}


def U5():
    r_, p, a, b = R.flag_compare(L, lambda x: x['com'] == 'VIR', lambda x: x['share'], lower=True)
    return p, 'Lists of men write the sign on a smaller share', {'VIR': a, 'goods': b, 'p': round(p, 4)}, {}


def U6():
    items = [(True, k) for x in L for k in x['kuro']] + [(False, s) for x in L for s in x['later_signed']]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'KU-RO entries carry the commodity sign more often than later entries', {'kuro_signed': a, 'later_signed': b, 'p': round(p, 4)}, {}


def U7():
    items = [x for x in L if all(v > 0 for v in x['q'])]
    real, p = spear([x['share'] for x in items], [W2.tau(x['q']) for x in items], True)
    return p, 'Lists that write the sign less often are more strictly largest-first', {'spearman': round(real, 3), 'p': round(p, 4), 'lists': len(items)}, {}


if __name__ == '__main__':
    R.run('round64', 'who wrote the commodity sign once, and where', __doc__, [U1, U2, U3, U4, U5, U6, U7])
