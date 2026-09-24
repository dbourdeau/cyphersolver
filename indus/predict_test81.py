"""Eighty-first registered prediction set (PREDICTIONS.md, KC1-KC20): what the two classes are. Writes
results/predict_test81.md. Distinct names and lines."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test62 import sims
from predict_test76 import fcounted
from signs import FISH

random.seed(101)


def classes_of(names, k=3):
    hc = defaultdict(Counter)
    for b, e in names:
        hc[b[-1]][e] += 1
    out = {}
    for h, c in hc.items():
        if sum(c.values()) >= k and c['740'] != c['520']:
            out[h] = '740' if c['740'] > c['520'] else '520'
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    cat = R.cat_of()
    rd = R.Round('Eighty-first registered predictions: what the two classes are', 'predict_test81')
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    DL = sorted({tuple(t) for t in AB})
    cl = classes_of(ns)
    c5 = sorted(h for h in cl if cl[h] == '520')
    rd.say('- classed heads %d; 520 class: %s.' % (len(cl), ', '.join(c5)))
    rd.say()
    cn = [(b, cl[b[-1]]) for b, e in ns if b[-1] in cl]
    num = lambda b: any(g in R.NUMS for g in b)
    rd.strat('KC1', 'the 520 class is counted', 'by fish head: numeral, 520 minus 740 class', [(c == '520', b[-1] in FISH, 1 if num(b) else 0) for b, c in cn])
    cnt = lambda b: len(b) >= 2 and b[-2] in R.NUMS
    nf = [(b, c) for b, c in cn if b[-1] not in FISH]
    rd.gtl('KC2', 'non-fish 520 heads are counted', 'counted, non-fish 520-class', [cnt(b) for b, c in nf if c == '520'], [cnt(b) for b, c in nf if c == '740'])

    def kc3(rows, key, lab):
        fm = lambda b: any(g in FISH for g in b[:-1])
        rd.gtl(key, 'the 520 class takes fish modifiers%s' % lab, 'fish modifier, non-fish 520-class', [fm(b) for b, c in rows if c == '520'], [fm(b) for b, c in rows if c == '740'])
    kc3(nf, 'KC3', '')
    tc, S, C = sims(AB, 5)
    fishS = [g for g in S if g in FISH]
    mc = lambda h: sum(C[(h, f)] for f in fishS if f != h) / max(1, len([f for f in fishS if f != h]))
    h5 = [h for h in cl if h not in FISH and h in S]
    rd.rank('KC4', 'the 520 class keeps fish company', '520 against 740 non-fish heads', [mc(h) for h in h5 if cl[h] == '520'], [mc(h) for h in h5 if cl[h] == '740'])
    ct = [(cat[h], cl[h]) for h in cl if h in cat]
    rd.mi('KC5', 'the class goes with the shape', 'classed head types', [a for a, _ in ct], [b for _, b in ct])
    tok = Counter(g for t in AB for g in t)
    rd.rank('KC6', 'the 520 class is rarer', '740 against 520 head tokens', [tok[h] for h in cl if cl[h] == '740'], [tok[h] for h in cl if cl[h] == '520'])
    FL = [t for t in DL if nonname(list(t))]
    fc = fcounted(FL)
    items = {s for v, k, s in fc}
    rd.gtl('KC7', 'the 520 class is counted in formulas', 'formula item, 520-class heads', [h in items for h in cl if cl[h] == '520'], [h in items for h in cl if cl[h] == '740'])
    rd.rank('KC8', 'the 520 class is counted higher', '520 against 740 values', [v for v, k, s in fc if cl.get(s) == '520'], [v for v, k, s in fc if cl.get(s) == '740'])
    pn = lambda b: len(b) >= 2 and (b[-2] in R.NUMS or b[-2] in FISH)
    rd.gtl('KC9', 'numbers and fish precede the 520 class', 'numeral or fish before, 520 class', [pn(b) for b, c in cn if c == '520'], [pn(b) for b, c in cn if c == '740'])
    fns = sorted({(b, e) for r in F for b, e in R.names_in(r) if b})
    fcl = classes_of(fns, 5)
    ab5 = classes_of(ns, 5)
    both = [h for h in ab5 if h in fcl]
    rd.thr('KC10', 'the classes hold in the fuller corpus', 'same class in A + B and F', sum(ab5[h] == fcl[h] for h in both), len(both), 0.9)
    fb = [(b, e) for b, e in ns if b[-1] in cl and cl[b[-1]] == '740' and len(b) >= 2 and b[-2] in FISH]
    rd.thr('KC11', 'a fish does not move a 740 head', '740-class names with a fish before the head taking 740', sum(e == '740' for b, e in fb), len(fb), 0.9)
    fs = sorted({(r['site'].strip(), b, e) for r in F if r['site'].strip() in ('Harappa', 'Mohenjo-daro') for b, e in R.names_in(r) if b})
    rd.gtl('KC12', 'Harappa writes the 520 class', '520, Harappa names', [e == '520' for s, b, e in fs if s == 'Harappa'], [e == '520' for s, b, e in fs if s == 'Mohenjo-daro'])

    def lines740(lines):
        out = []
        for t in lines:
            nm = R.name_of(list(t))
            if nm and nm[0] and nm[1] == '740':
                i = max(j for j, g in enumerate(t) if g in R.END)
                out.append((nm[0], t[i + 1] if i + 1 < len(t) else '#'))
        return out
    L7 = lines740(DL)

    def kc13(L, key, lab):
        rd.mi(key, 'the head calls 90%s' % lab, '740 lines', [b[-1] for b, f in L], [f == '90' for b, f in L])
    kc13(L7, 'KC13', '')
    rd.mi('KC14', 'the head calls 400', '740 lines', [b[-1] for b, f in L7], [f == '400' for b, f in L7])
    fol = [(b[-1], f) for b, f in L7 if f in ('90', '400', '151')]
    hh = [h for h, _ in fol]
    ff = [f for _, f in fol]

    def jac(fs_):
        a = {h for h, f in zip(hh, fs_) if f == '90'}
        c = {h for h, f in zip(hh, fs_) if f == '400'}
        return len(a & c) / max(1, len(a | c))
    obs = jac(ff)
    sh = ff[:]
    le = 0
    for _ in range(R.N):
        random.shuffle(sh)
        le += jac(sh) <= obs
    p = (le + 1) / (R.N + 1)
    rd.rec('KC15', '90 and 400 take different heads', 'lines %d; Jaccard %.3f; p = %.4f' % (len(fol), obs, p), p < 0.05)
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in F for ln in r['seq'] if ln})
    f7 = [(s, ty, f) for s, ty, t in FD for b, f in lines740([t])]
    rd.gtl('KC16', "'740 90' is a seal form", "seal, '740 90'", [ty == 'SEA' for s, ty, f in f7 if f == '90'], [ty == 'SEA' for s, ty, f in f7 if f != '90'])
    rd.gtl('KC17', "'740 90' is Mohenjo-daran", "Mohenjo-daro, '740 90'", [s == 'Mohenjo-daro' for s, ty, f in f7 if f == '90' and s in ('Harappa', 'Mohenjo-daro')],
           [s == 'Mohenjo-daro' for s, ty, f in f7 if f != '90' and s in ('Harappa', 'Mohenjo-daro')])
    rd.rank('KC18', "'740 90' names are long", "'740 90' against other 740 bodies", [len(b) for b, f in L7 if f == '90'], [len(b) for b, f in L7 if f != '90'])
    DB = sorted({tuple(t) for t in B})
    kc13(lines740(DB), 'KC19', ' (B)')
    nsB = sorted({(b, e) for b, e in T.names(B) if b})
    clB = classes_of(nsB)
    kc3([(b, clB[b[-1]]) for b, e in nsB if b[-1] in clB and b[-1] not in FISH], 'KC20', ' (B)')
    rd.finish()


if __name__ == '__main__':
    main()
