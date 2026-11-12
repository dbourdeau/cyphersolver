# Held-out check: keep only key entries whose cipher sign occurs in lines 01-10; decode lines 11-19 with that restricted key.
import sys,re
key={}
for l in open('work/KEY_B.txt'):
    if l.startswith('#'): continue
    for p in l.split(): a,b=p.split('='); key[a]=b
segs=[l.rstrip('\n').split('|') for l in open('tx/units_443R.seg') if not l.startswith('#')]
A=[s for s in segs if int(s[0])<=10]; B=[s for s in segs if int(s[0])>10]
symsA=set(ch for s in A if not s[1].isdigit() for ch in s[1] if ch!='-')
rk={k:v for k,v in key.items() if k in symsA}
print('signs in key',len(key),'; signs seen in lines 01-10',len(symsA),sorted(symsA),'; key signs absent from 01-10',sorted(set(key)-symsA))
full=0;S=0;words=0;miss=[]
for s in B:
    if s[1].isdigit(): continue
    words+=1
    d=''.join(rk.get(ch,'?') for ch in s[1] if ch!='-')
    if '?' not in d:
        full+=1
        if s[3]=='S': S+=1
    else: miss.append((s[1],d))
n=len(B)
print('lines 11-19: units',n,'of which cipher words',words,'; fully decoded by the restricted key',full,'; of those labelled S',S,'-> held-out strict %d/%d = %.2f%%'%(S,n,100*S/n))
print('not fully decoded:',miss)
