"""Round 58: words standing directly before a commodity sign (the descriptor slot). Benjamini-Hochberg at 5% across
the eight.

DS1 Words directly before a commodity sign are associated with that commodity (word x commodity, words 3+ times).
DS2 Transaction terms directly before a commodity sign are associated with the commodity.
DS3 Words directly before a commodity sign end in -JA more often than other words.
DS4 Words before a commodity sign recur more (lower type/token ratio) than words before a number.
DS5 Words before a commodity sign are attested at more sites than words before a number.
DS6 The syllable of an oil ligature (OLE+X) matches the first sign of the word directly before it more than chance.
DS7 Words directly before VIR differ in syllable profile from words directly before goods.
DS8 Words ending in -JA stand before VIR more often than before goods.
"""
from collections import Counter, defaultdict
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round41 as DD  # noqa: E402
import round57 as SY  # noqa: E402

B, X = R.B, R.X
WORD = SY.WORD
com_of = lambda t: (re.findall(r'[A-Z]{3,}', t['label']) or [None])[0]
PRE_COM = [(a, b) for a, b in SY.PAIRS if a['cls'] in WORD and b['cls'] == 'commodity' and com_of(b)]
PRE_NUM = [(a, b) for a, b in SY.PAIRS if a['cls'] in WORD and b['cls'] == 'number']


def DS1():
    pairs = [(a['label'], com_of(b)) for a, b in PRE_COM]
    c = Counter(w for w, _ in pairs)
    pairs = [x for x in pairs if c[x[0]] >= 3]
    real, p, nm = R.assoc(pairs)
    return p, 'Words before a commodity sign are associated with that commodity', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'pairs': len(pairs)},\
        {'word -> commodity': [f'{w} -> {g} x{n}' for (w, g), n in Counter(pairs).most_common(15)]}


def DS2():
    pairs = [(a['label'], com_of(b)) for a, b in PRE_COM if a['label'] in SY.TERMS]
    real, p, nm = R.assoc(pairs)
    return p, 'Transaction terms before a commodity sign are associated with that commodity', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'pairs': len(pairs)},\
        {'term -> commodity': [f'{w} -> {g} x{n}' for (w, g), n in Counter(pairs).most_common(10)]}


def DS3():
    pre = {a['label'] for a, _ in PRE_COM}
    words = sorted({a['label'] for a, _ in SY.PAIRS if a['cls'] in WORD})
    r_, p, a, b = R.flag_compare(words, lambda w: w in pre, lambda w: w.endswith('-JA'))
    return p, 'Pre-commodity words end in -JA more often', {'pre_commodity': a, 'other': b, 'p': round(p, 4)}, {}


def DS4():
    a = [x['label'] for x, _ in PRE_COM]
    b = [x['label'] for x, _ in PRE_NUM]
    n = len(a)
    real = len(set(a)) / n
    null = [len(set(R.rng.sample(b, n))) / n for _ in range(R.REPS)]
    p = R.pv_lo(null, real)
    return p, 'Pre-commodity words recur more than pre-number words', {'type_token_pre_commodity': round(real, 3), 'pre_number_same_size': round(sum(null) / len(null), 3), 'p': round(p, 4)}, {}


def DS5():
    sites = defaultdict(set)
    for r in B.READ['records']:
        for t in r['tokens']:
            if t['cls'] in WORD:
                sites[t['label']].add(r['site'])
    pre = {a['label'] for a, _ in PRE_COM}
    num = {a['label'] for a, _ in PRE_NUM} - pre
    words = sorted(pre | num)
    r_, p, a, b = R.flag_compare(words, lambda w: w in pre, lambda w: len(sites[w]))
    return p, 'Pre-commodity words are attested at more sites', {'pre_commodity_mean_sites': a, 'pre_number': b, 'p': round(p, 4)}, {}


def DS6():
    items = []
    for a, b in PRE_COM:
        lab = b['label'].split('-')[-1]
        if lab.startswith('OLE+'):
            adj = lab.split('+')[1]
            items.append((adj, a['label'].split('-')[0]))
    real = sum(x == y for x, y in items)
    adjs = [x for x, _ in items]
    null = []
    for _ in range(R.REPS):
        R.rng.shuffle(adjs)
        null.append(sum(x == y for x, (_, y) in zip(adjs, items)))
    p = R.pv_hi(null, real)
    return p, 'Oil ligature syllable matches the first sign of the preceding word', {'matches': f'{real}/{len(items)}', 'null': round(sum(null) / len(null), 2), 'p': round(p, 4)}, {'pairs': [f'{y}... OLE+{x}' for x, y in items][:15]}


def DS7():
    to_tuple = lambda l: tuple(l.lower().split('-'))
    plain = lambda l: all(re.fullmatch(r'[A-Z]+[0-9]?', x) for x in l.split('-'))
    vir = sorted({to_tuple(a['label']) for a, b in PRE_COM if com_of(b) == 'VIR' and plain(a['label'])})
    goods = sorted({to_tuple(a['label']) for a, b in PRE_COM if com_of(b) != 'VIR' and plain(a['label'])} - set(vir))
    real = DD.jsd_words(vir, goods)
    pool, k, null = vir + goods, len(vir), []
    for _ in range(R.REPS):
        R.rng.shuffle(pool)
        null.append(DD.jsd_words(pool[:k], pool[k:]))
    p = R.pv_hi(null, real)
    return p, 'Words before VIR differ in syllable profile from words before goods', {'jsd': round(real, 4), 'null': round(sum(null) / len(null), 4), 'p': round(p, 4), 'n': [len(vir), len(goods)]}, {}


def DS8():
    items = [(a['label'], com_of(b) == 'VIR') for a, b in PRE_COM]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0].endswith('-JA'), lambda x: x[1])
    return p, '-JA words stand before VIR more often than before goods', {'JA_before_VIR': a, 'other_before_VIR': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round58', 'words in the descriptor slot before a commodity sign', __doc__, [DS1, DS2, DS3, DS4, DS5, DS6, DS7, DS8])
