"""Hundred-and-ninety-second registered prediction set (PREDICTIONS.md, SQ1-SQ7): decipherment loop 17, rules for what the
grammar leaves (grammar.py EXT_RULES), with a shuffled-line control. Writes results/predict_test192.md."""
import random
from collections import Counter

import rtools as R
from grammar import ALL_RULES, CAGED, EXT_RULES, NEW_RULES, coverage, heads_from, parse, split_seq
from predict_test103 import CL
from progress import data
from signs import load


def shuffled(lines, n=20, seed=192):
    rnd = random.Random(seed)
    return [tuple(rnd.sample(t, len(t))) for _ in range(n) for t in lines]


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-ninety-second registered predictions: decipherment loop 17, rules for what the grammar leaves', 'predict_test192')
    DA, tr, te = data()
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    DF = sorted({tuple(ln) for r in F for ln in r['seq'] if ln} - set(DA) - set(DB))
    H = heads_from(DA)
    SB = shuffled(DB)
    g = lambda D, rules: coverage(D, H, rules)
    a0, a1 = g(DA, ALL_RULES), g(DA, EXT_RULES)
    b0, b1 = g(DB, ALL_RULES), g(DB, EXT_RULES)
    s0, s1 = g(SB, ALL_RULES), g(SB, EXT_RULES)
    f0, f1 = g(DF, ALL_RULES), g(DF, EXT_RULES)
    rd.say('- lines A %d, B %d, F extra %d; labels on B with the extension: %s.' % (len(DA), len(DB), len(DF), dict(Counter(parse(t, H, EXT_RULES) for t in DB))))
    rd.say()
    rd.rec('SQ1', 'G rises on A', 'G on A %.1f%% -> %.1f%%' % (100 * a0, 100 * a1), a1 - a0 >= 0.05)
    rd.rec('SQ2', 'G rises on B', 'G on B %.1f%% -> %.1f%%' % (100 * b0, 100 * b1), b1 - b0 >= 0.03)
    rd.rec('SQ3', 'the margin over shuffled lines rises (B)', 'shuffled B %.1f%% -> %.1f%%; margin %.1f -> %.1f points' % (100 * s0, 100 * s1, 100 * (b0 - s0), 100 * (b1 - s1)), (b1 - s1) > (b0 - s0))
    per = []
    for r in NEW_RULES:
        rr = ALL_RULES + (r,)
        per.append((r, g(DB, rr) - b0, g(SB, rr) - s0))
    rd.rec('SQ4', 'each new rule is specific', '; '.join('%s real %+.1f shuffled %+.1f' % (r, 100 * x, 100 * y) for r, x, y in per), all(x > y for r, x, y in per))
    rd.rec('SQ5', "F's extra lines", 'G on F %.1f%% -> %.1f%%' % (100 * f0, 100 * f1), f1 - f0 >= 0.05)
    endset = set(R.END) | set(CL) | CAGED
    real = [t[k - 1] in endset for t in DA + DB for k in [split_seq(t, H)] if k and parse(t, H, EXT_RULES) == 'seq']
    shuf = [t[k - 1] in endset for t in shuffled(DA + DB, 5) for k in [split_seq(t, H)] if k and parse(t, H, EXT_RULES) == 'seq']
    rd.gtl('SQ6', 'the split falls after an ending', 'first unit ends in an ending, real SEQ lines', real, shuf)
    ok = b1 - b0 >= 0.03 and (b1 - s1) > (b0 - s0)
    rd.rec('SQ7', 'progress rule', 'SQ2 %s, SQ3 %s' % (b1 - b0 >= 0.03, (b1 - s1) > (b0 - s0)), ok)
    rd.say('- still unparsed on A: %s.' % '; '.join(' '.join(t) for t in DA if parse(t, H, EXT_RULES) is None)[:1500])
    rd.finish()


if __name__ == '__main__':
    main()
