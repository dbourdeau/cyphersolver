"""Forty-third registered prediction set (PREDICTIONS.md, SK1-SK10): the slot ranking. Writes
results/predict_test43.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R

random.seed(63)


def ranks(ns, k=5):
    pos = defaultdict(list)
    for b, _ in ns:
        if len(b) >= 2:
            for i, g in enumerate(b):
                pos[g].append(i / (len(b) - 1))
    return {g: round(sum(v) / len(v), 2) for g, v in pos.items() if len(v) >= k}


def follow(ns, rk):
    out = []
    for b, _ in ns:
        for x, y in zip(b, b[1:]):
            if x in rk and y in rk and rk[x] != rk[y]:
                out.append(rk[x] < rk[y])
    return out


def sp_perm(a, b, n=R.N):
    obs = T.spearman(a, b)
    bb = list(b)
    ge = 0
    for _ in range(n):
        random.shuffle(bb)
        ge += T.spearman(a, bb) >= obs
    return obs, (ge + 1) / (n + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    cat = R.cat_of()
    rd = R.Round('Forty-third registered predictions: the slot ranking', 'predict_test43')
    nsAB = set(T.names(AB))
    rk = ranks(nsAB)
    rd.say('- ranked signs %d.' % len(rk))
    rd.say()
    f = follow(set(T.names(B)), ranks(set(T.names(A))))
    rd.thr('SK1', 'A ranks predict B', 'adjacent pairs in B following A ranks', sum(f), len(f), 0.85)
    fn = lambda cond: {nm for r in F if cond(r) for nm in R.names_in(r)}
    f = follow(fn(lambda r: r['site'].strip() == 'Harappa'), ranks(fn(lambda r: r['site'].strip() == 'Mohenjo-daro')))
    rd.thr('SK2', 'Mohenjo-daro ranks predict Harappa', 'adjacent pairs at Harappa following Mohenjo-daro ranks', sum(f), len(f), 0.8)
    seal = lambda r: r['type'].startswith('SEAL')
    f = follow(fn(lambda r: not seal(r)), ranks(fn(seal)))
    rd.thr('SK3', 'seal ranks predict other objects', 'adjacent pairs off seals following seal ranks', sum(f), len(f), 0.75)
    sg = sorted((g for g in rk if g in cat), key=lambda g: rk[g])
    ter = {g: 3 * i // len(sg) for i, g in enumerate(sg)}
    rd.mi('SK4', 'the rank goes with the category', 'ranked signs with a category', [cat[g] for g in sg], [ter[g] for g in sg])
    num, oth = [], []
    for b, _ in nsAB:
        if len(b) >= 3:
            for i, g in enumerate(b):
                (num if g in R.NUMS else oth).append(i / (len(b) - 1))
    rd.rank('SK5', 'numerals come early', 'other signs against numerals', oth, num)
    tok = Counter(g for b, _ in nsAB for g in b)
    gs = sorted(rk)
    o, p = sp_perm([tok[g] for g in gs], [rk[g] for g in gs])
    rd.rec('SK6', 'frequent signs rank later', 'signs %d; Spearman %.3f; p = %.4f' % (len(gs), o, p), o > 0 and p < 0.05)
    cnt = Counter(T.names(AB))
    inv = lambda b: any(x in rk and y in rk and rk[x] - rk[y] >= 0.2 for x, y in zip(b, b[1:]))
    a = [cnt[nm] == 1 for nm in nsAB if len(nm[0]) >= 2 and inv(nm[0])]
    c = [cnt[nm] == 1 for nm in nsAB if len(nm[0]) >= 2 and not inv(nm[0])]
    rd.gtl('SK7', 'inversions are rare names', 'attested once, bodies with an inversion', a, c)
    r3 = ranks({nm for nm in nsAB if len(nm[0]) == 3}, 3)
    r4 = ranks({nm for nm in nsAB if len(nm[0]) >= 4}, 3)
    gs = sorted(set(r3) & set(r4))
    o, p = sp_perm([r3[g] for g in gs], [r4[g] for g in gs])
    rd.rec('SK8', 'the rank does not depend on length', 'signs %d (3+ tokens each); Spearman %.3f; p = %.4f' % (len(gs), o, p),
           o >= 0.6 and p < 0.05)
    r7 = ranks({nm for nm in nsAB if nm[1] == '740'})
    r5 = ranks({nm for nm in nsAB if nm[1] == '520'})
    gs = sorted(set(r7) & set(r5))
    o, p = sp_perm([r7[g] for g in gs], [r5[g] for g in gs])
    rd.rec('SK9', 'the rank does not depend on the ending', 'signs %d; Spearman %.3f; p = %.4f' % (len(gs), o, p),
           o >= 0.6 and p < 0.05)
    rF = ranks(fn(lambda r: True))
    fs, fo = follow(fn(seal), rF), follow(fn(lambda r: not seal(r)), rF)
    rd.gtl('SK10', 'seals keep the order best', 'following the ranking, seals', fs, fo)
    rd.finish()


if __name__ == '__main__':
    main()
