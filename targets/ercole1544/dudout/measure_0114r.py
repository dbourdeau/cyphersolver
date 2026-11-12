import re,sys,random,collections
W=sys.argv[1]
key={};codes={}
for l in open(W+'/work/key_frozen.tsv'):
    if l.startswith('#') or not l.strip(): continue
    p=l.rstrip('\n').split('\t'); s,v=p[0],p[1]
    if len(s)==1 and s.isalpha() and s.islower(): key[s]=v
    else: codes[s]=v
NULL={'24','25','27'}
def toks(path):
    out=[]
    for l in open(path):
        if l.startswith('#') or not l.strip(): continue
        body=l.split(' ',1)[1]
        i=0
        while i<len(body):
            c=body[i]
            if c=='<': j=body.index('>',i); out.append(('n',body[i+1:j])); i=j+1
            elif c=='[': j=body.index(']',i); out.append(('l',body[i+1:j].split('/')[0])); i=j+1
            elif c=='^': out.append(('l',body[i+1])); i+=2
            elif c in ' \n': i+=1
            else: out.append(('l',c)); i+=1
    return out
def decode(t,k):
    s=''
    for typ,v in t:
        if typ=='n':
            if v in NULL: continue
            s+=codes.get(v,'#').replace(' ','') if codes.get(v)!='null' else ''
        else:
            if v=='y' or v=='L' and False: pass
            if v=='L': s+='et'
            elif v=='S': s+='ss'
            elif v in k: s+=k[v]
            else: s+='#'
    return s
freq=collections.Counter(re.findall(r'[a-z]+',open(W+'/work/it_nunz_clean.txt').read().lower().replace('j','i').replace('v','u')))
lex={w for w,c in freq.items() if c>=3 and len(w)>=3}
def cover(s):
    n=len(s); best=[0]*(n+1)
    for i in range(1,n+1):
        best[i]=best[i-1]
        for L in range(3,min(16,i)+1):
            if s[i-L:i] in lex: best[i]=max(best[i],best[i-L]+L)
    return best[n]/max(1,sum(ch!='#' for ch in s))
if __name__=='__main__':
    t=toks(sys.argv[2]); s=decode(t,key)
    s=s.replace('v','u')
    M=cover(s); print('M',round(M,4)); print(s)
    sig=sorted(key); vals=[key[x] for x in sig]; C=[]
    for seed in range(200):
        r=random.Random(seed); v=vals[:]; r.shuffle(v); C.append(cover(decode(t,dict(zip(sig,v)))))
    print('controls max',round(max(C),4),'mean',round(sum(C)/len(C),4))
    print('PASS' if M>max(C) and M>=0.5 else 'FAIL')
