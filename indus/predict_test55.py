"""Fifty-fifth registered prediction set (PREDICTIONS.md, EH1-EH10): other endings on seals. Writes
results/predict_test55.md."""
import random
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test44 import nonname

random.seed(75)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    head, attr = R.classes(A)
    rd = R.Round('Fifty-fifth registered predictions: other endings on seals', 'predict_test55')
    num = lambda t: any(g in R.NUMS for g in t)
    usf = [(r, ln) for r in F if r['type'].startswith('SEAL') for ln in r['seq'] if nonname(ln) and not num(ln)]
    lc = Counter(ln[-1] for _, ln in usf)
    cand = sorted((g for g in lc if lc[g] >= 10), key=lambda g: -lc[g])
    rd.say('- uncounted seal formulas %d; candidates %s.' % (len(usf), ', '.join('%s x%d' % (g, lc[g]) for g in cand)))
    rd.say()

    def lastshare(L, g):
        n = sum(t.count(g) for t in L)
        k = sum(1 for t in L if t and t[-1] == g)
        return k / n if n else 0
    sh = {g: lastshare(AB, g) for g in cand}
    rd.thr('EH1', 'they stand last', 'candidates last in 70%%+ of tokens (%s)' % ', '.join('%s %.2f' % (g, sh[g]) for g in cand),
           sum(v >= 0.7 for v in sh.values()), len(cand), 0.5)
    ce = [ln for _, ln in usf if ln[-1] in cand]
    rd.gtl('EH2', 'a head comes before', 'head class, sign before the candidate', [ln[-2] in head for ln in ce],
           [ln[i] in head for ln in ce for i in range(len(ln) - 2)])
    bodies = {b for b, _ in T.names(AB)}
    rd.thr('EH3', 'the rest is a name', 'lines whose rest is a name body', sum(tuple(ln[:-1]) in bodies for ln in ce), len(ce), 0.15)
    before = {tuple(t[:-1]) for t in AB if len(t) >= 2 and t[-1] in cand}
    both = before & {b for b in bodies if b}
    rd.rec('EH4', 'they alternate with the endings', 'bodies attested before both %d; threshold 10' % len(both), len(both) >= 10)
    rd.mi('EH5', 'the head picks the ending', 'candidate lines', [ln[-2] for ln in ce], [ln[-1] for ln in ce])
    snl = [ln for r in F if r['type'].startswith('SEAL') for ln in r['seq'] if R.name_of(ln)]
    rd.rank('EH6', 'they are short', 'name lines against candidate lines', [len(t) for t in snl], [len(t) for t in ce])
    fol = [t[i + 1] in R.END for t in AB for i in range(len(t) - 1) if t[i] in cand]
    rd.thr('EH7', 'they do not precede an ending', 'candidate tokens followed by 740/520', sum(fol), len(fol), 0.05, above=False)
    ss = lambda site: [nonname(ln) and not num(ln) and ln[-1] in cand for r in F if r['type'].startswith('SEAL')
                       and r['site'].strip() == site for ln in r['seq'] if len(ln) >= 2]
    rd.gtl('EH8', 'a Mohenjo-daro habit', 'candidate-ending seal lines, Mohenjo-daro', ss('Mohenjo-daro'), ss('Harappa'))
    shB = {g: lastshare(B, g) for g in cand}
    rd.thr('EH9', 'they stand last in B too', 'candidates last in 50%%+ of B tokens (%s)' % ', '.join('%s %.2f' % (g, shB[g]) for g in cand),
           sum(v >= 0.5 for v in shB.values()), len(cand), 0.7)
    rd.thr('EH10', 'a few endings', 'five commonest candidates', sum(lc[g] for g in cand[:5]), len(usf), 0.5)
    rd.finish()


if __name__ == '__main__':
    main()
