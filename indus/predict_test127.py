"""Hundred-and-twenty-seventh registered prediction set (PREDICTIONS.md, RA1-RA10): the rare signs. Writes
results/predict_test127.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test102 import blk
from predict_test103 import CL

random.seed(147)
CITY = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-twenty-seventh registered predictions: the rare signs', 'predict_test127')
    DL = sorted({tuple(t) for t in AB})

    def setup(lines):
        tc = Counter(g for t in lines for g in t)
        rare = {g for g in tc if 1 <= tc[g] <= 3 and g not in R.NUMS and g.isdigit()}
        common = {g for g in tc if tc[g] >= 20 and g not in R.NUMS and g.isdigit()}
        fr = defaultdict(set)
        for t in lines:
            s = ['#'] + list(t) + ['#']
            for i in range(1, len(s) - 1):
                if s[i] in common:
                    fr[(s[i - 1], s[i + 1])].add(s[i])
        return tc, rare, common, fr
    tc, rare, common, fr = setup(DL)
    rd.say('- rare signs %d, common signs %d.' % (len(rare), len(common)))
    rd.say()

    def mates(lines, rare_, fr_):
        out = []
        for t in lines:
            s = ['#'] + list(t) + ['#']
            for i in range(1, len(s) - 1):
                if s[i] in rare_:
                    for m in fr_[(s[i - 1], s[i + 1])]:
                        out.append((s[i], m))
        return out

    def ra1(lines, key, lab, test):
        tc_, rare_, common_, fr_ = setup(lines)
        mt = mates(lines, rare_, fr_)
        cl = sorted(common_)
        obs = sum(test(r, m) for r, m in mt)
        ge = sum(sum(test(r, random.choice(cl)) for r, m in mt) >= obs for _ in range(R.N))
        p = (ge + 1) / (R.N + 1)
        rd.rec(key, 'rare signs substitute for their shape family%s' % lab, 'mate pairs %d; matching %d; p = %.4f' % (len(mt), obs, p), p < 0.05)
    sameblk = lambda r, m: blk(r) == blk(m)
    near = lambda r, m: abs(int(r) - int(m)) <= 10
    ra1(DL, 'RA1', '', sameblk)
    ra1(DL, 'RA2', ' (catalogue number within 10)', near)
    tk = [(t, i) for t in DL for i in range(len(t))]
    med = lambda t, i: 0 < i < len(t) - 1
    rd.gtl('RA3', 'rare signs sit inside', 'medial, rare tokens', [med(t, i) for t, i in tk if t[i] in rare], [med(t, i) for t, i in tk if t[i] in common])

    def ra4(lines, rare_, key, lab):
        f = lambda t: sum(1 for x, y in zip(t, t[1:]) if x in rare_ and y in rare_)
        obs = sum(map(f, lines))
        ge = 0
        for _ in range(R.N // 10):
            k = 0
            for t in lines:
                s = list(t)
                random.shuffle(s)
                k += f(s)
            ge += k >= obs
        p = (ge + 1) / (R.N // 10 + 1)
        rd.rec(key, 'rare signs cluster%s' % lab, 'rare-rare adjacencies %d; p = %.4f (1,000 shuffles)' % (obs, p), p < 0.05)
    ra4(DL, rare, 'RA4', '')
    hr = lambda t: any(g in rare for g in t)
    rd.rank('RA5', 'rare signs are in long lines', 'with against without a rare sign', [len(t) for t in DL if hr(t)], [len(t) for t in DL if not hr(t)])
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FD = sorted({(r['site'].strip(), tuple(ln)) for r in Fn for ln in r['seq'] if ln})
    ft = [(s, g) for s, t in FD if s in CITY for g in t]
    rd.gtl('RA6', 'rare signs are Mohenjo-daran', 'Mohenjo-daro, rare tokens', [s == 'Mohenjo-daro' for s, g in ft if g in rare], [s == 'Mohenjo-daro' for s, g in ft if g in common])
    cn = {int(g) for g in common}
    rd.thr('RA7', 'rare signs are catalogue neighbours of common ones', 'rare signs with a common sign at number +/- 1', sum((int(g) - 1) in cn or (int(g) + 1) in cn for g in rare), len(rare), 0.5)
    endslot = lambda t, i: t[i] in CL or (i + 1 < len(t) and t[i + 1] in R.END and i + 2 >= len(t) - 1)
    rt = [(t, i) for t, i in tk if t[i] in rare]
    rd.thr('RA8', 'rare signs avoid the ending slot', 'rare tokens in the ending slot', sum(endslot(t, i) for t, i in rt), len(rt), 0.05, above=False)
    ra1(sorted({tuple(t) for t in B}), 'RA9', ' (B)', sameblk)
    FL = sorted({t for s, t in FD})
    tcF = Counter(g for t in FL for g in t)
    rareF = {g for g in tcF if 1 <= tcF[g] <= 3 and g not in R.NUMS and g.isdigit()}
    ra4(FL, rareF, 'RA10', " (F')")
    rd.finish()


if __name__ == '__main__':
    main()
