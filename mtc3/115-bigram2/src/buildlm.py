import numpy as np,re,sys
out=sys.argv[1]; extra=sys.argv[2:]  # extra: file:weight
raw=open(r'C:/Users/dbour/cypher/lang/corpora/en-gutenberg.txt',encoding='utf8',errors='ignore').read()
raw=re.sub(r'\b[IVXLCDM]{2,}\b','',raw)
raw=re.sub(r'([A-Za-z])\1{2,}',r'\1\1',raw)
seqs=[(re.sub(r'(.)\1{3,}',r'\1\1\1',re.sub('[^A-Z]','',raw.upper())),1.0)]
for e in extra:
    f,w=e.rsplit(':',1); seqs.append((re.sub('[^A-Z]','',open(f,encoding='utf8',errors='ignore').read().upper()),float(w)))
P=None; D=0.75; MINC=10
for n in range(1,6):
    c=np.zeros(26**n)
    for s,w in seqs:
        a=np.frombuffer(s.encode(),dtype=np.uint8).astype(np.int64)-65
        idx=np.zeros(len(a)-n+1,dtype=np.int64)
        for j in range(n): idx=idx*26+a[j:len(a)-n+1+j]
        c+=w*np.bincount(idx,minlength=26**n)
    c=c.reshape(-1,26)
    if n==1: P=((c[0]+1)/(c[0].sum()+26)).reshape(1,26)
    else:
        ch=c.sum(1,keepdims=True)
        c=np.where(ch>=MINC,c,0); ch=c.sum(1,keepdims=True)
        tp=(c>0).sum(1,keepdims=True).astype(float)
        hm=np.arange(26**(n-1))%(26**(n-2)) if n>2 else np.zeros(26,dtype=int)
        lo=P[hm]
        with np.errstate(divide='ignore',invalid='ignore'):
            p=np.maximum(c-D,0)/ch + (D*tp/ch)*lo
        P=np.where(ch>0,p,lo)
    np.log10(P).astype(np.float32).tofile(f'{out}/lp{n}.bin')
L5=np.log10(P).reshape(-1)
def q(s):
    x=[ord(c)-65 for c in s]; h=0
    for c in x[:4]: h=h*26+c
    return L5[h*26+x[4]]
for s in ['XXXXX','EEEEE','THERE','XXXIV','OFTHE']: print(s,q(s))
