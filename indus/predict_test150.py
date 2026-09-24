"""Hundred-and-fiftieth registered prediction set (PREDICTIONS.md, NC1-NC5): numeral compounds as a shared vocabulary.
Writes results/predict_test150.md."""
from collections import Counter, defaultdict
from math import comb

import rtools as R
from predict_test103 import CL
from predict_test112 import runs

M = set(R.END) | set(CL) | {'400', '90'}
CITIES = ('Mohenjo-daro', 'Harappa')


def sign_test(diffs):
    w = sum(d > 0 for d in diffs)
    l_ = sum(d < 0 for d in diffs)
    n = w + l_
    p = sum(comb(n, k) for k in range(w, n + 1)) / 2 ** n if n else 1.0
    return w, l_, p


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-fiftieth registered predictions: numeral compounds as a shared vocabulary', 'predict_test150')
    lex = lambda g: g not in R.NUMS and g not in M
    DL = sorted({tuple(t) for t in A + B})
    comp = Counter()
    big = Counter()
    for t in DL:
        cs, bs = set(), set()
        for i in range(len(t) - 1):
            if t[i] in R.NUMS and lex(t[i + 1]):
                cs.add((t[i], t[i + 1]))
            elif lex(t[i]) and lex(t[i + 1]):
                bs.add((t[i], t[i + 1]))
        comp.update(cs)
        big.update(bs)
    C = [p for p, n in comp.items() if n >= 3]
    site = defaultdict(set)
    typ = defaultdict(set)
    for r in F:
        ty = 'seal' if r['type'].startswith('SEAL') else ('tablet' if r['type'].startswith('TAB') else 'other')
        for ln in r['seq']:
            for p in zip(ln, ln[1:]):
                site[p].add(recs[r['sealid']][3])
                typ[p].add(ty)
    bl = list(big.items())

    def matched(p):
        d = min(abs(n - comp[p]) for q, n in bl)
        return [q for q, n in bl if abs(n - comp[p]) == d]
    rd.say('- compounds with 3+ distinct lines: %d; lexical bigrams: %d.' % (len(C), len(bl)))
    rd.say()
    mean = lambda f, qs: sum(f(q) for q in qs) / len(qs)

    def ptest(key, title, f):
        diffs = [f(p) - mean(f, matched(p)) for p in C]
        w, l_, p = sign_test(diffs)
        rd.rec(key, title, 'compounds higher %d, lower %d, ties %d; mean %.2f against %.2f; sign test p = %.4f' % (
            w, l_, len(diffs) - w - l_, sum(f(p) for p in C) / len(C), sum(mean(f, matched(p)) for p in C) / len(C), p), p < 0.05)
    ptest('NC1', 'compounds travel to more sites', lambda p: len(site[p]))
    ptest('NC2', 'compounds on more object types', lambda p: len(typ[p]))
    ptest('NC3', 'compounds in both cities', lambda p: float(all(c in site[p] for c in CITIES)))
    ptest('NC4', 'compounds at the smaller sites', lambda p: float(any(s not in CITIES for s in site[p])))
    vals = {c: defaultdict(Counter) for c in CITIES}
    for r in F:
        s = recs[r['sealid']][3]
        if s in CITIES:
            for ln in r['seq']:
                for i, j, rr in runs(ln):
                    if j < len(ln) and lex(ln[j]):
                        vals[s][ln[j]][sum(R.NUMS[g][0] for g in rr)] += 1
    shared = [x for x in vals[CITIES[0]] if x in vals[CITIES[1]]]
    same = [vals[CITIES[0]][x].most_common(1)[0][0] == vals[CITIES[1]][x].most_common(1)[0][0] for x in shared]
    rd.thr('NC5', 'the same value in both cities', 'signs counted in both cities with the same commonest value (%s)' % ', '.join(
        '%s %d/%d' % (x, vals[CITIES[0]][x].most_common(1)[0][0], vals[CITIES[1]][x].most_common(1)[0][0]) for x in shared[:15]), sum(same), len(same), 0.7)
    rd.finish()


if __name__ == '__main__':
    main()
