"""Hundred-and-first registered prediction set (PREDICTIONS.md, RR1-RR20): recent findings on held-out data. Writes
results/predict_test101.md."""
import random
from collections import Counter, defaultdict
from itertools import combinations

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test62 import sims
from predict_test91 import medial
from predict_test93 import pairs_of, shares
from predict_test99 import roles

random.seed(121)
HEAD = ('817', '820', '861')
J = ('705', '706')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-first registered predictions: recent findings on held-out data', 'predict_test101')
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FL = sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln})
    FT = sorted({(r['type'][:3], tuple(ln)) for r in Fn for ln in r['seq'] if ln})
    BL = sorted({tuple(t) for t in B})
    rd.say("- F' distinct lines %d; B distinct lines %d." % (len(FL), len(BL)))
    rd.say()

    def names_of(lines):
        return sorted({R.name_of(list(t)) for t in lines if R.name_of(list(t)) and R.name_of(list(t))[0]})

    def mx(lines, names, k1, k8, k13):
        toks = [(t, i) for t in lines for i in medial(t)]
        if k1:
            rd.thr(k1, "medial endings are 740 (F')", 'medial 740', sum(t[i] == '740' for t, i in toks), len(toks), 0.85)
        one = {(b[0], e) for b, e in names if len(b) == 1}
        lab = " (F')" if k1 else ' (B)'
        rd.thr(k8, "'X 740' is a name%s" % lab, "medial 'sign + ending' a 1-sign name", sum((t[i - 1], t[i]) in one for t, i in toks if i > 0), len(toks), 0.5)
        if k13:
            M = [(t, medial(t)) for t in lines if medial(t)]
            pc = Counter(t[ii[0] - 1] for t, ii in M if ii[0] > 0)
            rd.thr(k13, "the element recurs (F')", 'lines whose pre-ending sign recurs', sum(pc[t[ii[0] - 1]] >= 2 for t, ii in M if ii[0] > 0), len(M), 0.3)
    mx(FL, names_of(FL), 'RR1', 'RR2', 'RR3')
    hd = lambda t: len(t) >= 2 and t[0] in HEAD

    def hs9(lines, key, lab):
        hb = defaultdict(set)
        hc = Counter()
        for t in lines:
            if hd(t) and R.name_of(list(t)) and R.name_of(list(t))[0]:
                b = R.name_of(list(t))[0]
                hb[b].add(t[0])
                hc[b] += 1
        rep = [b for b in hc if hc[b] >= 2]
        rd.thr(key, 'heading signs interchangeable%s' % lab, 'bodies after 2+ heading signs', sum(len(hb[b]) >= 2 for b in rep), len(rep), 0.2)
    hs9(FL, 'RR4', " (F')")
    H = [t for t in FL if hd(t)]
    rd.mi('RR5', "the heading chooses its number (F')", 'headed lines', [t[0] for t in H], [t[1] == '2' for t in H])

    def hs4(lines, key, lab):
        h = [t for t in lines if hd(t)]
        rd.gtl(key, '861 heads formulas%s' % lab, 'formula, 861 lines', [nonname(list(t)) for t in h if t[0] == '861'], [nonname(list(t)) for t in h if t[0] == '817'])
    hs4(FL, 'RR6', " (F')")
    tk = lambda lines, s: [(t, i) for t in lines for i in range(len(t)) if t[i] in s]
    rd.gtl('RR7', "'1' follows the ending (F')", "after 740/520, '1'", [i > 0 and t[i - 1] in R.END for t, i in tk(FL, ('1',))],
           [i > 0 and t[i - 1] in R.END for t, i in tk(FL, ('2', '3'))])

    def on4(lines, key, lab):
        h1 = [t[0] for t in lines if len(t) >= 2 and t[1] == '1' and t[0] in HEAD]
        rd.thr(key, "'1' belongs to 820%s" % lab, "'heading + 1' that are '820 1'", sum(h == '820' for h in h1), len(h1), 0.9)
    on4(FL, 'RR8', " (F')")

    def pz7(lines, key, lab, typed=None):
        ro = roles([t for t in lines if len(t) >= 2])[0]
        I = {g for g in ro if ro[g] == 'I'}
        M = {g for g in ro if ro[g] == 'M'}
        tt = [(t, i) for t in lines for i in range(len(t))]
        nx = lambda t, i: i + 1 < len(t) and t[i + 1] in R.NUMS
        rd.gtl(key, 'openers precede numbers%s' % lab, 'numeral after, openers', [nx(t, i) for t, i in tt if t[i] in I], [nx(t, i) for t, i in tt if t[i] in M])
        return I, M
    I, M = pz7(FL, 'RR9', " (F')")
    ft = [(ty, g) for ty, t in FT for g in t]
    rd.gtl('RR10', "openers are seal signs (F')", 'seal, openers', [ty == 'SEA' for ty, g in ft if g in I], [ty == 'SEA' for ty, g in ft if g in M])
    nx = [t[i + 1] for t, i in tk(FL, J) if i + 1 < len(t) and t[i + 1] in R.NUMS]
    rd.thr('RR11', "the jar number is 33 (F')", 'numerals after 705/706 that are 33', sum(g == '33' for g in nx), len(nx), 0.6)

    def cf11(lines, key, lab):
        bj = [(t[i - 1], t[i]) for t, i in tk(lines, J) if i > 0]
        o, p = R.mi_perm([a for a, _ in bj], [b for _, b in bj])
        rd.rec(key, '705 and 706 are free variants%s' % lab, 'tokens %d; MI %.3f; p = %.4f' % (len(bj), o, p), p >= 0.05)
    cf11(FL, 'RR12', " (F')")
    sh, vc = shares(pairs_of(FL), 1)
    exp = {'236': 2, '632': 2, '717': 2, '923': 3}
    ok = [s for s in exp if s in vc and vc[s].most_common(1)[0][0] == exp[s]]
    rd.rec('RR13', "frozen counts hold (F')", 'kept: %s of %s; threshold 3' % (', '.join(ok), ', '.join('%s=%d' % kv for kv in exp.items())), len(ok) >= 3)
    tc, S, C = sims([list(t) for t in FL], 10)
    S = [s for s in S if s not in R.NUMS]
    ss = set(S)
    ap = [(a, str(int(a) + 1)) for a in S if a.isdigit() and str(int(a) + 1) in ss]
    allp = list(combinations(S, 2))
    rd.rank('RR14', "number neighbours share contexts (F')", 'adjacent-number against random pairs', [C[p] for p in ap], [C[p] for p in random.sample(allp, min(2000, len(allp)))])
    hs9(BL, 'RR15', ' (B)')
    on4(BL, 'RR16', ' (B)')
    pz7(BL, 'RR17', ' (B)')
    mx(BL, names_of(BL), None, 'RR18', None)
    hs4(BL, 'RR19', ' (B)')
    cf11(BL, 'RR20', ' (B)')
    rd.finish()


if __name__ == '__main__':
    main()
