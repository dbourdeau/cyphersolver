"""Build key.tsv from Brice Dudout's key v6 (targets/pandolfini1514/key_v6.json) plus our shape aliases.
python scripts/make_key.py ../pandolfini1514/key_v6.json out.tsv
key_frozen.tsv is this output with one FROZEN comment line on top; key.tsv adds the row for Φ."""
import json, sys
k = json.load(open(sys.argv[1], encoding='utf-8'))
ALIAS = {'H': '4#', 'δ': 'G', 'δ#': 'G#'}   # our shape names -> Dudout's token names (same shapes)
rows = []
for v, s in k['vowels'].items(): rows.append(('vowel', v, s, 'v6'))
for b, s in k['base'].items(): rows.append(('base', b, s, 'v6'))
for t, s in k['tokens'].items(): rows.append(('token', t, s, 'v6'))
for c, s in k['codes'].items(): rows.append(('code', c, s, 'v6'))
for a, b in ALIAS.items(): rows.append(('alias', a, b, 'shape alias'))
rows.append(('null', 'V^0', '', 'v6 (V^0 = nothing)'))
rows.append(('null', 'Θ', '', 'block-end mark'))
with open(sys.argv[2], 'w', encoding='utf-8', newline='\n') as f:
    f.write('# kind\tsign\tvalue\tsource\n')
    for r in rows: f.write('\t'.join(r) + '\n')
print(len(rows), 'rows')
