"""Hundred-and-ninety-third registered prediction set (PREDICTIONS.md, SP1-SP6): decipherment loop 18, a specific grammar
(grammar.py parse2) scored by its margin over shuffled lines. Writes results/predict_test193.md."""
from collections import Counter

import rtools as R
from grammar import coverage, head_stats, heads_from, margin, parse, parse2, shuffled
from progress import data
from signs import load


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-ninety-third registered predictions: decipherment loop 18, a specific grammar', 'predict_test193')
    DA, tr, te = data()
    Brecs = load(only_m77=True)
    DB = sorted({tuple(ln) for r in Brecs for ln in r['seq'] if ln})
    DF = sorted({tuple(ln) for r in F for ln in r['seq'] if ln} - set(DA) - set(DB))
    H = heads_from(DA)
    hc, mc = head_stats(DA)
    f0 = lambda t: parse(t, H) is not None
    f2 = lambda t: parse2(t, H, hc, mc) is not None
    mb0, mb2 = margin(DB, f0), margin(DB, f2)
    mf0, mf2 = margin(DF, f0), margin(DF, f2)
    ma0, ma2 = margin(DA, f0), margin(DA, f2)
    rd.say('- margins (points): A %.1f -> %.1f (design sample), B %.1f -> %.1f, F %.1f -> %.1f.' % (100 * ma0, 100 * ma2, 100 * mb0, 100 * mb2, 100 * mf0, 100 * mf2))
    rd.say()
    rd.rec('SP1', 'the margin rises on B', 'B margin %.1f -> %.1f points' % (100 * mb0, 100 * mb2), mb2 - mb0 >= 0.015)
    rd.rec('SP2', "the margin rises on F's extra lines", 'F margin %.1f -> %.1f points (%d lines)' % (100 * mf0, 100 * mf2, len(DF)), mf2 > mf0)
    SB = shuffled(DB)
    s0 = sum(map(f0, SB)) / len(SB)
    s2 = sum(map(f2, SB)) / len(SB)
    rd.rec('SP3', 'stricter on shuffled B lines', 'shuffled B parsed %.1f%% -> %.1f%%' % (100 * s0, 100 * s2), s2 < s0)
    occ = Counter(tuple(t) for t in A)
    for r in Brecs:
        for ln in r['seq']:
            if ln:
                occ[tuple(ln)] += 1
    dropped = [occ[t] == 1 for t in DA + DB if parse(t, H) == 'bare' and parse2(t, H, hc, mc) is None]
    kept = [occ[t] == 1 for t in DA + DB if parse2(t, H, hc, mc) == 'bare']
    rd.gtl('SP4', 'dropped bare lines are idiosyncratic', 'on one object only, dropped bare lines', dropped, kept)
    cb = sum(map(f2, DB)) / len(DB)
    rd.rec('SP5', 'still covers most of B', 'G2 parses %.1f%% of B (base %.1f%%)' % (100 * cb, 100 * coverage(DB, H)), cb >= 0.6)
    rd.rec('SP6', 'progress rule', 'SP1 %s, SP2 %s' % (mb2 - mb0 >= 0.015, mf2 > mf0), mb2 - mb0 >= 0.015 and mf2 > mf0)
    rd.finish()


if __name__ == '__main__':
    main()
