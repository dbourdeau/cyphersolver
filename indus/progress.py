"""The decipherment progress metric, measured the same way every loop (PROGRESS.md).

S  structure: held-out bits per sign on a fixed 80/20 split (seed 2026) of the distinct lines of A + B, with the best
   model registered so far (MODEL below); also as a share of the unigram entropy explained.
R  roles: share of sign tokens (distinct lines) whose job is fixed by a tested rule (ROLE_RULES below).
M  meanings: share of sign tokens whose sign has an externally anchored meaning (ANCHORS below).
P  sound values: signs with a sound value that passed a registered held-out test (VALUES below).
L  language: candidate families not yet excluded by registered tests (FAMILIES below).

A component changes only when a registered set (PREDICTIONS.md) supports the change; the entry that changed it is
named in the comment beside it. Usage: python progress.py [label]  (appends a row to results/progress_log.tsv).
"""
import math
import os
import random
import sys
from collections import Counter

import rtools as R
from predict_test103 import CL
from predict_test125 import M2, fit, xent
from predict_test161 import heading

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = {'keys': ['tri', 'pos', 'end'], 'kn': True}          # set 125 (BB2-BB4)
ANCHORS = {'749': 'markhor goat', '341': 'rhinoceros', '753': 'hare', '777': 'markhor goat / horned archer'}  # copper-tablet equations (fourth pass)
VALUES = {}                                                   # no sound value has passed a registered test
FAMILIES = {'Dravidian': 'open', 'Indo-Aryan': 'open', 'Burushaski / isolate': 'open', 'unknown (lost) language': 'open',
            'Sumerian': 'excluded (Q1, H7, TY1, LN1)', 'Elamite': 'excluded (head-initial order; Q1)',
            'Munda': 'excluded if the fish names are stars (class split, eleventh pass)'}


def data():
    A, B, rowsA, recs, F = R.load_all()
    DL = sorted({tuple(t) for t in A + B})
    rnd = random.Random(2026)
    ls = list(DL)
    rnd.shuffle(ls)
    k = int(0.8 * len(ls))
    return DL, ls[:k], ls[k:]


def structure(tr, te):
    w = fit(tr, MODEL['keys'], MODEL['kn'])
    m = M2(tr)
    bits = xent([r for t in te for r in m.rows(t, MODEL['kn'])], w)
    uni = Counter(g for t in tr for g in list(t) + ['</s>'])
    n = sum(uni.values())
    h1 = -sum(v / n * math.log2(v / n) for v in uni.values())
    return bits, h1


def roles(DL):
    tot = got = 0
    by = Counter()
    for t in DL:
        num_before = False
        for i, g in enumerate(t):
            role = None
            if g in R.NUMS:
                role = 'numeral'
            elif g in R.END:
                role = 'ending'
            elif g in CL:
                role = 'closer'
            elif g in ('400', '90') and i > 0 and (t[i - 1] in R.END or t[i - 1] in CL):
                role = 'post-ending marker'
            elif i == 0 and heading(t):
                role = 'heading'
            elif i + 1 < len(t) and t[i + 1] in R.END:
                role = 'name head'
            elif num_before:
                role = 'counted sign'
            num_before = g in R.NUMS
            tot += 1
            if role:
                got += 1
                by[role] += 1
    return got / tot, by, tot


def meanings(DL):
    tot = sum(len(t) for t in DL)
    n = sum(1 for t in DL for g in t if g in R.NUMS or g in ANCHORS)
    return n / tot


def main(label='measure'):
    DL, tr, te = data()
    bits, h1 = structure(tr, te)
    r, by, tot = roles(DL)
    m = meanings(DL)
    p = len(VALUES)
    open_f = [f for f, s in FAMILIES.items() if s == 'open']
    print('S  structure: %.3f bits/sign held out (unigram %.3f; %.1f%% explained)' % (bits, h1, 100 * (h1 - bits) / h1))
    print('R  roles: %.1f%% of %d tokens (%s)' % (100 * r, tot, ', '.join('%s %d' % kv for kv in by.most_common())))
    print('M  meanings: %.1f%% of tokens anchored' % (100 * m))
    print('P  sound values: %d' % p)
    print('L  language: %d families open (%s)' % (len(open_f), ', '.join(open_f)))
    row = '\t'.join([label, '%.3f' % bits, '%.1f' % (100 * (h1 - bits) / h1), '%.1f' % (100 * r), '%.1f' % (100 * m), str(p), str(len(open_f))])
    log = os.path.join(HERE, 'results', 'progress_log.tsv')
    new = not os.path.exists(log)
    with open(log, 'a', encoding='utf-8') as f:
        if new:
            f.write('label\tS_bits\tS_explained_pct\tR_roles_pct\tM_meanings_pct\tP_values\tL_open\n')
        f.write(row + '\n')
    return bits, r, m, p, len(open_f)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'measure')
