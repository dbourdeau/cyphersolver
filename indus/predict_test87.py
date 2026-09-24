"""Eighty-seventh registered prediction set (PREDICTIONS.md, RS1-RS20): regional name systems. Writes
results/predict_test87.md."""
import random
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test61 import units
from signs import FISH

random.seed(107)
HEAD = ('817', '820', '861')
MD, H = 'Mohenjo-daro', 'Harappa'


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Eighty-seventh registered predictions: regional name systems', 'predict_test87')
    SN = sorted({(r['site'].strip(), b, e) for r in F for b, e in R.names_in(r) if b})
    SL = sorted({(r['site'].strip(), tuple(ln)) for r in F for ln in r['seq'] if ln})
    reg = lambda s: R.region(s)
    guj = lambda s: reg(s) == 'gujarat'
    N = lambda cond: [(b, e) for s, b, e in SN if cond(s)]
    Lz = lambda cond: [t for s, t in SL if cond(s)]
    G = N(guj)
    rd.say('- distinct names: Gujarat %d, Mohenjo-daro %d, Harappa %d, Kalibangan %d, Chanhu-daro %d.' % (
        len(G), len(N(lambda s: s == MD)), len(N(lambda s: s == H)), len(N(lambda s: s == 'Kalibangan')), len(N(lambda s: s == 'Chanhu-daro'))))
    rd.say()
    f = lambda b: any(g in FISH for g in b)
    rd.gtl('RS1', 'fish-520 in Gujarat', 'fish, 520 names', [f(b) for b, e in G if e == '520'], [f(b) for b, e in G if e == '740'])
    nsAB = sorted({(b, e) for b, e in T.names(AB) if b})
    top = {h for h, _ in Counter(b[-1] for b, e in nsAB).most_common(10)}
    rd.ltl('RS2', 'Gujarat uses its own heads', 'top-10 head, Gujarat names', [b[-1] in top for b, e in G], [b[-1] in top for b, e in N(lambda s: s == MD)])
    hs = lambda cond: {b[-1] for b, e in N(cond)}
    jac = lambda a, b: len(a & b) / max(1, len(a | b))
    hG, hM, hH = hs(guj), hs(lambda s: s == MD), hs(lambda s: s == H)
    rd.rec('RS3', 'Gujarat looks to Sindh', 'Jaccard with MD %.3f, with H %.3f' % (jac(hG, hM), jac(hG, hH)), jac(hG, hM) > jac(hG, hH))

    def two(key, title, lab, a, c):
        p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
        rd.rec(key, title, '%s %s' % (lab, R.fl(sum(a), len(a), sum(c), len(c), p)), p < 0.05)
    two('RS4', 'Gujarat 520 share differs', '520, Gujarat against the cities', [e == '520' for b, e in G], [e == '520' for b, e in N(lambda s: s in (MD, H))])
    rd.rank('RS5', 'Gujarat names are short', 'MD against Gujarat', [len(b) for b, e in N(lambda s: s == MD)], [len(b) for b, e in G])
    isn = lambda t: bool(R.name_of(list(t)) and R.name_of(list(t))[0])
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    rd.ltl('RS6', 'Gujarat is not titled', 'heading unit, Gujarat name lines', [hu(t) for t in Lz(guj) if isn(t)], [hu(t) for t in Lz(lambda s: s == MD) if isn(t)])
    rd.gtl('RS7', 'Gujarat writes formulas', 'formulas, Gujarat', [nonname(list(t)) for t in Lz(guj)], [nonname(list(t)) for t in Lz(lambda s: s == MD)])
    sg = {g for t in Lz(guj) for g in t}
    sc = {g for t in Lz(lambda s: s in (MD, H)) for g in t}
    rd.thr('RS8', 'Gujarat has its own signs', 'Gujarat sign types at neither city', len(sg - sc), len(sg), 0.1)
    ng = [g for t in Lz(guj) for g in t if g in R.NUMS and 5 <= R.NUMS[g][0] <= 8]
    rd.thr('RS9', 'Gujarat uses the tiered form', 'tiered, Gujarat 5-8', sum(R.kind(g) == 'tiered' for g in ng), len(ng), 0.5)
    hL, hD = hs(lambda s: s == 'Lothal'), hs(lambda s: s == 'Dholavira')
    rd.rec('RS10', 'Gujarat is diverse', 'Jaccard Lothal-Dholavira %.3f, MD-H %.3f' % (jac(hL, hD), jac(hM, hH)), jac(hL, hD) < jac(hM, hH))
    D = N(lambda s: s == 'Dholavira')
    rd.thr('RS11', 'Dholavira avoids 520', 'Dholavira 520 names', sum(e == '520' for b, e in D), len(D), 0.1, above=False)
    hK, hC = hs(lambda s: s == 'Kalibangan'), hs(lambda s: s == 'Chanhu-daro')
    rd.rec('RS12', 'Kalibangan looks to Harappa', 'Jaccard with H %.3f, with MD %.3f' % (jac(hK, hH), jac(hK, hM)), jac(hK, hH) > jac(hK, hM))
    rd.rec('RS13', 'Chanhu-daro looks to Mohenjo-daro', 'Jaccard with MD %.3f, with H %.3f' % (jac(hC, hM), jac(hC, hH)), jac(hC, hM) > jac(hC, hH))
    topM = {h for h, _ in Counter(b[-1] for b, e in N(lambda s: s == MD)).most_common(10)}
    rd.gtl('RS14', 'Chanhu-daro uses Mohenjo-daro heads', 'MD top-10 head, Chanhu-daro names', [b[-1] in topM for b, e in N(lambda s: s == 'Chanhu-daro')],
           [b[-1] in topM for b, e in G])
    rd.rank('RS15', 'Kalibangan names are short', 'H against Kalibangan', [len(b) for b, e in N(lambda s: s == H)], [len(b) for b, e in N(lambda s: s == 'Kalibangan')])
    rd.ltl('RS16', 'Kalibangan is not titled', 'heading unit, Kalibangan name lines', [hu(t) for t in Lz(lambda s: s == 'Kalibangan') if isn(t)],
           [hu(t) for t in Lz(lambda s: s == H) if isn(t)])
    rn = [(reg(s), b, e) for s, b, e in SN if reg(s)]
    rd.mi('RS17', 'the head depends on the region', 'distinct (region, name)', [r_ for r_, b, e in rn], [b[-1] for r_, b, e in rn])
    rd.mi('RS18', 'the ending depends on the region', 'distinct (region, name)', [r_ for r_, b, e in rn], [e for r_, b, e in rn])
    rf = [(reg(s), t[0]) for s, t in SL if reg(s) and nonname(list(t))]
    rd.mi('RS19', 'formulas open by region', 'distinct (region, formula)', [a for a, _ in rf], [b for _, b in rf])
    U = units(sorted({b for b, e in nsAB if len(b) >= 2}))
    sm = [b for s, b, e in SN if s not in (MD, H) and len(b) >= 3]
    rd.thr('RS20', 'small sites use the city units', 'small-site names of 3+ with a unit', sum(any(p in U for p in zip(b, b[1:])) for b in sm), len(sm), 0.5)
    rd.finish()


if __name__ == '__main__':
    main()
