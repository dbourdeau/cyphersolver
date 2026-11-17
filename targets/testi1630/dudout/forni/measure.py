# measure.py - lexical coverage measure for the Forni cipher (fil 🔓, 17/11/2026)
# usage: python3 -I measure.py KEY.tsv TRANSCRIPTION.txt MINLEN [seed]
import sys,re,unicodedata,random,collections,glob
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(ch for ch in s if 'a'<=ch<='z' or ch in ' ?')
    s=s.replace('v','u').replace('j','i').replace('z','f').replace('y','i').replace('k','c').replace('x','s').replace('w','u')
    return re.sub(r'([a-z])\1+',r'\1',s)
def lexicon(minlen):
    c=collections.Counter()
    for f in glob.glob('/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/estense-testi-1630/doglio/2*_djvu.txt'):
        for w in norm(open(f,encoding='utf8',errors='ignore').read()).split(): c[w]+=1
    return {w for w,n in c.items() if n>=5 and len(w)>=minlen and '?' not in w}
def key(path):
    K={}
    for l in open(path,encoding='utf8'):
        if l.startswith('# ') or not l.strip(): continue
        p=l.rstrip('\n').split('\t'); K[p[0]]=p[1]
    return K
def tokens(path):
    T=[]
    for l in open(path,encoding='utf8'):
        if l.startswith('#') or ':' not in l: continue
        body=re.sub(r'\{[^}]*\}',' ',l.split(':',1)[1])
        T+=body.split()
    return T
def decode(T,K):
    out=''
    for t in T:
        d=t.endswith(':') and len(t)>1; s=t[:-1] if d else t
        v=K.get(s,'?'); out+=v*2 if d else v
    return norm(out).replace(' ','')
def coverage(s,L,maxlen=16):
    n=len(s); best=[0]*(n+1)
    for i in range(1,n+1):
        best[i]=best[i-1]
        for k in range(2,min(maxlen,i)+1):
            w=s[i-k:i]
            if w in L: best[i]=max(best[i],best[i-k]+k)
    return best[n]/n if n else 0
if __name__=='__main__':
    K=key(sys.argv[1]); T=tokens(sys.argv[2]); ml=int(sys.argv[3]); seed=int(sys.argv[4]) if len(sys.argv)>4 else 1634
    L=lexicon(ml); s=decode(T,K)
    car=coverage(s,L)
    labs=sorted({t.rstrip(':') if len(t)>1 else t for t in T} & set(K)); vals=[K[x] for x in labs]
    rng=random.Random(seed); W=[]
    for i in range(200):
        v=vals[:]; rng.shuffle(v); K2=dict(K); K2.update(dict(zip(labs,v))); W.append(coverage(decode(T,K2),L))
    print('tokens',len(T),'decoded_len',len(s),'lexicon',len(L)); print('decode',s)
    print('car %.3f  max_witness %.3f  margin %.3f  mean_witness %.3f'%(car,max(W),car-max(W),sum(W)/len(W)))
