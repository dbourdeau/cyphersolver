# List every occurrence of the key gaps in transcription 2, by aligning each decoded sign to the 19th-century text.
import json
import os as _os, sys as _sys; _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))  # so that python3 -I finds common.py
from common import *
from decode import VAL, value, reftext, norm
T=load(O+'transcription_T2.txt')
items=[]  # (set, line, pos, code)
for k in sorted(T):
    for p,t in enumerate(T[k],1):
        c=norm(t); cc=c.lower() if (t.startswith('{') or c.lower()=='ras') else c
        vs=value(cc,VAL)
        if not vs: items.append((None,k,p,c)); continue
        for v in vs:
            if v=='§': continue
            items.append(({x.replace('j','i').replace('v','u') for x in v},k,p,c))
words=reftext(); ref=''.join(w for w in words if w!='sultanum')
# word index per ref letter
widx=[]; 
for wi,w in enumerate([w for w in words if w!='sultanum']): widx+= [wi]*len(w)
W=[w for w in words if w!='sultanum']
seq=[it for it in items if it[0] is not None]
a=[s[0] for s in seq]; b=ref; n,m=len(a),len(b)
import numpy as np
D=np.zeros((n+1,m+1),dtype=np.int32); D[:,0]=-np.arange(n+1); D[0,:]=-np.arange(m+1)
for i in range(1,n+1):
    for j in range(1,m+1):
        D[i,j]=max(D[i-1,j-1]+(1 if b[j-1] in a[i-1] else -1),D[i-1,j]-1,D[i,j-1]-1)
i,j=n,m; pairs=[]
while i>0 and j>0:
    if D[i,j]==D[i-1,j-1]+(1 if b[j-1] in a[i-1] else -1): pairs.append((i-1,j-1)); i-=1;j-=1
    elif D[i,j]==D[i-1,j]-1: pairs.append((i-1,None)); i-=1
    else: pairs.append((None,j-1)); j-=1
pairs=pairs[::-1]
out={'g_sign':[], 'figure8':[], 'x':[], 'unaligned_signs':[], 'dropped_as_null':[]}
for si,rj in pairs:
    if si is None: continue
    s,k,p,c=seq[si]
    word=W[widx[rj]] if rj is not None else None
    if c=='??': out['g_sign'].append(f'{k} sign {p}: plaintext {b[rj] if rj is not None else "-"} in "{word}"')
    if c=='8': out['figure8'].append(f'{k} sign {p}: plaintext {b[rj] if rj is not None else "-"} in "{word}"')
    if rj is not None and b[rj]=='x': out['x'].append(f'{k} sign {p} [{c}] in "{word}"')
    if rj is None: out['unaligned_signs'].append(f'{k} sign {p} [{c}]')
for s,k,p,c in items:
    if s is None: out['dropped_as_null'].append(f'{k} sign {p} [{c}]')
json.dump(out,open(O+'key_gap_occurrences.json','w',encoding='utf-8',newline='\n'),indent=1)
for kk,v in out.items(): print(kk,len(v)); print('  '+'\n  '.join(v[:40]))
from collections import Counter
conf=Counter(); occ={}
for si,rj in pairs:
    if si is None or rj is None: continue
    s,k,p,c=seq[si]
    if b[rj] not in s:
        conf[(c,'/'.join(sorted(s)),b[rj])]+=1; occ.setdefault((c,b[rj]),[]).append(f'{k}.{p} "{W[widx[rj]]}"')
print('MISMATCHES code,keyvalue,plain:')
for (c,v,pl),nn in conf.most_common(): print(f'  {c} ={v} read as {pl}: {nn}  ', '; '.join(occ[(c,pl)][:12]))
gaps_ref=[ (j,b[j],W[widx[j]]) for si,j in pairs if si is None and j is not None]
print('ref letters with no sign:',len(gaps_ref), [f'{l} in {w}' for _,l,w in gaps_ref])
out['mismatches']={f'{c} (key {v}) for {pl}':occ[(c,pl)] for (c,v,pl),nn in conf.most_common()}
out['plaintext_letters_without_sign']=[f'{l} in "{w}"' for _,l,w in gaps_ref]
json.dump(out,open(O+'key_gap_occurrences.json','w',encoding='utf-8',newline='\n'),indent=1)
