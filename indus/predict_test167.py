"""Hundred-and-sixty-seventh registered prediction set (PREDICTIONS.md, AD1-AD10): administration, survival and scribal
hands. Writes results/predict_test167.md."""
import random
import re
from collections import Counter, defaultdict
from itertools import combinations

import predict_test13 as T
import rtools as R
from gulf import IRAN_WEST, WEST
from predict_test103 import CL
from predict_test112 import runs
from predict_test140 import GENERIC, pair_perm
from predict_test146 import pairs_list
from predict_test147 import chapman
from predict_test150 import sign_test
from predict_test161 import shared_openers
from predict_test18 import level

random.seed(187)
POST = set(CL) | {'400', '90', '842', '790', '151', '60', '621', '2', '33', '682'}


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-sixty-seventh registered predictions: administration, survival and scribal hands', 'predict_test167')
    site = lambda r: recs[r['sealid']][3]
    seals = [r for r in F if r['type'].startswith('SEAL')]
    tags = [r for r in F if r['type'].startswith('TAG')]
    st, tg = {tuple(r['flat']) for r in seals}, {tuple(r['flat']) for r in tags}
    lp = chapman(len(st), len(tg), len(st & tg))
    rd.rec('AD1', 'most seals are lost', 'seal texts %d, sealing texts %d, both %d; estimate %.0f (%.1fx); threshold 3x' % (len(st), len(tg), len(st & tg), lp, lp / len(st)), lp >= 3 * len(st))
    lt = {tuple(r['flat']) for r in tags if site(r) == 'Lothal'}
    rd.thr('AD2', 'Lothal sealings from lost seals', 'Lothal sealing texts found on a seal', len(lt & st), len(lt), 0.5, above=False)
    to = Counter(b[0] for r in tags for b, e in R.names_in(r) if b and len(b) >= 3)
    md = [r for r in seals if site(r) == 'Mohenjo-daro' and level('Mohenjo-daro', recs[r['sealid']])]
    ops = lambda r: [b[0] for b, e in R.names_in(r) if b and len(b) >= 3]

    def cv(labs):
        ce, cl = Counter(), Counter()
        for r, l_ in zip(md, labs):
            (ce if l_ == 'E' else cl).update(ops(r))
        te, tl = max(1, sum(ce.values())), max(1, sum(cl.values()))
        oo = sorted(set(ce) | set(cl))
        return T.spearman([to[o] for o in oo], [cl[o] / tl - ce[o] / te for o in oo])
    labs = [level('Mohenjo-daro', recs[r['sealid']]) for r in md]
    obs = cv(labs)
    ge = 0
    for _ in range(1000):
        random.shuffle(labs)
        ge += cv(labs) >= obs
    p = (ge + 1) / 1001
    rd.rec('AD3', 'the rising openers are the sealing openers', 'Spearman %.3f; p = %.4f (sealing openers %d)' % (obs, p, sum(to.values())), obs > 0 and p < 0.05)
    two = []
    for r in seals:
        ls = [tuple(ln) for ln in r['seq'] if ln]
        if len(ls) == 2:
            nm = [bool(R.name_of(list(x))) for x in ls]
            if nm.count(True) == 1:
                two.append((ls[nm.index(True)], ls[nm.index(False)]))
    rd.thr('AD4', 'the second line is a title field', 'non-name lines ending in a post-name sign (%s)' % dict(Counter(o[-1] for n, o in two).most_common(8)),
           sum(o[-1] in POST for n, o in two), len(two), 0.5)
    w, l_, p = sign_test([len(n) - len(o) for n, o in two])
    rd.rec('AD5', 'the second line is shorter', 'name line longer %d, shorter %d; sign test p = %.4f' % (w, l_, p), p < 0.05 and w > l_)
    cnt = Counter(tuple(ln) for r in seals for ln in {tuple(x) for x in r['seq'] if x})
    rd.gtl('AD6', 'second lines recur', 'on 2+ seals, non-name lines', [cnt[o] >= 2 for o in {o for n, o in two}], [cnt[n] >= 2 for n in {n for n, o in two}])
    cnt_f = Counter(g for r in F for g in r['flat'])
    prs = [(a, b) for a, b in pairs_list() if cnt_f[a] >= 5 and cnt_f[b] >= 5]
    pid = {}
    for k, (a, b) in enumerate(prs):
        pid.setdefault(a, (k, 0))
        pid.setdefault(b, (k, 1))
    objv = []
    for r in F:
        d = {}
        for g in r['flat']:
            if g in pid and pid[g][0] not in d:
                d[pid[g][0]] = pid[g][1]
        if len(d) >= 2:
            objv.append(d)
    combos = Counter((i, j) for d in objv for i, j in combinations(sorted(d), 2))
    use = [c for c, n in combos.items() if n >= 5]

    def stat(ov):
        return sum(T.mi([d[i] for d in ov if i in d and j in d], [d[j] for d in ov if i in d and j in d]) for i, j in use)
    obs = stat(objv)
    ge = 0
    for _ in range(1000):
        by = defaultdict(list)
        for k_, d in enumerate(objv):
            for i, v in d.items():
                by[i].append((k_, v))
        new = [dict() for _ in objv]
        for i, lst in by.items():
            vs = [v for _, v in lst]
            random.shuffle(vs)
            for (k_, _), v in zip(lst, vs):
                new[k_][i] = v
        ge += stat(new) >= obs
    p = (ge + 1) / 1001
    rd.rec('AD7', 'a scribe\'s hand', 'objects with 2+ variant pairs %d; pair combinations with 5+ objects %d; summed MI %.3f; p = %.4f' % (len(objv), len(use), obs, p), p < 0.05)
    lex = lambda g: g not in R.NUMS and g not in POST and g not in R.END
    items = []
    for r in seals:
        s_ = recs[r['sealid']][4].strip()
        if site(r) == 'Mohenjo-daro' and s_ not in GENERIC:
            cs = {(ln[i], ln[i + 1]) for ln in r['seq'] for i in range(len(ln) - 1) if ln[i] in R.NUMS and lex(ln[i + 1])}
            items += [(c, s_) for c in cs]
    o, e, p, n = pair_perm(items)
    rd.rec('AD8', 'numeral compounds are local within the city', 'pairs %d; same sub-area %.3f against %.3f; p = %.4f' % (n, o, e, p), o > e and p < 0.05)
    west = lambda r: recs[r['sealid']][2] in WEST or r['site'].strip() in IRAN_WEST
    counted = {ln[j] for r in F if not west(r) for ln in r['seq'] for i, j, rr in runs(ln) if j < len(ln)}
    wr = [(ln, j, rr) for r in F if west(r) for ln in r['seq'] for i, j, rr in runs(ln)]
    hr = [(ln, j, rr) for r in F if not west(r) and site(r) not in ('Other',) for ln in r['seq'] for i, j, rr in runs(ln)]
    rd.gtl('AD9', 'foreign strokes are not counts', 'next sign never counted at home, West Asian runs', [ln[j] not in counted for ln, j, rr in wr if j < len(ln)],
           [ln[j] not in counted for ln, j, rr in hr if j < len(ln)])
    val = lambda rr: sum(R.NUMS[g][0] for g in rr)
    rd.gtl('AD10', 'foreign strokes are small', 'worth 1 or 2, West Asian runs (%s)' % dict(Counter(val(rr) for _, _, rr in wr)), [val(rr) <= 2 for _, _, rr in wr], [val(rr) <= 2 for _, _, rr in hr])
    rd.finish()


if __name__ == '__main__':
    main()
