"""Two-hundred-and-twenty-ninth registered prediction set (PREDICTIONS.md, GD1-GD5): decipherment loop 54, do the cage and
the inner strokes behave the same in Mohenjo-daro and Harappa? Writes results/predict_test229.md."""
import rtools as R
from progress import CAGED
from predict_test7 import fisher_less


def final(t, i):
    return all(g in ('400', '90') for g in t[i + 1:])


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-twenty-ninth registered predictions: decipherment loop 54, the graphic devices in each city', 'predict_test229')
    by = {'Mohenjo-daro': set(), 'Harappa': set()}
    for r in F:
        if r['site'] in by:
            for ln in r['seq']:
                if ln:
                    by[r['site']].add(tuple(ln))
    keys = {'Mohenjo-daro': ('GD1', 'GD3'), 'Harappa': ('GD2', 'GD4')}
    oks = []
    for site, lines in by.items():
        nxt = lambda t, i: i + 1 < len(t) and t[i + 1] in R.END
        cg = [nxt(t, i) for t in lines for i, g in enumerate(t) if g in CAGED]
        ot = [nxt(t, i) for t in lines for i, g in enumerate(t) if g not in CAGED and g not in R.NUMS and g not in R.END and g not in ('400', '90')]
        rc, ro = sum(cg) / max(1, len(cg)), sum(ot) / max(1, len(ot))
        ok1 = rc <= 0.05 and rc < ro and len(cg) >= 10
        rd.rec(keys[site][0], 'caged signs do not take 740 / 520 (%s)' % site, 'caged %d of %d (%.1f%%) against other lexical signs %.1f%%' % (sum(cg), len(cg), 100 * rc, 100 * ro), ok1)
        s = [final(t, i) for t in lines for i, g in enumerate(t) if g in ('741', '742', '745')]
        p = [final(t, i) for t in lines for i, g in enumerate(t) if g == '740']
        pv = fisher_less(sum(s), len(s) - sum(s), sum(p), len(p) - sum(p))
        ok2 = pv < 0.05 and sum(s) / max(1, len(s)) < sum(p) / max(1, len(p))
        rd.rec(keys[site][1], 'stroked jars end lines less often (%s)' % site, 'stroked %d of %d, plain %d of %d; p = %.4f' % (sum(s), len(s), sum(p), len(p), pv), ok2)
        oks += [ok1, ok2]
    rd.rec('GD5', 'progress rule', 'all four: %s' % all(oks), all(oks))
    rd.finish()


if __name__ == '__main__':
    main()
