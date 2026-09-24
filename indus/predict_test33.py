"""Test of the thirty-third registered prediction set (PREDICTIONS.md, PL1-PL25): picture markers across label genres.

Usage: python predict_test33.py
Writes results/predict_test33.md. Sample A (data/corpus.tsv) with its 'motif' field; rebus/copper_tablets.tsv.
"""
import csv
import os
import random
import sys
from collections import Counter, defaultdict
from itertools import combinations

import predict_test13 as T
from numerals import NUMS
from predict_test7 import fisher_less
from predict_test14 import cat_of, classes, hyper_ge
from predict_test17 import headed, rank_perm
from predict_test32 import ANIMALS, one_apart, pic
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
POST = ('90', '400', '151')
random.seed(53)
CU_MARK = {'Hare': ['705', '321', '235'], 'Elep': ['923', '706'], 'Goat': ['3', '421', '176', '100', '790'],
           'Anth': ['61', '806', '850', '900'], 'Loop': ['220', '415']}
MO_ANIMAL = {'Bull1', 'Gavi', 'Bult', 'Gaur', 'Fish', 'Zebu', 'Bull', 'Goat'}


def say(s=''):
    OUT.append(s)
    print(s)


def fline(lab, a, na, c, nc, p):
    return '%s %d of %d (%.1f%%) against %d of %d (%.1f%%), p = %.4f' % (
        lab, a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


def gt(lab, a, na, c, nc):
    p = hyper_ge(a, na - a, c, nc - c)
    return fline(lab, a, na, c, nc, p), p < 0.05 and a / max(1, na) > c / max(1, nc)


def lt(lab, a, na, c, nc):
    p = fisher_less(a, na - a, c, nc - c)
    return fline(lab, a, na, c, nc, p), p < 0.05 and a / max(1, na) < c / max(1, nc)


def label_head(t):
    t = list(t)
    while t and t[-1] in POST:
        t.pop()
    if len(t) >= 2 and t[-1] in ('740', '520'):
        return t[-2]
    return t[-1] if t else None


def mi_perm(xs, ys):
    obs = T.mi(xs, ys)
    ge = 0
    xx = list(xs)
    for _ in range(N):
        random.shuffle(xx)
        ge += T.mi(xx, ys) >= obs
    return obs, (ge + 1) / (N + 1)


def share_pairs(objs, grp):
    """Pairs of labels in two 'animal' labels vs mixed; statistic = share(animal-animal sharing) - share(mixed sharing)."""
    sets = [set(r['flat']) for r in objs]
    labs = [grp(r) for r in objs]
    idx = list(combinations(range(len(objs)), 2))
    shr = [bool(sets[i] & sets[j]) for i, j in idx]

    def st(l_):
        aa = [s_ for (i, j), s_ in zip(idx, shr) if l_[i] and l_[j]]
        mx = [s_ for (i, j), s_ in zip(idx, shr) if l_[i] != l_[j]]
        return sum(aa) / max(1, len(aa)) - sum(mx) / max(1, len(mx))
    obs = st(labs)
    ge = 0
    sh = labs[:]
    for _ in range(N // 10):
        random.shuffle(sh)
        ge += st(sh) >= obs
    return obs, (ge + 1) / (N // 10 + 1)


def main():
    rows = [r for r in load() if r['flat']]
    cat = cat_of()
    head, _ = classes(T.sample('A'))
    cu = [r for r in rows if r['type'] == 'TAB:C' and pic(r) and pic(r) not in ('Othr', 'Unknown')]
    mo = [r for r in rows if r['type'] == 'TAB:B' and pic(r) and pic(r) not in ('Othr', 'Unknown')]
    moall = [r for r in rows if r['type'] == 'TAB:B']
    sealsA = [r for r in rows if r['type'].startswith('SEAL')]
    seals = [r for r in sealsA if pic(r)]
    stok = Counter(g for r in sealsA for g in r['flat'])
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    def show(k, title, lo):
        say('## %s %s' % (k, title))
        say('- %s.' % lo[0])
        rec_(k, lo[1])

    say('# Thirty-third registered predictions: picture markers across label genres')
    say()

    # copper
    say('## PL1 the copper label head depends on the picture')
    it = [(pic(r), label_head(r['flat'])) for r in cu if label_head(r['flat'])]
    o, p = mi_perm([a for a, _ in it], [b for _, b in it])
    say('- labels %d; MI %.3f; p = %.4f.' % (len(it), o, p))
    rec_('PL1', p < 0.05)
    say('## PL2 animal labels share signs')
    o, p = share_pairs(cu, lambda r: pic(r) in ANIMALS)
    say('- difference (animal-animal minus mixed pairs sharing a sign) %+.3f; p = %.4f (1,000 permutations).' % (o, p))
    rec_('PL2', o > 0 and p < 0.05)
    say('## PL3 Parpola\'s linked groups show the same reverse')
    grp = {}
    with open(os.path.join(HERE, 'rebus', 'copper_tablets.tsv'), encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('#') or ln.startswith('group\t'):
                continue
            p_ = ln.rstrip('\n').split('\t')
            if len(p_) >= 7:
                grp[p_[0]] = (p_[4].strip(), p_[5].strip(), p_[6].strip())
    pairs = set()
    for g, (_, _, link) in grp.items():
        for l_ in link.replace(',', ' ').split():
            base = [k for k in grp if k == l_ or k.rstrip('ab') == l_]
            for b in base:
                pairs.add(tuple(sorted((g, b))))
    same = [grp[a][1] == 'image' and grp[b][1] == 'image' and grp[a][0] == grp[b][0] for a, b in pairs]
    kinds = Counter(tuple(sorted((grp[a][1], grp[b][1]))) for a, b in pairs)
    say('- linked pairs %d; kinds %s; same reverse image %d; threshold 80%%.' % (len(pairs), dict(kinds), sum(same)))
    rec_('PL3', pairs and sum(same) / len(pairs) >= 0.8)
    say('## PL4 copper markers are rare on seals')
    lsig = sorted({g for r in cu for g in r['flat']})
    marks = {g for m in CU_MARK.values() for g in m}
    labm = [g in marks for g in lsig]
    vals = [stok[g] for g in lsig]

    def st4(l_):
        a = [v for v, x in zip(vals, l_) if x]
        b = [v for v, x in zip(vals, l_) if not x]
        return sum(b) / len(b) - sum(a) / len(a)
    obs = st4(labm)
    ge = 0
    sh = labm[:]
    for _ in range(N):
        random.shuffle(sh)
        ge += st4(sh) >= obs
    p = (ge + 1) / (N + 1)
    say('- markers %d of %d label signs; mean seal count others minus markers %+.1f; p = %.4f.' % (sum(labm), len(lsig), obs, p))
    rec_('PL4', obs > 0 and p < 0.05)
    say('## PL5 no marker is an animal sign')
    an = [g for g in marks if cat.get(g) in ('C', 'D')]
    say('- markers in Fairservis C / D: %s.' % (', '.join(an) or 'none'))
    rec_('PL5', not an)
    say('## PL6 labels of one picture have one length')
    lens = [len(r['flat']) for r in cu]
    pics = [pic(r) for r in cu]

    def bshare(ps):
        m = sum(lens) / len(lens)
        tot = sum((x - m) ** 2 for x in lens)
        by = defaultdict(list)
        for x, q in zip(lens, ps):
            by[q].append(x)
        return sum(len(v) * (sum(v) / len(v) - m) ** 2 for v in by.values()) / tot
    obs = bshare(pics)
    ge = 0
    sh = pics[:]
    for _ in range(N):
        random.shuffle(sh)
        ge += bshare(sh) >= obs
    p = (ge + 1) / (N + 1)
    say('- between-picture share of length variance %.2f; p = %.4f.' % (obs, p))
    rec_('PL6', p < 0.05)
    a = [g in head for g in lsig if g in marks]
    c = [g in head for g in lsig if g not in marks]
    show('PL7', 'markers are heads', gt('head-class, markers', sum(a), len(a), sum(c), len(c)))
    k = sum(len(r['seq']) == 1 for r in cu)
    say('## PL23 copper labels are one line')
    say('- one line %d of %d (%.0f%%); threshold 90%%.' % (k, len(cu), 100 * k / len(cu)))
    rec_('PL23', k / len(cu) >= 0.9)

    # moulded
    by = defaultdict(list)
    for r in mo:
        by[pic(r)].append(set(r['flat']))
    mk = {}
    for p_, sets in by.items():
        if len(sets) < 4:
            continue
        others = [s_ for q, ss in by.items() if q != p_ for s_ in ss]
        mk[p_] = [g for g in set().union(*sets) if sum(g in s_ for s_ in sets) / len(sets) >= 0.75
                  and sum(g in s_ for s_ in others) / max(1, len(others)) <= 0.25]
    say('## PL8 moulded pictures have markers')
    say('- %s.' % '; '.join('%s: %s' % (p_, ', '.join(m) or '-') for p_, m in mk.items()))
    rec_('PL8', mk and sum(1 for m in mk.values() if m) >= len(mk) / 2)
    pl = lambda r: any(cat.get(g) == 'E' for g in r['flat'])
    a = [pl(r) for r in mo if pic(r) == 'Phyt']
    c = [pl(r) for r in mo if pic(r) != 'Phyt']
    show('PL9', 'plant pictures, plant signs', gt('plant sign, Phyt labels', sum(a), len(a), sum(c), len(c)))
    say('## PL10 scene labels are longer')
    o, p = rank_perm([len(r['flat']) for r in mo if pic(r) == 'Scene'], [len(r['flat']) for r in mo if pic(r) != 'Scene'])
    say('- rank difference %+.1f; p = %.4f.' % (o, p))
    rec_('PL10', o > 0 and p < 0.05)
    say('## PL11 the moulded label head depends on the picture')
    it = [(pic(r), label_head(r['flat'])) for r in mo if label_head(r['flat'])]
    o, p = mi_perm([a for a, _ in it], [b for _, b in it])
    say('- labels %d; MI %.3f; p = %.4f.' % (len(it), o, p))
    rec_('PL11', p < 0.05)
    say('## PL12 moulded animal labels share signs')
    o, p = share_pairs(mo, lambda r: pic(r) in MO_ANIMAL)
    say('- difference %+.3f; p = %.4f (1,000 permutations).' % (o, p))
    rec_('PL12', o > 0 and p < 0.05)
    gc = set().union(*[set(r['flat']) for r in cu if pic(r) == 'Gaur']) if any(pic(r) == 'Gaur' for r in cu) else set()
    a = [bool(gc & set(r['flat'])) for r in mo if pic(r) == 'Gaur']
    c = [bool(gc & set(r['flat'])) for r in mo if pic(r) != 'Gaur']
    show('PL13', 'copper and moulded gaur labels share signs', gt('sharing a copper gaur sign, moulded gaur labels', sum(a), len(a), sum(c), len(c)))
    k = sum(r['site'] == 'Harappa' for r in mo)
    say('## PL14 moulded labels are from Harappa')
    say('- %d of %d (%.0f%%); threshold 90%%.' % (k, len(mo), 100 * k / len(mo)))
    rec_('PL14', k / len(mo) >= 0.9)
    pp = lambda r: bool(pic(r)) and pic(r) not in ('Othr', 'Unknown')
    a = [any(g in NUMS for g in r['flat']) for r in moall if pp(r)]
    c = [any(g in NUMS for g in r['flat']) for r in moall if not pp(r)]
    show('PL22', 'pictured moulded tablets are not counts', lt('numeral, pictured moulded', sum(a), len(a), sum(c), len(c)))
    a = [r['direction'] == 'L/R' for r in moall if pp(r)]
    c = [r['direction'] == 'L/R' for r in moall if not pp(r)]
    show('PL24', 'pictured moulded tablets run left to right', gt('left-to-right, pictured moulded', sum(a), len(a), sum(c), len(c)))
    dl = list({(pic(r), tuple(r['flat'])) for r in mo})
    same = [one_apart(a_[1], b_[1]) for a_, b_ in combinations(dl, 2) if a_[0] == b_[0]]
    diff = [one_apart(a_[1], b_[1]) for a_, b_ in combinations(dl, 2) if a_[0] != b_[0]]
    show('PL25', 'same-picture moulded labels are variants', gt('one sign apart, same picture', sum(same), len(same), sum(diff), len(diff)))
    a = [headed(t) for r in mo for t in r['seq'] if len(t) >= 3]
    c = [headed(t) for r in sealsA for t in r['seq'] if len(t) >= 3]
    show('PL21', 'moulded labels carry no heading', lt('headed, moulded label lines', sum(a), len(a), sum(c), len(c)))

    # seals
    ns = [r for r in seals if pic(r) != 'Bull1']
    sets = defaultdict(list)
    for r in ns:
        sets[pic(r)].append(set(r['flat']))
    anim = [a_ for a_, v in sets.items() if len(v) >= 10]
    lm = {}
    for a_ in anim:
        others = [s_ for q, v in sets.items() if q != a_ for s_ in v]
        lm[a_] = [g for g in set().union(*sets[a_]) if sum(g in s_ for s_ in sets[a_]) / len(sets[a_]) >= 0.3
                  and sum(g in s_ for s_ in others) / len(others) <= 0.1]
    say('## PL15 seal animals have loose markers')
    say('- %s.' % '; '.join('%s: %s' % (a_, ', '.join(m) or '-') for a_, m in lm.items()))
    rec_('PL15', lm and sum(1 for m in lm.values() if m) >= len(lm) / 2)
    say('## PL16 same-animal seal texts share signs')
    o, p_ = None, None
    idx = list(combinations(range(len(ns)), 2))
    ss = [set(r['flat']) for r in ns]
    labs = [pic(r) for r in ns]
    shr = [bool(ss[i] & ss[j]) for i, j in idx]

    def st16(l_):
        a_ = [x for (i, j), x in zip(idx, shr) if l_[i] == l_[j]]
        b_ = [x for (i, j), x in zip(idx, shr) if l_[i] != l_[j]]
        return sum(a_) / len(a_) - sum(b_) / len(b_)
    obs = st16(labs)
    ge = 0
    sh = labs[:]
    for _ in range(N // 10):
        random.shuffle(sh)
        ge += st16(sh) >= obs
    p = (ge + 1) / (N // 10 + 1)
    say('- non-unicorn seals %d; difference %+.3f; p = %.4f (1,000 permutations).' % (len(ns), obs, p))
    rec_('PL16', obs > 0 and p < 0.05)
    for key, title, animals, signs_ in (('PL17', 'elephant seals carry the elephant markers', {'Elep'}, {'923', '706'}),
                                        ('PL18', 'goat seals carry the goat markers', {'Goat'}, set(CU_MARK['Goat'])),
                                        ('PL19', 'composite seals carry the anthropomorph markers', {'Comp', 'CompBull', 'T-A-T', 'T-M-T'},
                                         set(CU_MARK['Anth'])),
                                        ('PL20', 'gaur seals carry the copper gaur signs', {'Gaur'}, gc)):
        a = [bool(signs_ & set(r['flat'])) for r in seals if pic(r) in animals]
        c = [bool(signs_ & set(r['flat'])) for r in seals if pic(r) not in animals]
        show(key, title, gt('with the markers, these seals', sum(a), len(a), sum(c), len(c)))

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test33.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
