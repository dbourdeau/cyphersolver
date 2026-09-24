"""Hundred-and-thirty-seventh registered prediction set (PREDICTIONS.md, SH1-SH10): sign shapes. Renders glyphs from
the ICIT webfont (path from the INDUS_FONT environment variable or the default below). Writes
results/predict_test137.md."""
import os
import random
from collections import Counter, defaultdict
from itertools import combinations

import numpy as np
from PIL import Image, ImageDraw, ImageFont

import predict_test13 as T
import rtools as R
from predict_test43 import sp_perm
from predict_test62 import sims
from predict_test81 import classes_of
from predict_test103 import CL
from signs import FISH

random.seed(157)
FONT = os.environ.get('INDUS_FONT', 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher--claude-worktrees-florence-1414-'
                      'cipher-160632/03a95ee0-e290-45c7-bab7-1e38cbd68d34/scratchpad/indus-website/src/assets/fonts/sk_indus_script-webfont.ttf')
N = 64


def glyphs():
    cps = {}
    for ln in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'glyphs.tsv'), encoding='utf-8'):
        p = ln.rstrip('\n').split('\t')
        if len(p) == 2 and p[1] and p[0] != 'glyph':
            cps[p[0]] = ''.join(chr(int(x, 16)) for x in p[1].split())
    font = ImageFont.truetype(FONT, 48)
    out = {}
    for g, ch in cps.items():
        im = Image.new('L', (N, N), 0)
        ImageDraw.Draw(im).text((4, 2), ch, font=font, fill=255)
        a = (np.asarray(im) > 127).astype(float)
        if a.sum() >= 15:
            out[g] = a
    return out


def corr(a, b):
    fa = np.fft.rfft2(a, s=(2 * N, 2 * N))
    fb = np.fft.rfft2(b[::-1, ::-1], s=(2 * N, 2 * N))
    return np.rint(np.fft.irfft2(fa * fb, s=(2 * N, 2 * N))).max()


def iou(a, b):
    ov = corr(a, b)
    return ov / (a.sum() + b.sum() - ov)


def contain(c, r):
    return corr(c, r) / c.sum()


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-thirty-seventh registered predictions: sign shapes', 'predict_test137')
    G = glyphs()
    DL = sorted({tuple(t) for t in AB})
    tc = Counter(g for t in DL for g in t)
    rare = sorted(g for g in tc if 1 <= tc[g] <= 3 and g in G and g not in R.NUMS)
    common = sorted(g for g in tc if tc[g] >= 20 and g in G and g not in R.NUMS)
    rd.say('- glyphs rendered %d; rare %d, common %d.' % (len(G), len(rare), len(common)))
    rd.say()
    base = {}
    for r in rare:
        best = max(((contain(G[c], G[r]), c) for c in common if G[r].sum() >= 1.2 * G[c].sum()), default=(0, None))
        if best[0] >= 0.8:
            base[r] = best[1]
    cc = 0
    for x in common:
        cc += any(G[x].sum() >= 1.2 * G[c].sum() and contain(G[c], G[x]) >= 0.8 for c in common if c != x)
    p = R.hyper_ge(len(base), len(rare) - len(base), cc, len(common) - cc)
    rd.rec('SH1', 'rare signs are compounds', 'rare compounds %d of %d (%.0f%%) against common %d of %d (%.0f%%); p = %.4f' % (
        len(base), len(rare), 100 * len(base) / max(1, len(rare)), cc, len(common), 100 * cc / max(1, len(common)), p),
        p < 0.05 and len(base) / max(1, len(rare)) > cc / max(1, len(common)))
    fr = defaultdict(set)
    for t in DL:
        s = ['#'] + list(t) + ['#']
        for i in range(1, len(s) - 1):
            if s[i] in common:
                fr[(s[i - 1], s[i + 1])].add(s[i])
    mates = defaultdict(set)
    for t in DL:
        s = ['#'] + list(t) + ['#']
        for i in range(1, len(s) - 1):
            if s[i] in base:
                mates[s[i]] |= fr[(s[i - 1], s[i + 1])]
    hit = sum(base[r] in mates[r] for r in base)
    exp = sum(len(mates[r]) / len(common) for r in base)
    rd.rec('SH2', 'a compound stands where its base stands', 'bases among frame-mates %d of %d (chance about %.1f)' % (hit, len(base), exp), hit > 2 * exp and hit >= 3)
    tcs, S, C = sims(AB, 20)
    S = [s for s in S if s in G and s not in R.NUMS]
    pairs = list(combinations(S, 2))
    random.shuffle(pairs)
    pairs = pairs[:1500]
    o, p = sp_perm([iou(G[a], G[b]) for a, b in pairs], [C[(a, b)] for a, b in pairs], n=1000)
    rd.rec('SH3', 'look-alikes keep company', 'pairs %d; Spearman %.3f; p = %.4f (1,000 shuffles)' % (len(pairs), o, p), o > 0 and p < 0.05)
    allg = sorted(g for g in G if g.isdigit() and g not in R.NUMS)
    adj = [(a, str(int(a) + 1)) for a in allg if str(int(a) + 1) in G]
    rnd = [tuple(random.sample(allg, 2)) for _ in range(len(adj) * 3)]
    rd.rank('SH4', 'catalogue neighbours look alike', 'adjacent-number against random pairs', [iou(G[a], G[b]) for a, b in adj], [iou(G[a], G[b]) for a, b in rnd])
    cand = [('435', '436'), ('526', '527'), ('336', '337'), ('554', '555'), ('705', '706')]
    cand = [p_ for p_ in cand if p_[0] in G and p_[1] in G]
    cm = sum(iou(G[a], G[b]) for a, b in cand) / len(cand)
    rv = sorted(iou(G[a], G[b]) for a, b in [tuple(random.sample(common, 2)) for _ in range(2000)])
    rd.rec('SH5', 'the free variants look alike', 'mean IoU %.3f; 95th percentile of random pairs %.3f' % (cm, rv[int(0.95 * len(rv))]), cm > rv[int(0.95 * len(rv))])

    def cohesion(key, title, members):
        m = [g for g in members if g in G]
        mm = sum(iou(G[a], G[b]) for a, b in combinations(m, 2)) / max(1, len(m) * (len(m) - 1) / 2)
        ge = 0
        for _ in range(1000):
            s = random.sample(allg, len(m))
            ge += sum(iou(G[a], G[b]) for a, b in combinations(s, 2)) / max(1, len(s) * (len(s) - 1) / 2) >= mm
        p_ = (ge + 1) / 1001
        rd.rec(key, title, 'members %d; mean IoU %.3f; p = %.4f (1,000 random sets)' % (len(m), mm, p_), p_ < 0.05)
    cohesion('SH6', 'fish look alike', sorted(FISH))
    cl = classes_of(sorted({(b, e) for b, e in T.names(AB) if b}))
    fish = [f for f in FISH if f in G]
    sf = lambda h: max(iou(G[h], G[f]) for f in fish if f != h)
    n5 = [h for h in cl if cl[h] == '520' and h not in FISH and h in G and h not in R.NUMS]
    n7 = [h for h in cl if cl[h] == '740' and h not in FISH and h in G and h not in R.NUMS]
    rd.rank('SH7', 'the 520 heads look fishy', '520 against 740 non-fish heads, best IoU with a fish', [sf(h) for h in n5], [sf(h) for h in n7])
    cohesion('SH8', 'closers look alike', list(CL))
    rd.rank('SH9', 'rare signs are more complex', 'rare against common ink', [G[g].sum() for g in rare], [G[g].sum() for g in common])
    pos = lambda t, i: 'F' if i == 0 else ('L' if i == len(t) - 1 else 'M')
    bp = defaultdict(Counter)
    for t in DL:
        for i, g in enumerate(t):
            bp[g][pos(t, i)] += 1
    toks = [(r, pos(t, i)) for t in DL for i, r in enumerate(t) if r in base]
    ok = sum(p_ == bp[base[r]].most_common(1)[0][0] for r, p_ in toks)
    rd.thr('SH10', 'compounds keep the base position', 'compound tokens in the base sign\'s usual position', ok, len(toks), 0.6)
    rd.say('- example compounds: %s.' % ', '.join('%s>%s' % (r, b) for r, b in list(base.items())[:15]))
    rd.finish()


if __name__ == '__main__':
    main()
