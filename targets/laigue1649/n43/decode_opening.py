"""Decode the unglossed opening of no. 43 (f. 117r ll. 0-11).
Values come from three sources, recorded per number:
  G = majority interlinear gloss on ff. 117v-118v (key43.txt, built by buildkey.py from pairs_c*.txt)
  S = structure of the code (four interleaved single-letter alphabets 3-25 up, 28-50 down, 51-73 up, ~80-98 down;
      numbers 99-250 are unglossed everywhere = nulls)
  C = context inside the opening (a second syllable series, values fixed by the surrounding words)
An underlined number reverses its syllable (385=ra, 385_=ar), as throughout the glossed pages."""
import re
G = {}
for l in open('key43.txt', encoding='utf-8'):
    n, rest = l.rstrip('\n').split('\t'); G[int(n)] = rest.split()[0].rsplit(':', 1)[0]
S = {37:'o', 38:'n', 46:'e', 59:'i', 80:'t', 81:'s', 86:'n'}
NULL = {99, 119, 129, 150, 206, 207, 222, 229, 230, 237, 240}
C = {279:'de', 277:'do', 354:'ne', 358:'me', 364:'la', 314:'je', 321:'gu', 390:'ru', 398:'que', 400:'pu', 407:'e',
     439:'se', 442:'ti', 443:'te', 445:'su'}
src = {}
def val(n):
    if n in NULL: return '', 'S'
    for d, t in ((S, 'S'), (C, 'C'), (G, 'G')):
        if n in d: return d[n], t
    return f'[{n}]', '?'
out, cnt = [], {'G':0, 'S':0, 'C':0, '?':0}
for line in open('opening_c245.txt', encoding='utf-8'):
    if line.startswith('#'): continue
    lab, body = line.split(':', 1)
    body = re.sub(r'\^\[([^\]]*)\]', r'\1', body)
    s = ''
    for tok in body.split():
        if tok.startswith('#'): s += ' ' + tok[1:] + ' '; continue
        n = int(re.sub(r'\D', '', tok)); v, t = val(n); cnt[t] += 1
        if tok.endswith('_') and v and not v.startswith('['):
            v = v[::-1] if len(v) == 2 else v
        s += v.upper()
    out.append(f'{lab}: ' + re.sub(' +', ' ', s).strip())
open('opening_decoded.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out)); print(cnt)
