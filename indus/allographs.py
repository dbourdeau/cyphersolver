"""Is the ICIT sign list over-split? Shape and context similarity of sign pairs.

The size of the sign inventory is the main argument for a logo-syllabic script (about 400-700
signs) and a point in the Farmer-Sproat-Witzel dispute. If many listed signs are graphic variants
of one sign, the working inventory is smaller.

A1  Shape: each glyph is rendered with the indus-website font, cropped, scaled to 40x40 and
    blurred slightly; shape similarity = the best normalised overlap (Dice) under shifts of up to
    2 pixels.
A2  Context: for every sign with 5+ tokens, counts of its left and right neighbours (with line
    start and end); similarity = cosine of the positive-PMI vectors.
A3  Candidate variants: pairs in the top 1% of shape similarity among all pairs and in the top 5%
    of context similarity. Their share against the share expected if shape and context were
    independent (does looking alike go with being used alike?), and a union-find merge of the
    candidate pairs: how far the inventory shrinks.

Usage: python allographs.py path/to/sk_indus_script-webfont.ttf
Writes results/allographs.md.
"""
import csv
import math
import os
import sys
from collections import Counter, defaultdict

from PIL import Image, ImageDraw, ImageFilter, ImageFont

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
N = 40


def say(s=''):
    OUT.append(s)
    print(s)


def glyph_bitmaps(font_path, ids):
    cps = {}
    for r in csv.DictReader(open(os.path.join(HERE, 'data', 'glyphs.tsv'), encoding='utf-8'), delimiter='\t'):
        if r['codepoints'].strip():
            cps[r['glyph']] = ''.join(chr(int(c, 16)) for c in r['codepoints'].split())
    font = ImageFont.truetype(font_path, 120)
    out = {}
    for g in ids:
        if g not in cps:
            continue
        im = Image.new('L', (220, 220), 0)
        ImageDraw.Draw(im).text((20, 20), cps[g], font=font, fill=255)
        box = im.getbbox()
        if not box:
            continue
        im = im.crop(box)
        w, h = im.size
        s = max(w, h)
        sq = Image.new('L', (s, s), 0)
        sq.paste(im, ((s - w) // 2, (s - h) // 2))
        sq = sq.resize((N, N)).filter(ImageFilter.GaussianBlur(1))
        px = [v / 255 for v in sq.getdata()]
        out[g] = px
    return out


def shifted(px):
    """The bitmap under shifts of up to 2 pixels, as a (25, N*N) array."""
    import numpy as np
    im = np.array(px).reshape(N, N)
    out = []
    for dx in (-2, -1, 0, 1, 2):
        for dy in (-2, -1, 0, 1, 2):
            sh = np.zeros_like(im)
            ys, yd = (slice(0, N - dy), slice(dy, N)) if dy >= 0 else (slice(-dy, N), slice(0, N + dy))
            xs, xd = (slice(0, N - dx), slice(dx, N)) if dx >= 0 else (slice(-dx, N), slice(0, N + dx))
            sh[yd, xd] = im[ys, xs]
            out.append(sh.ravel())
    return np.array(out)


def dice_row(a_sh, a_sum, others, sums):
    """Dice of sign a (all shifts) against every other bitmap; best over shifts."""
    import numpy as np
    inter = np.minimum(a_sh[:, None, :], others[None, :, :]).sum(axis=2).max(axis=0)
    return 2 * inter / (a_sum + sums)


def main(font_path):
    rows = [r for r in load() if r['flat']]
    freq = Counter(g for r in rows for g in r['flat'])
    signs = [g for g, c in freq.items() if c >= 5]
    ctx = defaultdict(Counter)
    for r in rows:
        for ln in r['seq']:
            s = ['<'] + ln + ['>']
            for i in range(1, len(s) - 1):
                ctx[s[i]]['L' + s[i - 1]] += 1
                ctx[s[i]]['R' + s[i + 1]] += 1
    tot = Counter()
    for g in ctx:
        tot.update(ctx[g])
    T = sum(tot.values())
    vec = {}
    for g in signs:
        n = sum(ctx[g].values())
        v = {}
        for f, c in ctx[g].items():
            pmi = math.log((c / n) / (tot[f] / T))
            if pmi > 0:
                v[f] = pmi
        vec[g] = v

    def cos(a, b):
        num = sum(a[k] * b.get(k, 0) for k in a)
        da = math.sqrt(sum(x * x for x in a.values()))
        db = math.sqrt(sum(x * x for x in b.values()))
        return num / (da * db) if da and db else 0
    bm = glyph_bitmaps(font_path, signs)
    signs = [g for g in signs if g in bm]
    say('# Is the sign list over-split?')
    say()
    say('- signs with 5+ tokens and a glyph in the font: %d (of %d sign types in the corpus).' % (len(signs), len(freq)))
    import numpy as np
    arr = np.array([bm[g] for g in signs])
    sums = arr.sum(axis=1)
    pairs = []
    for i, a in enumerate(signs):
        if i + 1 >= len(signs):
            break
        d = dice_row(shifted(bm[a]), sums[i], arr[i + 1:], sums[i + 1:])
        for j, b in enumerate(signs[i + 1:]):
            pairs.append((a, b, float(d[j]), cos(vec[a], vec[b])))
    sh = sorted(p[2] for p in pairs)
    cx = sorted(p[3] for p in pairs)
    t_sh = sh[int(0.99 * len(sh))]
    t_cx = cx[int(0.95 * len(cx))]
    look = [p for p in pairs if p[2] >= t_sh]
    both = [p for p in look if p[3] >= t_cx]
    say('- pairs: %d; top 1%% by shape (Dice >= %.2f): %d; of those, also top 5%% by context (cosine >= %.2f): %d '
        '(%.1f%%, against 5%% if shape and context were independent).' % (
            len(pairs), t_sh, len(look), t_cx, len(both), 100 * len(both) / len(look)))
    say('- mean context similarity: look-alike pairs %.3f, all pairs %.3f.' % (
        sum(p[3] for p in look) / len(look), sum(cx) / len(cx)))
    both.sort(key=lambda p: -(p[2] + p[3]))
    say('- candidate variant pairs (shape, context, tokens): %s.' % '; '.join(
        '%s~%s (%.2f, %.2f, %d/%d)' % (a, b, s, c, freq[a], freq[b]) for a, b, s, c in both[:30]))
    par = {g: g for g in signs}

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for a, b, _, _ in both:
        par[find(a)] = find(b)
    groups = defaultdict(list)
    for g in signs:
        groups[find(g)].append(g)
    say('- merging every candidate pair: %d signs become %d (%d groups of 2+: %s).' % (
        len(signs), len(groups), sum(1 for v in groups.values() if len(v) > 1),
        '; '.join(' '.join(sorted(v, key=lambda g: -freq[g])) for v in groups.values() if len(v) > 1)[:600]))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'allographs.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
