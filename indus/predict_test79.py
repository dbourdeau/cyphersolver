"""Seventy-ninth registered prediction set (PREDICTIONS.md, AR1-AR20): formulas as records. Writes
results/predict_test79.md. Counts over distinct lines."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test50 import ent
from predict_test53 import lab_perm
from predict_test78 import parse

random.seed(99)
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Seventy-ninth registered predictions: formulas as records', 'predict_test79')
    full = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()

    def setup(lines):
        ns = {(b, e) for b, e in T.names(lines) if b}
        bodies = {b for b, e in ns}
        P = [(t,) + parse(t) for t in sorted({tuple(t) for t in lines}) if nonname(list(t)) and parse(t)]
        return ns, bodies, P
    ns, bodies, P = setup(AB)
    heads = {b[-1] for b in bodies}
    nh = [(t, pre, runs) for t, pre, runs in P if pre in bodies and runs]
    rd.say('- numeral formulas %d; name headers %d.' % (len(P), len(nh)))
    rd.say()
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln), full(r).split(':')[0].strip()) for r in F for ln in r['seq'] if ln and nonname(ln) and parse(ln)})
    sealn = defaultdict(set)
    for r in F:
        if r['type'].startswith('SEAL'):
            for b, e in R.names_in(r):
                sealn[r['site'].strip()].add(b)
    fn = [(s, parse(t)[0]) for s, ty, t, m in FD if parse(t)[0] in bodies]
    sites = [s for s, _ in fn]
    hs = [h for _, h in fn]
    st = lambda ss: sum(h in sealn[s] for s, h in zip(ss, hs))
    obs = st(sites)
    sh = sites[:]
    ge = 0
    for _ in range(R.N):
        random.shuffle(sh)
        ge += st(sh) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('AR1', 'the header has a seal at home', 'name-header formulas %d; header a seal name at its site %d; p = %.4f' % (len(fn), obs, p), p < 0.05)

    def ar2(nhl, key, lab):
        pi = [(pre[-1], runs[0][1]) for t, pre, runs in nhl]
        rd.mi(key, 'the named header selects the item%s' % lab, 'name-header formulas', [a for a, _ in pi], [b for _, b in pi])
    ar2(nh, 'AR2', '')
    it = [(pre in bodies, runs[0][1]) for t, pre, runs in P if pre and runs]
    rd.mi('AR3', 'named headers count their own things', 'headed formulas', [a for a, _ in it], [b for _, b in it])
    fs = [(ty, parse(t)[0] in bodies) for s, ty, t, m in FD if ty in ('SEA', 'TAB')]
    rd.gtl('AR4', 'named records are on seals', 'seal, name-header formulas', [ty == 'SEA' for ty, n in fs if n], [ty == 'SEA' for ty, n in fs if not n])
    hb = {pre for t, pre, runs in nh}
    rd.rank('AR5', 'header names are short', 'names against header names', [len(b) for b in bodies], [len(b) for b in hb])
    rd.gtl('AR6', 'header names take 740', '740, header names', [e == '740' for b, e in ns if b in hb], [e == '740' for b, e in ns if b not in hb])
    hd = [pre for t, pre, runs in P if pre]
    rd.thr('AR7', 'many headers are headings', 'headers of a heading sign only', sum(len(p_) == 1 and p_[0] in HEAD for p_ in hd), len(hd), 0.3)
    rd.thr('AR8', 'headers are short', 'headers of 1-2 signs', sum(len(p_) <= 2 for p_ in hd), len(hd), 0.8)
    items = {v_[1] for t, pre, runs in P for v_ in runs}
    hf = {p_[-1] for p_ in hd}
    rd.thr('AR9', 'headers and items are different words', 'header-final types also items', len(hf & items), len(hf), 0.5, above=False)
    bsig = {g for b in bodies for g in b}
    rd.gtl('AR10', 'headed records count formula things', 'formula-only item, headed', [runs[0][1] not in bsig for t, pre, runs in P if pre and runs],
           [runs[0][1] not in bsig for t, pre, runs in P if not pre and runs])
    ih = [runs[0][1] for t, pre, runs in P if pre and runs]
    iu = [runs[0][1] for t, pre, runs in P if not pre and runs]
    o, p = lab_perm(ih, iu, lambda a, b: ent(a) - ent(b), R.N)
    rd.rec('AR11', 'bare counts count few things', 'item entropy headed %.2f, numeral-first %.2f; p = %.4f' % (ent(ih), ent(iu), p), o > 0 and p < 0.05)
    rd.gtl('AR12', 'headings count name things', 'item a name head, heading headers', [runs[0][1] in heads for t, pre, runs in P if len(pre) == 1 and pre[0] in HEAD and runs],
           [runs[0][1] in heads for t, pre, runs in nh])
    sm = [(m, parse(t)[1][0][1]) for s, ty, t, m in FD if ty == 'SEA' and m and parse(t)[1]]
    rd.mi('AR13', 'the picture goes with the item', 'distinct seal formulas', [m for m, _ in sm], [i for _, i in sm])

    def ar14(Pl, key, lab):
        hp = [(pre, runs[0][1], runs[0][0]) for t, pre, runs in Pl if pre and runs]
        hdr = [h for h, i, v in hp]
        its = [i for h, i, v in hp]
        rec_ = lambda xs: sum(n >= 2 for n in Counter(zip(hdr, xs)).values())
        obs = rec_(its)
        ii = its[:]
        ge = 0
        for _ in range(R.N):
            random.shuffle(ii)
            ge += rec_(ii) >= obs
        p = (ge + 1) / (R.N + 1)
        rd.rec(key, 'records repeat%s' % lab, '(header, item) pairs on 2+ lines %d; p = %.4f' % (obs, p), p < 0.05)
        return hp
    hp = ar14(P, 'AR14', '')
    vv = defaultdict(set)
    cnt = Counter()
    for h, i, v in hp:
        vv[(h, i)].add(v)
        cnt[(h, i)] += 1
    rp = [k for k in cnt if cnt[k] >= 2]
    rd.thr('AR15', 'the same entry, a new count', 'repeated (header, item) with different values', sum(len(vv[k]) >= 2 for k in rp), len(rp), 0.7)
    val = lambda runs: runs[0][0]
    rd.rank('AR16', 'headed records count more', 'headed against numeral-first values', [val(runs) for t, pre, runs in P if pre and runs],
            [val(runs) for t, pre, runs in P if not pre and runs])
    fs2 = [(s, not parse(t)[0]) for s, ty, t, m in FD if s in ('Harappa', 'Mohenjo-daro')]
    rd.gtl('AR17', 'Harappa writes bare counts', 'numeral-first, Harappa', [x for s, x in fs2 if s == 'Harappa'], [x for s, x in fs2 if s == 'Mohenjo-daro'])
    nsB, bodB, PB = setup(B)
    ar2([(t, pre, runs) for t, pre, runs in PB if pre in bodB and runs], 'AR18', ' (B)')
    ar14(PB, 'AR19', ' (B)')
    si = [(s, parse(t)[1][0][1]) for s, ty, t, m in FD if s in ('Harappa', 'Mohenjo-daro') and parse(t)[0] and parse(t)[1]]
    rd.mi('AR20', 'each city records its own things', 'headed formulas', [s for s, _ in si], [i for _, i in si])
    rd.finish()


if __name__ == '__main__':
    main()
