"""Two-hundred-and-second registered prediction set (PREDICTIONS.md, WM1-WM6): decipherment loop 27, weighted phrase
matching (rare pairs and triples count more) for the picture vault, and phrase matching on seals. Writes
results/predict_test202.md."""
import math
import random
from collections import Counter, defaultdict

import rtools as R
from predict_test200 import objects, split
from predict_test201 import phrase_test


def grams(t):
    return {t[i:i + 2] for i in range(len(t) - 1)} | {t[i:i + 3] for i in range(len(t) - 2)}


def wm_predict(design, vault):
    gm = defaultdict(list)
    for t, m in design:
        gm[t].append(m)
    dg = {t: grams(t) for t in gm}
    df = Counter(g for q in dg.values() for g in q)
    D = len(dg)
    hits = n = 0
    for t, m in vault:
        p = grams(t)
        sc = {d: sum(math.log(D / df[g]) for g in p & q) for d, q in dg.items() if p & q}
        if not sc:
            continue
        best = max(sc.values())
        ms = [x for d, v in sc.items() if v == best for x in gm[d]]
        n += 1
        hits += Counter(ms).most_common(1)[0][0] == m
    return hits, n


def wm_test(objs, seed, perms=1000):
    design, vault = split(objs, seed)
    hits, n = wm_predict(design, vault)
    acc = hits / max(1, n)
    gm = defaultdict(list)
    for t, m in design:
        gm[t].append(m)
    keys = sorted(gm)
    rnd = random.Random(seed + 9)
    ge = 0
    for _ in range(perms):
        lab = [gm[k] for k in keys]
        rnd.shuffle(lab)
        h2, n2 = wm_predict([(k, m) for k, ms in zip(keys, lab) for m in ms], vault)
        ge += h2 / max(1, n2) >= acc
    return hits, n, (ge + 1) / (perms + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-second registered predictions: decipherment loop 27, sharper phrase matching and phrases on seals', 'predict_test202')
    tabs = objects(F, recs, ('TAB:C', 'TAB:B', 'TAB:I'))
    res = {s: wm_test(tabs, s) for s in (200, 201, 202)}
    for s, (h, n, p) in res.items():
        rd.say('- split %d: weighted %d of %d (%.1f%%), p = %.4f.' % (s, h, n, 100 * h / max(1, n), p))
    rd.say()
    a200 = res[200][0] / max(1, res[200][1])
    a201 = res[201][0] / max(1, res[201][1])
    rd.rec('WM1', 'weighted beats set 201', 'split 200 %.1f%% (was 24.5%%), split 201 %.1f%% (was 18.6%%)' % (100 * a200, 100 * a201), a200 > 26 / 106 and a201 > 21 / 113)
    rd.rec('WM2', 'new split beats its null', 'split 202 %d of %d, p = %.4f' % (res[202][0], res[202][1], res[202][2]), res[202][2] < 0.05)
    rd.rec('WM3', 'splits 200 and 201 beat their nulls', 'p = %.4f, %.4f' % (res[200][2], res[201][2]), res[200][2] < 0.05 and res[201][2] < 0.05)
    seals = objects(F, recs, ('SEAL:S',))
    h, n, nv, p = phrase_test(seals, 200, perms=300)
    d, v = split(seals, 200)
    maj = Counter(m for t, m in d).most_common(1)[0][0]
    base = sum(m == maj for t, m in v) / max(1, len(v))
    rd.rec('WM4', 'seals: phrases beat the majority class', 'phrase matching %d of %d (%.1f%%); majority class %s on all unseen seals %.1f%%' % (h, n, 100 * h / max(1, n), maj, 100 * base), h / max(1, n) > base)
    rd.rec('WM5', 'seals: phrases beat their null', 'p = %.4f' % p, p < 0.05)
    ok = a200 > 26 / 106 and a201 > 21 / 113 and res[202][2] < 0.05
    rd.rec('WM6', 'progress rule', 'WM1 %s, WM2 %s' % (a200 > 26 / 106 and a201 > 21 / 113, res[202][2] < 0.05), ok)
    rd.finish()


if __name__ == '__main__':
    main()
