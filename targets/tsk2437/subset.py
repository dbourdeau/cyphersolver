"""Write a line transcription with the signs below a grade replaced by '?'. Usage: python subset.py <final.txt> <out> <min grade: firm|likely>"""
import sys
import tok

rows = tok.parse(sys.argv[1])
keep = {'firm'} if sys.argv[3] == 'firm' else {'firm', 'likely'}
L = {}
for ln, x, c, g, n in rows:
    if c in ('|', '-', '.'):
        L.setdefault(ln, []).append(c)
    else:
        L.setdefault(ln, []).append(c if g in keep else '?')
with open(sys.argv[2], 'w', encoding='utf-8') as f:
    for ln in sorted(L, key=lambda s: int(s[1:])):
        f.write('%s: %s\n' % (ln, ' '.join(L[ln])))
