"""Erving to Madison, 24 Mar 1807: the "watch it decipher" passage for the site (written 14 Oct 2026, page split).

  python targets/erving1807/build_reveal.py

Takes the recorded group runs of erving_groups.txt from "of the march of troops into France" to "of such a project"
(the Hanover offer and the exchange for Gibraltar) and gives each group its value from the Pinckney code as rebuilt
in the sibling entry (targets/erving1807aug/key_pinckney.tsv, which already holds the pairs of this letter, source
E24Mar). The runs are the phrases recorded from the decode, not one unbroken line: a gap between runs is shown as an
ellipsis. A group the key does not list is unknown; a group with two values in the key, or whose value is not in Madison's
decode of that run, is marked uncertain.
Writes docs/reveal/erving1807.json and prints each run next to Madison's decode for checking by eye.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
KEYF = ROOT / 'targets' / 'erving1807aug' / 'key_pinckney.tsv'

key = {}
for line in KEYF.read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or not line.strip(): continue
    cols = line.split('\t')
    vals = [re.sub(r'\(.*?\)', '', v).strip() for v in cols[1].split('/')] if len(cols) > 1 and cols[1].strip() else []
    if not vals and len(cols) > 2 and cols[2].strip(): vals = [cols[2].strip()]
    key[cols[0]] = [v for v in vals if v]

runs = []
for line in (HERE / 'erving_groups.txt').read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or '|' not in line: continue
    g, jm = line.split('|')[:2]
    runs.append((g.strip().split('.'), jm.strip()))
start = next(i for i, (_, jm) in enumerate(runs) if jm.startswith('of the march of troops'))
end = next(i for i, (_, jm) in enumerate(runs) if jm.startswith('of such a project'))

tokens, n, known = [], 0, 0
# holes in Madison's decode closed in NOTES.md: 529 = nov (Hanover); 1497 = al (Gibraltar)
NOTES_FIX = {'529': 'nov', '1497': 'al'}
for i in range(start, end + 1):
    groups, jm = runs[i]
    if tokens: tokens.append({'g': '', 'p': '…', 'cls': 'plain'})
    out = []
    for g in groups:
        n += 1
        v = key.get(g, [])
        if not v and g in NOTES_FIX: v = [NOTES_FIX[g]]
        if not v:
            tokens.append({'g': g, 'p': '?', 'cls': 'unk'}); out.append('?'); continue
        known += 1
        t = {'g': g, 'p': v[0]}
        jml = re.sub(r'[^a-z]', '', jm.lower().replace('mister', 'mr'))
        if len(set(x.lower() for x in v)) > 1 or re.sub(r'[^a-z]', '', v[0].lower()) not in jml: t['cls'] = 'unc'
        tokens.append(t); out.append(v[0])
    print(f'{".".join(groups)}\n  key: {" ".join(out)}\n  JM : {jm}')

data = {
    'slug': 'erving1807',
    'anchor': 'holes',
    'title': 'Erving to Madison, 24 March 1807: the Hanover offer',
    'caption': 'Erving to Madison, Madrid, 24 March 1807, No. 21, in Pinckney\'s legation code, NARA RG 59, M31 reel 12, frames 0284-0285: the recorded runs from the march of troops to the exchange of Hanover for Gibraltar (an ellipsis marks a stretch between runs not recorded group by group).',
    'unit': 'code groups',
    'key_note': 'Values from the Pinckney code as rebuilt in the sibling entry erving1807aug (key_pinckney.tsv), which holds the pairs of this letter; 529 nov and 1497 al are the values that close the holes in Madison\'s decode. Groups the key does not list are shown as ?; groups with two values in the key, or whose value does not appear in Madison\'s decode of the run, are marked uncertain.',
    'tokens': tokens,
}
(ROOT / 'docs' / 'reveal' / 'erving1807.json').write_text(json.dumps(data, ensure_ascii=False) + '\n', encoding='utf-8')
print(f'{n} groups, {known} with a value')
