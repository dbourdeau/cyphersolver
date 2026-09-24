"""Ninety-third registered prediction set (PREDICTIONS.md, FZ1-FZ20): frozen numbers and real counts. Writes
results/predict_test93.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname

random.seed(113)
HEAD = ('817', '820', '861')


def pairs_of(lines):
    """[(line, run start j, sign index i, value, kind, sign)]"""
    out = []
    for t in lines:
        for i in range(1, len(t)):
            if t[i] not in R.NUMS and t[i - 1] in R.NUMS:
                j = i - 1
                while j > 0 and t[j - 1] in R.NUMS:
                    j -= 1
                out.append((t, j, i, sum(R.NUMS[g][0] for g in t[j:i]), R.kind(t[i - 1]), t[i]))
    return out


def shares(P, k=5):
    vc = defaultdict(Counter)
    for t, j, i, v, kd, s in P:
        vc[s][v] += 1
    return {s: (c.most_common(1)[0][1] / sum(c.values()), c.most_common(1)[0][0]) for s, c in vc.items() if sum(c.values()) >= k}, vc


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Ninety-third registered predictions: frozen numbers and real counts', 'predict_test93')
    DL = sorted({tuple(t) for t in AB})
    P = pairs_of(DL)
    sh, vc = shares(P)
    fr = {s for s, (x, v) in sh.items() if x >= 0.9}
    va = {s for s, (x, v) in sh.items() if x < 0.6}
    rd.say('- signs counted 5+ times %d; frozen %d (%s); variable %d.' % (len(sh), len(fr), ', '.join('%s=%d' % (s, sh[s][1]) for s in sorted(fr)), len(va)))
    rd.say()
    rd.thr('FZ1', 'some counts are frozen', 'frozen signs', len(fr), len(sh), 0.2)
    Pf = [x for x in P if x[5] in fr]
    Pv = [x for x in P if x[5] in va]
    isn = lambda t: bool(R.name_of(list(t)))
    rd.gtl('FZ2', 'frozen counts are in names', 'name lines, frozen', [isn(x[0]) for x in Pf], [isn(x[0]) for x in Pv])
    rd.gtl('FZ3', 'frozen counts use long strokes', 'long kind, frozen', [x[4] == 'long' for x in Pf], [x[4] == 'long' for x in Pv])
    tok = Counter(g for t in DL for g in t)
    cnt = Counter(x[5] for x in P)
    rd.rank('FZ4', 'frozen signs are always counted', 'frozen against variable counted share', [cnt[s] / tok[s] for s in fr], [cnt[s] / tok[s] for s in va])
    ne = lambda x: x[2] + 1 < len(x[0]) and x[0][x[2] + 1] in R.END
    rd.gtl('FZ5', 'frozen counts close names', 'ending next, frozen', [ne(x) for x in Pf], [ne(x) for x in Pv])
    rd.gtl('FZ6', 'variable counts are in formulas', 'formula, variable', [nonname(list(x[0])) for x in Pv], [nonname(list(x[0])) for x in Pf])
    rd.gtl('FZ7', 'variable counts close lines', 'line-final, variable', [x[2] == len(x[0]) - 1 for x in Pv], [x[2] == len(x[0]) - 1 for x in Pf])
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in F for ln in r['seq'] if ln})
    fp = [(s, ty, x[5]) for s, ty, t in FD for x in pairs_of([t])]
    rd.gtl('FZ8', 'frozen counts are Mohenjo-daran', 'Mohenjo-daro, frozen', [s == 'Mohenjo-daro' for s, ty, g in fp if g in fr and s in ('Mohenjo-daro', 'Harappa')],
           [s == 'Mohenjo-daro' for s, ty, g in fp if g in va and s in ('Mohenjo-daro', 'Harappa')])
    rd.gtl('FZ9', 'variable counts are on tablets', 'tablet, variable', [ty == 'TAB' for s, ty, g in fp if g in va], [ty == 'TAB' for s, ty, g in fp if g in fr])
    shB, vcB = shares(pairs_of(sorted({tuple(t) for t in B})), 3)
    fb = [s for s in fr if s in vcB]
    rd.thr('FZ10', 'frozen values hold in B', 'frozen signs with the same value in B', sum(vcB[s].most_common(1)[0][0] == sh[s][1] for s in fb), len(fb), 0.9)
    rd.gtl('FZ11', 'frozen counts are three', 'value 3, frozen signs', [sh[s][1] == 3 for s in fr], [sh[s][1] == 3 for s in va])
    lc = Counter((x[3], x[5]) for x in P)
    rd.gtl('FZ12', 'frozen counts recur', 'in 2+ lines, frozen pairs', [lc[(x[3], x[5])] >= 2 for x in Pf], [lc[(x[3], x[5])] >= 2 for x in Pv])
    pb = lambda x: x[1] > 0 and x[0][x[1] - 1] in HEAD
    rd.ltl('FZ13', 'frozen counts are not headed', 'heading before, frozen', [pb(x) for x in Pf], [pb(x) for x in Pv])
    pn = lambda x: x[1] > 0
    rd.gtl('FZ14', 'frozen counts stand inside', 'sign before the numeral, frozen', [pn(x) for x in Pf], [pn(x) for x in Pv])
    kk = defaultdict(Counter)
    for x in P:
        kk[x[5]][x[4]] += 1
    ks = [(kk[s].most_common(1)[0][0], s in fr) for s in sh]
    rd.mi('FZ15', 'the notation marks frozen counts', 'signs', [a for a, _ in ks], [b for _, b in ks])
    rd.rank('FZ16', 'long-stroke signs are frozen', 'long against short signs, value share', [sh[s][0] for s in sh if kk[s].most_common(1)[0][0] == 'long'],
            [sh[s][0] for s in sh if kk[s].most_common(1)[0][0] == 'short'])
    rd.rec('FZ17', '700 is a real count', '700 value share %.2f; threshold under 0.6' % sh.get('700', (1, 0))[0], sh.get('700', (1, 0))[0] < 0.6)
    heads = {b[-1] for b, e in T.names(AB) if b}
    rd.gtl('FZ18', 'frozen signs are name heads', 'name head, frozen signs', [s in heads for s in fr], [s in heads for s in va])
    DB = sorted({tuple(t) for t in B})
    PB = pairs_of(DB)
    rd.gtl('FZ19', 'frozen counts are in names (B)', 'name lines, frozen', [isn(x[0]) for x in PB if x[5] in fr], [isn(x[0]) for x in PB if x[5] in va])
    shF, vcF = shares(pairs_of(sorted({tuple(ln) for r in F for ln in r['seq'] if ln})))
    rd.thr('FZ20', 'some counts are frozen (F)', 'frozen signs', sum(x >= 0.9 for x, v in shF.values()), len(shF), 0.2)
    rd.finish()


if __name__ == '__main__':
    main()
