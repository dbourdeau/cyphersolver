"""Two-hundred-and-first registered prediction set (PREDICTIONS.md, PH1-PH3, GF1-GF4): decipherment loop 26, phrase-level
picture anchors on unseen tablets; graphic (decade) families against learned classes in the S model. Writes
results/predict_test201.md."""
import random
from collections import Counter, defaultdict

import rtools as R
from famlm import fam, learned_classes, score3, with_fam
from predict_test200 import objects, split
from progress import MODEL, data
from signs import load


def pairs(t):
    return {t[i:i + 2] for i in range(len(t) - 1)}


def nn_predict(design, vault):
    gm = defaultdict(list)
    for t, m in design:
        gm[t].append(m)
    dp = {t: pairs(t) for t in gm}
    hits = n = 0
    for t, m in vault:
        p = pairs(t)
        sc = {d: len(p & q) for d, q in dp.items()}
        best = max(sc.values()) if sc else 0
        if best < 1:
            continue
        ms = [x for d, v in sc.items() if v == best for x in gm[d]]
        n += 1
        hits += Counter(ms).most_common(1)[0][0] == m
    return hits, n


def phrase_test(objs, seed, perms=1000):
    design, vault = split(objs, seed)
    hits, n = nn_predict(design, vault)
    acc = hits / max(1, n)
    gm = defaultdict(list)
    for t, m in design:
        gm[t].append(m)
    keys = sorted(gm)
    rnd = random.Random(seed + 7)
    ge = 0
    for _ in range(perms):
        lab = [gm[k] for k in keys]
        rnd.shuffle(lab)
        h2, n2 = nn_predict([(k, m) for k, ms in zip(keys, lab) for m in ms], vault)
        ge += h2 / max(1, n2) >= acc
    return hits, n, len(vault), (ge + 1) / (perms + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-first registered predictions: decipherment loop 26, phrase-level picture anchors; graphic against learned families', 'predict_test201')
    tabs = objects(F, recs, ('TAB:C', 'TAB:B', 'TAB:I'))
    h, n, nv, p = phrase_test(tabs, 200)
    rd.rec('PH1', 'shared phrases predict unseen pictures (seed 200)', 'right %d of %d matched (%.1f%%); permutation p = %.4f' % (h, n, 100 * h / max(1, n), p), p < 0.05)
    h2, n2, nv2, p2 = phrase_test(tabs, 201)
    rd.rec('PH2', 'second split (seed 201)', 'right %d of %d (%.1f%%); p = %.4f' % (h2, n2, 100 * h2 / max(1, n2), p2), p2 < 0.05)
    rd.rec('PH3', '30% of unseen tablets share a pair', '%d of %d (%.1f%%)' % (n, nv, 100 * n / max(1, nv)), n / max(1, nv) >= 0.3)
    DL, tr, te = data()
    keys = MODEL['keys']
    dec, _ = score3(tr, te, keys)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    decb, _ = score3(DA, DBx, keys)
    fx, ab = {}, {}
    for k in (40, 80, 150):
        mp = learned_classes(tr, k)
        fx[k], _ = score3(tr, te, keys, cls=with_fam(lambda g, mp=mp: mp.get(g, g)))
        mpa = learned_classes(DA, k)
        ab[k], _ = score3(DA, DBx, keys, cls=with_fam(lambda g, mp=mpa: mp.get(g, g)))
    rd.say('- S with decade families %.4f (A->B %.4f); learned classes %s (A->B %s).' % (dec, decb, ', '.join('k%d %.4f' % kv for kv in fx.items()), ', '.join('k%d %.4f' % kv for kv in ab.items())))
    rd.say()
    g1 = all(dec < v for v in fx.values())
    g2 = all(decb < v for v in ab.values())
    rd.rec('GF1', 'decade families beat learned classes (fixed test)', 'decade %.4f; learned %s' % (dec, ', '.join('%.4f' % v for v in fx.values())), g1)
    rd.rec('GF2', 'and A -> B', 'decade %.4f; learned %s' % (decb, ', '.join('%.4f' % v for v in ab.values())), g2)
    mp = learned_classes(tr, 80)
    both, _ = score3(tr, te, keys, cls=with_fam(lambda g, mp=mp: fam(g) + '|' + mp.get(g, g)))
    rd.rec('GF3', 'decade|learned pairs add nothing', 'pairs %.4f against decade %.4f' % (both, dec), both >= dec)
    ok = (p < 0.05 and p2 < 0.05) or (g1 and g2)
    rd.rec('GF4', 'progress rule', 'phrases %s; graphic families %s' % (p < 0.05 and p2 < 0.05, g1 and g2), ok)
    rd.finish()


if __name__ == '__main__':
    main()
