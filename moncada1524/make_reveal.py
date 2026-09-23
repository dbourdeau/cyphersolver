"""Build docs/reveal/moncada1524.json from the EM alignment (em_align.py) of runs 9-12.

Clear text between the runs is taken from the letter. A sign whose aligned value is not its most frequent value
in the whole letter is marked 'unc'; a sign aligned to nothing is 'null'."""
import json, os, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import em_align as E

runs = [r for r in E.load() if r[2] != '?']
signs = sorted({t for _, toks, _ in runs for t in toks})
letters = sorted({c for _, _, p in runs for c in E.norm(p) if c != '*'})
emit = {t: {c: 1.0 / len(letters) for c in letters} for t in signs}
for _ in range(12):
    counts = defaultdict(lambda: defaultdict(float))
    for rid, toks, p in runs:
        for t, s in E.align(toks, E.norm(p), emit)[1]:
            if t is not None and s != '?':
                counts[t][s] += 1
    for t in signs:
        tot = sum(counts[t].values()) + 0.5
        emit[t] = {s: (c + 0.01) / tot for s, c in counts[t].items()}
        emit[t].setdefault('', 0.01 / tot)
top = {t: max(c.items(), key=lambda x: x[1])[0] for t, c in counts.items() if c}

CLEAR = {'9': '', '10': ', lo que siendo en Genoua ', '11': ' se entendera mas ', '12': '.'}
out = []
for rid in ['9', '10', '11', '12']:
    toks, p = next((t, p) for r, t, p in runs if r == rid)
    ends, n = set(), 0
    for w in p.split():
        n += len(E.norm(w)); ends.add(n)
    pos = 0
    for t, s in E.align(toks, E.norm(p), emit)[1]:
        if t is None:
            pos += len(s)
            if s and out and out[-1].get('g') == 'lay':
                continue
            if pos in ends:
                out.append({'g': '', 'p': ' ', 'cls': 'plain'})
            continue
        pos += len(s)
        if s == '':
            out.append({'g': t, 'p': '·', 'cls': 'null'})
        elif t == 'lay':  # code group for 'yo'; the aligner scores it as one letter plus a skip
            tok = {'g': t, 'p': 'yo', 'cls': 'code'}
            out.append(tok)
        else:
            tok = {'g': t, 'p': s}
            if top.get(t) != s:
                tok['cls'] = 'unc'
            out.append(tok)
        if s and pos in ends and pos != n:
            out.append({'g': '', 'p': ' ', 'cls': 'plain'})
    if CLEAR.get(rid):
        out.append({'g': '', 'p': CLEAR[rid], 'cls': 'plain'})

doc = {
    'slug': 'moncada1524',
    'anchor': 'reading',
    'title': 'Monaco, 6 October 1524: cipher lines 11-13',
    'caption': "Hugo de Moncada to Charles V, BNE MSS/20213/12 f. 1r, cipher lines 11-13, decoded sign by sign with the key rebuilt against the 1854 print (Biblioteca Nacional de España, via DECODE R1191).",
    'unit': 'signs',
    'key_note': "Sign names as in ct.txt; 'unc' marks a sign read with a value other than its commonest one in the letter (a homophone collision or a slip), 'null' a sign the alignment leaves without a value.",
    'tokens': out,
}
json.dump(doc, open('../docs/reveal/moncada1524.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(len([t for t in out if t['g']]), 'signs;', sum(1 for t in out if t.get('cls') == 'unc'), 'unc')
