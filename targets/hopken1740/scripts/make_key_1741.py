"""key_1741.tsv = key.tsv (the hopken1740 key, unchanged) + values read from the gloss of Lit. A (image R0003635_00147)
+ two corrections of single values from the same gloss. Run from this folder: python scripts/make_key_1741.py"""
rows = [l.rstrip('\n').split('\t') for l in open('key.tsv', encoding='utf-8') if l.strip() and not l.startswith('#')]
key = {r[0]: r for r in rows}
CHANGED = {'1504': ('vo', 'voulu, savoir, pouvoir in the 1741a gloss (frozen: r, single)'),
           '1840': ('au', 'auparavant, auquel in the 1741a gloss; u = v (frozen: a, single)')}
for g, (v, ev) in CHANGED.items():
    key[g] = [g, v, key[g][2], key[g][3], 'changed_1741a', 'frozen ' + key[g][1] + '; ' + ev]
for l in open('scripts/gloss_values.tsv', encoding='utf-8'):
    g, v, ev = l.rstrip('\n').split('\t')
    assert g not in key, g
    key[g] = [g, v, '', '', 'gloss_1741a', ev]
with open('key_1741.tsv', 'w', encoding='utf-8') as f:
    f.write('# group\tvalue\tseen\tagree\tstatus\tother\n')
    for g in sorted(key): f.write('\t'.join(key[g]) + '\n')
print(len(key), 'groups;', sum(1 for r in key.values() if r[4] == 'gloss_1741a'), 'new from the 1741a gloss;', len(CHANGED), 'changed')
