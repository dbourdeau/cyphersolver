"""Hundred-and-ninety-first registered prediction set (PREDICTIONS.md, GR1-GR6): decipherment loop 16, a parser for the
whole grammar (grammar.py). Writes results/predict_test191.md."""
from collections import Counter

import rtools as R
from grammar import ALL_RULES, coverage, heads_from, parse
from signs import load


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-ninety-first registered predictions: decipherment loop 16, a parser for the whole grammar', 'predict_test191')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    DF = sorted({tuple(ln) for r in F for ln in r['seq'] if ln} - set(DA) - set(DB))
    heads = heads_from(DA)
    ga, gb, gf = coverage(DA, heads), coverage(DB, heads), coverage(DF, heads)
    rd.say('- labels on A: %s.' % dict(Counter(parse(t, heads) for t in DA)))
    rd.say()
    rd.rec('GR1', 'the grammar parses most of A', 'G on A %.1f%% of %d lines' % (100 * ga, len(DA)), ga >= 0.7)
    rd.rec('GR2', 'not fitted to A', 'G on B %.1f%% of %d lines (A %.1f%%)' % (100 * gb, len(DB), 100 * ga), abs(ga - gb) <= 0.10)
    rd.rec('GR3', "F's extra lines", 'G on %d F lines %.1f%%' % (len(DF), 100 * gf), gf >= 0.6)
    costs = {r: ga - coverage(DA, heads, tuple(x for x in ALL_RULES if x != r)) for r in ALL_RULES}
    rd.rec('GR4', 'each rule is needed', 'cost of dropping each rule (points): %s' % ', '.join('%s %.1f' % (r, 100 * c) for r, c in costs.items()),
           all(c >= 0.01 for c in costs.values()))
    un = [len(t) for t in DA if parse(t, heads) is None]
    pa = [len(t) for t in DA if parse(t, heads) is not None]
    rd.rank('GR5', 'what remains is the long texts', 'length, unparsed against parsed lines', un, pa)
    rd.rec('GR6', 'progress rule', 'GR1 %s, GR2 %s' % (ga >= 0.7, abs(ga - gb) <= 0.10), ga >= 0.7 and abs(ga - gb) <= 0.10)
    rd.say('- unparsed examples: %s.' % '; '.join(' '.join(t) for t in DA if parse(t, heads) is None)[:1500])
    rd.finish()


if __name__ == '__main__':
    main()
