"""Two-hundred-and-thirty-second registered prediction set (PREDICTIONS.md, FE1-FE4): decipherment loop 57, do heads of one
graphic family (ICIT decade block) choose endings alike beyond the fish? Writes results/predict_test232.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from famlm import fam
from predict_test103 import CL
from progress import CAGED
from signs import load


def eclass(e):
    return e if e in ('740', '520') else ('closer' if e in CL else ('caged' if e in CAGED else 'other'))


def head_endings(lines):
    he = defaultdict(Counter)
    for b, e in T.names(lines):
        if b:
            he[b[-1]][eclass(e)] += 1
    return {h: c for h, c in he.items() if sum(c.values()) >= 5}


def homog(groups, he):
    tot = score = 0
    for g in groups:
        c = Counter()
        for h in g:
            c.update(he[h])
        n = sum(c.values())
        if n:
            score += c.most_common(1)[0][1]
            tot += n
    return score / max(1, tot)


def test(he, seed, n=1000):
    fams = defaultdict(list)
    for h in he:
        fams[fam(h)].append(h)
    groups = list(fams.values())
    obs = homog(groups, he)
    heads = list(he)
    sizes = [len(g) for g in groups]
    rnd = random.Random(seed)
    ge = 0
    for _ in range(n):
        rnd.shuffle(heads)
        k, rg = 0, []
        for s in sizes:
            rg.append(heads[k:k + s])
            k += s
        ge += homog(rg, he) >= obs
    return obs, (ge + 1) / (n + 1), len(heads), sum(1 for g in groups if len(g) >= 2)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-thirty-second registered predictions: decipherment loop 57, does the ending follow the graphic family?', 'predict_test232')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    ha, hb = head_endings(DA), head_endings(DB)
    fish = lambda h: h.isdigit() and 219 <= int(h) <= 240
    res = {}
    for key, he, seed in (('FE1', ha, 232), ('FE2', hb, 233)):
        o, p, nh, nf = test(he, seed)
        res[key] = p
        rd.rec(key, 'endings homogeneous within graphic families (%s)' % ('A' if key == 'FE1' else 'B'), 'modal-ending share %.3f over %d heads (%d families with 2+ heads); p = %.4f' % (o, nh, nf, p), p < 0.05)
    oa, pa, na, fa = test({h: c for h, c in ha.items() if not fish(h)}, 234)
    ob, pb, nb, fb = test({h: c for h, c in hb.items() if not fish(h)}, 235)
    rd.rec('FE3', 'without the fish block', 'A %.3f (%d heads), p = %.4f; B %.3f (%d heads), p = %.4f' % (oa, na, pa, ob, nb, pb), pa < 0.05 and pb < 0.05)
    rd.rec('FE4', 'progress rule', 'FE3 %s' % (pa < 0.05 and pb < 0.05), pa < 0.05 and pb < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
