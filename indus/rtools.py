"""Shared loaders and statistics for the registered prediction rounds from the thirty-seventh set on.

Samples: A = data/corpus.tsv (with 'site', 'type', 'motif', 'direction'), B = data/corpus_m77_added.tsv (lines of 2+
signs), F = the fuller ICIT corpus, intact objects, lines reversed (PREDICTIONS.md M4). Tests report through a Round
object that writes results/<name>.md.
"""
import math
import os
import random
from collections import Counter, defaultdict

import icit_full
import predict_test13 as T
from numerals import NUMS
from predict_test4 import name_of
from predict_test7 import fisher_less
from predict_test14 import cat_of, classes, hyper_ge
from predict_test15 import binom_ge, strat_perm
from predict_test17 import headed, rank_perm
from predict_test18 import level, lstrat, n700
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
FPATH = os.environ.get('ICIT_FULL', 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher--claude-worktrees-'
                       'florence-1414-cipher-160632/03a95ee0-e290-45c7-bab7-1e38cbd68d34/scratchpad/outside/'
                       'icit_full_records_indusscript_net.csv')
N = 10000
END = ('740', '520')
POST = ('90', '400', '151')
SINDH = {'Mohenjo-daro', 'Chanhu-daro', 'Chanhujo-daro', 'Allahdino', 'Amri', 'Kot Diji', 'Lakhanjo-daro', 'Nausharo'}
GUJ = {'Lothal', 'Dholavira', 'Surkotada', 'Desalpur', 'Kanmer', 'Gola Dhoro (Bagasra)', 'Gola Dhoro', 'Rangpur'}
NORTH = {'Harappa', 'Kalibangan', 'Banawali', 'Rakhigarhi', 'Farmana', 'Bhirrana', 'Rupar'}


def region(site):
    s = site.strip()
    return 'sindh' if s in SINDH else ('gujarat' if s in GUJ else ('north' if s in NORTH else None))


def kind(g):
    return NUMS[g][1]


def load_all():
    A = T.sample('A')
    B = T.sample('B')
    rowsA = [r for r in load() if r['flat']]
    icit_full.LINES_REVERSED = True
    recs = {rec[0]: rec for rec in icit_full.records(FPATH)}
    F = [r for r in icit_full.objects(FPATH) if r['flat'] and '?' not in r['flat'] and not any(
        ln['broken_start'] or ln['broken_end'] or ln['gap'] for ln in r['raw'])]
    return A, B, rowsA, recs, F


def names_in(r):
    return [name_of(ln) for ln in r['seq'] if name_of(ln)]


def mi_perm(xs, ys, n=N):
    obs = T.mi(xs, ys)
    ge = 0
    xx = list(xs)
    for _ in range(n):
        random.shuffle(xx)
        ge += T.mi(xx, ys) >= obs
    return obs, (ge + 1) / (n + 1)


def fl(a, na, c, nc, p):
    return '%d of %d (%.1f%%) against %d of %d (%.1f%%), p = %.4f' % (a, na, 100 * a / max(1, na), c, nc, 100 * c / max(1, nc), p)


class Round:
    def __init__(self, title, out):
        self.out = out
        self.lines = ['# ' + title, '']
        self.res = []

    def say(self, s=''):
        self.lines.append(s)
        print(s)

    def rec(self, key, title, text, ok):
        self.say('## %s %s' % (key, title))
        for t in (text if isinstance(text, list) else [text]):
            self.say('- %s.' % t)
        self.say('- **%s %s.**' % (key, T.verdict(ok)))
        self.say()
        self.res.append((key, ok))

    def gt(self, key, title, lab, a, na, c, nc):
        p = hyper_ge(sum(a) if isinstance(a, list) else a, na - (sum(a) if isinstance(a, list) else a), c, nc - c)
        a_ = sum(a) if isinstance(a, list) else a
        self.rec(key, title, '%s %s' % (lab, fl(a_, na, c, nc, p)), p < 0.05 and a_ / max(1, na) > c / max(1, nc))

    def gtl(self, key, title, lab, a, c):
        self.gt(key, title, lab, sum(a), len(a), sum(c), len(c))

    def ltl(self, key, title, lab, a, c):
        p = fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))
        self.rec(key, title, '%s %s' % (lab, fl(sum(a), len(a), sum(c), len(c), p)),
                 p < 0.05 and sum(a) / max(1, len(a)) < sum(c) / max(1, len(c)))

    def mi(self, key, title, lab, xs, ys):
        o, p = mi_perm(xs, ys)
        self.rec(key, title, '%s: %d items; MI %.4f bits; p = %.4f' % (lab, len(xs), o, p), p < 0.05)

    def strat(self, key, title, lab, items):
        o, p = strat_perm(items)
        self.rec(key, title, '%s: labelled %d of %d; stratified difference %+.1f points; p = %.4f' % (
            lab, sum(l_ for l_, _, _ in items), len(items), 100 * o, p), o > 0 and p < 0.05)

    def rank(self, key, title, lab, a, b):
        d, p = rank_perm(a, b)
        self.rec(key, title, '%s: %d against %d; means %.2f and %.2f; rank difference %+.1f; p = %.4f' % (
            lab, len(a), len(b), sum(a) / max(1, len(a)), sum(b) / max(1, len(b)), d, p), d > 0 and p < 0.05)

    def thr(self, key, title, lab, k, n, t, above=True):
        ok = n > 0 and ((k / n >= t) if above else (k / n <= t))
        self.rec(key, title, '%s: %d of %d (%.0f%%); threshold %s %.0f%%' % (
            lab, k, n, 100 * k / max(1, n), 'at least' if above else 'at most', 100 * t), ok)

    def finish(self):
        self.say('## Summary')
        self.say()
        self.say('Held: %s. Failed: %s.' % (', '.join(k for k, o in self.res if o) or 'none',
                                           ', '.join(k for k, o in self.res if not o) or 'none'))
        os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
        with open(os.path.join(HERE, 'results', self.out + '.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.lines) + '\n')
        return self.res
