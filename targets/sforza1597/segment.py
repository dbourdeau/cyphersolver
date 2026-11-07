import re,collections,math,sys
txt=open('src/src/main/resources/italian.txt',encoding='utf-8',errors='ignore').read().lower()
txt=txt.translate(str.maketrans({'à':'a','è':'e','é':'e','ì':'i','ò':'o','ù':'u','j':'i','k':'c','w':'v','y':'i','z':'s'}))
ws=collections.Counter(re.findall('[a-z]+',txt)); N=sum(ws.values())
# normalise like CTTS: u->v, no double letters
def norm(w): w=w.replace('u','v'); return re.sub(r'(.)\1+',r'\1',w)
nw=collections.Counter()
for w,c in ws.items(): nw[norm(w)]+=c
cost={w:-math.log(c/N) for w,c in nw.items() if c>=3 and len(w)>=1}
UNK=9.0
def seg(t):
    n=len(t); best=[1e9]*(n+1); back=[0]*(n+1); best[0]=0
    for i in range(n):
        if best[i]>=1e9: continue
        c=best[i]+UNK+1.5          # one unknown letter
        if c<best[i+1]: best[i+1]=c; back[i+1]=i
        for L in range(2,13):
            w=t[i:i+L]
            if len(w)<L: break
            if w in cost and len(w)>=3:
                c=best[i]+cost[w]
                if c<best[i+L]: best[i+L]=c; back[i+L]=i
    out=[];i=n
    while i>0: out.append(t[back[i]:i]); i=back[i]
    return out[::-1],best[n]
if __name__=='__main__':
    d=open(sys.argv[1],encoding='utf-8').read().split('--- decryption')[1].split('\n',1)[1].strip().split('\n')
    tot=0;known=0
    for line in d[int(sys.argv[2]):int(sys.argv[3])]:
        w,c=seg(line.lower()); print(' '.join(w))
