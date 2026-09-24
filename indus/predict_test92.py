"""Ninety-second registered prediction set (PREDICTIONS.md, CF1-CF20): the jar signs 700, 705, 706. Writes
results/predict_test92.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test62 import sims
from predict_test63 import body_span

random.seed(112)
J = ('705', '706')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    cat = R.cat_of()
    rd = R.Round('Ninety-second registered predictions: the jar signs 700, 705, 706', 'predict_test92')
    DL = sorted({tuple(t) for t in AB})
    tc, S, C = sims(AB, 5)
    q = T.quintiles(tc, S)
    byq = defaultdict(list)
    for s in S:
        byq[q[s]].append(s)
    rd.say('- tokens: 700 %d, 705 %d, 706 %d; context signs %d.' % (tc['700'], tc['705'], tc['706'], len(S)))
    rd.say()
    obs = C[('705', '706')]
    ge = 0
    for _ in range(R.N):
        a = random.choice(byq[q['705']])
        b = random.choice(byq[q['706']])
        while b == a:
            b = random.choice(byq[q['706']])
        ge += C[(a, b)] >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('CF1', '705 and 706 keep one company', 'cosine %.3f; p = %.4f' % (obs, p), p < 0.05)
    obs = (C[('700', '705')] + C[('700', '706')]) / 2
    ge = 0
    for _ in range(R.N):
        x = random.choice([s for s in byq[q['700']] if s not in J])
        ge += (C[(x, '705')] + C[(x, '706')]) / 2 >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('CF2', '700 keeps jar company', 'mean cosine 700 to 705/706 %.3f; p = %.4f' % (obs, p), p < 0.05)

    def tok(lines, s):
        return [(t, i) for t in lines for i in range(len(t)) if t[i] in s]

    def cf3(lines, key, lab):
        tk = tok(lines, J)
        rd.thr(key, 'jars are followed by a number%s' % lab, '705/706 tokens followed by a numeral', sum(i + 1 < len(t) and t[i + 1] in R.NUMS for t, i in tk), len(tk), 0.5)

    def cf4(lines, key, lab):
        nx = [t[i + 1] for t, i in tok(lines, J) if i + 1 < len(t) and t[i + 1] in R.NUMS]
        rd.thr(key, 'the number is 33%s' % lab, 'numerals after 705/706 that are 33 (%s)' % dict(Counter(nx).most_common(4)), sum(g == '33' for g in nx), len(nx), 0.6)
    cf3(DL, 'CF3', '')
    cf4(DL, 'CF4', '')
    after = [(t[i - 1] in J, R.kind(t[i]) == 'long') for t in DL for i in range(1, len(t)) if t[i] in R.NUMS and t[i - 1] not in R.NUMS]
    rd.gtl('CF5', 'jars take long strokes', 'long kind, after 705/706', [k for j, k in after if j], [k for j, k in after if not j])
    tk = tok(DL, J)
    rd.thr('CF6', 'jars are not counted', '705/706 tokens after a numeral', sum(i > 0 and t[i - 1] in R.NUMS for t, i in tk), len(tk), 0.1, above=False)
    jl = [t for t in DL if any(g in J for g in t)]
    rd.thr('CF7', 'jar lines end in 520', '705/706 lines ending in 520', sum(t[-1] == '520' for t in jl), len(jl), 0.5)
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in F for ln in r['seq'] if ln})
    fj = [(s, ty) for s, ty, t in FD if any(g in J for g in t)]
    rd.thr('CF8', 'jar lines are on seals', '705/706 lines on seals', sum(ty == 'SEA' for s, ty in fj), len(fj), 0.7)
    rd.gtl('CF9', 'jars are Mohenjo-daran', '705/706 lines, Mohenjo-daro', [any(g in J for g in t) for s, ty, t in FD if s == 'Mohenjo-daro'],
           [any(g in J for g in t) for s, ty, t in FD if s == 'Harappa'])
    f7 = [ty for s, ty, t in FD if '700' in t]
    rd.thr('CF10', '700 lines are on tablets', '700 lines on tablets', sum(ty == 'TAB' for ty in f7), len(f7), 0.8)
    bj = [(t[i - 1], t[i]) for t, i in tk if i > 0]
    o, p = R.mi_perm([a for a, _ in bj], [b for _, b in bj])
    rd.rec('CF11', '705 and 706 are free variants', 'tokens with a sign before %d; MI %.3f; p = %.4f' % (len(bj), o, p), p >= 0.05)
    n2 = [t[i + 2] for t, i in tk if i + 2 < len(t) and t[i + 1] in R.NUMS]
    rd.thr('CF12', 'the jar count ends in 520', "sign after '705/706 + numeral' is 520", sum(g == '520' for g in n2), len(n2), 0.5)

    def cf13(lines, key, lab):
        v = [R.NUMS[t[i + 1]][0] for t, i in tok(lines, J) if i + 2 < len(t) and t[i + 1] in R.NUMS and t[i + 2] == '520']
        rd.thr(key, 'the jar count is three%s' % lab, "value 3 in '705/706 N 520' (%s)" % dict(Counter(v)), sum(x == 3 for x in v), len(v), 0.8)
    cf13(DL, 'CF13', '')
    rd.thr('CF14', 'jar lines are names', '705/706 name lines', sum(bool(R.name_of(list(t))) for t in jl), len(jl), 0.6)
    t7 = tok(DL, ('700',))
    ins = lambda t, i: bool(body_span(list(t))) and body_span(list(t))[0] <= i < body_span(list(t))[1]
    rd.thr('CF15', '700 is never a name sign', '700 tokens inside a name body', sum(ins(t, i) for t, i in t7), len(t7), 0.05, above=False)
    b33 = [t[i - 1] for t in DL for i in range(1, len(t)) if t[i] == '33' and t[i - 1] not in R.NUMS]
    rd.thr('CF16', '33 belongs to the jars', 'signs before 33 that are 705/706 (%s)' % dict(Counter(b33).most_common(5)), sum(g in J for g in b33), len(b33), 0.3)
    DB = sorted({tuple(t) for t in B})
    cf3(DB, 'CF17', ' (B)')
    cf4(DB, 'CF18', ' (B)')
    cf13(sorted({tuple(ln) for r in F for ln in r['seq'] if ln}), 'CF19', ' (F)')
    rd.rec('CF20', 'the jars look alike', 'categories 700 %s, 705 %s, 706 %s' % (cat.get('700'), cat.get('705'), cat.get('706')),
           cat.get('700') is not None and cat.get('705') == cat.get('700') == cat.get('706'))
    rd.finish()


if __name__ == '__main__':
    main()
