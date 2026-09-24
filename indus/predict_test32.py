"""Test of the thirty-second registered prediction set (PREDICTIONS.md, CT1-CT25): pictures as outside labels.

Usage: python predict_test32.py
Writes results/predict_test32.md. Sample A (data/corpus.tsv) with its 'motif' field.
"""
import os
import random
import sys
from collections import Counter, defaultdict
from itertools import combinations

import predict_test13 as T
from numerals import NUMS
from predict_test4 import name_of
from predict_test7 import fisher_less
from predict_test14 import cat_of, classes, hyper_ge
from predict_test15 import binom_ge
from predict_test17 import rank_perm
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 10000
POST = ('90', '400', '151')
ANIMALS = {'Hare', 'Elep', 'Gaur', 'Goat', 'Rhin', 'Tigr', 'Buff', 'Bull1'}
NONANIMAL = {'Anth', 'Comp', 'Loop'}
CU_ANCH = [('341', 'Rhin'), ('749', 'Goat'), ('778', 'Goat'), ('753', 'Hare')]
MO_ANCH = [('347', 'Mult'), ('460', 'Phyt'), ('645', 'Cros'), ('318', 'Gavi')]
random.seed(52)


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


def pic(r):
    return r['motif'].split(':')[0].strip()


def ends740(t):
    t = list(t)
    while t and t[-1] in POST:
        t.pop()
    return bool(t) and t[-1] == '740'


def ends520(t):
    t = list(t)
    while t and t[-1] in POST:
        t.pop()
    return bool(t) and t[-1] == '520'


def one_apart(a, b):
    if a == b:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    if abs(len(a) - len(b)) == 1:
        s, l_ = (a, b) if len(a) < len(b) else (b, a)
        return any(l_[:i] + l_[i + 1:] == s for i in range(len(l_)))
    return False


def anchor_perm(labels, anchors):
    """labels: list of (picture, set of signs). Statistic: number of (anchor, label) with the anchor in a label of its
    own picture; pictures permuted among labels."""
    pics = [p_ for p_, _ in labels]
    sets = [s_ for _, s_ in labels]

    def st(ps):
        return sum(1 for (g, pa) in anchors for p_, s_ in zip(ps, sets) if p_ == pa and g in s_)
    obs = st(pics)
    ge = 0
    sh = pics[:]
    for _ in range(N):
        random.shuffle(sh)
        ge += st(sh) >= obs
    return obs, (ge + 1) / (N + 1)


def main():
    rows = [r for r in load() if r['flat']]
    cat = cat_of()
    head, _ = classes(T.sample('A'))
    cu = [r for r in rows if r['type'] == 'TAB:C' and pic(r) and pic(r) not in ('Othr', 'Unknown')]
    mo = [r for r in rows if r['type'] == 'TAB:B' and pic(r) and pic(r) not in ('Othr', 'Unknown')]
    moall = [r for r in rows if r['type'] == 'TAB:B']
    seals = [r for r in rows if r['type'].startswith('SEAL') and pic(r)]
    res = []

    def rec_(k, ok):
        say('- **%s %s.**' % (k, T.verdict(ok)))
        say()
        res.append((k, ok))

    def show(k, title, lo):
        say('## %s %s' % (k, title))
        say('- %s.' % lo[0])
        rec_(k, lo[1])

    say('# Thirty-second registered predictions: pictures as outside labels for meaning')
    say()
    say('- copper labels %d (%s); moulded labels %d; seals with a picture %d.' % (
        len(cu), dict(Counter(map(pic, cu)).most_common()), len(mo), len(seals)))
    say()

    def markers(objs, pmin):
        by = defaultdict(list)
        for r in objs:
            by[pic(r)].append(set(r['flat']))
        out = {}
        for p_, sets in by.items():
            if len(sets) < pmin:
                continue
            others = [s_ for q, ss in by.items() if q != p_ for s_ in ss]
            ms = [g for g in set().union(*sets) if sum(g in s_ for s_ in sets) / len(sets) >= 0.75
                  and sum(g in s_ for s_ in others) / max(1, len(others)) <= 0.25]
            out[p_] = ms
        return out
    mk = markers(cu, 4)
    say('## CT1 copper pictures have marker signs')
    say('- pictures with 4+ labels: %s.' % '; '.join('%s: %s' % (p_, ', '.join(m) or '-') for p_, m in mk.items()))
    rec_('CT1', mk and sum(1 for m in mk.values() if m) >= len(mk) / 2)
    say('## CT2 copper labels are standard texts')
    dt = {p_: len({tuple(r['flat']) for r in cu if pic(r) == p_}) for p_ in mk}
    say('- distinct texts per picture: %s.' % dt)
    rec_('CT2', sum(1 for v in dt.values() if v <= 2) >= len(dt) / 2)

    say('## CT3 labels share a final element')
    tx = [t for t in {tuple(r['flat']) for r in cu} if len(t) >= 2]
    d = lambda xs: T.entropy(Counter(x[0] for x in xs)) - T.entropy(Counter(x[-1] for x in xs))
    obs = d(tx)
    ge = 0
    for _ in range(N):
        sh = []
        for t in tx:
            s_ = list(t)
            random.shuffle(s_)
            sh.append(s_)
        ge += d(sh) >= obs
    p = (ge + 1) / (N + 1)
    say('- distinct texts %d; entropy first minus last %+.2f bits; p = %.4f.' % (len(tx), obs, p))
    rec_('CT3', obs > 0 and p < 0.05)

    a = [ends740(r['flat']) for r in cu if pic(r) in ANIMALS]
    c = [ends740(r['flat']) for r in cu if pic(r) in NONANIMAL]
    show('CT4', 'animal labels take 740', gt('740, animal labels', sum(a), len(a), sum(c), len(c)))
    say('## CT5 the copper anchors mark their pictures')
    o, p = anchor_perm([(pic(r), set(r['flat'])) for r in cu], CU_ANCH)
    say('- anchor-in-own-picture count %d; p = %.4f.' % (o, p))
    rec_('CT5', p < 0.05)
    hum = lambda r: any(cat.get(g) == 'A' for g in r['flat'])
    a = [hum(r) for r in cu if pic(r) == 'Anth']
    c = [hum(r) for r in cu if pic(r) != 'Anth']
    show('CT11', 'the anthropomorph label has a human sign', gt('human sign, Anth labels', sum(a), len(a), sum(c), len(c)))
    say('## CT12 same-picture labels are variants')
    dl = [(pic(r), tuple(r['flat'])) for r in cu]
    dl = list({x for x in dl})
    same = [one_apart(a_[1], b_[1]) for a_, b_ in combinations(dl, 2) if a_[0] == b_[0]]
    diff = [one_apart(a_[1], b_[1]) for a_, b_ in combinations(dl, 2) if a_[0] != b_[0]]
    line, ok = gt('one sign apart, same picture', sum(same), len(same), sum(diff), len(diff))
    say('- %s.' % line)
    rec_('CT12', ok)
    say('## CT13 the picture word comes first')
    f = l_ = 0
    for a_, b_ in combinations(dl, 2):
        if a_[0] == b_[0] and a_[1] != b_[1]:
            x, y = a_[1][0] == b_[1][0], a_[1][-1] == b_[1][-1]
            f += x and not y
            l_ += y and not x
    p = binom_ge(f, f + l_)
    say('- same-picture pairs sharing only the first sign %d, only the last %d; p = %.4f.' % (f, l_, p))
    rec_('CT13', f > l_ and p < 0.05)
    say('## CT21 composite labels are longer')
    o, p = rank_perm([len(r['flat']) for r in cu if pic(r) == 'Comp'], [len(r['flat']) for r in cu if pic(r) != 'Comp'])
    say('- rank difference %+.1f; p = %.4f.' % (o, p))
    rec_('CT21', o > 0 and p < 0.05)

    def hb(objs):
        v = [t[i - 1] in head for r in objs for t in r['seq'] for i, g in enumerate(t) if g == '740' and i > 0]
        return sum(v), len(v)
    a, na = hb(cu)
    c, nc = hb([r for r in rows if r['type'].startswith('SEAL')])
    show('CT22', 'labels have name grammar', gt('head before 740, copper labels', a, na, c, nc))

    # moulded
    say('## CT7 moulded text, moulded picture')
    ml = [(pic(r), tuple(r['flat'])) for r in mo]
    prs = [(i, j) for i, j in combinations(range(len(ml)), 2) if ml[i][1] == ml[j][1]]
    ps = [p_ for p_, _ in ml]
    obs = sum(ps[i] == ps[j] for i, j in prs) / max(1, len(prs))
    ge = 0
    for _ in range(N):
        random.shuffle(ps)
        ge += sum(ps[i] == ps[j] for i, j in prs) / max(1, len(prs)) >= obs
    p = (ge + 1) / (N + 1)
    say('- moulded labels %d; same-text pairs %d; same picture %.0f%%; p = %.4f.' % (len(ml), len(prs), 100 * obs, p))
    rec_('CT7', prs and p < 0.05)
    same = [bool(set(a_[1]) & set(b_[1])) for a_, b_ in combinations(ml, 2) if a_[0] == b_[0]]
    diff = [bool(set(a_[1]) & set(b_[1])) for a_, b_ in combinations(ml, 2) if a_[0] != b_[0]]
    show('CT8', 'same-picture moulded labels share signs', gt('sharing a sign, same picture', sum(same), len(same), sum(diff), len(diff)))
    say('## CT9 the moulded anchors mark their pictures')
    o, p = anchor_perm([(pic(r), set(r['flat'])) for r in mo], MO_ANCH)
    say('- anchor-in-own-picture count %d; p = %.4f.' % (o, p))
    rec_('CT9', p < 0.05)
    a = [any(g in FISH for g in r['flat']) for r in mo if pic(r) == 'Fish']
    c = [any(g in FISH for g in r['flat']) for r in mo if pic(r) != 'Fish']
    show('CT17', 'the fish picture has fish signs', gt('fish sign, Fish-picture labels', sum(a), len(a), sum(c), len(c)))
    hasend = lambda r: any(name_of(t) for t in r['seq'])
    a = [hasend(r) for r in moall if pic(r) and pic(r) not in ('Othr', 'Unknown')]
    c = [hasend(r) for r in moall if not pic(r)]
    show('CT18', 'pictured moulded tablets are labels', lt('ending, pictured moulded tablets', sum(a), len(a), sum(c), len(c)))
    tc = Counter((bool(pic(r) and pic(r) not in ('Othr', 'Unknown')), tuple(r['flat'])) for r in moall)
    a = [n_ >= 2 for (pp, _), n_ in tc.items() if pp]
    c = [n_ >= 2 for (pp, _), n_ in tc.items() if not pp]
    show('CT19', 'pictured moulded texts recur', gt('distinct pictured texts on 2+', sum(a), len(a), sum(c), len(c)))

    # across
    say('## CT6 the copper anchors on seals of their animal')
    o, p = anchor_perm([(pic(r), set(r['flat'])) for r in seals], [x for x in CU_ANCH if x[1] != 'Hare'])
    say('- anchor-on-own-animal seals %d; p = %.4f.' % (o, p))
    rec_('CT6', p < 0.05)
    say('## CT10 labels share a vocabulary')
    ct_ = [g for r in cu for g in r['flat']]
    mt_ = [g for r in mo for g in r['flat']]
    st_ = [g for r in rows if r['type'].startswith('SEAL') for g in r['flat']]
    m = len(ct_)
    pos = 0
    for _ in range(1000):
        b = Counter(random.choice(ct_) for _ in range(m))
        pos += T.jsd(b, Counter(random.sample(mt_, m))) < T.jsd(b, Counter(random.sample(st_, m)))
    say('- copper tokens %d; draws with copper closer to moulded labels than to seals %d of 1000.' % (m, pos))
    rec_('CT10', pos >= 950)
    say('## CT14 seals share signs with their animal\'s copper labels')
    an = ['Elep', 'Gaur', 'Goat', 'Rhin', 'Tigr', 'Buff']
    sets = {x: set().union(*[set(r['flat']) for r in cu if pic(r) == x]) if any(pic(r) == x for r in cu) else set() for x in an}
    common = set.intersection(*[s_ for s_ in sets.values() if s_]) if any(sets.values()) else set()
    spec = {x: s_ - common for x, s_ in sets.items()}
    ss = [r for r in seals if pic(r) in an]
    labs = [pic(r) for r in ss]
    fl = [set(r['flat']) for r in ss]
    st = lambda ls: sum(1 for x, s_ in zip(ls, fl) if s_ & spec[x])
    obs = st(labs)
    ge = 0
    sh = labs[:]
    for _ in range(N):
        random.shuffle(sh)
        ge += st(sh) >= obs
    p = (ge + 1) / (N + 1)
    say('- seals of these animals %d (%s); carrying a sign of their own animal\'s copper labels %d; p = %.4f.' % (
        len(ss), dict(Counter(labs)), obs, p))
    rec_('CT14', p < 0.05)
    anc = {'341', '749', '778', '753'}
    a = [pic(r) != 'Bull1' for r in seals if anc & set(r['flat'])]
    c = [pic(r) != 'Bull1' for r in seals if not (anc & set(r['flat']))]
    show('CT15', 'anchor signs are on other-animal seals', gt('non-unicorn, seals with an anchor sign', sum(a), len(a), sum(c), len(c)))
    k = sum(1 for r in rows if r['type'].startswith('SEAL') and '753' in r['flat'])
    say('## CT16 the hare sign stays off seals')
    say('- seals with 753: %d; threshold under 2.' % k)
    rec_('CT16', k < 2)
    a = [ends520(r['flat']) for r in cu if pic(r) in NONANIMAL]
    c = [ends520(r['flat']) for r in cu if pic(r) in ANIMALS]
    show('CT20', 'non-animal labels take 520', gt('520, non-animal labels', sum(a), len(a), sum(c), len(c)))
    say('## CT23 copper labels are shorter')
    o, p = rank_perm([len(r['flat']) for r in mo], [len(r['flat']) for r in cu])
    say('- rank difference (moulded minus copper) %+.1f; p = %.4f.' % (o, p))
    rec_('CT23', o > 0 and p < 0.05)
    bull_bodies = {name_of(t)[0] for r in seals if pic(r) == 'Bull1' for t in r['seq'] if name_of(t)}
    mb = lambda r: any(name_of(t) and name_of(t)[0] in bull_bodies for t in r['seq'])
    a = [mb(r) for r in mo if pic(r) == 'Bull1']
    c = [mb(r) for r in mo if pic(r) != 'Bull1']
    show('CT24', 'unicorn tablets carry unicorn names', gt('unicorn-seal name, unicorn moulded tablets', sum(a), len(a), sum(c), len(c)))
    say('## CT25 the same name, the same animal across objects')
    sb = defaultdict(list)
    for r in seals:
        for t in r['seq']:
            if name_of(t):
                sb[name_of(t)[0]].append(pic(r))
    it = [(pic(r), name_of(t)[0]) for r in mo for t in r['seq'] if name_of(t) and name_of(t)[0] in sb]
    obs = sum(p_ in sb[b] for p_, b in it)
    allpics = [pic(r) for r in seals]
    ge = 0
    for _ in range(N):
        k = sum(p_ in [random.choice(allpics) for _ in sb[b]] for p_, b in it)
        ge += k >= obs
    p = (ge + 1) / (N + 1)
    say('- pictured moulded names found on seals %d; seal shows the same animal %d; p = %.4f.' % (len(it), obs, p))
    rec_('CT25', it and p < 0.05)

    say('## Summary')
    say()
    say('Held: %s. Failed: %s.' % (', '.join(k for k, o in res if o) or 'none',
                                   ', '.join(k for k, o in res if not o) or 'none'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'predict_test32.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
