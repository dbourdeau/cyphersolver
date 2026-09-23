"""Export the data the in-browser test bench (docs/indus-bench.html) needs: the corpus lines of 3+
signs (ICIT-derived), the consonant-skeleton sets of the three lexicons (bench.skel, the same
classes as bench.py), the case-ending consonants, the copper-tablet anchor texts and the keys in
keys/*.tsv. Writes docs/indus_bench.json.

Yajnadevam's key is not bundled (his repository states no licence); a reader can paste it.

Usage: python export_bench.py <mw.txt> <dedr forms.csv> <sux_gloss.tsv>
"""
import glob
import json
import os
import sys

import bench
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))


def main(mw, dedr, sux):
    rows = [r for r in load() if r['flat']]
    texts = [ln for r in rows for ln in r['seq'] if len(ln) >= 3]
    lex, gl = bench.lexicons(mw, dedr, sux)
    gl['dra'] = bench.dedr_glosses(dedr)
    animals = {L: {a: sorted(bench.animal_words(L, gl, a)) for a in bench.ANIMAL_PAT} for L in gl}
    keys = {}
    for p in sorted(p for p in glob.glob(os.path.join(HERE, 'keys', '*.tsv')) if not p.endswith('_raw.tsv')):
        meta, key, gloss = bench.load_key(p)
        keys[os.path.basename(p)[:-4]] = {'title': meta['title'], 'lang': meta['lang'],
                                          'tsv': open(p, encoding='utf-8').read()}
    out = {'texts': [' '.join(t) for t in texts],
           'lex': {L: sorted(v) for L, v in lex.items()},
           'endings': {L: ''.join(sorted(v)) for L, v in bench.ENDINGS.items()},
           'anchors': bench.TEXT_ANCHORS, 'animals': animals, 'keys': keys,
           'classes': bench.CLASS}
    path = os.path.join(HERE, '..', 'docs', 'indus_bench.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, separators=(',', ':'))
    print('wrote', path, os.path.getsize(path), 'bytes;', len(texts), 'lines;',
          {L: len(v) for L, v in lex.items()}, 'keys', list(keys))


if __name__ == '__main__':
    main(*sys.argv[1:4])
