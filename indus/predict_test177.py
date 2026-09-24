"""Hundred-and-seventy-seventh registered prediction set (PREDICTIONS.md, VP1-VP8): decipherment loop 2. A variable-order
(Witten-Bell, order 1-5) model for S, the provisional picture anchors 347 and 460 on objects not used to propose them
for M, and head / modifier roles for bare lines for R. Writes results/predict_test177.md."""
import math
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test108 import genre
from predict_test176 import M3, em, xent
from progress import data, roles


class WB:
    def __init__(self, train, order=5):
        self.n = order
        self.c = defaultdict(Counter)
        self.vocab = {g for t in train for g in t} | {'</s>'}
        for t in train:
            s = ['<s>'] * (order - 1) + list(t) + ['</s>']
            for i in range(order - 1, len(s)):
                for k in range(order):
                    self.c[tuple(s[i - k:i])][s[i]] += 1
        self.V = len(self.vocab) + 1

    def p(self, ctx, w):
        if not ctx:
            c = self.c[()]
            n, t = sum(c.values()), len(c)
            return (c[w] + t / self.V) / (n + t)
        lower = self.p(ctx[1:], w)
        c = self.c.get(ctx)
        if not c:
            return lower
        n, t = sum(c.values()), len(c)
        return (c[w] + t * lower) / (n + t)

    def probs(self, t):
        s = ['<s>'] * (self.n - 1) + list(t) + ['</s>']
        return [self.p(tuple(s[i - self.n + 1:i]), s[i]) for i in range(self.n - 1, len(s))]


def bits(model, lines):
    ps = [p for t in lines for p in model.probs(t)]
    return sum(-math.log2(max(p, 1e-12)) for p in ps) / len(ps)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-seventy-seventh registered predictions: decipherment loop 2', 'predict_test177')
    DL, tr, te = data()
    wb = WB(tr)
    s_wb = bits(wb, te)
    base = 4.712
    rd.rec('VP1', 'a variable-order model alone', 'Witten-Bell order 5: %.3f bits against %.3f' % (s_wb, base), base - s_wb >= 0.05)
    rnd = random.Random(11)
    ls = list(tr)
    rnd.shuffle(ls)
    k = int(0.8 * len(ls))
    mdev, wdev = M3(ls[:k]), WB(ls[:k])
    rows = []
    for t in ls[k:]:
        rr = mdev.rows(t, True)
        for r, p in zip(rr, wdev.probs(t)):
            r['vo'] = p
        rows += rr
    keys = ['tri', 'pos', 'end', 'vo']
    w = em(rows, keys)
    m = M3(tr)
    trows = []
    for t in te:
        rr = m.rows(t, True)
        for r, p in zip(rr, wb.probs(t)):
            r['vo'] = p
        trows += rr
    s_mix = xent(trows, w)
    rd.rec('VP2', 'the variable-order model in the mixture', '%.3f against %.3f (weights %s)' % (s_mix, base, ', '.join('%s %.2f' % kv for kv in w.items())), base - s_mix >= 0.05)
    wbr = WB([t[::-1] for t in tr])
    s_rev = bits(wbr, [t[::-1] for t in te])
    rd.rec('VP3', 'forwards is easier than backwards', 'forwards %.3f, backwards %.3f' % (s_wb, s_rev), s_rev - s_wb >= 0.05)
    Acisi = {r['cisi'].strip() for r in rowsA}
    new = [r for r in F if recs[r['sealid']][1].strip() not in Acisi]
    mot = lambda r: {recs[r['sealid']][18].strip(), recs[r['sealid']][19].strip()}
    res = []
    for key, sign, codes, lab in (('VP4', '347', {'Mult'}, 'multi-headed animal'), ('VP5', '460', {'Phyt', 'Pipal', 'Plant'}, 'tree / plant')):
        objs = [r for r in new if sign in r['flat']]
        hit = sum(bool(mot(r) & codes) for r in objs)
        res.append((hit, len(objs)))
        rd.thr(key, 'anchor %s = %s' % (sign, lab), 'new objects with %s carrying the picture (%s)' % (sign, '; '.join(sorted({'/'.join(sorted(mot(r))) for r in objs}))[:200]), hit, len(objs), 0.5)
    ok = any(n >= 3 and h / n >= 0.5 for h, n in res)
    rd.rec('VP6', 'an anchor can be added', 'VP4 %d/%d, VP5 %d/%d; needs 3+ objects and 50%%+' % (res[0][0], res[0][1], res[1][0], res[1][1]), ok)
    heads = {R.name_of(list(t))[0][-1] for t in DL if R.name_of(list(t)) and R.name_of(list(t))[0]}
    bare = [t for t in DL if len(t) >= 2 and genre(t) == 'bare']
    rd.thr('VP7', 'bare lines end in a name head', 'bare lines whose last sign is a known head', sum(t[-1] in heads for t in bare), len(bare), 0.5)
    r0, by0, tot = roles(DL)
    add = 0
    for t in bare:
        known = {i for i, g in enumerate(t) if g in R.NUMS}
        add += sum(1 for i in range(len(t)) if i not in known)
    rd.rec('VP8', 'bare-line roles raise R', 'R %.1f%% -> %.1f%% (+%d tokens, numerals excluded)' % (100 * r0, 100 * (r0 + add / tot), add), add / tot >= 0.03)
    rd.finish()


if __name__ == '__main__':
    main()
