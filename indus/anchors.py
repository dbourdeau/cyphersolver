"""More sign = picture anchors: signs and texts tied to one picture across the pictured objects.

The copper tablets fix seven sign = image equations (copper.py). Seals and tablets with a field
picture can give more: a sign that turns up with one picture far beyond that picture's share of
objects, or a text that is always written with the same picture.

A1  Sign against picture. Unit: a distinct (text, picture) pair, so that copies of one tablet or
    sealings of one seal count once. For each sign in 3+ units and each picture: units with both,
    against the picture's share of all units (binomial upper tail), Bonferroni over all sign x
    picture pairs tested. The unicorn (60% of pictured units) is left out as a target: a sign
    'associated' with it says little.
A2 Text against picture: texts on 3+ objects that always carry the same picture (unicorn left out).
A3 Contact sheet of the A1 candidates (with the picture name) to judge by eye whether the sign
    draws its picture, as 341 draws the rhinoceros on the copper tablets.

Usage: python anchors.py [path/to/sk_indus_script-webfont.ttf]
Writes results/anchors.md (and results/anchors.png with a font).
"""
import csv
import math
import os
import sys
from collections import Counter, defaultdict

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
NAMES = {'Bull1': 'unicorn', 'Gaur': 'gaur (bison)', 'Elep': 'elephant', 'Zebu': 'zebu', 'Bult': 'short-horned bull',
         'Gavi': 'gharial', 'Mult': 'multi-headed animal', 'Phyt': 'tree / plant', 'Rhin': 'rhinoceros', 'Fish': 'fish',
         'Scene': 'scene', 'Buff': 'buffalo', 'Anth': 'anthropomorph', 'Tigr': 'tiger', 'Hare': 'hare',
         'Comp': 'composite animal', 'CompBull': 'composite bull', 'Cros': 'cross', 'Crs': 'cross', 'Goat': 'goat',
         'Pipal': 'pipal leaf', 'Loop': 'loop / knot', 'T-A-T': 'tree-animal-tree', 'T-M-T': 'tree-man-tree',
         'Othr': 'other', 'Bull': 'bull', 'Bull2': 'bull (2)', 'Bull3': 'bull (3)', 'Maze': 'maze', 'Box': 'box'}


def say(s=''):
    OUT.append(s)
    print(s)


def binom_upper(k, n, p):
    if k <= 0:
        return 1.0
    return min(1.0, sum(math.exp(math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
                                 + i * math.log(p) + (n - i) * math.log(1 - p)) for i in range(k, n + 1)))


def base(m):
    return m.split(':')[0]


def main(font=None):
    rows = [r for r in load() if r['flat'] and r['motif']]
    units = {}
    for r in rows:
        units.setdefault((tuple(r['flat']), base(r['motif'])), r)
    say('# More sign = picture anchors')
    say()
    say('- pictured objects: %d; distinct (text, picture) units: %d.' % (len(rows), len(units)))
    mfreq = Counter(m for _, m in units)
    N = len(units)
    say('- pictures (units): %s.' % ', '.join('%s %d' % (NAMES.get(m, m), c) for m, c in mfreq.most_common(20)))
    say()
    sign_units = defaultdict(Counter)
    for (t, m) in units:
        for g in set(t):
            sign_units[g][m] += 1
    tests = [(g, m) for g, c in sign_units.items() if sum(c.values()) >= 3 for m in c if m != 'Bull1']
    alpha = 0.05 / max(1, len(tests))
    cands = []
    for g, m in tests:
        c = sign_units[g]
        n, k = sum(c.values()), c[m]
        p = binom_upper(k, n, mfreq[m] / N)
        if k >= 3 and p < alpha:
            cands.append((p, g, m, k, n))
    cands.sort()
    say('## A1 Signs tied to one picture (Bonferroni over %d sign x picture pairs, alpha %.1e)' % (len(tests), alpha))
    say()
    say('| sign | picture | units with both / units with the sign | picture\'s share of units | p |')
    say('|---|---|---|---|---|')
    for p, g, m, k, n in cands:
        say('| %s | %s | %d / %d | %.1f%% | %.1g |' % (g, NAMES.get(m, m), k, n, 100 * mfreq[m] / N, p))
    say()
    say('## A2 Texts always written with the same picture (3+ objects, unicorn left out)')
    say()
    tm = defaultdict(Counter)
    for r in rows:
        tm[' '.join(r['flat'])][base(r['motif'])] += 1
    fixed = [(t, c) for t, c in tm.items() if sum(c.values()) >= 3 and len(c) == 1 and 'Bull1' not in c]
    for t, c in sorted(fixed, key=lambda x: -sum(x[1].values())):
        m = next(iter(c))
        types = Counter(r['type'] for r in rows if ' '.join(r['flat']) == t)
        say('- %s: %s on %d objects (%s).' % (t, NAMES.get(m, m), c[m], ', '.join('%s %d' % kv for kv in types.items())))
    say()
    say('## A1b The same within one object class, counting distinct texts (a sign in 2+ distinct texts, 60%% or more of them '
        'with one picture, unicorn left out)')
    say()
    for lab, keep in (('seals', lambda t: t.startswith('SEAL')), ('tablets', lambda t: t.startswith('TAB'))):
        dt = {}
        for r in rows:
            if keep(r['type']):
                dt.setdefault(tuple(r['flat']), Counter())[base(r['motif'])] += 1
        mt = Counter(c.most_common(1)[0][0] for c in dt.values())
        n_t = len(dt)
        by = defaultdict(Counter)
        for t, c in dt.items():
            m = c.most_common(1)[0][0]
            for g in set(t):
                by[g][m] += 1
        found = []
        for g, c in by.items():
            n = sum(c.values())
            for m, k in c.items():
                if m != 'Bull1' and k >= 2 and k / n >= 0.6:
                    found.append((binom_upper(k, n, mt[m] / n_t), g, m, k, n))
        found.sort()
        say('- %s (%d distinct texts): %s.' % (lab, n_t, '; '.join(
            '%s with %s in %d of %d texts (share of texts %.1f%%, p %.1g)' % (g, NAMES.get(m, m), k, n, 100 * mt[m] / n_t, p)
            for p, g, m, k, n in found[:15]) or 'none'))
    say()
    say('## A3 Judged by eye (render sheet of the candidates)')
    say()
    say('- 347, a horned quadruped with a crest, drawn like 341 (the rhinoceros sign of the copper tablets): with the '
        'multi-headed animal on 8 of its 9 objects (one text, 347 741 176 740 90, on 8 moulded tablets; the ninth is a '
        'gaur seal). A logogram for the animal on the other face, as 341 is on the copper tablets: **candidate anchor**.')
    say('- 645, an X between two dotted lines: with the cross motif on 7 moulded tablets (one text, 104 645 590 235 240 '
        '740 90); 6 other occurrences on seals, a rod and an implement. The sign draws the picture: **candidate, weak**.')
    say('- 318, a bar with a row of teeth: with the gharial on 11 of 12 (one text on 11 moulded tablets, with 436 '
        'and 803 415 220 ...). The toothed snout of a gharial is possible; one text only: **candidate, weak**.')
    say('- 460, three tall cones on a base (Fairservis: three conical structures): with the tree / plant picture in '
        '4 of its 5 distinct tablet texts (354 460 798 740, 15 460 798 740, 495 460 740 400, 415 240 495 460 752 740: '
        'moulded tablets with a tree; p = 0.0005 against the 10% of tablet texts that carry a tree). Several different texts, not '
        'copies of one: the best supported of the new candidates, if the cones are trees or shoots: **candidate**.')
    say('- 158, a crossed figure with two leaf-like crests: with the tree in 3 of 5 tablet texts (x 806 158); '
        'weak.')
    say('- 27 (six short strokes in two rows) with the fish on 3 incised tablets (27 32 740 400), 465 (A-shape) with '
        'a tree on 5 tablets, 736 (U with rays) with the multi-headed animal: do not draw their picture, and each '
        'rests on one text; left out.')
    say()
    if font:
        from PIL import Image, ImageDraw, ImageFont
        cps = {}
        for r in csv.DictReader(open(os.path.join(HERE, 'data', 'glyphs.tsv'), encoding='utf-8'), delimiter='\t'):
            if r['codepoints'].strip():
                cps[r['glyph']] = ''.join(chr(int(x, 16)) for x in r['codepoints'].split())
        f = ImageFont.truetype(font, 70)
        small = ImageFont.truetype('arial.ttf', 14) if os.path.exists('C:/Windows/Fonts/arial.ttf') else ImageFont.load_default()
        seen, items = set(), []
        for p, g, m, k, n in cands:
            if (g, m) not in seen:
                seen.add((g, m))
                items.append((g, m, k, n))
        cols = 8
        W, H = 170, 150
        im = Image.new('RGB', (cols * W, max(1, (len(items) + cols - 1) // cols) * H), 'white')
        d = ImageDraw.Draw(im)
        for i, (g, m, k, n) in enumerate(items):
            x, y = (i % cols) * W, (i // cols) * H
            if g in cps:
                d.text((x + 40, y + 10), cps[g], font=f, fill='black')
            d.text((x + 6, y + 112), '%s: %s %d/%d' % (g, NAMES.get(m, m)[:14], k, n), font=small, fill=(160, 0, 0))
        im.save(os.path.join(HERE, 'results', 'anchors.png'))
        say('Contact sheet of the A1 candidates: results/anchors.png.')
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'anchors.md'), 'w', encoding='utf-8') as fo:
        fo.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:2])
