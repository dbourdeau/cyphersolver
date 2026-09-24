"""Round 65 (saturation loop 7): who kept the once-only logogram at Knossos? BH at 5% across the eight.
"Share" = share of a single-logogram Linear B list's numbered lines that carry the logogram (lower = more economical).

V7  Knossos lists with more Minoan-shaped personal names (stem score) have a lower share (Spearman, negative).
V8  Knossos scribes with lower mean share have more Minoan-shaped names (Spearman over scribes, negative).
V9  Knossos lists from the Room of the Chariot Tablets have a lower share than lists from later deposits.
V10 Knossos lists of women (MUL) have a lower share than lists of men (VIR).
V13 Knossos lists with a lower share contain words with undeciphered signs more often.
V14 Share differs by Knossos scribe (scribes with 3+ lists).
V15 Share differs by Knossos findspot (findspots with 3+ lists).
V16 At Pylos, personnel lists (VIR, MUL) have a lower share than lists of goods.
"""
from collections import Counter, defaultdict
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round55 as C  # noqa: E402
import round34 as W  # noqa: E402

B, T, X = R.B, R.T, R.X
KN = set(T.KN_N)


def lb_lists():
    out = []
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
            words = [tuple(x.lower().split('-')) for ln in lines for x in ln if re.fullmatch(r'[a-zA-Z0-9*]+(-[a-zA-Z0-9*]+)+', x)]
            out.append({'site': r['site'], 'logo': next(iter(logos)), 'share': sum(1 for ln in lines if any(C.LOGO.match(x) for x in ln)) / len(lines),
                        'scribe': r.get('scribe') or None, 'spot': r.get('findspot') or None, 'words': words})
    return out


LL = lb_lists()
KNL = [x for x in LL if x['site'] == 'Knossos']


def spear(xs, ys, lower):
    real = B.spearman(xs, ys)
    null = []
    for _ in range(5000):
        y2 = list(ys)
        R.rng.shuffle(y2)
        null.append(B.spearman(xs, y2))
    return real, (R.pv_lo(null, real) if lower else R.pv_hi(null, real))


def V7():
    items = []
    for x in KNL:
        names = [w for w in x['words'] if w in KN]
        if names:
            items.append((sum(map(R.X.stem_score, names)) / len(names), x['share']))
    real, p = spear([a for a, _ in items], [b for _, b in items], True)
    return p, 'Knossos lists with more Minoan names omit the logogram more', {'spearman': round(real, 3), 'p': round(p, 4), 'lists': len(items)}, {}


def V8():
    by = defaultdict(lambda: {'share': [], 'names': []})
    for x in KNL:
        if x['scribe']:
            by[x['scribe']]['share'].append(x['share'])
            by[x['scribe']]['names'] += [w for w in x['words'] if w in KN]
    rows = [(sum(v['share']) / len(v['share']), sum(map(R.X.stem_score, v['names'])) / len(v['names'])) for v in by.values() if len(v['share']) >= 2 and v['names']]
    real, p = spear([a for a, _ in rows], [b for _, b in rows], True)
    return p, 'Scribes who omit the logogram more have more Minoan names', {'spearman': round(real, 3), 'p': round(p, 4), 'scribes': len(rows)}, {}


def V9():
    items = [x for x in KNL if x['spot']]
    r_, p, a, b = R.flag_compare(items, lambda x: 'RCT' in x['spot'], lambda x: x['share'], lower=True)
    return p, 'Room of the Chariot Tablets lists omit the logogram more', {'RCT': a, 'later': b, 'p': round(p, 4)}, {}


def V10():
    items = [x for x in KNL if x['logo'] in ('MUL', 'VIR')]
    r_, p, a, b = R.flag_compare(items, lambda x: x['logo'] == 'MUL', lambda x: x['share'], lower=True)
    return p, 'Knossos lists of women omit the logogram more than lists of men', {'MUL': a, 'VIR': b, 'p': round(p, 4)}, {}


def V13():
    items = [x for x in KNL]
    r_, p, a, b = R.flag_compare(items, lambda x: x['share'] < 1.0, lambda x: any(any(s.startswith('*') for s in w) for w in x['words']))
    return p, 'Knossos lists that omit the logogram contain undeciphered-sign words more often', {'omitting': a, 'full': b, 'p': round(p, 4)}, {}


def group_ss(key, text):
    c = Counter(x[key] for x in KNL if x[key])
    items = [x for x in KNL if x[key] and c[x[key]] >= 3]
    vals = [x['share'] for x in items]
    real, p, nm = X.shuffle_test(lambda s: W.between(vals, s), [x[key] for x in items], reps=R.REPS)
    return p, text, {'between_SS': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'lists': len(items), 'groups': len({x[key] for x in items})}, {}


def V14():
    return group_ss('scribe', 'Logogram omission differs by Knossos scribe')


def V15():
    return group_ss('spot', 'Logogram omission differs by Knossos findspot')


def V16():
    items = [x for x in LL if x['site'] == 'Pylos']
    r_, p, a, b = R.flag_compare(items, lambda x: x['logo'] in ('VIR', 'MUL'), lambda x: x['share'], lower=True)
    return p, 'Pylos personnel lists omit the logogram more than goods lists', {'personnel': a, 'goods': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round65', 'who kept the once-only logogram at Knossos', __doc__, [V7, V8, V9, V10, V13, V14, V15, V16])
