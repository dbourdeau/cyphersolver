"""Hundred-and-ninety-ninth registered prediction set (PREDICTIONS.md, F41-F45): decipherment loop 24, a family 4-gram
context for the S model (famlm.py f4). Writes results/predict_test199.md."""
import random
from collections import defaultdict

import rtools as R
from famlm import fam, score3, with_fam
from progress import data
from signs import load

OLD = ['tri', 'pos', 'end', 'ftri']
NEW = ['tri', 'pos', 'end', 'f4']


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-ninety-ninth registered predictions: decipherment loop 24, a longer family context for S', 'predict_test199')
    DL, tr, te = data()
    s0, w0 = score3(tr, te, OLD)
    s1, w1 = score3(tr, te, NEW)
    rd.say('- fixed split: tri+pos+end+ftri %.4f (%s); tri+pos+end+f4 %.4f (%s).' % (s0, w0, s1, w1))
    rd.say()
    rd.rec('F41', 'S improves on the fixed test', 'S %.4f -> %.4f (gain %.4f); threshold 0.003' % (s0, s1, s0 - s1), s0 - s1 >= 0.003)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, OLD)
    b1, wb = score3(DA, DBx, NEW)
    rd.rec('F42', 'the gain replicates A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    base, _ = score3(tr, te, ['tri', 'pos', 'end'])
    signs = sorted({g for t in DL for g in t})
    groups = defaultdict(list)
    for g in signs:
        groups[fam(g)].append(g)
    sizes = [len(v) for v in groups.values()]
    rnd = random.Random(199)
    gains = []
    for d in range(20):
        perm = signs[:]
        rnd.shuffle(perm)
        mp, k = {}, 0
        for j, n in enumerate(sizes):
            for g in perm[k:k + n]:
                mp[g] = 'r%d' % j
            k += n
        sr, _ = score3(tr, te, NEW, cls=with_fam(lambda g, mp=mp: mp.get(g, g)))
        gains.append(base - sr)
    beat = sum(base - s1 > x for x in gains)
    rd.rec('F43', 'random families gain less', 'decade gain over tri+pos+end %.4f; random %s; decade larger in %d of 20' % (base - s1, ', '.join('%.4f' % x for x in sorted(gains)), beat), beat >= 19)
    rd.rec('F44', 'f4 gets weight', 'fixed %.3f, A->B %.3f' % (w1['f4'], wb['f4']), w1['f4'] > 0 and wb['f4'] > 0)
    rd.rec('F45', 'progress rule', 'F41 %s, F42 %s' % (s0 - s1 >= 0.003, b1 < b0), s0 - s1 >= 0.003 and b1 < b0)
    rd.finish()


if __name__ == '__main__':
    main()
