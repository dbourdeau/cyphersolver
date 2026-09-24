"""Ninetieth registered prediction set (PREDICTIONS.md, MM1-MM20): the minor media. Writes results/predict_test90.md."""
import random
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test44 import nonname

random.seed(110)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Ninetieth registered predictions: the minor media', 'predict_test90')
    med = lambda ty: ('seal' if ty.startswith('SEAL') else 'graf' if ty == 'POT:T:g' else 'stamp' if ty == 'POT:T:s' else
                      'copper' if ty == 'TAB:C' else 'TAB:I' if ty == 'TAB:I' else 'TAB:B' if ty == 'TAB:B' else
                      'bangle' if ty == 'BNGL' else 'tag' if ty in ('TAG', 'TAG:L') else None)
    D = sorted({(med(r['type']), tuple(ln)) for r in F for ln in r['seq'] if ln and med(r['type'])})
    L = lambda m: [t for m_, t in D if m_ == m]
    rd.say('- distinct lines: %s.' % dict(Counter(m for m, t in D)))
    rd.say()
    S, G = L('seal'), L('graf')
    rd.rank('MM1', 'graffiti are short', 'seal against graffiti', [len(t) for t in S], [len(t) for t in G])
    num = lambda t: any(g in R.NUMS for g in t)
    rd.gtl('MM2', 'graffiti count', 'numeral, graffiti', [num(t) for t in G], [num(t) for t in S])
    ct = lambda t: len(t) >= 2 and t[-1] == '700' and all(g in R.NUMS for g in t[:-1])
    rd.gtl('MM3', 'graffiti are count tokens', 'count token, graffiti', [ct(t) for t in G], [ct(t) for t in S])
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    top = {h for h, _ in Counter(b[-1] for b, e in ns).most_common(10)}
    nm = lambda X: [R.name_of(list(t)) for t in X if R.name_of(list(t)) and R.name_of(list(t))[0]]
    rd.gtl('MM4', 'graffiti name the common roles', 'top-10 head, graffiti names', [b[-1] in top for b, e in nm(G)], [b[-1] in top for b, e in nm(S)])
    bsig = {g for b, e in ns for g in b}
    fo = lambda X: [g not in bsig for t in X if nonname(list(t)) for g in t if g not in R.NUMS]
    rd.gtl('MM5', 'graffiti use formula words', 'formula-only, graffiti tokens', fo(G), fo(S))
    sk = lambda X: [R.kind(g) == 'short' for t in X for g in t if g in R.NUMS]
    rd.gtl('MM6', 'graffiti count with strokes', 'short, graffiti numerals', sk(G), sk(S))
    gs = sorted({(r['site'].strip() == 'Harappa', tuple(ln)) for r in F if r['type'] == 'POT:T:g' for ln in r['seq'] if ln})
    rd.gtl('MM7', 'Harappa graffiti are counts', 'count token, Harappa graffiti', [ct(t) for h, t in gs if h], [ct(t) for h, t in gs if not h])
    sealset = set(S)
    st, tg = L('stamp'), L('tag')
    rd.thr('MM8', 'stamped pots carry seal texts', 'stamped-pot lines on a seal', sum(t in sealset for t in st), len(st), 0.3)
    rd.gtl('MM9', 'stamps, not graffiti, copy seals', 'on a seal, stamped-pot lines', [t in sealset for t in st], [t in sealset for t in G])
    rd.thr('MM10', 'tags carry seal texts', 'tag lines on a seal', sum(t in sealset for t in tg), len(tg), 0.3)
    cobj = [r for r in F if r['type'] == 'TAB:C']
    ctext = Counter(tuple(tuple(ln) for ln in r['seq'] if ln) for r in cobj)
    rd.thr('MM11', 'copper tablets repeat', 'distinct copper texts on 2+ tablets', sum(n >= 2 for n in ctext.values()), len(ctext), 0.3)
    C = L('copper')
    isn = lambda t: bool(R.name_of(list(t)) and R.name_of(list(t))[0])
    rd.ltl('MM12', 'copper tablets are not name tags', 'name lines, copper', [isn(t) for t in C], [isn(t) for t in S])
    rd.thr('MM13', 'copper is Mohenjo-daran', 'copper tablets from Mohenjo-daro', sum(r['site'].strip() == 'Mohenjo-daro' for r in cobj), len(cobj), 0.9)
    rd.thr('MM14', 'copper texts are their own', 'copper lines on a seal', sum(t in sealset for t in C), len(C), 0.1, above=False)
    Bg = L('bangle')
    rd.thr('MM15', 'bangle texts are short', 'bangle lines of 3 or fewer', sum(len(t) <= 3 for t in Bg), len(Bg), 0.8)
    rd.gtl('MM16', 'bangles carry formulas', 'formula, bangle lines', [nonname(list(t)) for t in Bg], [nonname(list(t)) for t in S])
    six = [(m, t) for m, t in D if m in ('seal', 'TAB:I', 'TAB:B', 'copper', 'graf', 'bangle')]
    rd.mi('MM17', 'the medium sets the length', 'distinct lines', [m for m, t in six], [R.lstrat(len(t)) for m, t in six])
    rd.mi('MM18', 'the medium sets the last sign', 'distinct lines', [m for m, t in six], [t[-1] for m, t in six])
    rd.mi('MM19', 'the medium sets the first sign', 'distinct lines', [m for m, t in six], [t[0] for m, t in six])
    ne = [(m == 'seal', R.name_of(list(t))[1]) for m, t in D if isn(t)]
    a = [e == '520' for s, e in ne if s]
    c = [e == '520' for s, e in ne if not s]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('MM20', 'the medium changes the class share', '520, seal names %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
