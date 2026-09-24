"""Round 60 (saturation loop 2): consequences of the two word classes of round 59. BH at 5% across the ten.

P1  Khania tablets carry fewer distinct name-slot words per tablet than Haghia Triada tablets.
P2  On goods tablets, descriptor entries stand earlier in their list (relative position) than name entries.
P3  Tablets whose heading word is a term (also used in the descriptor slot) contain descriptor entries more often.
P4  Descriptor words repeat within a tablet more often than name words.
P6  Name-slot words show consonant harmony (different signs) more often than descriptor words.
P8  Q-initial words stand in the name slot more often than in the descriptor slot.
P9  Vowel-initial words stand in the descriptor slot more often than in the name slot.
P10 Descriptor words (2+ tablets) are written by more distinct scribes than name words (2+ tablets).
P11 Descriptor words also occur in religious texts more often than name words.
P12 Descriptor words (2+ tablets) are attested at more sites than name words (2+ tablets).
"""
from collections import Counter, defaultdict
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round29 as P  # noqa: E402
import round59 as N  # noqa: E402

B, X = R.B, R.X
cons, vow = P.cons, P.vow
TOK, DESC, NAME = N.TOK, N.DESC, N.NAME
DSET = {x['label'] for x in DESC}
NSET = {x['label'] for x in NAME} - DSET
w_of = lambda l: tuple(l.lower().split('-'))


def P1():
    per = defaultdict(set)
    site = {}
    for x in NAME:
        per[X.whole(x['rec'])].add(x['label'])
        site[X.whole(x['rec'])] = x['site']
    tabs = [k for k in {X.whole(x['rec']) for x in TOK} if site.get(k) in ('Khania', 'Haghia Triada') or k in per]
    items = [(k, len(per.get(k, ()))) for k in tabs if site.get(k, None) in ('Khania', 'Haghia Triada') or True]
    items = [(k, n) for k, n in items if (site.get(k) or next((x['site'] for x in TOK if X.whole(x['rec']) == k), None)) in ('Khania', 'Haghia Triada')]
    st = {k: (site.get(k) or next(x['site'] for x in TOK if X.whole(x['rec']) == k)) for k, _ in items}
    r_, p, a, b = R.flag_compare(items, lambda x: st[x[0]] == 'Khania', lambda x: x[1], lower=True)
    return p, 'Khania tablets carry fewer name-slot words than Haghia Triada tablets', {'Khania': a, 'HT': b, 'p': round(p, 4)}, {}


def P2():
    vir = {r['name'] for r in B.READ['records'] if any(t['cls'] == 'commodity' and t['label'].startswith('VIR') for t in r['tokens'])}
    by = defaultdict(list)
    for x in TOK:
        if x['rec'] not in vir:
            by[x['rec']].append(x)
    items = []
    for rec, xs in by.items():
        if len(xs) >= 3 and any(x['slot'] == 'desc' for x in xs) and any(x['slot'] == 'name' for x in xs):
            for i, x in enumerate(xs):
                items.append((x['slot'] == 'desc', i / (len(xs) - 1)))
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1], lower=True)
    return p, 'Descriptor entries stand earlier in the list', {'desc_mean_position': a, 'name_mean_position': b, 'p': round(p, 4)}, {}


def P3():
    heads = {}
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        for t in r['tokens']:
            if t['cls'] in N.WORD and t.get('function') == 'heading':
                heads.setdefault(X.whole(r['name']), t['label'])
                break
    has_desc = {X.whole(x['rec']) for x in DESC}
    items = [(h in DSET, k in has_desc) for k, h in heads.items()]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'Tablets headed by a term contain descriptor entries more often', {'term_headed': a, 'other': b, 'p': round(p, 4)}, {}


def P4():
    def rep(xs):
        by = defaultdict(list)
        for x in xs:
            by[x['rec']].append(x['label'])
        tot = sum(len(v) for v in by.values())
        return sum(len(v) - len(set(v)) for v in by.values()) / max(1, tot)
    r, p, nm = R.compare(DESC, NAME, rep)
    return p, 'Descriptor words repeat within a tablet more than name words', {'desc': round(rep(DESC), 3), 'name': round(rep(NAME), 3), 'p': round(p, 4)}, {}


harm = lambda w: any(cons(w[i]) and cons(w[i]) == cons(w[i + 1]) and w[i] != w[i + 1] for i in range(len(w) - 1))


def slot_types():
    d = sorted(w_of(l) for l in DSET if N.plain(l))
    n = sorted(w_of(l) for l in NSET if N.plain(l))
    return d, n


def P6():
    d, n = slot_types()
    f = lambda ws: sum(map(harm, ws)) / len(ws)
    r, p, nm = R.compare(n, d, f)
    return p, 'Name words show harmony more than descriptor words', {'name': round(f(n), 3), 'desc': round(f(d), 3), 'p': round(p, 4)}, {}


def P8():
    d, n = slot_types()
    f = lambda ws: sum(1 for w in ws if cons(w[0]) == 'q') / len(ws)
    r, p, nm = R.compare(n, d, f)
    return p, 'Q-initial words are name-slot words more often', {'name': round(f(n), 3), 'desc': round(f(d), 3), 'p': round(p, 4)}, {}


def P9():
    d, n = slot_types()
    f = lambda ws: sum(1 for w in ws if vow(w[0])) / len(ws)
    r, p, nm = R.compare(d, n, f)
    return p, 'Vowel-initial words are descriptor-slot words more often', {'desc': round(f(d), 3), 'name': round(f(n), 3), 'p': round(p, 4)}, {}


def spread(key):
    tabs = defaultdict(set)
    vals = defaultdict(set)
    for x in TOK:
        k = X.whole(x['rec'])
        tabs[x['label']].add(k)
        v = X.SCRIBE_W.get(k) if key == 'scribe' else x['site']
        if v:
            vals[x['label']].add(v)
    words = [w for w in tabs if len(tabs[w]) >= 2 and (w in DSET or w in NSET)]
    return words, vals


def P10():
    words, vals = spread('scribe')
    r_, p, a, b = R.flag_compare(words, lambda w: w in DSET, lambda w: len(vals[w]))
    return p, 'Descriptor words are written by more scribes', {'desc': a, 'name': b, 'p': round(p, 4)}, {}


def P11():
    rel = {'-'.join(w).upper() for _, _, w in B.LA_RELIG}
    words = sorted(DSET | NSET)
    r_, p, a, b = R.flag_compare(words, lambda w: w in DSET, lambda w: w in rel)
    return p, 'Descriptor words occur in religious texts more often', {'desc': a, 'name': b, 'p': round(p, 4)}, {}


def P12():
    words, vals = spread('site')
    r_, p, a, b = R.flag_compare(words, lambda w: w in DSET, lambda w: len(vals[w]))
    return p, 'Descriptor words (2+ tablets) are attested at more sites', {'desc': a, 'name': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round60', 'consequences of the two word classes', __doc__, [P1, P2, P3, P4, P6, P8, P9, P10, P11, P12])
