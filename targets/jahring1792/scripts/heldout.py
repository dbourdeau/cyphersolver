"""Held-out test. The key (Porta table + keyword) was frozen after a test on the first 22 letters of run 120.5 only;
every run in runs.json is held out. Per mechanical letter position we compare the decryption with the final reading
(holes left out; positions under {x/y} count as wrong). Controls: the same keyword with Vigenere and Beaufort tables.
Frozen key as frozen: the looped d-shape taken as d (as in pass 1) and the dot dropped."""
import json, re, string, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from decrypt import load_key, porta, HERE, A
from check_marks import TOK

def target(reading):
    # list of (mechanical letter, reading letter or None for hole)
    out = []
    for m in TOK.finditer(reading):
        if m.group(1): out.append((m.group(1), m.group(2)))
        elif m.group(4): out += [(c, None) for c in m.group(4)]
        elif m.group(5): out.append((m.group(5), m.group(5)))
    return out

def letters(signs, sv):
    s = re.sub(r'\[[^\]]*\]', '', signs)
    return ''.join(c if c in A else sv.get(c, '') for c in s)

vig = lambda c, k: A[(A.index(c) - A.index(k)) % 26]
beau = lambda c, k: A[(A.index(k) - A.index(c)) % 26]
kw, sv = load_key()
rows = json.load(open(HERE / 'runs.json', encoding='utf8'))
for label, smap in [('working key (ð=f, •=o)', sv), ('frozen key as frozen (ð=d, • dropped)', {'ð': 'd'})]:
    for tname, f in [('porta', porta), ('vigenere', vig), ('beaufort', beau)]:
        tot = ok = 0
        for doc, run, signs, reading, *_ in rows:
            tg = [t for t in target(reading)]
            ct = letters(signs, smap)
            for i, c in enumerate(ct):
                if i >= len(tg) or tg[i][1] is None: continue
                tot += 1; ok += f(c, kw[i % 20]) == tg[i][1]
        print(f'{label:40s} {tname:9s} {ok}/{tot} = {ok/tot:.3f}')
