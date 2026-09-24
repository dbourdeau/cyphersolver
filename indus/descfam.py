"""Graphic families from Parpola's sign descriptions (set 208): ICIT sign -> M77 (data/icit_m77_map.tsv) -> CISI
description (data/cisi_signs.tsv, mayig digitisation) -> the first shape noun of the description (articles, numbers
and adjectives dropped, plural -s stripped). Signs without a description keep their own id."""
import csv
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
STOP = set('a an the with of and or on in at to by from its it is as for one two three four five six seven eight nine '
           'ten single simple classic small large big long short tall full-height half-height top-aligned bottom-aligned '
           'adjacent vertical horizontal diagonal double triple thin thick wide narrow upper lower left right top bottom '
           'inner outer open closed extra possibly perhaps unknown like shaped similar stacked upside-down slightly squashed '
           'semi-realistic several multiple but facing decorated asymmetric flowering trifurcated isocele isocolese '
           'realistic rotated mirrored prismed'.split())


def families():
    m = {r[0]: r[1] for r in csv.reader(open(os.path.join(HERE, 'data', 'icit_m77_map.tsv'), encoding='utf-8'), delimiter='\t') if r and r[0] != 'icit'}
    desc = {}
    for r in csv.DictReader((l for l in open(os.path.join(HERE, 'data', 'cisi_signs.tsv'), encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        for mm in r['mahadevan'].split(','):
            x = re.sub(r'\D', '', mm)
            if x:
                desc.setdefault(x.lstrip('0'), r['description'])
    out = {}
    for g, mm in m.items():
        x = re.sub(r'\D', '', mm).lstrip('0')
        d = desc.get(x)
        if not d:
            continue
        for w in re.findall(r"[a-z\-']+", d.lower()):
            if w not in STOP and len(w) > 1:
                out[g] = 'd:' + re.sub(r's$', '', w)
                break
    return out
