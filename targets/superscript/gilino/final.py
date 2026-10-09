import re
exec(open('dec.py').read().split('n=int(')[0])
K.update({'bf':'l','m':'t','S':'r','o.28':'t','b+':'o','np':'i','ut':'a','th':'a','+':'e','xo':'s','6':'n','mp':'g','pb':'i','q':'q','iy':'a',
 '6.2w':'to','SS':'e','xp':'v','44':'r','R':'p','dots':'h','gf':'f','36':'n','20':'b','lam':'b','pi':'m','oto':'c',
 'a++':'','Hvv':'','vv':'','P.25':'','x':''})
lines=[]
for line in open(r'C:\Users\dbour\cypher\targets\superscript\r8572_tokens.txt',encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    lines.append(re.sub(r'\bo t o\b','oto',line.strip()))
out=[]
for l in lines:
    s=''
    for t in l.split():
        u=t.rstrip('?')
        if u.startswith('{') or u.endswith('}'): s+=' '+t+' '; continue
        s+= K[u] if u in K else '['+t+']'
    out.append(s)
open('r8572_test_decrypt.txt','w',encoding='utf-8').write('\n'.join(out))
import sys
for s in out[:int(sys.argv[1])]: print(s)
