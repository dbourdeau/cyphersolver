import sys
from asac import *
def msvc(seed=1):
    s=seed
    while True:
        s=(s*214013+2531011)&0xFFFFFFFF; yield (s>>16)&0x7FFF
def glibc(seed=1):
    r=[0]*34; r[0]=seed
    for i in range(1,31):
        hi,lo=divmod(r[i-1],127773); w=16807*lo-2836*hi
        if w<0: w+=2147483647
        r[i]=w
    for i in range(31,34): r[i]=r[i-31]
    o=[]; 
    for i in range(34,344): r.append((r[i-31]+r[i-3])&0xFFFFFFFF)
    i=344
    while True:
        r.append((r[i-31]+r[i-3])&0xFFFFFFFF); yield (r[i]>>1); i+=1
key=[int(c) for c in '24181941454348833609']
sq=square(key[:10],key[10:])
d=open('c01.txt').read().strip()
cells=[int(d[i])+10*int(d[i+1]) for i in range(0,len(d),2)]
for name,g in [('msvc',msvc()),('glibc',glibc())]:
    ok=0
    for idx in cells:
        r=next(g)%100; ch=sq[idx]
        n=0
        while sq[(r+n)%100]!=ch: n+=1
        ok+= ((r+n)%100==idx)
    print(name, ok, len(cells))
import collections,math
g=msvc(); dy=collections.Counter(); dx=collections.Counter(); dd=collections.Counter()
for idx in cells:
    r=next(g)%100
    dy[(idx//10 - r//10)%10]+=1; dx[(idx%10 - r%10)%10]+=1; dd[(idx-r)%100]+=1
n=len(cells)
print('dy',[round(dy[i]/n,3) for i in range(10)])
print('dx',[round(dx[i]/n,3) for i in range(10)])
print('KL y (log10)',sum(dy[i]/n*math.log10(dy[i]/n/0.1) for i in range(10) if dy[i]), 'KL x', sum(dx[i]/n*math.log10(dx[i]/n/0.1) for i in range(10) if dx[i]))
print('d mean',sum(k*v for k,v in dd.items())/n, 'max', max(dd))
