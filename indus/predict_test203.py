"""Two-hundred-and-third registered prediction set (PREDICTIONS.md, LO1-LO5): decipherment loop 28, the picture vault
estimated by leave-one-out over text groups and text families (near duplicates together), with and without the
elephant phrase, and over 50 random splits. Writes results/predict_test203.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test200 import objects
from predict_test201 import pairs


def family(t):
    t = list(t)
    while t and t[0] in R.NUMS:
        t = t[1:]
    while t and t[-1] in R.NUMS:
        t = t[:-1]
    return tuple(t)


def build(objs, key):
    groups = defaultdict(list)
    for t, m in objs:
        groups[key(t)].append((t, m))
    return groups


def loo(groups, motifs):
    """motifs: group key -> list of motifs aligned with groups[k]."""
    gp = {k: set().union(*(pairs(t) for t, m in v)) for k, v in groups.items()}
    hits = n = 0
    for k, v in groups.items():
        for (t, _), m in zip(v, motifs[k]):
            p = pairs(t)
            best, ms = 0, []
            for k2, q in gp.items():
                if k2 == k:
                    continue
                s = len(p & q)
                if s > best:
                    best, ms = s, list(motifs[k2])
                elif s == best and s > 0:
                    ms += motifs[k2]
            if best < 1:
                continue
            n += 1
            hits += Counter(ms).most_common(1)[0][0] == m
    return hits, n


def loo_test(groups, perms=500, seed=203):
    real = {k: [m for t, m in v] for k, v in groups.items()}
    h, n = loo(groups, real)
    keys = sorted(groups)
    rnd = random.Random(seed)
    ge = 0
    for _ in range(perms):
        lab = [real[k] for k in keys]
        rnd.shuffle(lab)
        # a shuffled group keeps its size by recycling the donor's motifs
        mot = {k: [lab[i][j % len(lab[i])] for j in range(len(groups[k]))] for i, k in enumerate(keys)}
        h2, n2 = loo(groups, mot)
        ge += h2 / max(1, n2) >= h / max(1, n)
    return h, n, (ge + 1) / (perms + 1)


def split_test(groups, seed, perms=100):
    keys = sorted(groups)
    rnd = random.Random(seed)
    rnd.shuffle(keys)
    d, v = keys[:len(keys) // 2], keys[len(keys) // 2:]
    dp = {k: set().union(*(pairs(t) for t, m in groups[k])) for k in d}

    def acc(mot):
        hits = n = 0
        for k in v:
            for t, m in groups[k]:
                p = pairs(t)
                sc = {k2: len(p & q) for k2, q in dp.items()}
                best = max(sc.values())
                if best < 1:
                    continue
                ms = [x for k2, s in sc.items() if s == best for x in mot[k2]]
                n += 1
                hits += Counter(ms).most_common(1)[0][0] == m
        return hits / max(1, n)
    real = {k: [m for t, m in groups[k]] for k in d}
    a = acc(real)
    nulls = []
    for _ in range(perms):
        lab = [real[k] for k in d]
        rnd.shuffle(lab)
        nulls.append(acc(dict(zip(d, lab))))
    return a, sorted(nulls)[len(nulls) // 2]


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-third registered predictions: decipherment loop 28, the picture vault without split luck', 'predict_test203')
    tabs = objects(F, recs, ('TAB:C', 'TAB:B', 'TAB:I'))
    g1 = build(tabs, lambda t: t)
    gf = build(tabs, family)
    rd.say('- %d tablets; %d text groups; %d text families.' % (len(tabs), len(g1), len(gf)))
    rd.say()
    h, n, p = loo_test(g1)
    rd.rec('LO1', 'leave-one-group-out beats its null', '%d of %d (%.1f%%); p = %.4f' % (h, n, 100 * h / max(1, n), p), p < 0.01)
    h2, n2, p2 = loo_test(gf)
    rd.rec('LO2', 'leave-one-family-out beats its null', '%d of %d (%.1f%%); p = %.4f' % (h2, n2, 100 * h2 / max(1, n2), p2), p2 < 0.05)
    ne = build([(t, m) for t, m in tabs if '923' not in t], family)
    h3, n3, p3 = loo_test(ne)
    rd.rec('LO3', 'without the elephant phrase', '%d of %d (%.1f%%); p = %.4f' % (h3, n3, 100 * h3 / max(1, n3), p3), p3 < 0.05)
    wins = 0
    accs = []
    for s in range(300, 350):
        a, med = split_test(gf, s)
        accs.append(a)
        wins += a > med
    rd.rec('LO4', 'over 50 splits', 'above the null median in %d of 50; accuracy median %.1f%% (range %.1f-%.1f%%)' % (wins, 100 * sorted(accs)[25], 100 * min(accs), 100 * max(accs)), wins >= 40)
    rd.rec('LO5', 'progress rule', 'LO1 %s, LO2 %s' % (p < 0.01, p2 < 0.05), p < 0.01 and p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
