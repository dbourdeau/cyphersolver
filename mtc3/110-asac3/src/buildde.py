# German char LM over 28 symbols: A-Z=0..25, space=26, digit=27. Order 5, interpolated absolute discounting.
import numpy as np,re,sys
K=28
raw=open(r'C:/Users/dbour/cypher/lang/corpora/de-gutenberg.txt',encoding='utf8',errors='ignore').read()
raw=raw.replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('Ä','Ae').replace('Ö','Oe').replace('Ü','Ue').replace('ß','ss')
t=raw.upper()
t=re.sub(r'[0-9]','#',t)
t=re.sub(r'[^A-Z#]+',' ',t)
a=np.array([26 if c==' ' else (27 if c=='#' else ord(c)-65) for c in t],dtype=np.int64)
print(len(a))
P=None; D=0.75; MINC=5
for n in range(1,6):
    idx=np.zeros(len(a)-n+1,dtype=np.int64)
    for j in range(n): idx=idx*K+a[j:len(a)-n+1+j]
    c=np.bincount(idx,minlength=K**n).astype(float).reshape(-1,K)
    if n==1: P=((c[0]+1)/(c[0].sum()+K)).reshape(1,K)
    else:
        ch=c.sum(1,keepdims=True); c=np.where(ch>=MINC,c,0); ch=c.sum(1,keepdims=True)
        tp=(c>0).sum(1,keepdims=True).astype(float)
        hm=np.arange(K**(n-1))%(K**(n-2)) if n>2 else np.zeros(K,dtype=int)
        lo=P[hm]
        with np.errstate(divide='ignore',invalid='ignore'):
            p=np.maximum(c-D,0)/ch+(D*tp/ch)*lo
        P=np.where(ch>0,p,lo)
    np.log10(P).astype(np.float32).tofile(f'lmde/lp{n}.bin')
open('de_clean.txt','w').write(t[:3000000])
print('ok')
