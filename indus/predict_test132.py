"""Hundred-and-thirty-second registered prediction set (PREDICTIONS.md, RS1-RS12): the rectangular seals. Writes
results/predict_test132.md."""
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test108 import genre

HEAD = ('817', '820', '861')
CITY = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-thirty-second registered predictions: the rectangular seals', 'predict_test132')
    size = lambda r: float(recs[r['sealid']][31]) if recs[r['sealid']][31].strip() not in ('0', '', '-') else None
    mat = lambda r: recs[r['sealid']][13].strip() if recs[r['sealid']][13].strip() not in ('-', '') else None
    lines = lambda r: [tuple(ln) for ln in r['seq'] if ln]
    S = [r for r in F if r['type'] == 'SEAL:S' and lines(r)]
    Rr = [r for r in F if r['type'] == 'SEAL:R' and lines(r)]
    rd.say('- square seals %d, rectangular %d.' % (len(S), len(Rr)))
    rd.say()
    LS = [t for r in S for t in lines(r)]
    LR = [t for r in Rr for t in lines(r)]
    rd.ltl('RS1', 'rectangular seals are not name seals', 'name lines, rectangular', [genre(t) == 'name' for t in LR], [genre(t) == 'name' for t in LS])
    lv = lambda r: R.level('Harappa', recs[r['sealid']])
    rd.gtl('RS2', 'rectangular seals are late', 'later, Harappa rectangular', [lv(r) == 'L' for r in Rr if r['site'].strip() == 'Harappa' and lv(r) in ('E', 'L')],
           [lv(r) == 'L' for r in S if r['site'].strip() == 'Harappa' and lv(r) in ('E', 'L')])
    rd.gtl('RS3', 'rectangular seals are provincial', 'rectangular share, small sites', [r['type'] == 'SEAL:R' for r in S + Rr if r['site'].strip() not in CITY],
           [r['type'] == 'SEAL:R' for r in S + Rr if r['site'].strip() in CITY])
    e = lambda rs: [e_ for r in rs for b, e_ in R.names_in(r) if b]
    rd.ltl('RS4', 'rectangular seals avoid 520', '520, rectangular names', [x == '520' for x in e(Rr)], [x == '520' for x in e(S)])
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    rd.ltl('RS5', 'rectangular seals are not titled', 'heading unit, rectangular lines', [hu(t) for t in LR], [hu(t) for t in LS])
    objs = defaultdict(set)
    for r in F:
        objs[tuple(lines(r))].add(r['sealid'])
    rd.ltl('RS6', 'rectangular texts repeat', 'one-off, rectangular texts', [len(objs[tuple(lines(r))]) == 1 for r in Rr], [len(objs[tuple(lines(r))]) == 1 for r in S])
    bsig = {g for b, _ in T.names(AB) for g in b}
    fo = lambda t: any(g not in bsig and g not in R.NUMS for g in t)
    rd.gtl('RS7', 'rectangular seals use formula words', 'formula-only sign, rectangular lines', [fo(t) for t in LR], [fo(t) for t in LS])
    rd.rank('RS8', 'rectangular seals are small', 'square against rectangular', [size(r) for r in S if size(r)], [size(r) for r in Rr if size(r)])
    rd.gtl('RS9', 'rectangular seals carry closers', 'closer lines, rectangular', [genre(t) == 'closer' for t in LR], [genre(t) == 'closer' for t in LS])
    rd.gtl('RS10', 'rectangular seals carry bare labels', 'bare lines, rectangular', [genre(t) == 'bare' for t in LR], [genre(t) == 'bare' for t in LS])
    m = [mat(r) for r in Rr if mat(r)]
    rd.thr('RS11', 'rectangular seals are steatite', 'steatite (%s)' % dict(Counter(m).most_common(3)), sum(x == 'Steatite' for x in m), len(m), 0.9)
    fs = [('R', t[0]) for t in LR] + [('S', t[0]) for t in LS]
    rd.mi('RS12', 'the shape goes with the opening sign', 'seal lines', [a for a, _ in fs], [b for _, b in fs])
    rd.say('- rectangular genre mix: %s; square: %s.' % (dict(Counter(genre(t) for t in LR)), dict(Counter(genre(t) for t in LS))))
    rd.finish()


if __name__ == '__main__':
    main()
