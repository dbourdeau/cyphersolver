"""Hundred-and-ninetieth registered prediction set (PREDICTIONS.md, LF1-LF6): decipherment loop 15, the leaf family
(attachments: diamond on top, tree below, stroke inside, hatched square, diagonal stroke). Writes
results/predict_test190.md."""
import rtools as R
from signs import load

FAM = {'817': 'diamond', '824': 'diamond', '856': 'diamond', '861': 'diamond', '803': 'tree', '838': 'tree',
       '808': 'stroke', '809': 'stroke', '830': 'stroke', '832': 'stroke', '810': 'hatch', '812': 'hatch', '814': 'hatch', '831': 'diagonal'}


def pos(t, i):
    if i + 1 < len(t) and t[i + 1] in R.END:
        return 'head'
    if all(g in ('400', '90') for g in t[i + 1:]):
        return 'final'
    return 'initial' if i == 0 else 'medial'


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-ninetieth registered predictions: decipherment loop 15, the leaf family', 'predict_test190')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    ta = [(FAM[g], pos(t, i)) for t in DA for i, g in enumerate(t) if g in FAM]
    tb = [(FAM[g], pos(t, i)) for t in DB for i, g in enumerate(t) if g in FAM]
    rd.mi('LF1', 'the attachment predicts position (A)', 'leaf tokens in A', [a for a, p in ta], [p for a, p in ta])
    rd.mi('LF2', 'on B', 'leaf tokens in B', [a for a, p in tb], [p for a, p in tb])
    tab = ta + tb
    rd.gtl('LF3', 'stroke-leaf is a head', 'name head, leaf + stroke', [p == 'head' for a, p in tab if a == 'stroke'], [p == 'head' for a, p in tab if a == 'tree'])
    rd.gtl('LF4', 'tree-leaf is medial', 'medial, leaf + tree', [p == 'medial' for a, p in tab if a == 'tree'], [p == 'medial' for a, p in tab if a == 'stroke'])
    rd.thr('LF5', 'the diamond-leaf opens the line', 'leaf + diamond tokens that are initial', sum(p == 'initial' for a, p in tab if a == 'diamond'), sum(1 for a, p in tab if a == 'diamond'), 0.6)
    rate = lambda xs: sum(xs) / max(1, len(xs))
    da = rate([p == 'head' for a, p in ta if a == 'stroke']) > rate([p == 'head' for a, p in ta if a == 'tree'])
    db = rate([p == 'head' for a, p in tb if a == 'stroke']) > rate([p == 'head' for a, p in tb if a == 'tree'])
    o1, p1 = R.mi_perm([a for a, p in ta], [p for a, p in ta])
    o2, p2 = R.mi_perm([a for a, p in tb], [p for a, p in tb])
    rd.rec('LF6', 'progress rule', 'LF1/LF2 p %.4f/%.4f; LF3 direction A %s, B %s' % (p1, p2, da, db), (p1 < 0.05 and p2 < 0.05) or (da and db))
    rd.finish()


if __name__ == '__main__':
    main()
