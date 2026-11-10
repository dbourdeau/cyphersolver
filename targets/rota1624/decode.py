"""Decode transcription.txt with key.tsv -> reading.txt; print token counts."""
import re, os, io
d = os.path.dirname(os.path.abspath(__file__))
L = {'10':'a','90':'e','30':'i','40':'o','50':'u','21':'f','22':'r','31':'b','32':'n','41':'c','51':'g',
     '71':'h','81':'l','91':'m','92':'t','94':'s','20':'n','70':'o'}
S = {'q':'che','t':'non','p':'per','z':'se','&':'et',"p'":'però'}
n = dict(letters=0, letters_read=0, ticked=0, bar=0, signs=0, signs_read=0)
out = []
CODES = {'64'}; PFX = {'g','c','m'}
for line in io.open(os.path.join(d, 'transcription.txt'), encoding='utf-8'):
    if line.startswith('#'): continue
    res = []; prev_cipher = False; after_pfx = False
    for tok in line.split():
        m = re.fullmatch(r"(\d\d)(['^]?)", tok)
        s = re.fullmatch(r"\{(.+)\}", tok)
        if m:
            g, mark = m.groups()
            if mark == "'": n['ticked'] += 1; res.append(' [%s’]' % g); prev_cipher = False
            elif mark == '^': n['bar'] += 1; res.append('[%s]' % g); prev_cipher = False
            elif g in CODES or after_pfx: n['ticked'] += 1; res.append(' [%s]' % g); prev_cipher = False
            else:
                n['letters'] += 1
                if g in L: n['letters_read'] += 1; v = L[g]
                else: v = '[%s]' % g
                res.append(('' if prev_cipher else ' ') + v); prev_cipher = True
        after_pfx = bool(s and s.group(1) in PFX)
        if m: pass
        elif s:
            n['signs'] += 1; k = s.group(1)
            if k in S: n['signs_read'] += 1; res.append(' ' + S[k])
            else: res.append(' {%s}' % k)
            prev_cipher = False
        else:
            res.append(' ' + tok); prev_cipher = False
    out.append(''.join(res).strip())
io.open(os.path.join(d, 'decode_raw.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(n)
