"""Decrypt R478 (Bay to Rakoczi, 8 Mar 1706) with Rakoczi's key DECODE R609 (G15 C 43/56)."""
import re, sys
from score_keys import parse_key
k = parse_key('keys/DOC_R609_D2784_2784.txt')
k['59'] = 'ho'   # R609 lists 59 as both U and ho; ho reads (Vilnahoz)
k['50'] = 'ba'   # not in R609; 'barat' (50 ra t) -- context value
for x in ('15','16','17','18','19','200','300'): k[x] = '<NULL>'   # R609 null line (with Ψ, +)
t = open('R478_transcription.txt', encoding='utf-8').read()
out, n, read = [], 0, 0
for part in re.split(r'(<[^>]*>)', t):
    if part.startswith('<'):
        if 'CLEARTEXT' in part: out.append(' «' + part.split(' ', 2)[-1][:-1] + '» ')
        continue
    part = '\n'.join(l for l in part.splitlines() if not l.startswith('#'))
    for g in re.split(r'[,.\n]', part):
        g = g.replace(' ', '').replace('i', '1').replace('I', '1')
        if re.fullmatch(r'\d+', g):
            n += 1; v = k.get(str(int(g)))
            if v: read += 1
            out.append('·' if v == '<NULL>' else ('[' + v + ']' if v and len(v) > 3 else (v or '{' + g + '}').lower()))
        elif g.strip(): out.append(g)
print(''.join(out))
print(f'groups {n}, with a key value {read} ({read/n:.1%}); 50 is a context value', file=sys.stderr)
