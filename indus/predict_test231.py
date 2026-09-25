"""Two-hundred-and-thirty-first registered prediction set (PREDICTIONS.md, CC1-CC3): decipherment loop 56, is the slot
before a count restricted in each city? Writes results/predict_test231.md."""
import rtools as R
from predict_test108 import genre
from predict_test215 import test


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-thirty-first registered predictions: decipherment loop 56, the count-label slot in each city', 'predict_test231')
    by = {'Mohenjo-daro': set(), 'Harappa': set()}
    for r in F:
        if r['site'] in by:
            for ln in r['seq']:
                if ln:
                    by[r['site']].add(tuple(ln))
    oks = []
    for key, site, seed in (('CC1', 'Mohenjo-daro', 231), ('CC2', 'Harappa', 232)):
        c = [t for t in sorted(by[site]) if genre(t) == 'count']
        o, n, p = test(c, seed)
        rd.rec(key, 'pre-count slot restricted, %s' % site, 'top-ten share %.1f%% of %d pre-count tokens (%d count lines); p = %.4f' % (100 * o, n, len(c), p), p < 0.05)
        oks.append(p < 0.05)
    rd.rec('CC3', 'progress rule', 'CC1 %s, CC2 %s' % tuple(oks), all(oks))
    rd.finish()


if __name__ == '__main__':
    main()
