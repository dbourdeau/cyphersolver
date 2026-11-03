"""decode_any.py FILE: decode a cipher group file (lines 'LABEL: g g g') with key_bouille.tsv; [g] = no value."""
import sys, re
key = {}
for l in open('key_bouille.tsv', encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    if len(p) > 1 and p[0].isdigit(): key[p[0]] = p[1].split('/')[0]
tot = val = 0
for l in open(sys.argv[1], encoding='utf8'):
    if l[0] == '#' or ':' not in l: continue
    lab, body = l.split(':', 1)
    out = []
    for g in body.split():
        g = g.rstrip("?")
        if g == "|": continue
        tot += 1
        if g in key: val += 1; out.append(key[g])
        else: out.append('[' + g + ']')
    print(lab, ' '.join(out))
print('groups', tot, 'valued', val, '= %.1f%%' % (100 * val / max(tot, 1)))
