"""Hundred-and-fortieth registered prediction set (PREDICTIONS.md, FS1-FS10): find spots inside Mohenjo-daro (ICIT fields
4 area, 5 block/house or street). Writes results/predict_test140.md."""
import random
import re
from collections import defaultdict
from itertools import combinations

import rtools as R
from predict_test108 import genre

random.seed(160)
GENERIC = ('DK-', 'HR-', 'VS-', 'DKG', '--', '')


def major(a):
    a = a.strip()
    for k in ('DK', 'HR', 'VS', 'SD', 'MN'):
        if a.startswith(k):
            return k
    return 'L' if a.startswith('L') else None


def pair_perm(items, n=1000):
    """items: (key, place). Share of same-key pairs in the same place, against permuted places."""
    keys = [k for k, _ in items]
    groups = defaultdict(list)
    for i, k in enumerate(keys):
        groups[k].append(i)
    pairs = [(i, j) for g in groups.values() if len(g) >= 2 for i, j in combinations(g, 2)]
    if not pairs:
        return 0, 0, 1.0, 0
    pl = [p for _, p in items]
    obs = sum(pl[i] == pl[j] for i, j in pairs) / len(pairs)
    ge = 0
    tot = 0
    for _ in range(n):
        random.shuffle(pl)
        v = sum(pl[i] == pl[j] for i, j in pairs) / len(pairs)
        tot += v
        ge += v >= obs
    return obs, tot / n, (ge + 1) / (n + 1), len(pairs)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-fortieth registered predictions: find spots inside Mohenjo-daro', 'predict_test140')
    md = [r for r in F if recs[r['sealid']][3] == 'Mohenjo-daro']
    sub = lambda r: recs[r['sealid']][4].strip() if recs[r['sealid']][4].strip() not in GENERIC else None
    f5 = lambda r: recs[r['sealid']][5].strip()
    house = lambda r: (sub(r), f5(r)) if sub(r) and re.search(r'[IVX]+$', f5(r)) else None
    text = lambda r: tuple(r['seq'][0]) if r['seq'] and r['seq'][0] else None
    seals = [r for r in md if r['type'].startswith('SEAL') and text(r)]
    rd.say('- Mohenjo-daro intact objects %d; seals with text %d, with a sub-area %d, in a house %d.' % (
        len(md), len(seals), sum(1 for r in seals if sub(r)), sum(1 for r in seals if house(r))))
    rd.say()

    def ptest(key, title, items):
        o, e, p, n = pair_perm(items)
        rd.rec(key, title, 'pairs %d; same place %.3f against %.3f by chance; p = %.4f' % (n, o, e, p), o > e and p < 0.05)
    ptest('FS1', 'same text, same sub-area', [(text(r), sub(r)) for r in seals if sub(r)])
    hd = lambda r: R.name_of(list(text(r)))[0][-1] if R.name_of(list(text(r))) and R.name_of(list(text(r)))[0] else None
    ptest('FS2', 'same head, same sub-area', [(hd(r), sub(r)) for r in seals if sub(r) and hd(r)])
    hs = [r for r in seals if house(r)]
    sg = [frozenset(g for g in text(r) if g not in R.NUMS) for r in hs]
    hl = [house(r) for r in hs]
    sb = [sub(r) for r in hs]
    idx = [(i, j) for i, j in combinations(range(len(hs)), 2) if sb[i] == sb[j]]

    def diff(lab):
        a = [bool(sg[i] & sg[j]) for i, j in idx if lab[i] == lab[j]]
        c = [bool(sg[i] & sg[j]) for i, j in idx if lab[i] != lab[j]]
        return sum(a) / max(1, len(a)) - sum(c) / max(1, len(c)), len(a)
    obs, npair = diff(hl)
    bysub = defaultdict(list)
    for i, s in enumerate(sb):
        bysub[s].append(i)
    ge = 0
    for _ in range(1000):
        lab = list(hl)
        for s, ix in bysub.items():
            v = [hl[i] for i in ix]
            random.shuffle(v)
            for i, x in zip(ix, v):
                lab[i] = x
        ge += diff(lab)[0] >= obs
    p = (ge + 1) / 1001
    rd.rec('FS3', 'a household vocabulary', 'same-house pairs %d; share-a-sign difference (same house minus same sub-area) %+.3f; p = %.4f' % (npair, obs, p), obs > 0 and p < 0.05)
    dh = [r for r in seals if major(recs[r['sealid']][4]) in ('DK', 'HR')]
    rd.mi('FS4', 'genre mix differs DK / HR', 'seals', [genre(text(r)) for r in dh], [major(recs[r['sealid']][4]) for r in dh])
    ct = [r for r in md if sub(r) and text(r) and (r['type'].startswith('SEAL') or r['type'] == 'TAB:C')]
    rd.mi('FS5', 'copper tablets lie elsewhere', 'seals and copper tablets with a sub-area', [r['type'] == 'TAB:C' for r in ct], [sub(r) for r in ct])
    cu = [r for r in md if r['type'] == 'TAB:C' and text(r) and sub(r)]
    ptest('FS6', 'same copper text, same sub-area', [(tuple(r['flat']), sub(r)) for r in cu])
    en = [(R.name_of(list(text(r)))[1], sub(r)) for r in seals if sub(r) and R.name_of(list(text(r))) and R.name_of(list(text(r)))[1] in R.END]
    rd.mi('FS7', 'the ending depends on sub-area', 'seal names ending 740 / 520', [a for a, _ in en], [b for _, b in en])
    ms = [r for r in seals if sub(r) and recs[r['sealid']][18].strip() not in ('-', '')]
    rd.mi('FS8', 'the motif depends on sub-area', 'seals with a motif', [recs[r['sealid']][18].startswith('Bull1') for r in ms], [sub(r) for r in ms])
    ls = [r for r in seals if sub(r)]
    rd.mi('FS9', 'long texts depend on sub-area', 'seals', [len(text(r)) >= 5 for r in ls], [sub(r) for r in ls])
    street = [r for r in seals if re.search('street|lane', f5(r), re.I)]
    rd.ltl('FS10', 'street seals are names less often', 'name, street/lane seals', [genre(text(r)) == 'name' for r in street], [genre(text(r)) == 'name' for r in hs])
    rd.finish()


if __name__ == '__main__':
    main()
