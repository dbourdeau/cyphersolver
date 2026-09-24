"""Hundred-and-seventh registered prediction set (PREDICTIONS.md, RH1-RH20): sets 102-106 on held-out data. Writes
results/predict_test107.md."""
import random
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test81 import classes_of
from predict_test102 import blk
from predict_test103 import CL
from predict_test104 import template
from predict_test105 import cbody
from signs import FISH

random.seed(127)
CITY = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-seventh registered predictions: sets 102-106 on held-out data', 'predict_test107')
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FL = [t for t in sorted({tuple(ln) for r in Fn for ln in r['seq'] if ln}) if len(t) >= 2]
    OL = [t for t in sorted({tuple(ln) for r in Fn if r['site'].strip() not in CITY for ln in r['seq'] if ln}) if len(t) >= 2]
    OS = sorted({(r['type'][:3], tuple(ln)) for r in Fn if r['site'].strip() not in CITY for ln in r['seq'] if len(ln) >= 2})
    BL = [t for t in sorted({tuple(t) for t in B}) if len(t) >= 2]
    rd.say("- F' lines %d; small-site lines %d; B lines %d." % (len(FL), len(OL), len(BL)))
    rd.say()
    ok = lambda g: g not in R.NUMS and blk(g) is not None

    def names(lines):
        return sorted({R.name_of(list(t)) for t in lines if R.name_of(list(t)) and R.name_of(list(t))[0]})

    def rh1(lines, key, lab):
        bt = [(b, i) for b, e in names(lines) for i in range(len(b)) if ok(b[i])]
        rd.gtl(key, 'block 1 heads names%s' % lab, 'last body sign, block 1', [i == len(b) - 1 for b, i in bt if blk(b[i]) == 1],
               [i == len(b) - 1 for b, i in bt if blk(b[i]) != 1])
    rh1(FL, 'RH1', " (F')")
    tk = [(t, i) for t in FL for i in range(len(t)) if ok(t[i]) and (R.name_of(list(t)) or nonname(list(t)))]
    rd.gtl('RH2', "block 3 is a formula block (F')", 'formula, block 3', [nonname(list(t)) for t, i in tk if blk(t[i]) == 3], [nonname(list(t)) for t, i in tk if blk(t[i]) != 3])
    same = lambda t: sum(1 for x, y in zip(t, t[1:]) if ok(x) and ok(y) and blk(x) == blk(y))
    obs = sum(map(same, FL))
    ge = 0
    for _ in range(R.N // 10):
        k = 0
        for t in FL:
            s = list(t)
            random.shuffle(s)
            k += same(s)
        ge += k >= obs
    p = (ge + 1) / (R.N // 10 + 1)
    rd.rec('RH3', "families cluster (F')", 'same-block adjacent pairs %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    nsF = names(FL)
    heads = {b[-1] for b, e in nsF}
    ct = [(t, i) for t in FL for i in range(len(t)) if t[i] in CL]
    rd.thr('RH4', "closers follow heads (F')", 'closer tokens after a name head', sum(i > 0 and t[i - 1] in heads for t, i in ct), len(ct), 0.5)
    pv = [(t[i], t[i - 1]) for t, i in ct if i > 0]
    rd.mi('RH5', "each closer has its partners (F')", 'closer tokens', [a for a, _ in pv], [b for _, b in pv])
    rd.thr('RH6', "one closer per line (F')", 'lines with two closers', sum(len({g for g in t if g in CL}) >= 2 for t in FL), len(FL), 0.03, above=False)

    def rh7(lines, nsx, key, lab):
        cb = sorted({cbody(t) for t in lines if cbody(t)})
        fish = lambda b: any(g in FISH for g in b)
        rd.ltl(key, 'closer bodies are not fish names%s' % lab, 'fish, closer bodies', [fish(b) for b in cb], [fish(b) for b, e in nsx])
        return cb
    cb = rh7(FL, nsF, 'RH7', " (F')")
    cl = classes_of(nsF)
    c5 = {h for h in cl if cl[h] == '520'}
    rd.ltl('RH8', "closers avoid the 520 class (F')", '520-class head before, closers', [b[-1] in c5 for b in cb if b], [b[-1] in c5 for b, e in nsF if e == '520'])
    rd.thr('RH9', "one number per line (F')", 'lines with 2+ N', sum(template(t).count('N') >= 2 for t in FL), len(FL), 0.1, above=False)
    tf = {k for k, _ in Counter(template(t) for t in FL).most_common(5)}
    ta = {k for k, _ in Counter(template(t) for t in sorted({tuple(t) for t in AB})).most_common(5)}
    rd.rec('RH10', "the templates hold in F'", "F' top 5 %s; shared with A + B %d; threshold 4" % (sorted(tf), len(tf & ta)), len(tf & ta) >= 4)
    bare = lambda t: template(t) == 'X'

    def bare_tests(lines, nsx, k1, k6, k7, lab):
        X = [t for t in lines if bare(t)]
        NL = [t for t in lines if R.name_of(list(t))]
        hd = {b[-1] for b, e in nsx}
        op = {b[0] for b, e in nsx if len(b) >= 2}
        if k1:
            rd.rank(k1, 'bare lines are short%s' % lab, 'name against bare lines', [len(t) for t in NL], [len(t) for t in X])
        if k6:
            rd.thr(k6, 'bare lines end in a head%s' % lab, 'bare lines ending in a name head', sum(t[-1] in hd for t in X), len(X), 0.5)
        if k7:
            rd.thr(k7, 'bare lines start with an opener%s' % lab, 'bare lines starting with a name opener', sum(t[0] in op for t in X), len(X), 0.5)
        return X, NL
    X, NL = bare_tests(FL, nsF, 'RH11', 'RH12', 'RH13', " (F')")
    bsig = {g for b, e in nsF for g in b}
    rd.gtl('RH14', "bare lines use formula words (F')", 'formula-only, bare tokens', [g not in bsig for t in X for g in t], [g not in bsig for t in NL for g in t])
    t368 = [(t, i) for t in FL for i in range(len(t)) if t[i] == '368']
    rd.thr('RH15', "368 follows a head (F')", '368 after a name head', sum(i > 0 and t[i - 1] in heads for t, i in t368), len(t368), 0.6)
    si = [cbody(t) is not None for ty, t in OS if ty == 'SEA' and (cbody(t) is not None or R.name_of(list(t)))]
    rd.thr('RH16', 'closers at the small sites', 'closer share of small-site seal inscriptions', sum(si), len(si), 0.1)
    bare_tests(OL, nsF, 'RH17', None, 'RH18', ' (small sites)')
    rh1(BL, 'RH19', ' (B)')
    rh7(BL, names(BL), 'RH20', ' (B)')
    rd.finish()


if __name__ == '__main__':
    main()
