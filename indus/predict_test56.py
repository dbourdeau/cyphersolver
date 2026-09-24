"""Fifty-sixth registered prediction set (PREDICTIONS.md, RQ1-RQ10): replicating loop 2 on held-out data. Writes
results/predict_test56.md."""
import random
from collections import defaultdict

import predict_test13 as T
import rtools as R
from predict_test42 import dom, pairs
from predict_test43 import ranks
from predict_test44 import nonname
from predict_test53 import lab_perm, rate

random.seed(76)
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Fifty-sixth registered predictions: replicating loop 2 on held-out data', 'predict_test56')
    num = lambda t: any(g in R.NUMS for g in t)
    fmB = [t for t in B if nonname(t)]
    nlB = [t for t in B if R.name_of(t)]
    res = defaultdict(set)
    wn = [t for t in fmB if num(t)]
    for t in wn:
        res[tuple(g for g in t if g not in R.NUMS)].add(tuple(R.NUMS[g][0] for g in t if g in R.NUMS))
    k = sum(len(res[tuple(g for g in t if g not in R.NUMS)]) >= 2 for t in wn if any(g not in R.NUMS for g in t))
    rd.thr('RQ1', 'same formula, different number (FI5)', 'B formulas with a numeral sharing their residue', k, len(wn), 0.2)
    oth = [r for r in F if r['site'].strip() not in ('Mohenjo-daro', 'Harappa')]
    of = [(r, ln) for r in oth for ln in r['seq'] if nonname(ln)]
    rd.say('- other-site formulas %d; B formulas %d, name lines %d.' % (len(of), len(fmB), len(nlB)))
    rd.say()
    pr = [(R.kind(x), y) for _, t in of for x, y in zip(t, t[1:]) if x in R.NUMS and y not in R.NUMS]
    rd.mi('RQ2', 'the sign sets the kind (FI1)', 'other-site numeral + sign pairs', [a for a, _ in pr], [b for _, b in pr])
    items = [(r['type'].startswith('TAB'), R.lstrat(len(ln)), 1 if ln[0] in R.NUMS else 0) for r, ln in of if r['type'].startswith(('TAB', 'SEAL'))]
    rd.strat('RQ3', 'tablets open with a number (FI8)', 'other sites, tablets minus seals', items)
    sealn = [g for r, t in of if r['type'].startswith('SEAL') and num(t) for g in t if g in R.NUMS]
    tabn = [g for r, t in of if r['type'].startswith('TAB') and num(t) for g in t if g in R.NUMS]
    rd.gtl('RQ4', 'seals use the tiered form (SC2)', 'other sites: tiered, seal numerals', [R.kind(g) == 'tiered' for g in sealn],
           [R.kind(g) == 'tiered' for g in tabn])
    rd.gtl('RQ5', 'seal counts are headed (SC8)', 'other sites: heading first, seal numeral formulas',
           [t[0] in HEAD for r, t in of if r['type'].startswith('SEAL') and num(t)],
           [t[0] in HEAD for r, t in of if r['type'].startswith('TAB') and num(t)])
    nsA, nsB = set(T.names(A)), set(T.names(B))
    rk = ranks(nsB)
    dB = dom(pairs(nsB, 3))
    pw = sc = 0
    for b, _ in nsA:
        for x, y in zip(b, b[1:]):
            if x in rk and y in rk and rk[x] != rk[y] and tuple(sorted((x, y))) in dB:
                a_ = dB[tuple(sorted((x, y)))] == (x, y)
                b_ = rk[x] < rk[y]
                pw += a_ and not b_
                sc += b_ and not a_
    p = R.binom_ge(pw, pw + sc)
    rd.rec('RQ6', 'pairs beat the rank (PO10)', 'B to A, discordant: pairwise right %d, rank right %d; p = %.4f' % (pw, sc, p),
           pw > sc and p < 0.05)
    o, p = lab_perm(nlB, fmB, lambda a, b: rate(a) - rate(b), R.N // 10)
    rd.rec('RQ7', 'names are the repetitive genre (EN1)', 'B repeat rate names %.3f, formulas %.3f; p = %.4f (1,000 shuffles)' % (
        rate(nlB), rate(fmB), p), o > 0 and p < 0.05)
    tf = [g for t in fmB for g in t]
    tn = [g for t in nlB for g in t]
    m = min(len(tf), len(tn))
    wins = sum(len(set(random.sample(tf, m))) > len(set(random.sample(tn, m))) for _ in range(1000))
    rd.rec('RQ8', 'formulas are the open genre (EN2)', 'B tokens per subsample %d; formulas more in %d of 1,000' % (m, wins), wins >= 950)
    bB = {g for b, _ in T.names(B) for g in b}
    tok = [(t, i) for t in fmB for i, g in enumerate(t) if g not in R.NUMS]
    rd.gtl('RQ9', 'formula-only signs close (FO1)', 'B: last, formula-only tokens', [i == len(t) - 1 for t, i in tok if t[i] not in bB],
           [i == len(t) - 1 for t, i in tok if t[i] in bB])
    bodies = {b for b, _ in nsB if b}
    before = {tuple(t[:-1]) for t in B if len(t) >= 2 and t[-1] in ('400', '151', '527', '156', '154')}
    n = len(before & bodies)
    rd.rec('RQ10', 'other closers alternate with the endings (EH4)', 'B bodies before both %d; threshold 5' % n, n >= 5)
    rd.finish()


if __name__ == '__main__':
    main()
