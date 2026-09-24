"""Round 59 (saturation loop): the name slot (word directly before a number) and the descriptor slot (word directly
before a commodity sign). Benjamini-Hochberg at 5% across the ten.

N1  The two slots are lexically separate: fewer word types occur in both than when slot labels are shuffled
    among the word tokens.
N2  Word types in the two slots differ in syllable profile.
N3  Entries whose word stands in the descriptor slot have larger amounts than name-slot entries.
N4  Descriptor-slot words contain unread signs less often than name-slot words.
N5  Heading words recur more (lower type/token ratio) than name-slot words at the same sample size.
N6  Heading word types overlap with descriptor-slot types more than with name-slot types (share of heading types).
N7  Descriptor-slot words are shorter than name-slot words.
N8  Descriptor words used 2+ times go with a single commodity more often than when commodities are shuffled.
N9  Use of the descriptor slot (share of word-plus-commodity entries) differs by site.
N10 Descriptor-slot entries carry fractions more often than name-slot entries.
"""
from collections import Counter, defaultdict
from math import log
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round41 as DD  # noqa: E402
import round57 as SY  # noqa: E402
import round58 as DS  # noqa: E402

B, X = R.B, R.X
WORD = SY.WORD
com_of = DS.com_of


def slot_tokens():
    """(label, slot, record, amount, fraction flag, commodity) for each word followed by a number or commodity."""
    out = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        ents = defaultdict(list)
        for t in r['tokens']:
            if t['cls'] != 'apparatus':
                ents[t['entry']].append(t)
        toks = [t for t in r['tokens'] if t['cls'] != 'apparatus']
        for i in range(len(toks) - 1):
            a, b = toks[i], toks[i + 1]
            if a['cls'] not in WORD or b['cls'] not in ('number', 'commodity'):
                continue
            e = ents[a['entry']]
            q = sum(t['value'] for t in e if t['cls'] == 'number')
            out.append({'label': a['label'], 'slot': 'desc' if b['cls'] == 'commodity' else 'name', 'rec': r['name'], 'site': r['site'],
                        'q': q, 'frac': any(t['cls'].startswith('fraction') for t in e), 'com': com_of(b) if b['cls'] == 'commodity' else None})
    return out


TOK = slot_tokens()
DESC = [x for x in TOK if x['slot'] == 'desc']
NAME = [x for x in TOK if x['slot'] == 'name']


def N1():
    labels = [x['label'] for x in TOK]
    slots = [x['slot'] for x in TOK]
    stat = lambda sl: len({l for l, s in zip(labels, sl) if s == 'desc'} & {l for l, s in zip(labels, sl) if s == 'name'})
    real = stat(slots)
    null = []
    for _ in range(R.REPS):
        R.rng.shuffle(slots)
        null.append(stat(slots))
    p = R.pv_lo(null, real)
    return p, 'The two slots are lexically separate', {'shared_types': real, 'null': round(sum(null) / len(null), 1), 'p': round(p, 4)}, {}


def tup(l):
    return tuple(l.lower().split('-'))


def plain(l):
    return all(re.fullmatch(r'[A-Z]+[0-9]?', x) for x in l.split('-'))


def N2():
    d = sorted({tup(x['label']) for x in DESC if plain(x['label'])})
    n = sorted({tup(x['label']) for x in NAME if plain(x['label'])} - set(d))
    real = DD.jsd_words(d, n)
    pool, k, null = d + n, len(d), []
    for _ in range(R.REPS):
        R.rng.shuffle(pool)
        null.append(DD.jsd_words(pool[:k], pool[k:]))
    p = R.pv_hi(null, real)
    return p, 'The slots differ in syllable profile', {'jsd': round(real, 4), 'null': round(sum(null) / len(null), 4), 'p': round(p, 4), 'n': [len(d), len(n)]}, {}


def N3():
    items = [x for x in TOK if x['q'] > 0]
    r_, p, a, b = R.flag_compare(items, lambda x: x['slot'] == 'desc', lambda x: log(x['q']))
    return p, 'Descriptor-slot entries have larger amounts', {'desc_mean_log': a, 'name_mean_log': b, 'p': round(p, 4)}, {}


def N4():
    r_, p, a, b = R.flag_compare(TOK, lambda x: x['slot'] == 'desc', lambda x: '*' in x['label'], lower=True)
    return p, 'Descriptor words contain unread signs less often', {'desc': a, 'name': b, 'p': round(p, 4)}, {}


def headings():
    return [t['label'] for r in B.READ['records'] if r['support'] in B.ADMIN for t in r['tokens'] if t['cls'] in WORD and t.get('function') == 'heading']


def N5():
    h = headings()
    names = [x['label'] for x in NAME]
    n = min(len(h), len(names))
    h_ttr = sum(len(set(R.rng.sample(h, n))) / n for _ in range(200)) / 200
    null = [len(set(R.rng.sample(names, n))) / n for _ in range(R.REPS)]
    p = R.pv_lo(null, h_ttr)
    return p, 'Heading words recur more than name-slot words', {'heading_ttr': round(h_ttr, 3), 'name_ttr_same_size': round(sum(null) / len(null), 3), 'p': round(p, 4), 'n': n}, {}


def N6():
    h = set(headings())
    d = {x['label'] for x in DESC}
    n = {x['label'] for x in NAME} - d
    pool = sorted(d | n)
    is_d = [w in d for w in pool]
    stat = lambda fl: sum(1 for w, f in zip(pool, fl) if f and w in h) / max(1, sum(fl)) - sum(1 for w, f in zip(pool, fl) if not f and w in h) / max(1, len(fl) - sum(fl))
    real = stat(is_d)
    null = []
    for _ in range(R.REPS):
        R.rng.shuffle(is_d)
        null.append(stat(is_d))
    p = R.pv_hi(null, real)
    return p, 'Heading types overlap descriptor types more than name types', {'diff': round(real, 3), 'null': round(sum(null) / len(null), 3), 'p': round(p, 4)}, {}


def N7():
    d = sorted({x['label'] for x in DESC})
    n = sorted({x['label'] for x in NAME} - set(d))
    ln = lambda ws: sum(len(w.split('-')) for w in ws) / len(ws)
    r, p, nm = R.compare(d, n, ln, lower=True)
    return p, 'Descriptor words are shorter', {'desc_len': round(ln(d), 2), 'name_len': round(ln(n), 2), 'p': round(p, 4)}, {}


def N8():
    by = defaultdict(list)
    for x in DESC:
        by[x['label']].append(x['com'])
    words = [w for w, c in by.items() if len(c) >= 2]
    items = [(w, c) for w in words for c in by[w]]
    stat = lambda cs: sum(len(set(c for (w2, _), c in zip(items, cs) if w2 == w)) == 1 for w in words) / len(words)
    coms = [c for _, c in items]
    real = stat(coms)
    null = []
    for _ in range(R.REPS):
        R.rng.shuffle(coms)
        null.append(stat(coms))
    p = R.pv_hi(null, real)
    return p, 'Descriptor words keep a single commodity', {'single_commodity_share': round(real, 3), 'null': round(sum(null) / len(null), 3), 'p': round(p, 4), 'words': len(words)}, {}


def N9():
    c = Counter(x['site'] for x in TOK)
    items = [(x['site'], x['slot']) for x in TOK if c[x['site']] >= 10]
    real, p, nm = R.assoc(items)
    return p, 'Use of the descriptor slot differs by site', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4)},\
        {'descriptor share by site': {s: round(sum(1 for s2, sl in items if s2 == s and sl == 'desc') / n, 3) for s, n in Counter(s for s, _ in items).items()}}


def N10():
    r_, p, a, b = R.flag_compare(TOK, lambda x: x['slot'] == 'desc', lambda x: x['frac'])
    return p, 'Descriptor entries carry fractions more often', {'desc': a, 'name': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round59', 'the name slot and the descriptor slot', __doc__, [N1, N2, N3, N4, N5, N6, N7, N8, N9, N10])
