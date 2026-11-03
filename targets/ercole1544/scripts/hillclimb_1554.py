# Ciphertext-only attack, no table as input: strict one-to-one substitution on the letter signs, random starts, swaps only.
# Italian trigrams from clear text independent of this table: sibling clear decipherments cc. 104r, 107 and the plaintext of catalogue 1567.
# Run from the target folder. Catalogue 1567 is not in this folder: pass the folder of its decryptions as argument, otherwise the training text is shorter and the short letters may differ. Needs numpy.
import re,sys,random,math,collections,glob
import numpy as np
sys.stdout.reconfigure(encoding='utf8')
T=dict(zip('abcdefghnopqrstuxyzk','nopqrstuabcdefghilmz'))
txt=''
for f in ['transcription_0104r.txt','transcription_0107.txt']+(glob.glob(sys.argv[1]+'/decryption_*.txt') if len(sys.argv)>1 else []):
    for l in open(f,encoding='utf8'):
        if not l.startswith('#'): txt+=l.partition(' ')[2] if 'decryption' in f else l
txt=re.sub(r'[^a-z]','',txt.lower().replace('v','u').replace('j','i').replace('y','i').replace('k','c').replace('x','s'))
A='abcdefghilmnopqrstuz'; ix={c:i for i,c in enumerate(A)}
txt=''.join(c for c in txt if c in ix)
n=len(A); L=np.full((n,n,n),.1)
for i in range(len(txt)-2): L[ix[txt[i]],ix[txt[i+1]],ix[txt[i+2]]]+=1
L=np.log(L/L.sum())
print('training letters',len(txt))
def runs(fs):
    out=[]
    for f in fs:
        for l in open(f,encoding='utf8'):
            if l.startswith('#') or not l.strip(): continue
            b=l.strip().partition(' ')[2]
            for s in re.split(r'L\^\w+|\d+|L|S|\?',b):
                s=s.replace(' ','')
                if len(s)>2: out.append(s)
    return out
signs='abcdefghnopqrstuxyzk'; si={c:i for i,c in enumerate(signs)}
def counts(rs):
    C=np.zeros((20,20,20))
    tot=0
    for r in rs:
        r=[c for c in r if c in si]
        for i in range(len(r)-2): C[si[r[i]],si[r[i+1]],si[r[i+2]]]+=1
        tot+=len(r)
    return C,tot
def val(C,p): return (C*L[np.ix_(p,p,p)]).sum()
tp=np.array([ix[T[c]] for c in signs])
def attack(C,seed,restarts=30,iters=6000):
    rng=random.Random(seed); best=None;bv=-1e18
    for r in range(restarts):
        p=list(range(20)); rng.shuffle(p); p=np.array(p); cur=val(C,p); t=30.
        for it in range(iters):
            a,b=rng.randrange(20),rng.randrange(20)
            if a==b: continue
            p[a],p[b]=p[b],p[a]; v=val(C,p)
            if v>=cur or rng.random()<math.exp((v-cur)/t): cur=v
            else: p[a],p[b]=p[b],p[a]
            t=max(.3,t*.9985)
        if cur>bv: bv=cur;best=p.copy()
    return best,bv
groups={'113r':['0113r'],'114r':['0114r'],'115r':['0115r'],'116r':['0116r'],'117-118':['0117r','0117v','0118r'],'119r':['0119r'],'120':['0120r','0120v']}
groups['ALL']=sum(groups.values(),[])
for name,ps in groups.items():
    rs=runs([f'validation/1554_pass2/{p}.txt' for p in ps]); C,tot=counts(rs)
    b,v=attack(C,1554,restarts=30 if name=='ALL' else 16)
    use=C.sum((1,2))+C.sum((0,2))+C.sum((0,1))
    ag=(b==tp); 
    print(f'{name}: {tot} letters; attack score {v/tot:.3f}, frozen table {val(C,tp)/tot:.3f}; agrees on {ag.sum()}/20 signs, {100*(use*ag).sum()/use.sum():.1f}% of letters',flush=True)
