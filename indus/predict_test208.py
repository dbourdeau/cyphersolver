"""Two-hundred-and-eighth registered prediction set (PREDICTIONS.md, DF1-DF5): decipherment loop 33, graphic families
from Parpola's sign descriptions (descfam.py) in the S model. Writes results/predict_test208.md."""
import random
from collections import defaultdict

import rtools as R
from descfam import families
from famlm import learned_classes, score3, with_fam, with_fam2
from progress import MODEL, data
from signs import load


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-eighth registered predictions: decipherment loop 33, graphic families from Parpola\'s descriptions', 'predict_test208')
    DL, tr, te = data()
    fm = families()
    dfam = lambda g: fm.get(g, g)
    base, _ = score3(tr, te, ['tri', 'pos', 'end'])
    dec, _ = score3(tr, te, MODEL['keys'])
    dsc, _ = score3(tr, te, MODEL['keys'], cls=with_fam(dfam))
    rd.say('- fixed test: tri+pos+end %.4f; + decade f4 %.4f; + description f4 (instead) %.4f.' % (base, dec, dsc))
    signs = sorted({g for t in DL for g in t})
    groups = defaultdict(list)
    for g in signs:
        groups[dfam(g)].append(g)
    sizes = [len(v) for v in groups.values()]
    rnd = random.Random(208)
    gains = []
    for _ in range(20):
        perm = signs[:]
        rnd.shuffle(perm)
        mp, k = {}, 0
        for j, n in enumerate(sizes):
            for g in perm[k:k + n]:
                mp[g] = 'r%d' % j
            k += n
        sr, _ = score3(tr, te, MODEL['keys'], cls=with_fam(lambda g, mp=mp: mp.get(g, g)))
        gains.append(base - sr)
    beat = sum(base - dsc > x for x in gains)
    rd.say()
    rd.rec('DF1', 'description families beat random families', 'gain %.4f; random %s; larger in %d of 20' % (base - dsc, ', '.join('%.4f' % x for x in sorted(gains)), beat), beat >= 19)
    both, w = score3(tr, te, MODEL['keys'] + ['f4d'], cls=with_fam2(dfam))
    rd.rec('DF2', 'a second family component helps', 'decade f4 %.4f -> + description f4d %.4f (gain %.4f; weights %s)' % (dec, both, dec - both, {k: round(v, 3) for k, v in w.items()}), dec - both >= 0.003)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    b0, _ = score3(DA, DBx, MODEL['keys'])
    b1, _ = score3(DA, DBx, MODEL['keys'] + ['f4d'], cls=with_fam2(dfam))
    rd.rec('DF3', 'and A -> B', '%.4f -> %.4f (gain %.4f)' % (b0, b1, b0 - b1), b1 < b0)
    mp = learned_classes(tr, 80)
    lc, _ = score3(tr, te, MODEL['keys'], cls=with_fam(lambda g, mp=mp: mp.get(g, g)))
    rd.rec('DF4', 'description families beat learned classes', 'description %.4f, learned k80 %.4f' % (dsc, lc), dsc < lc)
    rd.rec('DF5', 'progress rule', 'DF2 %s, DF3 %s' % (dec - both >= 0.003, b1 < b0), dec - both >= 0.003 and b1 < b0)
    rd.finish()


if __name__ == '__main__':
    main()
