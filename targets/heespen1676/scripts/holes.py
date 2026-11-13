"""Write holes.md: every 537L word unit not counted read under key v1, and every sign with no value (own code, standard library).
usage: python3 -I holes.py <folder>"""
import sys, re, collections, pathlib
d = pathlib.Path(sys.argv[1])
def key(p):
    K = {}
    for ln in open(p, encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] == 'tok': K[f[1]] = f[2]
    return K
K1, K2 = key(d / 'gloss/KEY_HB_v1.tsv'), key(d / 'gloss/KEY_HB_v2.tsv')
toks = [t for l in open(d / 'transcriptions/heespen_1676-04-17_537L.txt', encoding='utf-8')
        if l.strip() and not re.search(r'[a-z]{4,}', l) for t in l.split()]
rows = [l.rstrip('\n').split('\t') for l in open(d / 'units/heespen_1676-04-17_537L_v1_ledger.tsv', encoding='utf-8') if not l.startswith('#')]
c = collections.Counter(r[3] for r in rows)
o = ['# Holes: 537L word units not counted read, and signs with no value', '',
     'Written by scripts/holes.py from the frozen transcription, the v1 ledger (figure of record) and both keys.', '',
     f'Units: S {c["S"]} + N {c["N"]} + E {c["E"]} = {len(rows)}. Holes = N + E = {c["N"] + c["E"]}.', '',
     '## 1. Units not read (key v1)', '', '| unit | tokens | decoded | class | unvalued signs in v1 | note |', '|---|---|---|---|---|---|']
for r in rows:
    if r[3] == 'S': continue
    tk = r[1].replace('margin:', '').split()
    o.append(f'| {r[0]} | {" ".join(tk)} | {r[2]} | {r[3]} | {" ".join(t for t in tk if t not in K1) or "-"} | {r[4] if len(r) > 4 else ""} |')
o += ['', '## 2. Signs with no value', '', '| sign | tokens in 537L | no value in v1 | no value in v2 | v2 value (non-blind) |', '|---|---|---|---|---|']
n = collections.Counter(toks)
un1 = un2 = 0
for t in sorted({t for t in toks if t not in K1 or t not in K2}, key=lambda t: (not t.isdigit(), int(t) if t.isdigit() else 0, t)):
    a, b = t not in K1, t not in K2
    un1 += n[t] * a; un2 += n[t] * b
    o.append(f'| {t} | {n[t]} | {"yes" if a else "no"} | {"yes" if b else "no"} | {K2.get(t, "-")} |')
o += ['', f'Unvalued tokens: v1 {un1} of {len(toks)}; v2 {un2} of {len(toks)}.',
      'In v2, codes 9 and 402 are ties in the gloss (9: r 1, t 1; 402: de 1, di 1) and are left unvalued; v1 had 9 = r and no 402.', '',
      '## 3. Why the holes are there', '',
      '- No key material: the key is rebuilt only from the chancery glosses on images 96, 117, 118 (v1) and 240, 241, 320 (v2 adds).',
      '  The other glossed pages of unit 262098 (336, 340, 342, 389, 391, 401, 411, 455, 481, 526, 97-98, 115-116, 119, 145-148, 335, 341)',
      '  were not transcribed. Transcribing them is the way to fill most of these signs.',
      '- No fresh test text: 2,919 images screened in units 262098, 262100, 262102, 262105 and 262107 (628 by b179 + 2,291 by b180)',
      '  found no other bare passage in this code. A bigger key could be checked only on held-out glossed pages, not on new bare text.',
      '- Oldenburg, NLA Best. 20-44 Nr. 8 (catalogue row 602), parallel Klingenberg/Heespen relations with cipher: not digitised, not seen.']
(d / 'holes.md').write_text('\n'.join(o) + '\n', encoding='utf-8')
print(f'holes.md: {c["N"] + c["E"]} hole units; unvalued v1 {un1}, v2 {un2}')
