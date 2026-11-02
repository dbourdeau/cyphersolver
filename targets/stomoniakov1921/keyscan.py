"""Scan text files for a window whose letters sort into message A's key rank pattern (ties left to right)."""
import sys,re,json,glob,os
rank=[2,5,21,17,19,0,15,8,11,4,14,16,12,7,23,22,6,1,9,10,13,18,20,3]
w=len(rank)
def pattern(s):
    idx=sorted(range(len(s)),key=lambda i:(s[i],i));r=[0]*len(s)
    for k,i in enumerate(idx): r[i]=k
    return r
def scan(f,cyr=False):
    t=open(f,encoding='utf-8',errors='replace').read().lower()
    s=re.sub('[^а-я]' if cyr else '[^a-z]','',t);best=(0,'')
    # quick check: order constraint rank[5]==0 means position 5 holds the minimum
    for i in range(len(s)-w):
        win=s[i:i+w]
        if win[5]!=min(win): continue
        p=pattern(win);m=sum(a==b for a,b in zip(p,rank))
        if m>best[0]: best=(m,win)
        if p==rank: print('EXACT',f,i,win,flush=True)
    return len(s),best
fs=sys.argv[1:]
for f in fs:
    n,b=scan(f,cyr='ru_' in f);print(os.path.basename(f),n,'best match',b[0],'/',w,b[1],flush=True)
