"""Cretan Hieroglyphic sign groups against Linear A words.

Cretan Hieroglyphic (CHIC, Olivier and Godart 1996) was written on Crete before and beside Linear A. Its
sign groups are read here with values carried over from Linear A by *shape*, as tabulated in CHIC p. 19 and
set out in J. Younger's Hieroglyphic grid 1 (archived pages, 2007): certain and probable identifications only.
Younger's own grid 2, which partly rests on proposed word matches, is used only as a sensitivity check,
since matches found with it would be partly circular.

Sign groups: every entry of Younger's Hieroglyphic Lexicon (archived 2012), in CHIC sign numbers. A group is
readable if every sign has a value; readable groups of 2+ and 3+ signs are matched exactly against Linear A
word types. Null: Linear A sign values shuffled within frequency bins (as soundvalues.py), 5,000 runs.
"""
from collections import Counter
import html
import json
from pathlib import Path
import random
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lang_test as L  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CH = ROOT / 'data/chic'

GRID1_CERTAIN = {'042': 'a', '038': 'ja', 'catface': 'ma', '012': 'mu', '024': 'ni', '039': 'pa3', '058': 'pu',
                 '031': 're', '070': 'ro', '092': 'ru', '019': 'sa', '025': 'te', '041': 'wa'}
GRID1_PROBABLE = {'062': 'na', '052': 'ne', '006': 'nwa', '021': 'pi', '096': 'qa', '093': 'ti', '045': 'ze',
                  '007': 'mi'}
GRID1_POSSIBLE = {'094': 'e', '017': 'au', '043': 'so', '035': 'su', '085': 'wi', '069': 'ra2', '050': 'ti'}
GRID2 = {'009': 'a', '008': 'a', '014': 'i', '064': 'da', '054': 'de', '078': 'do', '053': 'ja', '072': 'ka',
         '055': 'ke', '057': 'ki', '016': 'ki', '051': 'ki', '044': 'ko', '056': 'ku', '028': 'ku', '073': 'ku',
         '029': 'ma', '013': 'mu', '063': 'pa', '030': 'pu', '047': 'qe', '095': 'ra', '027': 'ra', '018': 'ra',
         '032': 're', '010': 'ri', '040': 'ro', '049': 'ro', '077': 'ru', '036': 'sa', '034': 'si', '011': 'si',
         '023': 'to', '020': 'ai'}


def lexicon_groups():
    t = (CH / 'Lexicon.html').read_bytes().decode('latin-1')
    x = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    x = re.sub(r'\s+', ' ', x)
    groups = Counter()
    for m in re.finditer(r'(?<![\d-])((?:\d{3}|catface)(?:\s*-\s*(?:\d{3}|catface))+)(?![\d-])', x, flags=re.I):
        g = tuple(s.strip().lower() for s in m.group(1).split('-'))
        groups[g] += 1
    return groups


def read(groups, values):
    out = {}
    for g in groups:
        if all(s in values for s in g):
            out[g] = tuple(values[s] for s in g)
    return out


def la_types():
    return {tuple(x.lower() for x in w) for w in L.la_types()}


def test(readable, la, minlen, rng, reps):
    words = {r for r in readable.values() if len(r) >= minlen}
    la_m = {w for w in la if len(w) >= minlen}
    real = sorted(w for w in words if w in la_m)
    freq = Counter(s for w in la_m for s in w)
    signs = sorted(freq, key=lambda s: -freq[s])
    size = -(-len(signs) // 10)
    bins = [signs[i:i + size] for i in range(0, len(signs), size)]
    null = []
    for _ in range(reps):
        mp = {}
        for b in bins:
            v = b[:]
            rng.shuffle(v)
            mp.update(zip(b, v))
        shuffled = {tuple(mp[s] for s in w) for w in la_m}
        null.append(sum(1 for w in words if w in shuffled))
    return {'readable_groups': len(words), 'matches': ['-'.join(w).upper() for w in real],
            'null_mean': round(sum(null) / reps, 3), 'p_ge': round((sum(n >= len(real) for n in null) + 1) / (reps + 1), 4)}


def main(reps=5000, seed=20260923):
    rng = random.Random(seed)
    groups = lexicon_groups()
    la = la_types()
    sets = {'grid 1 certain': GRID1_CERTAIN,
            'grid 1 certain + probable': {**GRID1_CERTAIN, **GRID1_PROBABLE},
            'grid 1 all (incl. possible)': {**GRID1_CERTAIN, **GRID1_PROBABLE, **GRID1_POSSIBLE},
            'grid 1 + Younger grid 2 (partly circular)': {**GRID2, **GRID1_CERTAIN, **GRID1_PROBABLE, **GRID1_POSSIBLE}}
    res = {'method': __doc__.strip(), 'lexicon_groups': len(groups), 'tests': {}}
    for name, values in sets.items():
        readable = read(groups, values)
        res['tests'][name] = {'values': len(values), 'readable_groups_all': len(readable),
                              '2+ signs': test(readable, la, 2, rng, reps), '3+ signs': test(readable, la, 3, rng, reps),
                              'readable_sample': ['-'.join(v).upper() for v in list(readable.values())[:40]]}
    (ROOT / 'reading/chic_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('Lexicon sign groups:', len(groups))
    for name, v in res['tests'].items():
        print(f"== {name}: {v['values']} values, {v['readable_groups_all']} groups fully readable")
        for k in ('2+ signs', '3+ signs'):
            t = v[k]
            print(f"   {k}: {t['readable_groups']} readable, matches {len(t['matches'])} {t['matches']}  null {t['null_mean']}  p {t['p_ge']}")


if __name__ == '__main__':
    main()
