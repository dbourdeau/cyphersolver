import re,collections,json,math,sys
c=open('../../../sforza1597/ctts/lm_qc/italian.txt',encoding='utf-8',errors='ignore').read().lower().replace('u','v').replace('j','i')
cnt=collections.Counter(re.findall('[a-z]+',c)); N=sum(cnt.values())
W={w:math.log(n/N) for w,n in cnt.items() if 2<=len(w)<=13 and n>=3}
def seg(s):  # DP word segmentation; unknown char penalty
    n=len(s);b=[0]+[-1e9]*n
    for i in range(n):
        if b[i]<=-1e9: continue
        if b[i]-14>b[i+1]: b[i+1]=b[i]-14
        for L in range(2,14):
            w=s[i:i+L]
            if len(w)<L: break
            if w in W and b[i]+W[w]>b[i+L]: b[i+L]=b[i]+W[w]
    return b[n]
def key(f):
    k={}
    for l in open(f):
        m=re.match(r'^(\S+) - (\S)$',l.strip())
        if m:
            for s in m.group(1).split('|'): k[s]=m.group(2).lower()
    return k
L=[l.split() for l in open('t3.txt').read().strip().split('\n')]
TR=L[:37]; HO=L[37:]   # R5518+R5514 train, R5517 holdout
def score(k,lines): return sum(seg(''.join(k.get(x,'x') for x in l)) for l in lines)
k=key('ja.txt'); k['r']='b'
for s in set(t for l in L for t in l): k.setdefault(s,'x')
syms=sorted(set(t for l in TR for t in l),key=lambda s:-sum(l.count(s) for l in TR))
best=score(k,TR); print('start train',round(best),'holdout',round(score(k,HO)))
for sweep in range(3):
    ch=0
    for s in syms:
        cur=k[s];bl=cur
        for a in 'abcdefghilmnopqrstvxz':
            k[s]=a; v=score(k,TR)
            if v>best+1: best=v;bl=a
        k[s]=bl
        if bl!=cur: ch+=1; print(' ',s,cur,'->',bl,round(best),flush=True)
    print('sweep',sweep,'changes',ch,'train',round(best),'holdout',round(score(k,HO)),flush=True)
    if not ch: break
json.dump(k,open('key_ref.json','w'))
