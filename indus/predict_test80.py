"""Eightieth registered prediction set (PREDICTIONS.md, CG1-CG20): is the ending a case or a class? Writes
results/predict_test80.md. Distinct lines and names."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test15 import strat_perm
from predict_test44 import nonname
from signs import FISH

random.seed(100)
HEAD = ('817', '820', '861')


def two_sided(items):
    o, p1 = strat_perm(items)
    _, p2 = strat_perm([(not l_, s, y) for l_, s, y in items])
    return o, min(1, 2 * min(p1, p2))


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Eightieth registered predictions: is the ending a case or a class?', 'predict_test80')
    DL = sorted({tuple(t) for t in AB})

    def nlines(lines):
        return [(t, R.name_of(list(t))) for t in lines if R.name_of(list(t)) and R.name_of(list(t))[0]]
    NL = nlines(DL)
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in F for ln in r['seq'] if ln and R.name_of(ln) and R.name_of(ln)[0]})

    def within(key, title, rows):
        """rows: (label, head, ending); keeps heads with both endings; case holds if significant."""
        he = defaultdict(set)
        for l_, h, e in rows:
            he[h].add(e)
        items = [(l_, h, 1 if e == '520' else 0) for l_, h, e in rows if len(he[h]) == 2]
        if not items or len({l_ for l_, _, _ in items}) < 2:
            rd.rec(key, title, 'no usable heads', False)
            return None
        o, p = two_sided(items)
        rd.rec(key, title, 'names %d in %d heads; 520 difference %+.1f points; two-sided p = %.4f' % (
            len(items), len({h for _, h, _ in items}), 100 * o, p), p < 0.05)
        return p
    within('CG1', 'the object sets the case', [(ty == 'SEA', R.name_of(list(t))[0][-1], R.name_of(list(t))[1]) for s, ty, t in FD])
    after = lambda t: next(i for i in range(len(t) - 1, -1, -1) if t[i] in R.END)
    f400 = lambda t: after(t) + 1 < len(t) and t[after(t) + 1] == '400'
    within('CG2', '400 sets the case', [(f400(t), nm[0][-1], nm[1]) for t, nm in NL])
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    within('CG3', 'the heading sets the case', [(hu(t), nm[0][-1], nm[1]) for t, nm in NL])
    within('CG4', 'the city sets the case', [(s == 'Harappa', R.name_of(list(t))[0][-1], R.name_of(list(t))[1]) for s, ty, t in FD if s in ('Harappa', 'Mohenjo-daro')])
    within('CG5', 'what follows sets the case', [(after(t) + 1 < len(t), nm[0][-1], nm[1]) for t, nm in NL])
    cnt = lambda b: len(b) >= 2 and b[-2] in R.NUMS
    within('CG6', 'counting sets the case', [(cnt(nm[0]), nm[0][-1], nm[1]) for t, nm in NL])

    def cg7(names, key, lab):
        hc = defaultdict(Counter)
        for b, e in names:
            hc[b[-1]][e] += 1
        h5 = [h for h in hc if sum(hc[h].values()) >= 5]
        k = sum(max(hc[h].values()) / sum(hc[h].values()) >= 0.9 for h in h5)
        rd.thr(key, 'each head has its class%s' % lab, 'heads with one ending in 90%+', k, len(h5), 0.8)
        return hc
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    hc = cg7(ns, 'CG7', '')
    cg7(sorted({(b, e) for b, e in T.names(B) if b}), 'CG8', ' (B)')
    fs = lambda site: sorted({(b, e) for r in F if r['site'].strip() == site for b, e in R.names_in(r) if b})
    cg7(fs('Harappa'), 'CG9', ' (Harappa)')
    cg7(fs('Mohenjo-daro'), 'CG10', ' (Mohenjo-daro)')
    be = defaultdict(set)
    for b, e in ns:
        be[b].add(e)
    rd.thr('CG11', 'a body keeps its ending', 'bodies with both endings', sum(len(v) == 2 for v in be.values()), len(be), 0.02, above=False)
    h5 = [h for h in hc if sum(hc[h].values()) >= 3 and hc[h]['520'] > hc[h]['740']]
    rd.thr('CG12', 'the 520 class is the fish class', '520-majority heads that are fish (%s)' % ', '.join(h5), sum(h in FISH for h in h5), len(h5), 0.8)
    both = [h for h in hc if len(hc[h]) == 2]
    one = [h for h in hc if len(hc[h]) == 1]
    rd.gtl('CG13', 'fish heads waver', 'fish, heads with both endings', [h in FISH for h in both], [h in FISH for h in one])
    maj = {h: c.most_common(1)[0][0] for h, c in hc.items() if sum(c.values()) >= 3}

    def concord(key, title, pos):
        rows = [(maj[b[pos]], e) for b, e in ns if len(b) >= 2 and b[pos] in maj]
        m = [a for a, _ in rows]
        es = [e for _, e in rows]
        obs = sum(a == e for a, e in zip(m, es))
        ee = es[:]
        ge = 0
        for _ in range(R.N):
            random.shuffle(ee)
            ge += sum(a == e for a, e in zip(m, ee)) >= obs
        p = (ge + 1) / (R.N + 1)
        rd.rec(key, title, 'names %d; matching %d; p = %.4f' % (len(rows), obs, p), p < 0.05)
    concord('CG14', 'the opener agrees', 0)
    concord('CG15', 'the sign before the head agrees', -2)
    fr = [(maj[b[-2]] == '520', e == '520') for b, e in ns if len(b) >= 2 and b[-1] in FISH and b[-2] in maj]
    rd.gtl('CG16', 'the fish takes its neighbour class', '520, fish heads after a 520-class sign', [e for m, e in fr if m], [e for m, e in fr if not m])
    pr = [tuple(g for g in t if g in R.END) for t in DL]
    pr = [x for x in pr if len(x) == 2]
    s7 = sum(e == '740' for b, e in ns) / len(ns)
    q = s7 ** 2 + (1 - s7) ** 2
    k = sum(a == b for a, b in pr)
    from math import comb
    p = sum(comb(len(pr), i) * q ** i * (1 - q) ** (len(pr) - i) for i in range(k, len(pr) + 1))
    rd.rec('CG17', 'two names in a line agree', 'lines with two endings %d; same %d (chance %.2f); p = %.4f' % (len(pr), k, q, p), p < 0.05)
    bodies = {b for b, e in ns if len(b) >= 2}
    mx = max(len(b) for b in bodies)
    cited = set()
    for t in DL:
        if nonname(list(t)):
            for k_ in range(min(mx, len(t)), 1, -1):
                hit = [tuple(t[i:i + k_]) for i in range(len(t) - k_ + 1) if tuple(t[i:i + k_]) in bodies]
                if hit:
                    cited.add(hit[-1])
                    break
    a = [e == '740' for b, e in ns if b in cited]
    c = [e == '740' for b, e in ns if b not in cited]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('CG18', 'citing does not change the class', '740, cited names %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p >= 0.05)
    p19 = within('CG19x', 'seal against tablet (control)', [(ty == 'SEA', R.name_of(list(t))[0][-1], R.name_of(list(t))[1]) for s, ty, t in FD if ty in ('SEA', 'TAB')])
    rd.res[-1] = ('CG19', p19 is not None and p19 >= 0.05)
    rd.lines.append('- (CG19 is the control reading of the line above: holds if p >= 0.05.)')
    DB = sorted({tuple(t) for t in B})
    p20 = within('CG20x', '400 in B (control)', [(f400(t), nm[0][-1], nm[1]) for t, nm in nlines(DB)])
    rd.res[-1] = ('CG20', p20 is not None and p20 >= 0.05)
    rd.lines.append('- (CG20 is the control reading of the line above: holds if p >= 0.05.)')
    rd.finish()


if __name__ == '__main__':
    main()
