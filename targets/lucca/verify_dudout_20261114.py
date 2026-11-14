"""Independent check of R2159 (lucca), 14 Nov 2026 (Brice Dudout, Claude Opus 5.5).

    python3 targets/lucca/verify_dudout_20261114.py

Reads only texts/key.md (the key table) and ct.txt (the corrected transcription); does not use decode.py,
validation.tsv or the annealers. Decodes each group with the single letter of the key, then aligns the result
with plaintext.txt letter by letter and lists every place where they differ.
"""
import difflib, pathlib, re, unicodedata
D = pathlib.Path(__file__).resolve().parent
rows = [l for l in (D / 'texts' / 'key.md').read_text(encoding='utf8').splitlines() if l.startswith('| ')]
fig = [c.strip() for c in rows[0].strip('|').split('|')][1:]
let = [c.strip().strip('*') for c in rows[1].strip('|').split('|')][1:]
key = dict(zip(map(int, fig), let))
ct = [int(t) for t in (D / 'ct.txt').read_text().split()]
dec = ''.join(key[t] for t in ct)
def norm(s):
    s = re.sub(r'\[[^\]]*\]|\{[^}]*\}', '', s)                   # editorial marks: compare cipher letters only
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalpha() and not unicodedata.combining(c)).replace('v', 'u')
pt = norm((D / 'plaintext.txt').read_text(encoding='utf8'))
print('groups', len(ct), 'distinct', len(set(ct)), 'figures without a value', sorted(set(ct) - set(key)))
print('decoded letters', len(dec), 'reading letters', len(pt))
sm = difflib.SequenceMatcher(None, dec, pt, autojunk=False)
same = sum(b.size for b in sm.get_matching_blocks())
print('letters equal', same, round(same / len(dec), 4))
pos = 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op != 'equal':
        print(f'  {op:7} group {i1+1:3}  key {dec[i1:i2]!r:6} reading {pt[j1:j2]!r:6}  ...{dec[max(0,i1-6):i2+6]}...')
