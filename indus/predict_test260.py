"""Two-hundred-and-sixtieth registered prediction set (PREDICTIONS.md, CH1-CH4): decipherment loop 85, a head + modifier
frame before closers. Head class H = signs heading 5+ A names more often than they modify (grammar.head_stats, as
parse2). Closer line = genre 'closer' (predict_test108), 3+ signs; the pre-closer sign is the one before the closer; the
earlier body = lexical signs after the heading unit and before the pre-closer sign. Writes results/predict_test260.md."""
from scipy.stats import fisher_exact

import rtools as R
from grammar import head_stats, lexical
from predict_test108 import genre
from predict_test161 import heading
from signs import load


def frames(lines):
    pre, early = [], []
    for t in lines:
        t = tuple(t)
        if len(t) < 3 or genre(t) != 'closer':
            continue
        start = 2 if heading(t) and len(t) >= 4 else 0
        if lexical(t[-2]):
            pre.append(t[-2])
        early += [g for g in t[start:-2] if lexical(g)]
    return pre, early


def mods_names(lines):
    out = []
    for t in lines:
        nm = R.name_of(list(t))
        if nm and len(nm[0]) >= 2:
            out += [g for g in nm[0][:-1] if lexical(g)]
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-sixtieth registered predictions: decipherment loop 85, a head + modifier frame before closers', 'predict_test260')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    hc, mc = head_stats(DA)
    H = {g for g in hc if hc[g] >= 5 and hc[g] > mc[g]}
    res = {}
    for nm, L in (('A', DA), ('B', DB)):
        pre, early = frames(L)
        a, b = sum(g in H for g in pre), sum(g in H for g in early)
        p = fisher_exact([[a, len(pre) - a], [b, len(early) - b]], alternative='greater')[1] if pre and early else 1.0
        res[nm] = (a, len(pre), b, len(early), p)
        rd.say('- %s: pre-closer signs head-class %d of %d (%.0f%%); earlier body signs %d of %d (%.0f%%); p = %.2g.' % (nm, a, len(pre), 100 * a / max(1, len(pre)), b, len(early), 100 * b / max(1, len(early)), p))
    mn = mods_names(DA)
    mh = sum(g in H for g in mn) / max(1, len(mn))
    rd.say('- A name modifiers head-class %.0f%% (%d tokens).' % (100 * mh, len(mn)))
    rd.say()
    a = res['A']
    b = res['B']
    ch1 = a[4] < 0.05
    ch2 = b[4] < 0.05
    ch3 = a[2] / max(1, a[3]) <= mh + 0.10
    rd.rec('CH1', 'A: the pre-closer sign is head-class more often than earlier body signs', '%d/%d against %d/%d, p = %.2g' % (a[0], a[1], a[2], a[3], a[4]), ch1)
    rd.rec('CH2', 'B: the same', '%d/%d against %d/%d, p = %.2g' % (b[0], b[1], b[2], b[3], b[4]), ch2)
    rd.rec('CH3', 'A: earlier body signs are head-class no more than name modifiers + 10 points', '%.0f%% against %.0f%%' % (100 * a[2] / max(1, a[3]), 100 * mh), ch3)
    rd.rec('CH4', 'progress rule: CH1-CH3 (roles gain closer head / modifier)', 'CH1 %s, CH2 %s, CH3 %s' % (ch1, ch2, ch3), ch1 and ch2 and ch3)
    rd.finish()


if __name__ == '__main__':
    main()
