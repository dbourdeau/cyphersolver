"""Hundred-and-eighty-ninth registered prediction set (PREDICTIONS.md, UI1-UI7): decipherment loop 14, strokes inside the
U (700 plain; 704-706 long stroke inside; 702-703 short strokes inside). Writes results/predict_test189.md."""
import rtools as R
from signs import load


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-eighty-ninth registered predictions: decipherment loop 14, strokes inside the U', 'predict_test189')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    tok = lambda D, S: [(t, i) for t in D for i, g in enumerate(t) if g in S]
    pv = lambda t, i: i > 0 and t[i - 1] in R.NUMS
    fin = lambda t, i: all(g in ('400', '90') for g in t[i + 1:])
    LS = ('704', '705', '706')
    rd.say('- tokens A: 700 %d, 704-706 %d, 702-703 %d; B: %d, %d, %d.' % (len(tok(DA, ('700',))), len(tok(DA, LS)), len(tok(DA, ('702', '703'))),
                                                                            len(tok(DB, ('700',))), len(tok(DB, LS)), len(tok(DB, ('702', '703')))))
    rd.say()
    rd.gtl('UI1', 'the plain U is counted (A)', 'preceded by a numeral, 700', [pv(t, i) for t, i in tok(DA, ('700',))], [pv(t, i) for t, i in tok(DA, LS)])
    rd.gtl('UI2', 'on B', 'preceded by a numeral, 700 (B)', [pv(t, i) for t, i in tok(DB, ('700',))], [pv(t, i) for t, i in tok(DB, LS)])
    f33 = lambda t, i: i + 1 < len(t) and t[i + 1] == '33'
    DAB = DA + DB
    rd.gtl('UI3', 'the stroked U opens the closing formula', 'followed by 33, 705/706', [f33(t, i) for t, i in tok(DAB, ('705', '706'))], [f33(t, i) for t, i in tok(DAB, ('700',))])
    rd.gtl('UI4', 'the plain U ends the text (A)', 'final, 700', [fin(t, i) for t, i in tok(DA, ('700',))], [fin(t, i) for t, i in tok(DA, LS)])
    rd.gtl('UI5', 'on B', 'final, 700 (B)', [fin(t, i) for t, i in tok(DB, ('700',))], [fin(t, i) for t, i in tok(DB, LS)])
    rd.ltl('UI6', 'short-stroked U are counted less', 'preceded by a numeral, 702/703', [pv(t, i) for t, i in tok(DAB, ('702', '703'))], [pv(t, i) for t, i in tok(DAB, ('700',))])
    rate = lambda xs: sum(xs) / max(1, len(xs))
    u1 = rate([pv(t, i) for t, i in tok(DA, ('700',))]) > rate([pv(t, i) for t, i in tok(DA, LS)])
    u2 = rate([pv(t, i) for t, i in tok(DB, ('700',))]) > rate([pv(t, i) for t, i in tok(DB, LS)])
    u4 = rate([fin(t, i) for t, i in tok(DA, ('700',))]) > rate([fin(t, i) for t, i in tok(DA, LS)])
    u5 = rate([fin(t, i) for t, i in tok(DB, ('700',))]) > rate([fin(t, i) for t, i in tok(DB, LS)])
    rd.rec('UI7', 'progress rule', 'UI1/UI2 directions %s/%s; UI4/UI5 %s/%s' % (u1, u2, u4, u5), (u1 and u2) or (u4 and u5))
    rd.finish()


if __name__ == '__main__':
    main()
