"""Hundred-and-sixty-first registered prediction set (PREDICTIONS.md, OF1-OF10): the opener as an office. Also holds the
helpers used by the hundred-and-sixty-second set. Writes results/predict_test161.md."""
import math
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from gulf import IRAN_WEST, WEST
from predict_test157 import kind, profile
from predict_test18 import level

random.seed(181)
CITIES = ('Mohenjo-daro', 'Harappa')


def heading(t):
    return len(t) >= 3 and t[0] in ('817', '820', '861') and t[1] in ('2', '60', '1')


def shared_openers(F, recs):
    by = defaultdict(set)
    for r in F:
        c = recs[r['sealid']][3]
        if r['type'].startswith('SEAL') and c in CITIES:
            for b, e in R.names_in(r):
                if b and len(b) >= 3:
                    by[b[0]].add(c)
    return {o for o, cs in by.items() if len(cs) == 2}


def zmi(xs, ys, n=1000):
    o = T.mi(xs, ys)
    yy = list(ys)
    v = []
    for _ in range(n):
        random.shuffle(yy)
        v.append(T.mi(xs, yy))
    m = sum(v) / len(v)
    sd = math.sqrt(sum((x - m) ** 2 for x in v) / len(v)) or 1e-9
    return (o - m) / sd, o


def motif(recs, r):
    m = recs[r['sealid']][18].strip()
    return None if m in ('-', '') else m


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-sixty-first registered predictions: the opener as an office', 'predict_test161')
    SO = shared_openers(F, recs)
    seals = [r for r in F if r['type'].startswith('SEAL')]
    mh = [r for r in seals if recs[r['sealid']][3] in CITIES]
    rd.say('- shared openers %d: %s.' % (len(SO), ', '.join(sorted(SO))))
    rd.say()
    for key, L, want in (('OF1', 2, 'person-like'), ('OF2', 1, 'title-like')):
        cat = {c: Counter() for c in CITIES}
        for r in mh:
            for nm in {x for x in R.names_in(r) if x[0] and len(x[0]) == L}:
                cat[recs[r['sealid']][3]][nm] += 1
        p = profile(cat)
        rd.rec(key, '%d-sign bodies are %s' % (L, want), '%s; %.2f, %.2f, %.2f -> %s' % (p['n'], p['ratio'], p['shared'], p['one'], kind(p)), kind(p) == want)
    mo = [(b, motif(recs, r)) for r in seals for b, e in R.names_in(r) if b and len(b) >= 3 and motif(recs, r)]
    res = []
    ok = True
    for lab, sel in (('3-sign', lambda b: len(b) == 3), ('4+-sign', lambda b: len(b) >= 4)):
        xs = [(b, m) for b, m in mo if sel(b)]
        zo, _ = zmi([b[0] for b, m in xs], [m for b, m in xs])
        zh, _ = zmi([b[-1] for b, m in xs], [m for b, m in xs])
        res.append('%s bodies %d: opener z %.2f, head z %.2f' % (lab, len(xs), zo, zh))
        ok = ok and zo > zh
    rd.rec('OF3', 'the motif link holds at each length', res, ok)
    om, hm = defaultdict(Counter), defaultdict(Counter)
    for b, m in mo:
        om[b[0]][m] += 1
        hm[b[-1]][m] += 1
    maj = lambda d: (sum(c.most_common(1)[0][1] for c in d.values() if sum(c.values()) >= 5), sum(sum(c.values()) for c in d.values() if sum(c.values()) >= 5))
    a, na = maj(om)
    c, nc = maj(hm)
    rd.gt('OF4', 'openers keep one motif', 'names in the majority motif, openers', a, na, c, nc)
    has = lambda r: any(b and len(b) >= 3 and b[0] in SO for b, e in R.names_in(r))
    rd.ltl('OF5', 'pictureless seals lack the office', 'shared opener, pictureless seals', [has(r) for r in seals if motif(recs, r) == 'None'],
           [has(r) for r in seals if motif(recs, r) not in (None, 'None')])
    hd = [(heading(tuple(ln)), R.name_of(list(ln))) for r in seals for ln in r['seq'] if ln]
    hd = [(h, nm[0]) for h, nm in hd if nm and nm[0] and len(nm[0]) >= 3]
    rd.ltl('OF6', 'heading and opener exclude each other', 'shared opener, names under a heading', [b[0] in SO for h, b in hd if h], [b[0] in SO for h, b in hd if not h])
    n3 = sorted({(b, e) for b, e in T.names(A + B) if len(b) >= 3})
    cores = lambda ops: sum(1 for v in _group(n3, ops).values() if len(v) >= 2)
    obs = cores([b[0] for b, e in n3])
    ops = [b[0] for b, e in n3]
    draws = []
    for _ in range(1000):
        random.shuffle(ops)
        draws.append(cores(ops))
    med = sorted(draws)[500]
    rd.rec('OF7', 'cores recombine with openers', 'cores with 2+ openers %d; shuffled median %d (range %d-%d)' % (obs, med, min(draws), max(draws)), obs >= med)
    lv = {'opener': {'E': set(), 'L': set()}, 'core': {'E': set(), 'L': set()}}
    for r in mh:
        l_ = level(recs[r['sealid']][3], recs[r['sealid']])
        if l_:
            for b, e in R.names_in(r):
                if b and len(b) >= 3:
                    lv['opener'][l_].add(b[0])
                    lv['core'][l_].add((b[1:], e))
    sh = lambda d: (len(d['E'] & d['L']), min(len(d['E']), len(d['L'])))
    a, na = sh(lv['opener'])
    c, nc = sh(lv['core'])
    rd.gt('OF8', 'openers last across levels', 'shared across levels, openers', a, na, c, nc)
    west = lambda r: recs[r['sealid']][2] in WEST or r['site'].strip() in IRAN_WEST
    wn = [R.name_of(list(ln)) for r in F if west(r) for ln in r['seq'] if ln]
    wn = [nm[0] for nm in wn if nm and nm[0] and len(nm[0]) >= 3]
    hn = [b for r in seals if not west(r) for b, e in R.names_in(r) if b and len(b) >= 3]
    rd.ltl('OF9', 'foreigners lack the office', 'shared opener, West Asian names (%s)' % '; '.join(' '.join(b) for b in wn), [b[0] in SO for b in wn], [b[0] in SO for b in hn])
    cu = [r for r in F if r['type'] == 'TAB:C' and r['flat']]
    rd.ltl('OF10', 'copper labels lack the office', 'shared opener first, copper texts', [r['flat'][0] in SO for r in cu], [b[0] in SO for b in hn])
    rd.finish()


def _group(n3, ops):
    g = defaultdict(set)
    for (b, e), o in zip(n3, ops):
        g[(b[1:], e)].add(o)
    return g


if __name__ == '__main__':
    main()
