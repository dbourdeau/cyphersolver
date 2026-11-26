import re,collections,math,json
c=open('../../sforza1597/ctts/lm_qc/italian.txt',encoding='utf-8',errors='ignore').read().lower().replace('u','v').replace('j','i')
c=re.sub('[^a-z]','',c)[:6000000]
n=5;G=collections.Counter(c[i:i+n] for i in range(len(c)-n));H=collections.Counter(c[i:i+n-1] for i in range(len(c)-n))
def lp(s):
    t=0
    for i in range(len(s)-n+1):
        g=s[i:i+n];t+=math.log((G[g]+0.1)/(H[g[:-1]]+2.6))
    return t
k=json.load(open('keyB.json'));syms=sorted(set(k))
fl=[]
for f in ['t62','t76','t72','t77','t75','t86','t73']:
    for li,l in enumerate(open(f+'.txt')):
        t=l.split()
        for i in range(len(t)):
            a,b=max(0,i-6),min(len(t),i+7)
            ctx=lambda tok:''.join(k.get(x,'?') for x in t[a:i]+[tok]+t[i+1:b])
            base=lp(ctx(t[i]));best=(0,None)
            for s in syms:
                if k[s]==k.get(t[i]):continue
                d=lp(ctx(s))-base
                if d>best[0]:best=(d,s)
            if best[0]>9: fl.append((round(best[0],1),f,li+1,i,len(t),t[i],best[1],ctx(t[i]),ctx(best[1])))
fl.sort(reverse=True);json.dump(fl,open('flags.json','w'))
print(len(fl))
for x in fl[:60]: print(x)
