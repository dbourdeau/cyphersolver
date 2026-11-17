import re,collections,math,json,sys
c=open('../../sforza1597/ctts/lm_qc/italian.txt',encoding='utf-8',errors='ignore').read().lower().replace('u','v').replace('j','i')
cnt=collections.Counter(re.findall('[a-z]+',c));N=sum(cnt.values())
W={w:math.log(n/N) for w,n in cnt.items() if n>=2 and (len(w)>=2 or w in('a','e','o'))}
for w in ['ludovico','tomasino','corsica','nicodemo','galeasmo','galeaso','iovan','sarsane','firense','firensa','volterra','modena','etcetera','meser','madona','signore']: W[w]=-8
def seg(s):
    n=len(s);b=[0]+[-1e9]*n;bp=[None]*(n+1)
    for i in range(n):
        if b[i]-12>b[i+1]: b[i+1]=b[i]-12;bp[i+1]=(i,0)
        for L in range(1,15):
            w=s[i:i+L]
            if i+L<=n and w in W and b[i]+W[w]>b[i+L]: b[i+L]=b[i]+W[w];bp[i+L]=(i,1)
    out=[];j=n
    while j>0:
        i,ok=bp[j];out.append((s[i:j],ok));j=i
    return out[::-1]
k=json.load(open('keyB.json'))
tot=rd=0
for f in sys.argv[1:]:
    s=''.join(k.get(x,'?') for l in open(f) for x in l.split())
    sg=seg(s); r=sum(len(w) for w,ok in sg if ok); tot+=len(s); rd+=r
    txt=' '.join(w if ok else w.upper() for w,ok in sg)
    txt=re.sub(r'(?<=[A-Z?]) (?=[A-Z?])','',txt)
    open(f.replace('t','seg',1),'w').write(txt+'\n')
    print(f,len(s),'%.3f'%(r/len(s)))
print('all %.3f'%(rd/tot))
