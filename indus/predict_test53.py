"""Fifty-third registered prediction set (PREDICTIONS.md, EN1-EN10): how predictable each genre is. Writes
results/predict_test53.md."""
import math
import random
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test44 import nonname
from predict_test50 import ent

random.seed(73)


def rate(lines):
    c = Counter()
    for t in lines:
        c.update(set(zip(t, t[1:])))
    tok = [p for t in lines for p in zip(t, t[1:])]
    return sum(c[p] >= 2 for p in tok) / max(1, len(tok))


def slope(lines):
    c = sorted(Counter(g for t in lines for g in t).values(), reverse=True)[:50]
    xs = [math.log(i + 1) for i in range(len(c))]
    ys = [math.log(v) for v in c]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def lab_perm(L1, L2, stat, n):
    """p for stat(L1, L2) >= observed under shuffled labels."""
    obs = stat(L1, L2)
    al = L1 + L2
    ge = 0
    for _ in range(n):
        random.shuffle(al)
        ge += stat(al[:len(L1)], al[len(L1):]) >= obs
    return obs, (ge + 1) / (n + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Fifty-third registered predictions: how predictable each genre is', 'predict_test53')
    fm = [t for t in AB if nonname(t)]
    nl = [t for t in AB if R.name_of(t)]
    rdiff = lambda a, b: rate(a) - rate(b)
    o, p = lab_perm(fm, nl, rdiff, R.N // 10)
    rd.rec('EN1', 'formulas repeat', 'repeat rate formulas %.3f, names %.3f; p = %.4f (1,000 shuffles)' % (rate(fm), rate(nl), p), o > 0 and p < 0.05)
    tf = [g for t in fm for g in t]
    tn = [g for t in nl for g in t]
    m = min(len(tf), len(tn))
    wins = sum(len(set(random.sample(tf, m))) < len(set(random.sample(tn, m))) for _ in range(1000))
    rd.rec('EN2', 'formulas use fewer signs', 'tokens per subsample %d; formulas fewer in %d of 1,000' % (m, wins), wins >= 950)
    tc = Counter(g for t in AB for g in t)
    rd.gtl('EN3', 'rare signs are in names', 'once-attested signs, name-line tokens', [tc[g] == 1 for g in tn], [tc[g] == 1 for g in tf])
    o, p = lab_perm([t[0] for t in nl], [t[0] for t in fm], lambda a, b: ent(a) - ent(b), R.N)
    rd.rec('EN4', 'names start more freely', 'first-sign entropy difference %+.3f bits; p = %.4f' % (o, p), o > 0 and p < 0.05)
    hb = [R.name_of(t)[0][-1] for t in nl if R.name_of(t)[0]]
    o, p = lab_perm([t[-1] for t in fm], hb, lambda a, b: ent(a) - ent(b), R.N)
    rd.rec('EN5', 'names close on fewer signs', 'formula minus name-head entropy %+.3f bits; p = %.4f' % (o, p), o > 0 and p < 0.05)
    fl = lambda cond: [ln for r in F if cond(r) for ln in r['seq'] if len(ln) >= 2]
    h, md = fl(lambda r: r['site'].strip() == 'Harappa'), fl(lambda r: r['site'].strip() == 'Mohenjo-daro')
    o, p = lab_perm(h, md, rdiff, R.N // 10)
    rd.rec('EN6', 'Harappa is more formulaic', 'repeat rate Harappa %.3f, Mohenjo-daro %.3f; p = %.4f (1,000 shuffles)' % (rate(h), rate(md), p), o > 0 and p < 0.05)
    tb, sl = fl(lambda r: r['type'].startswith('TAB')), fl(lambda r: r['type'].startswith('SEAL'))
    o, p = lab_perm(tb, sl, rdiff, R.N // 10)
    rd.rec('EN7', 'tablets are more formulaic', 'repeat rate tablets %.3f, seals %.3f; p = %.4f (1,000 shuffles)' % (rate(tb), rate(sl), p), o > 0 and p < 0.05)
    o, p = lab_perm(nl, fm, lambda a, b: slope(a) - slope(b), R.N // 10)
    rd.rec('EN8', 'formulas are more skewed', 'slopes names %.2f, formulas %.2f; p = %.4f (1,000 shuffles)' % (slope(nl), slope(fm), p), o > 0 and p < 0.05)
    lines = [(r['site'].strip(), ln) for r in F if r['site'].strip() in ('Harappa', 'Mohenjo-daro') for ln in r['seq']]
    nlF = [(s, ln) for s, ln in lines if R.name_of(ln)]
    fmF = [(s, ln) for s, ln in lines if nonname(ln)]

    def jac(L):
        a = {g for s, ln in L if s == 'Harappa' for g in ln}
        b = {g for s, ln in L if s == 'Mohenjo-daro' for g in ln}
        return len(a & b) / len(a | b)
    o, p = lab_perm(nlF, fmF, lambda a, b: jac(a) - jac(b), R.N)
    rd.rec('EN9', 'names share signs across cities', 'Jaccard names %.3f, formulas %.3f; p = %.4f' % (jac(nlF), jac(fmF), p), o > 0 and p < 0.05)
    lg, sh = [t for t in AB if len(t) >= 8], [t for t in AB if 3 <= len(t) <= 5]
    o, p = lab_perm(sh, lg, rdiff, R.N // 10)
    rd.rec('EN10', 'long lines are less formulaic', 'repeat rate 3-5 signs %.3f, 8+ signs %.3f; p = %.4f (1,000 shuffles)' % (rate(sh), rate(lg), p), o > 0 and p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
