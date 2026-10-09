"""Build docs/reveal/hesse1672.json from ct.txt with decrypt.py (key 255 letter table) plus the glossed codes."""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from decrypt import dec
# readings that depart from the bare table (see NOTES): slips and look-alike signs
OVERRIDE = {('2', 1): ('g', 'unc'), ('2', 11): ('ll', 'unc'), ('2', 18): ('au', 'unc'), ('2', 19): ('ff', 'unc')}
OPEN = {('1', i) for i in (12, 13, 14, 15, 16)}
SPACE = {'1': {8, 11, 16, 18}, '2': {0, 3, 6, 9, 11, 14}}
toks = []; p = 0
for line in open(os.path.join(here, 'ct.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    p += 1
    if p == 1: toks.append({'g': '', 'p': 'Totaliter ', 'cls': 'plain'})
    else: toks.append({'g': '', 'p': ' — insidiosus hostis ', 'cls': 'plain'})
    for i, t in enumerate(line.split()):
        v = dec(t); cls = ''
        if t.startswith('['): 
            if t[1:-1].isdigit(): v, cls = v.strip('<>'), 'code'
            t = t.strip('[]')
        if (str(p), i) in OVERRIDE: v, cls = OVERRIDE[(str(p), i)]
        if (str(p), i) in OPEN: cls = 'unc'
        toks.append({'g': t, 'p': v, 'cls': cls})
        if i in SPACE[str(p)]: toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
out = {'slug': 'hesse1672', 'anchor': 'the-passages', 'title': 'The two letter-cipher passages of f. 4r',
       'caption': 'Each sign deciphered with the letter table of HCPortal key 255; codes from the glosses on the leaf. Uncertain values marked; the five signs e r t a d make no word.',
       'unit': 'sign', 'key_note': 'HCPortal key 255 (HStAM 4 d Nr. 1234), letter table; st and tt are syllable signs', 'tokens': toks}
json.dump(out, open(os.path.join(here, '..', '..', 'docs', 'reveal', 'hesse1672.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(' '.join(f"{x['g']}={x['p']}" for x in toks))
