"""Ninety-first registered prediction set (PREDICTIONS.md, MX1-MX20): endings in mid-line. Writes
results/predict_test91.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from signs import FISH

random.seed(111)
HEAD = ('817', '820', '861')
POST = ('400', '90', '151')


def medial(t):
    t = list(t)
    out = []
    for i, g in enumerate(t):
        if g in R.END:
            rest = t[i + 1:]
            if rest and not (len(rest) == 1 and rest[0] in POST):
                out.append(i)
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    head, attr = R.classes(A)
    rd = R.Round('Ninety-first registered predictions: endings in mid-line', 'predict_test91')
    DL = sorted({tuple(t) for t in AB})
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    bodies = {b for b, e in ns}
    M = [(t, medial(t)) for t in DL if medial(t)]
    toks = [(t, i) for t, ii in M for i in ii]
    rd.say('- lines with a medial ending %d; medial tokens %d.' % (len(M), len(toks)))
    rd.say()

    def mx1(tk, key, lab):
        rd.thr(key, 'medial endings are 740%s' % lab, 'medial 740', sum(t[i] == '740' for t, i in tk), len(tk), 0.85)
    mx1(toks, 'MX1', '')
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in F for ln in r['seq'] if ln})
    fm = [(s, ty) for s, ty, t in FD if medial(t)]
    rd.thr('MX2', 'a Mohenjo-daro habit', 'medial-ending lines from Mohenjo-daro', sum(s == 'Mohenjo-daro' for s, ty in fm), len(fm), 0.7)
    fin = [(t, i) for t in DL for i in range(1, len(t)) if t[i] in R.END and i not in medial(t)]
    rd.ltl('MX3', 'no head before a medial ending', 'head class before, medial', [t[i - 1] in head for t, i in toks if i > 0], [t[i - 1] in head for t, i in fin])

    def mx4(Ml, key, lab):
        x = y = 0
        for t, ii in Ml:
            nm = R.name_of(list(t))
            if not nm:
                continue
            i = ii[0]
            before, after = tuple(t[:i]), nm[0][nm[0].index(t[i]) + 1:] if t[i] in nm[0] else tuple(t[i + 1:len(t) - 1])
            a_, c_ = after in bodies, before in bodies
            x += a_ and not c_
            y += c_ and not a_
        p = R.binom_ge(x, x + y)
        rd.rec(key, 'the name comes after%s' % lab, 'after only %d, before only %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
    mx4(M, 'MX4', '')
    rd.gtl('MX5', 'medial endings are counted', 'after a numeral, medial', [i > 0 and t[i - 1] in R.NUMS for t, i in toks], [t[i - 1] in R.NUMS for t, i in fin])
    rd.thr('MX6', 'a fish follows', 'medial endings followed by a fish', sum(t[i + 1] in FISH for t, i in toks), len(toks), 0.2)
    ba = [(t[i - 1], t[i + 1]) for t, i in toks if i > 0]
    rd.mi('MX7', 'a fixed phrase around the ending', 'medial tokens', [a for a, _ in ba], [b for _, b in ba])
    one = {(b[0], e) for b, e in ns if len(b) == 1}
    rd.thr('MX8', "'X 740' is a name", "medial 'sign + ending' also a 1-sign name", sum((t[i - 1], t[i]) in one for t, i in toks if i > 0), len(toks), 0.5)
    rd.thr('MX9', 'the line ends in a name', 'medial-ending lines ending in a name', sum(bool(R.name_of(list(t))) for t, ii in M), len(M), 0.7)
    rd.thr('MX10', 'on seals', 'medial-ending lines on seals', sum(ty == 'SEA' for s, ty in fm), len(fm), 0.7)
    hu = lambda t: len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1')
    nl = [t for t in DL if R.name_of(list(t)) and not medial(t)]
    rd.ltl('MX11', 'not headed', 'heading unit, medial-ending lines', [hu(t) for t, ii in M], [hu(t) for t in nl])
    rd.thr('MX12', 'a short element before', 'segments before of 1-2 signs', sum(ii[0] <= 2 for t, ii in M), len(M), 0.8)
    pc = Counter(t[ii[0] - 1] for t, ii in M if ii[0] > 0)
    rd.thr('MX13', 'the element recurs', 'lines whose pre-ending sign recurs (%s)' % ', '.join('%s x%d' % kv for kv in pc.most_common(5)),
           sum(pc[t[ii[0] - 1]] >= 2 for t, ii in M if ii[0] > 0), len(M), 0.3)
    a = [R.name_of(list(t))[1] == '740' for t, ii in M if R.name_of(list(t))]
    c = [R.name_of(list(t))[1] == '740' for t in nl]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('MX14', 'the final class is unaffected', '740 final, medial-ending lines %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p >= 0.05)
    rd.thr('MX15', 'no number after', 'medial endings followed by a numeral', sum(t[i + 1] in R.NUMS for t, i in toks), len(toks), 0.1, above=False)
    num = lambda t: any(g in R.NUMS for g in t)
    rd.gtl('MX16', 'medial-ending lines count', 'numeral, medial-ending lines', [num(t) for t, ii in M], [num(t) for t in nl])
    m5 = [(t, i) for t, i in toks if t[i] == '520' and i > 0]
    rd.thr('MX17', 'medial 520 follows a fish', 'medial 520 after a fish', sum(t[i - 1] in FISH for t, i in m5), len(m5), 0.5)
    objs = defaultdict(set)
    for r in F:
        for ln in r['seq']:
            if ln:
                objs[tuple(ln)].add(r['sealid'])
    rd.gtl('MX18', 'medial-ending texts are unique', 'one object, medial-ending texts', [len(objs[t]) == 1 for s, ty, t in FD if medial(t)],
           [len(objs[t]) == 1 for s, ty, t in FD if not medial(t) and R.name_of(list(t))])
    DB = sorted({tuple(t) for t in B})
    MB = [(t, medial(t)) for t in DB if medial(t)]
    mx1([(t, i) for t, ii in MB for i in ii], 'MX19', ' (B)')
    mx4(MB, 'MX20', ' (B)')
    rd.finish()


if __name__ == '__main__':
    main()
