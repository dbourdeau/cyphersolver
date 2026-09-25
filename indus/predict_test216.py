"""Two-hundred-and-sixteenth registered prediction set (PREDICTIONS.md, GL1-GL4): decipherment loop 41, the count label
(set 215) as a grammar rule (grammar.parse3). Writes results/predict_test216.md."""
from collections import Counter

import rtools as R
from grammar import head_stats, heads_from, margin, parse2, parse3, shuffled
from predict_test108 import genre
from predict_test215 import slots
from progress import data
from signs import load


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-sixteenth registered predictions: decipherment loop 41, the count label in the grammar', 'predict_test216')
    DL, tr, te = data()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    DF = sorted({tuple(ln) for r in F for ln in r['seq'] if ln} - set(DA) - set(DB))
    H = heads_from(DL)
    hc, mc = head_stats(DL)
    labels = {g for g, v in Counter(s[0] for s in (slots(t) for t in DA if genre(t) == 'count') if s).most_common(10)}
    f2 = lambda t: parse2(t, H, hc, mc) is not None
    f3 = lambda t: parse3(t, H, hc, mc, labels) is not None
    rd.say('- labels (A): %s.' % ', '.join(sorted(labels)))
    rd.say()
    b2, b3 = margin(DB, f2), margin(DB, f3)
    rd.rec('GL1', 'the B margin rises', '%.2f -> %.2f points' % (100 * b2, 100 * b3), b3 > b2)
    SB = shuffled(DB)
    r2, r3 = sum(map(f2, DB)) / len(DB), sum(map(f3, DB)) / len(DB)
    s2, s3 = sum(map(f2, SB)) / len(SB), sum(map(f3, SB)) / len(SB)
    rd.rec('GL2', 'real B coverage rises more than shuffled', 'real %+.2f, shuffled %+.2f points' % (100 * (r3 - r2), 100 * (s3 - s2)), r3 - r2 > s3 - s2)
    fm2, fm3 = margin(DF, f2), margin(DF, f3)
    rd.rec('GL3', "F's extra lines", '%.2f -> %.2f points' % (100 * fm2, 100 * fm3), fm3 > fm2)
    rd.rec('GL4', 'progress rule', 'GL1 %s, GL2 %s' % (b3 > b2, r3 - r2 > s3 - s2), b3 > b2 and r3 - r2 > s3 - s2)
    rd.finish()


if __name__ == '__main__':
    main()
