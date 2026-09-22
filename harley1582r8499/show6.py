import sys, json, re
from pinrun6 import NULLS, CODES, PIN
key=json.load(open(sys.argv[1]))['key']
def dec(t):
    b=t.strip('.')
    if b in NULLS: return '_'
    if b in CODES: return '['+CODES[b]+']'
    if b in PIN: return PIN[b]
    return key.get(t, key.get(b,'?'))
import solve
for l in open('transcription.txt',encoding='utf8'):
    if not l.startswith('p'): continue
    lab,body=l.split(' ',1)
    out=[]
    for part in re.split(r'(\[[^\]]*\])',body):
        if part.startswith('['): out.append(' '+part.upper()+' '); continue
        r0=part.split()
        r=[t for j,t in enumerate(r0) if t!=':' and not (t=='.' and j>0 and r0[j-1]==':')]
        i=0
        while i<len(r):
            t=r[i]
            if t=='.': i+=1; continue
            pre=i>0 and r[i-1]=='.' and not (i>1 and r[i-2] in solve.TRAIL)
            post=i+1<len(r) and r[i+1]=='.' and t not in solve.TRAIL
            tt=('.' if pre else '')+t+('.' if post else '')
            out.append(dec(tt)); i+=1
    print(lab, ''.join(out))
