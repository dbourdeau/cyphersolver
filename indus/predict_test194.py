"""Hundred-and-ninety-fourth registered prediction set (PREDICTIONS.md, FB1-FB6): decipherment loop 19, graphic families
(ICIT decade blocks) as context for the S model (famlm.py). Writes results/predict_test194.md."""
import random
from collections import defaultdict

import rtools as R
from famlm import M3, fam, score3, with_fam
from progress import data
from signs import load

BASE = ['tri', 'pos', 'end']
FULL = BASE + ['ftri']


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-ninety-fourth registered predictions: decipherment loop 19, graphic families as context', 'predict_test194')
    DL, tr, te = data()
    s0, w0 = score3(tr, te, BASE)
    s1, w1 = score3(tr, te, FULL)
    rd.say('- fixed split: base %.4f (weights %s), with families %.4f (weights %s).' % (s0, w0, s1, w1))
    rd.say()
    rd.rec('FB1', 'S improves on the fixed test', 'S %.4f -> %.4f (gain %.4f); threshold 0.005' % (s0, s1, s0 - s1), s0 - s1 >= 0.005)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, BASE)
    b1, wb = score3(DA, DBx, FULL)
    rd.rec('FB2', 'the gain replicates A -> B', 'trained on %d A lines, tested on %d B lines: %.4f -> %.4f (gain %.4f)' % (len(DA), len(DBx), b0, b1, b0 - b1), b1 < b0)
    signs = sorted({g for t in DL for g in t})
    groups = defaultdict(list)
    for g in signs:
        groups[fam(g)].append(g)
    sizes = [len(v) for v in groups.values()]
    rnd = random.Random(194)
    gains = []
    for d in range(20):
        perm = signs[:]
        rnd.shuffle(perm)
        mp, k = {}, 0
        for j, n in enumerate(sizes):
            for g in perm[k:k + n]:
                mp[g] = 'r%d' % j
            k += n
        sr, _ = score3(tr, te, FULL, cls=with_fam(lambda g, mp=mp: mp.get(g, g)))
        gains.append(s0 - sr)
    beat = sum(s0 - s1 > x for x in gains)
    rd.rec('FB3', 'random families gain less', 'decade gain %.4f; random gains %s; decade larger in %d of 20' % (s0 - s1, ', '.join('%.4f' % x for x in sorted(gains)), beat), beat >= 19)
    sh, _ = score3(tr, te, FULL, cls=with_fam(lambda g: 'h%d' % (int(g) // 100) if g.isdigit() else g))
    rd.rec('FB4', 'decades beat hundred blocks', 'gain decade %.4f, hundred blocks %.4f' % (s0 - s1, s0 - sh), s0 - s1 > s0 - sh)
    rd.rec('FB5', 'ftri gets weight', 'fixed %.3f, A->B %.3f' % (w1['ftri'], wb['ftri']), w1['ftri'] > 0 and wb['ftri'] > 0)
    rd.rec('FB6', 'progress rule', 'FB1 %s, FB2 %s' % (s0 - s1 >= 0.005, b1 < b0), s0 - s1 >= 0.005 and b1 < b0)
    rd.finish()


if __name__ == '__main__':
    main()
