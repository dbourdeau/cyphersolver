"""Forty-seventh registered prediction set (PREDICTIONS.md, FI1-FI10): inside the number-first formulas. Writes
results/predict_test47.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname

random.seed(67)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Forty-seventh registered predictions: inside the number-first formulas', 'predict_test47')
    fm = [t for t in AB if nonname(t)]
    rd.say('- formulas %d.' % len(fm))
    rd.say()
    pr = [(R.kind(x), y) for t in fm for x, y in zip(t, t[1:]) if x in R.NUMS and y not in R.NUMS]
    rd.mi('FI1', 'the sign sets the numeral kind', 'numeral + sign pairs', [k for k, _ in pr], [y for _, y in pr])
    rd.mi('FI2', 'the opening sets the close', 'formulas', [t[0] in R.NUMS for t in fm], [t[-1] for t in fm])
    rd.rank('FI3', 'numeral-first formulas are shorter', 'other against numeral-first formulas',
            [len(t) for t in fm if t[0] not in R.NUMS], [len(t) for t in fm if t[0] in R.NUMS])
    slots = [(i, j) for i, t in enumerate(fm) for j in range(len(t) - 1) if t[j] in R.NUMS and t[j + 1] not in R.NUMS]
    vals = [R.NUMS[fm[i][j]][0] for i, j in slots]
    nxt = [fm[i][j + 1] for i, j in slots]
    obs = len(set(zip(vals, nxt)))
    le = 0
    vv = vals[:]
    for _ in range(R.N):
        random.shuffle(vv)
        le += len(set(zip(vv, nxt))) <= obs
    p = (le + 1) / (R.N + 1)
    rd.rec('FI4', 'number and sign are idioms', 'pairs %d; distinct %d; p = %.4f' % (len(slots), obs, p), p < 0.05)
    res = defaultdict(set)
    wn = [t for t in fm if any(g in R.NUMS for g in t)]
    for t in wn:
        res[tuple(g for g in t if g not in R.NUMS)].add(tuple(R.NUMS[g][0] for g in t if g in R.NUMS))
    k = sum(len(res[tuple(g for g in t if g not in R.NUMS)]) >= 2 for t in wn if any(g not in R.NUMS for g in t))
    rd.thr('FI5', 'the same formula with different numbers', 'formulas with a numeral sharing their residue', k, len(wn), 0.2)
    nn_ = [(t, j) for t in fm for j, g in enumerate(t) if g in R.NUMS]
    rd.thr('FI6', 'the numeral precedes its sign', 'numerals directly before a non-numeral', sum(
        j + 1 < len(t) and t[j + 1] not in R.NUMS for t, j in nn_), len(nn_), 0.9)
    items = [(r['site'].strip() == 'Harappa', R.lstrat(len(ln)), 1 if ln[0] in R.NUMS else 0) for r in F
             if r['site'].strip() in ('Harappa', 'Mohenjo-daro') for ln in r['seq'] if nonname(ln)]
    rd.strat('FI7', 'Harappa formulas open with a number', 'Harappa minus Mohenjo-daro', items)
    items = [(r['type'].startswith('TAB'), R.lstrat(len(ln)), 1 if ln[0] in R.NUMS else 0) for r in F
             if r['type'].startswith(('TAB', 'SEAL')) for ln in r['seq'] if nonname(ln)]
    rd.strat('FI8', 'tablet formulas open with a number', 'tablets minus seals', items)
    bsig = {g for b, _ in T.names(AB) for g in b}
    tk = [g for t in fm for g in t if g not in R.NUMS]
    rd.thr('FI9', 'formulas have their own signs', 'formula tokens of signs never in a name body', sum(g not in bsig for g in tk), len(tk), 0.1)
    tc = Counter(tuple(ln) for r in F for ln in r['seq'] if nonname(ln))
    rd.rank('FI10', 'repeated formulas are short', 'unique against repeated formulas',
            [len(t) for t, n in tc.items() if n == 1], [len(t) for t, n in tc.items() if n >= 2])
    rd.finish()


if __name__ == '__main__':
    main()
