# Key-free check of the 15 Oct transcription: machine shape labels (no language, no key used in labelling)
# passed through key.tsv and aligned with the final decryption; shuffled tables as control.
import re, random, numpy as np, subprocess, sys, difflib
key={}
for l in open('key.tsv',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    p=l.rstrip('\n').split('\t'); key[p[0]]=p[1]
M={}
for l in open('pass_A_machine.txt',encoding='utf8'):
    t=l.split(); M[t[0]]=[x.rstrip('?') for x in t[1:] if x.rstrip('?')!='|']
E_={}
for l in open('transcription_15oct_ff34r-35v.txt',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    t=l.split(); E_[t[0]]=[x.split('{')[0].lstrip('^') for x in t[1:]]
def dec(sq,k): return ''.join(k.get(x,'?') for x in sq if k.get(x,'?')!='null')
tot=match=0; rows=[]
mc=[];ec=[]
for ln,e in E_.items():
    m=M.get(ln.split('.')[0]+'.'+ln.split('.')[1],[])
    mc+=m; ec+=e
sm=difflib.SequenceMatcher(None,ec,mc,autojunk=False)
same=sum(b.size for b in sm.get_matching_blocks())
print('signs eye',len(ec),'machine',len(mc),'same in order',same,round(same/len(ec),3))
def lcs(a,b):
    A=np.frombuffer(a.encode(),dtype=np.uint8); prev=np.zeros(len(A)+1,dtype=np.int32)
    for ch in b.encode():
        d=prev[:-1]+(A==ch)
        c=np.maximum(d,prev[1:]); c=np.concatenate([[0],c]); c=np.maximum.accumulate(c); prev=c
    return int(prev[-1])
F=dec(ec,key); D=dec(mc,key)
print('letters final',len(F),'machine decrypted',len(D),'LCS',lcs(F,D),round(lcs(F,D)/len(F),3))
random.seed(7); keys=list(key); vals=[key[k] for k in keys]; ctl=[]
for i in range(200):
    v=vals[:]; random.shuffle(v); k=dict(zip(keys,v)); d=dec(mc,k); ctl.append(lcs(F,d)/len(F))
print('shuffled tables mean',round(float(np.mean(ctl)),3),'max',round(max(ctl),3))
print(D[:400])
