"""Fifty-fourth registered prediction set (PREDICTIONS.md, FO1-FO10): signs used only in formulas. Writes
results/predict_test54.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname

random.seed(74)
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Fifty-fourth registered predictions: signs used only in formulas', 'predict_test54')
    bsig = {g for b, _ in T.names(AB) for g in b}
    fm = [t for t in AB if nonname(t)]
    tok = [(t, i) for t in fm for i, g in enumerate(t) if g not in R.NUMS]
    fo = lambda g: g not in bsig
    only = sorted({t[i] for t, i in tok if fo(t[i])})
    rd.say('- formula-only signs %d; formula tokens %d.' % (len(only), len(tok)))
    rd.say()
    rd.gtl('FO1', 'they close the formula', 'last, formula-only tokens', [i == len(t) - 1 for t, i in tok if fo(t[i])],
           [i == len(t) - 1 for t, i in tok if not fo(t[i])])
    after = lambda t, i: i > 0 and t[i - 1] in R.NUMS
    rd.gtl('FO2', 'they are counted', 'after a numeral, formula-only tokens', [after(t, i) for t, i in tok if fo(t[i])],
           [after(t, i) for t, i in tok if not fo(t[i])])
    tc = Counter(g for t in AB for g in t)
    shared = sorted({t[i] for t, i in tok if not fo(t[i])})
    rd.rank('FO3', 'they are rare', 'shared against formula-only signs', [tc[g] for g in shared], [tc[g] for g in only])
    has = lambda ln: any(g not in R.NUMS and g not in bsig for g in ln)
    items = [(has(ln), R.lstrat(len(ln)), 0 if r['type'].startswith('SEAL') else 1) for r in F for ln in r['seq'] if nonname(ln)]
    rd.strat('FO4', 'they are off the seals', 'off seals, formulas with a formula-only sign', items)
    fc = Counter(g for r in F for ln in r['seq'] for g in ln)
    fsites = defaultdict(set)
    for r in F:
        for ln in r['seq']:
            for g in ln:
                fsites[g].add(r['site'].strip())
    mid = [g for g in fc if 2 <= fc[g] <= 5 and g not in R.NUMS]
    rd.gtl('FO5', 'they are local', 'one site, formula-only signs with 2-5 tokens', [len(fsites[g]) == 1 for g in mid if g not in bsig],
           [len(fsites[g]) == 1 for g in mid if g in bsig])
    rd.rank('FO6', 'their formulas are short', 'other against formula-only formulas', [len(t) for t in fm if not has(t)],
            [len(t) for t in fm if has(t)])
    ftok = [(r['type'], g) for r in F for ln in r['seq'] if nonname(ln) for g in ln if g not in R.NUMS]
    oth = lambda ty: not ty.startswith(('SEAL', 'TAB'))
    rd.gtl('FO7', 'they are on other objects', 'other objects, formula-only tokens', [oth(ty) for ty, g in ftok if g not in bsig],
           [oth(ty) for ty, g in ftok if g in bsig])
    bA = {g for b, _ in T.names(A) for g in b}
    bB = {g for b, _ in T.names(B) for g in b}
    onlyA = {g for t in A if nonname(t) for g in t if g not in R.NUMS and g not in bA}
    inB = {g for t in B for g in t}
    k = [g not in bB for g in onlyA if g in inB]
    rd.thr('FO8', 'the class holds in the other transcription', 'A formula-only signs absent from B name bodies', sum(k), len(k), 0.8)
    pre = lambda t, i: i > 0 and t[i - 1] in HEAD
    rd.gtl('FO9', 'they follow a heading', 'after a heading, formula-only tokens', [pre(t, i) for t, i in tok if fo(t[i])],
           [pre(t, i) for t, i in tok if not fo(t[i])])
    num = lambda t: any(g in R.NUMS for g in t)
    rd.gtl('FO10', 'they label rather than count', 'no numeral, formulas with a formula-only sign', [not num(t) for t in fm if has(t)],
           [not num(t) for t in fm if not has(t)])
    rd.finish()


if __name__ == '__main__':
    main()
