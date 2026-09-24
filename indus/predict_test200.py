"""Two-hundredth registered prediction set (PREDICTIONS.md, PB1-PB6): decipherment loop 25, picture anchors fixed on half
of the pictured tablets (split by distinct text) and tested on the unseen half. Writes results/predict_test200.md."""
import random
from collections import Counter, defaultdict

import rtools as R

SKIP = {'Othr', 'Unknown', 'None', '-', ''}


def objects(F, recs, types):
    out = []
    for r in F:
        rec = recs.get(r['sealid'])
        if not rec or not any(rec[20].startswith(t) for t in types):
            continue
        m = rec[18].split(':')[0]
        if m in SKIP or not r['flat']:
            continue
        out.append((tuple(r['flat']), m))
    return out


def anchors(design):
    occ = defaultdict(list)
    texts = defaultdict(set)
    for t, m in design:
        for g in set(t):
            occ[g].append(m)
            texts[g].add(t)
    out = {}
    for g, ms in occ.items():
        if len(ms) >= 3 and len(texts[g]) >= 2:
            k, v = Counter(ms).most_common(1)[0]
            if v / len(ms) >= 0.8:
                out[g] = k
    return out


def predict(anc, vault):
    hits = n = 0
    per = defaultdict(lambda: [0, 0])
    for t, m in vault:
        a = [anc[g] for g in set(t) if g in anc]
        if not a:
            continue
        p = Counter(a).most_common(1)[0][0]
        n += 1
        hits += p == m
        for g in set(t):
            if g in anc:
                per[g][0] += anc[g] == m
                per[g][1] += 1
    return hits, n, per


def split(objs, seed):
    groups = sorted({t for t, m in objs})
    rnd = random.Random(seed)
    rnd.shuffle(groups)
    d = set(groups[:len(groups) // 2])
    return [o for o in objs if o[0] in d], [o for o in objs if o[0] not in d]


def run(objs, seed=200, perms=1000):
    design, vault = split(objs, seed)
    anc = anchors(design)
    hits, n, per = predict(anc, vault)
    acc = hits / max(1, n)
    # null: motifs shuffled among design text groups
    gm = defaultdict(list)
    for t, m in design:
        gm[t].append(m)
    keys = sorted(gm)
    rnd = random.Random(seed + 1)
    ge = 0
    for _ in range(perms):
        lab = [gm[k] for k in keys]
        rnd.shuffle(lab)
        d2 = [(k, m) for k, ms in zip(keys, lab) for m in ms]
        h2, n2, _ = predict(anchors(d2), vault)
        ge += (h2 / max(1, n2)) >= acc
    return acc, hits, n, len(vault), anc, per, (ge + 1) / (perms + 1), len(design)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundredth registered predictions: decipherment loop 25, picture anchors on unseen tablets', 'predict_test200')
    tabs = objects(F, recs, ('TAB:C', 'TAB:B', 'TAB:I'))
    rd.say('- pictured tablets: %d objects, %d distinct texts; motifs %s.' % (len(tabs), len({t for t, m in tabs}), dict(Counter(m for t, m in tabs).most_common())))
    acc, hits, n, nv, anc, per, p, nd = run(tabs)
    rd.say('- design %d objects; anchors: %s.' % (nd, ', '.join('%s=%s' % kv for kv in sorted(anc.items()))))
    rd.say('- per anchor on the vault (right / carried): %s.' % ', '.join('%s %d/%d' % (g, a, b) for g, (a, b) in sorted(per.items())))
    rd.say()
    rd.rec('PB1', 'frozen anchors predict unseen pictures', 'vault accuracy %d of %d (%.1f%%); permutation p = %.4f' % (hits, n, 100 * acc, p), p < 0.01)
    rd.rec('PB2', 'anchors reach 20% of the vault', '%d of %d vault objects carry an anchor (%.1f%%)' % (n, nv, 100 * n / max(1, nv)), n / max(1, nv) >= 0.2)
    cu = objects(F, recs, ('TAB:C',))
    ca, ch, cn, cnv, canc, cper, cp, cnd = run(cu)
    rd.rec('PB3', 'copper tablets alone', 'vault %d of %d (%.1f%%); anchors %d; p = %.4f' % (ch, cn, 100 * ca, len(canc), cp), cp < 0.05)
    se = objects(F, recs, ('SEAL:S',))
    sa, sh, sn, snv, sanc, sper, sp, snd = run(se, perms=300)
    rd.rec('PB4', 'seals: no picture anchors', 'seal vault %d of %d (%.1f%%); anchors %d; p = %.4f' % (sh, sn, 100 * sa, len(sanc), sp), sp >= 0.05)
    rd.rec('PB5', 'accuracy 50% or more', '%.1f%%' % (100 * acc), acc >= 0.5)
    good = sorted(g for g, (a, b) in per.items() if a > b / 2)
    rd.rec('PB6', 'progress rule', 'PB1 %s; anchors right more often than not on the vault: %s' % (p < 0.01, ', '.join('%s=%s' % (g, anc[g]) for g in good)), p < 0.01)
    rd.finish()


if __name__ == '__main__':
    main()
