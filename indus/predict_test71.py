"""Seventy-first registered prediction set (PREDICTIONS.md, EF1-EF20): why 520 goes with fish. Writes
results/predict_test71.md."""
import random
from collections import Counter

import predict_test13 as T
import rtools as R
from signs import FISH

random.seed(91)
ROOF = ('235', '236')
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Seventy-first registered predictions: why 520 goes with fish', 'predict_test71')
    nm = [(b, e) for b, e in T.names(AB) if b]
    fish = lambda b: any(g in FISH for g in b)
    is5 = lambda e: e == '520'
    nf = [(b, e) for b, e in nm if b[-1] not in FISH]
    rd.say('- names %d; non-fish-headed %d.' % (len(nm), len(nf)))
    rd.say()
    rd.gtl('EF1', 'a fish anywhere calls 520', '520, non-fish-headed names with a fish', [is5(e) for b, e in nf if fish(b)],
           [is5(e) for b, e in nf if not fish(b)])
    hc = Counter(b[-1] for b, _ in nf)
    rd.strat('EF2', 'the fish counts beyond the head', 'by head: 520, with minus without a fish',
             [(fish(b), b[-1], 1 if is5(e) else 0) for b, e in nf if hc[b[-1]] >= 5])
    rd.strat('EF3', 'the fish counts beyond length', 'by length: 520, with minus without a fish',
             [(fish(b), R.lstrat(len(b)), 1 if is5(e) else 0) for b, e in nf])
    dist = lambda b: len(b) - 1 - max(i for i, g in enumerate(b) if g in FISH)
    rd.rank('EF4', 'a nearer fish calls 520', '740 against 520 distances', [dist(b) for b, e in nf if fish(b) and not is5(e)],
            [dist(b) for b, e in nf if fish(b) and is5(e)])
    one = [(next(g for g in b if g in FISH), e) for b, e in nm if sum(g in FISH for g in b) == 1]
    rd.mi('EF5', 'each fish has its ending', 'names with one fish', [f for f, _ in one], [e for _, e in one])
    fn = [(b, e) for b, e in nm if fish(b)]
    rd.gtl('EF6', 'roof fish call 520', '520, roof-fish names', [is5(e) for b, e in fn if any(g in ROOF for g in b)],
           [is5(e) for b, e in fn if not any(g in ROOF for g in b)])
    nfish = lambda b: sum(g in FISH for g in b)
    rd.gtl('EF7', 'more fish, more 520', '520, names with 2+ fish', [is5(e) for b, e in fn if nfish(b) >= 2], [is5(e) for b, e in fn if nfish(b) == 1])
    cf = lambda b: any(x in R.NUMS and y in FISH for x, y in zip(b, b[1:]))
    rd.gtl('EF8', 'counted fish call 520', '520, counted-fish names', [is5(e) for b, e in fn if cf(b)], [is5(e) for b, e in fn if not cf(b)])
    ns = set(nm)
    x7 = x5 = 0
    for b, e in ns:
        if e != '520' or not fish(b):
            continue
        red = [b[:i] + b[i + 1:] for i, g in enumerate(b) if g in FISH and len(b) >= 2]
        a7 = any((r_, '740') in ns for r_ in red)
        a5 = any((r_, '520') in ns for r_ in red)
        x7 += a7 and not a5
        x5 += a5 and not a7
    p = R.binom_ge(x7, x7 + x5)
    rd.rec('EF9', 'without the fish the name takes 740', 'reduced bodies attested with 740 only %d, 520 only %d; p = %.4f' % (x7, x5, p), x7 > x5 and p < 0.05)
    nofish = lambda b: len([g for g in b if g not in FISH])
    rd.rank('EF10', 'the fish replaces part of the name', '740 against 520 fish-free lengths', [nofish(b) for b, e in nm if not is5(e)],
            [nofish(b) for b, e in nm if is5(e)])
    hs = Counter(b[-1] for b, _ in nf)
    h5 = [h for h in hs if hs[h] >= 5 and sum(is5(e) for b, e in nf if b[-1] == h) / hs[h] >= 0.5]
    nextto = {x for b, _ in nm for i, x in enumerate(b) if (i > 0 and b[i - 1] in FISH) or (i + 1 < len(b) and b[i + 1] in FISH)}
    rd.thr('EF11', '520 heads keep fish company', '520-taking non-fish heads next to a fish (%s)' % ', '.join(h5), sum(h in nextto for h in h5), len(h5), 0.6)

    def share(nms):
        return [fish(b) for b, e in nms if e == '520'], [fish(b) for b, e in nms if e == '740']
    a, c = share([(b, e) for b, e in T.names(B) if b])
    rd.gtl('EF12', 'fish-520 in B', 'fish, B 520 names', a, c)
    fsite = lambda cond: [(b, e) for r in F if cond(r['site'].strip()) for b, e in R.names_in(r) if b]
    for key, lab, cond in (('EF13', 'Harappa', lambda s: s == 'Harappa'), ('EF14', 'Mohenjo-daro', lambda s: s == 'Mohenjo-daro'),
                           ('EF15', 'other sites', lambda s: s not in ('Harappa', 'Mohenjo-daro'))):
        a, c = share(fsite(cond))
        rd.gtl(key, 'fish-520 at %s' % lab, 'fish, 520 names', a, c)
    nfB = [(b, e) for b, e in T.names(B) if b and b[-1] not in FISH]
    rd.gtl('EF16', 'a fish anywhere calls 520 in B', '520, B non-fish-headed names with a fish', [is5(e) for b, e in nfB if fish(b)],
           [is5(e) for b, e in nfB if not fish(b)])
    fol = [(t[i], t[i + 1] == '400') for t in AB for i in range(len(t) - 1) if t[i] in R.END]
    rd.ltl('EF17', '520 does not take 400', 'followed by 400, 520', [x for g, x in fol if g == '520'], [x for g, x in fol if g == '740'])
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    nl = [t for t in AB if R.name_of(t)]
    rd.ltl('EF18', '520 names are not titled', 'heading unit, 520 name lines', [hu(t) for t in nl if R.name_of(t)[1] == '520'],
           [hu(t) for t in nl if R.name_of(t)[1] == '740'])
    full = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    sm = [(e, full(r).split(':')[0].strip() == 'Bull1') for r in F if r['type'].startswith('SEAL') and full(r) for b, e in R.names_in(r)]
    rd.ltl('EF19', '520 is not the unicorn ending', 'unicorn, seal 520 names', [u for e, u in sm if e == '520'], [u for e, u in sm if e == '740'])
    cnt = Counter(nm)
    d5 = [k for k in cnt if k[1] == '520' and fish(k[0])]
    d7 = [k for k in cnt if k[1] == '740' and fish(k[0])]
    rd.ltl('EF20', '520 fish names repeat', 'one-off, distinct 520 fish names', [cnt[k] == 1 for k in d5], [cnt[k] == 1 for k in d7])
    rd.finish()


if __name__ == '__main__':
    main()
