"""Hundred-and-fifty-fourth registered prediction set (PREDICTIONS.md, SP1-SP6): same name, same person? Writes
results/predict_test154.md."""
from collections import defaultdict
from itertools import combinations

import rtools as R
from predict_test18 import level
from predict_test140 import GENERIC, pair_perm


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-fifty-fourth registered predictions: same name, same person?', 'predict_test154')
    seals = [r for r in F if r['type'].startswith('SEAL')]
    by = defaultdict(list)
    for r in seals:
        for nm in {x for x in R.names_in(r) if x[0]}:
            by[nm].append(r)
    rec = lambda r: recs[r['sealid']]
    sub = lambda r: rec(r)[4].strip() if rec(r)[4].strip() not in GENERIC else None
    pairs = {'long': [], 'short': []}
    for (b, e), rs in by.items():
        if len(rs) >= 2:
            k = 'long' if len(b) >= 3 else ('short' if len(b) == 1 else None)
            if k:
                pairs[k] += [(x, y) for x, y in combinations(rs, 2)]
    rd.say('- recurring names: long %d (%d seal pairs), short %d (%d seal pairs).' % (
        sum(1 for (b, e), rs in by.items() if len(rs) >= 2 and len(b) >= 3), len(pairs['long']),
        sum(1 for (b, e), rs in by.items() if len(rs) >= 2 and len(b) == 1), len(pairs['short'])))
    rd.say()
    L, S = pairs['long'], pairs['short']
    same_site = lambda x, y: rec(x)[3] == rec(y)[3]
    rd.gtl('SP1', 'long names stay in one site', 'same site, long-name pairs', [same_site(x, y) for x, y in L], [same_site(x, y) for x, y in S])
    md = lambda ps: [(x, y) for x, y in ps if rec(x)[3] == rec(y)[3] == 'Mohenjo-daro' and sub(x) and sub(y)]
    rd.gtl('SP2', 'long names stay in one area', 'same sub-area, long-name pairs', [sub(x) == sub(y) for x, y in md(L)], [sub(x) == sub(y) for x, y in md(S)])
    lv = lambda ps: [(x, y) for x, y in ps if same_site(x, y) and level(rec(x)[3], rec(x)) and level(rec(y)[3], rec(y))]
    lev = lambda r: level(rec(r)[3], rec(r))
    rd.gtl('SP3', 'long names stay in one level', 'same level, long-name pairs', [lev(x) == lev(y) for x, y in lv(L)], [lev(x) == lev(y) for x, y in lv(S)])
    for key, title, lab, want in (('SP4', 'long names co-located beyond chance', 'long', True), ('SP5', 'short names not co-located', 'short', False)):
        items = [((b, e), sub(r)) for (b, e), rs in by.items() for r in rs
                 if rec(r)[3] == 'Mohenjo-daro' and sub(r) and ((len(b) >= 3) if lab == 'long' else (len(b) == 1))]
        o, ex, p, n = pair_perm(items)
        ok = (o > ex and p < 0.05) if want else p >= 0.05
        rd.rec(key, title, '%s-name pairs %d; same sub-area %.3f against %.3f; p = %.4f' % (lab, n, o, ex, p), ok)
    mot = lambda r: rec(r)[18].strip()
    ok_m = lambda ps: [(x, y) for x, y in ps if mot(x) not in ('-', '') and mot(y) not in ('-', '')]
    rd.gtl('SP6', 'long names keep the motif', 'same motif, long-name pairs', [mot(x) == mot(y) for x, y in ok_m(L)], [mot(x) == mot(y) for x, y in ok_m(S)])
    rd.finish()


if __name__ == '__main__':
    main()
