"""The published keys against the provisional anchors of anchors.py (the B3 test of bench.py on new material).

Provisional anchors: sign 460 = tree (with a tree in 4 of its 5 distinct tablet texts), and the
texts written with one picture on the moulded and incised tablets: the tree (354 460 798 740,
15 460 798 740, 495 460 740 400, 415 240 495 460 752 740, 465 806 158), the gharial (803 415 220
318 920 255 436 690 590 407 740, 605 760 740 400, 503 16 740 400, 440 740 400 840 712) and the fish
(27 32 740 400). Sign 347 (with the multi-headed animal) has no dictionary word to test against.

For each key: does its value (or gloss) for 460 name a tree in its language; and how many of the
anchor texts contain a word (2+ consonants) for their picture in its reading, against 200 shuffles
of the key.

Usage: python anchors_bench.py <mw.txt> <dedr forms.csv> <sux_gloss.tsv> [yajnadevam xlits.csv]
Writes results/anchors_bench.md.
"""
import glob
import os
import re
import sys
from collections import Counter

import bench
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
PAT = {'tree': r'\b(trees?|shrub|plant)\b', 'gharial': r'\b(crocodile|alligator|gharial)s?\b', 'fish': r'\bfish'}
TEXTS = [('354 460 798 740', 'tree'), ('15 460 798 740', 'tree'), ('495 460 740 400', 'tree'),
         ('415 240 495 460 752 740', 'tree'), ('465 806 158', 'tree'),
         ('803 415 220 318 920 255 436 690 590 407 740', 'gharial'), ('605 760 740 400', 'gharial'),
         ('503 16 740 400', 'gharial'), ('440 740 400 840 712', 'gharial'), ('27 32 740 400', 'fish')]


def say(s=''):
    OUT.append(s)
    print(s)


def words(gl, lang, pat):
    p = re.compile(pat)
    return {bench.skel(w) for w, g in gl[lang] if p.search(g) and len(bench.skel(w)) >= 2}


def main(mw, dedr, sux, yaj=None):
    lex, gl, _ = bench.lexicons(mw, dedr, sux)
    gl['dra'] = bench.dedr_glosses(dedr)
    texts = [ln for r in load() for ln in r['seq'] if len(ln) >= 3]
    freq = Counter(g for t in texts for g in t)
    keys = []
    if yaj:
        keys.append(bench.load_yajnadevam(yaj))
    for p in sorted(p for p in glob.glob(os.path.join(HERE, 'keys', '*.tsv')) if not p.endswith('_raw.tsv')):
        keys.append(bench.load_key(p))
    say('# The published keys against the provisional anchors')
    say()
    say('| key | 460 (tree) | anchor texts naming their picture | shuffles: mean, as many or more |')
    say('|---|---|---|---|')
    for meta, key, gloss in keys:
        lang = meta['lang']
        aw = {a: words(gl, lang, p) for a, p in PAT.items()}
        v = key.get('460')
        if v is None:
            s460 = 'no value'
        else:
            hit = re.search(PAT['tree'], gloss.get('460', '').lower()) or bench.skel(v) in aw['tree']
            s460 = '%s%s: %s' % (v, ' "%s"' % gloss['460'][:30] if '460' in gloss else '', 'names a tree' if hit else 'no')

        def hits(k):
            return sum(any(w in ''.join(bench.runs(t.split(), k)) for w in aw[a]) for t, a in TEXTS)
        h = hits(key)
        sims = [hits(k2) for k2 in bench.shuffles(key, freq, n=200, band=10 if len(key) > 60 else 3)]
        say('| %s | %s | %d of %d | %.2f, %d of 200 |' % (meta['title'][:60], s460, h, len(TEXTS), sum(sims) / len(sims),
                                                         sum(1 for x in sims if x >= h)))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'anchors_bench.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:5])
