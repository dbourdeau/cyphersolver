"""Forty-fifth registered prediction set (PREDICTIONS.md, EM1-EM10): names inside the other formulas. Writes
results/predict_test45.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname

random.seed(65)
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Forty-fifth registered predictions: names inside the other formulas', 'predict_test45')
    ncount = Counter(b for b, _ in T.names(AB))
    bodies = {b for b in ncount if len(b) >= 2}
    mx = max(len(b) for b in bodies)

    def emb(t):
        for k in range(min(mx, len(t)), 1, -1):
            for i in range(len(t) - k, -1, -1):
                if tuple(t[i:i + k]) in bodies:
                    return i, i + k
        return None
    nn = [t for t in AB if nonname(t)]
    ems = [(t, emb(t)) for t in nn if emb(t)]
    rd.say('- non-name lines %d, with an embedded body %d.' % (len(nn), len(ems)))
    rd.say()
    aft = [t[j] for t, (i, j) in ems if j < len(t)]
    rd.thr('EM1', 'the name is followed by a post-name or container sign', 'next sign 400, 90, 151 or 700 (%s)' % ', '.join(
        '%s x%d' % kv for kv in Counter(aft).most_common(6)), sum(g in ('400', '90', '151', '700') for g in aft), len(aft), 0.3)
    eb = {tuple(t[i:j]) for t, (i, j) in ems}
    two = [b for b in bodies if len(b) == 2]
    rd.rank('EM2', 'embedded names are common names', 'embedded against never-embedded 2-sign bodies',
            [ncount[b] for b in two if b in eb], [ncount[b] for b in two if b not in eb])
    fol = defaultdict(list)
    for t, (i, j) in ems:
        fol[tuple(t[i:j])].append(t[j] if j < len(t) else '#')
    rep = [len(set(v)) >= 2 for v in fol.values() if len(v) >= 2]
    rd.thr('EM3', 'the name combines freely', 'bodies embedded 2+ times with 2+ different followers', sum(rep), len(rep), 0.5)
    items = [(emb(ln) is not None, R.lstrat(len(ln)), 0 if r['type'].startswith('SEAL') else 1) for r in F for ln in r['seq']
             if nonname(ln)]
    rd.strat('EM4', 'embedding lines are off the seals', 'off seals, embedding minus other non-name lines', items)
    items = [(r['site'].strip() == 'Mohenjo-daro', R.lstrat(len(ln)), 1 if emb(ln) else 0) for r in F
             if r['site'].strip() in ('Harappa', 'Mohenjo-daro') for ln in r['seq'] if nonname(ln)]
    rd.strat('EM5', 'Harappa embeds less', 'embedding, Mohenjo-daro minus Harappa', items)
    bef = [t[i - 1] for t, (i, j) in ems if i > 0]
    rd.thr('EM6', 'a number or a heading comes before', 'previous sign a numeral or heading', sum(g in R.NUMS or g in HEAD for g in bef),
           len(bef), 0.4)
    num = lambda t: any(g in R.NUMS for g in t)
    nl = [t for t in AB if R.name_of(t)]
    rd.gtl('EM7', 'the number opens the formula', 'numeral first, non-name lines with a numeral',
           [t[0] in R.NUMS for t in nn if num(t)], [t[0] in R.NUMS for t in nl if num(t)])
    fs = [(0, t[0]) for t in nn] + [(1, t[0]) for t in nl]
    rd.mi('EM8', 'the first sign tells the kind', 'lines', [k for k, _ in fs], [g for _, g in fs])
    rd.gtl('EM9', 'short formulas are counts', 'numeral + sign, 2-sign non-name lines',
           [t[0] in R.NUMS and t[1] not in R.NUMS for t in nn if len(t) == 2],
           [b[0] in R.NUMS and b[1] not in R.NUMS for b, _ in T.names(AB) if len(b) == 2])
    e4 = [t for t in nn if t[-1] == '400']
    rd.thr('EM10', 'the ending is dropped before 400', 'lines ending in 400 with a body just before', sum(
        any(tuple(t[i:-1]) in bodies for i in range(max(0, len(t) - 1 - mx), len(t) - 2)) for t in e4), len(e4), 0.3)
    rd.finish()


if __name__ == '__main__':
    main()
