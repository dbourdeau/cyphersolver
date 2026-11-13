# Single measure for catalogue 1555 (PREREG-1555.md). Usage: python3 -I measure_1555.py KEY.json HELDOUT.txt LEXCORPUS
import sys,json,re,random,collections
key=json.load(open(sys.argv[1])); parse=key.pop('_parse','units')
codes={k:v for k,v in key.items() if not k.startswith('_')}
def digits(path):
    segs=[];cur=''
    for l in open(path):
        if l.startswith('#') or not l.strip(): continue
        b=l.strip().split(' ',1)[1] if ' ' in l.strip() else ''
        b=re.sub(r'\{[^}]*\}',' W ',b)
        for x in b.split():
            if x=='W':
                if cur: segs.append(cur); cur=''
                continue
            m=re.match(r'\[?([0-9])',x)
            if m: cur+=m.group(1)
    if cur: segs.append(cur)
    return segs
def split(seg):
    if parse=='units':
        out=re.findall(r'[13579]*[02468]|[13579]+$',seg); return out
    out=[];i=0;L=max(len(k) for k in codes)
    while i<len(seg):
        for n in range(min(L,len(seg)-i),0,-1):
            if seg[i:i+n] in codes: out.append(seg[i:i+n]); i+=n; break
        else: out.append(seg[i]); i+=1
    return out
def decode(segs,k):
    s=''
    for seg in segs:
        for u in split(seg):
            v=k.get(u)
            if v is None: s+='#'
            elif v.startswith('['): s+='|'
            else: s+=v
        s+='|'
    return s
freq=collections.Counter(re.findall(r'[a-z]+',open(sys.argv[3]).read().lower().replace('j','i').replace('v','u')))
lex={w for w,c in freq.items() if c>=3 and len(w)>=3}
def cover(s):
    tot=cov=0
    for part in s.split('|'):
        n=len(part); best=[0]*(n+1)
        for i in range(1,n+1):
            best[i]=best[i-1]
            for L in range(3,min(16,i)+1):
                if part[i-L:i] in lex: best[i]=max(best[i],best[i-L]+L)
        cov+=best[n]; tot+=n
    return cov/max(1,tot)
segs=digits(sys.argv[2]); s=decode(segs,codes).replace('v','u')
M=cover(s); print('M',round(M,4)); print(s)
plain=[k for k,v in codes.items() if v and not v.startswith('[')]
vals=[codes[k] for k in plain]; C=[]
for seed in range(200):
    r=random.Random(seed); v=vals[:]; r.shuffle(v); kk=dict(codes); kk.update(zip(plain,v))
    C.append(cover(decode(segs,kk).replace('v','u')))
print('controls max',round(max(C),4),'mean',round(sum(C)/len(C),4))
print('PASS' if (M>max(C) and M>=0.60) else 'FAIL')
