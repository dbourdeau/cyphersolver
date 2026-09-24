"""Hundred-and-eighty-fourth registered prediction set (PREDICTIONS.md, CG1-CG7): decipherment loop 9, is the cage (four
small strokes around a sign) a grammatical affix? Writes results/predict_test184.md."""
import math
import random
from collections import Counter, defaultdict

import rtools as R
from signs import load

random.seed(244)
PAIRS = [('226', ('220',)), ('232', ('231',)), ('153', ('231',)), ('236', ('235',)), ('241', ('240',)), ('144', ('142',)),
         ('393', ('390', '392', '405', '406', '407', '409', '48', '64')), ('895', ('892',)),
         ('466', ('465', '467', '468', '471', '472', '474')), ('804', ('803', '838')), ('878', ('877',)), ('689', ('71',))]
FISHC = {'226', '232', '153', '236', '241'}
CAGED = {c for c, b in PAIRS}
BASE = {x for c, b in PAIRS for x in b}


def final(t, i):
    return all(g in ('400', '90') for g in t[i + 1:])


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-eighty-fourth registered predictions: decipherment loop 9, is the cage a grammatical affix?', 'predict_test184')
    DL = sorted({tuple(t) for t in A + B})
    tok = lambda lines, S: [(t, i) for t in lines for i, g in enumerate(t) if g in S]
    ct, bt = tok(DL, CAGED), tok(DL, BASE)
    rd.say('- caged tokens %d (%s); base tokens %d.' % (len(ct), dict(Counter(t[i] for t, i in ct)), len(bt)))
    rd.say()
    rd.gtl('CG1', 'caged signs end lines', 'final, caged', [final(t, i) for t, i in ct], [final(t, i) for t, i in bt])
    nxt = lambda t, i: i + 1 < len(t) and t[i + 1] in R.END
    rd.ltl('CG2', 'the cage takes the place of the ending', 'followed by 740 / 520, caged', [nxt(t, i) for t, i in ct], [nxt(t, i) for t, i in bt])
    nf_c = tok(DL, CAGED - FISHC)
    nf_b = tok(DL, {x for c, b in PAIRS if c not in FISHC for x in b})
    rd.gtl('CG3', 'not only the fish', 'final, non-fish caged (%d tokens)' % len(nf_c), [final(t, i) for t, i in nf_c], [final(t, i) for t, i in nf_b])
    prev = defaultdict(Counter)
    for t in DL:
        for i in range(1, len(t)):
            prev[t[i]][t[i - 1]] += 1
    tc = Counter(g for t in DL for g in t)

    def cos(a, b):
        va, vb = prev[a], prev[b]
        num = sum(va[k] * vb[k] for k in va)
        den = math.sqrt(sum(v * v for v in va.values())) * math.sqrt(sum(v * v for v in vb.values()))
        return num / den if den else 0.0
    cp = []
    for c, bs in PAIRS:
        if prev[c]:
            bmax = max(bs, key=lambda x: tc[x])
            cp.append(cos(c, bmax))
    obs = sum(cp) / len(cp)
    signs = [g for g in tc if prev[g]]
    rnd = []
    for _ in range(1000):
        v = []
        for c, bs in PAIRS:
            if prev[c]:
                v.append(cos(c, random.choice(signs)))
        rnd.append(sum(v) / len(v))
    p = (sum(x >= obs for x in rnd) + 1) / 1001
    rd.rec('CG4', 'caged and base share their stems', 'mean cosine %.3f over %d pairs; random partners %.3f; p = %.4f' % (obs, len(cp), sum(rnd) / len(rnd), p), p < 0.05)
    Bl = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    cB, bB = tok(Bl, CAGED), tok(Bl, BASE)
    rd.gtl('CG5', 'CG1 on B', 'final, caged (B, %d tokens)' % len(cB), [final(t, i) for t, i in cB], [final(t, i) for t, i in bB])
    closer = [final(t, i) and not any(g in R.END for g in t[i + 1:]) for t, i in ct]
    rd.thr('CG6', 'caged signs are closers', 'caged tokens final with no ending after them', sum(closer), len(closer), 0.6)
    rd.finish()


if __name__ == '__main__':
    main()
