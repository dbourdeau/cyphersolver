"""Fuzzy lookup: masked token -> Spanish candidates. python fuzzy.py TOKEN [maxdist]"""
import sys, re, collections, functools, pickle, os
sys.stdout.reconfigure(encoding='utf-8')
FW = {'a':'-','e':'i','i':'x','o':'.','á':'-','é':'i','í':'x','ó':'.'}
def mask(w): return ''.join(FW.get(c,c) for c in w)
P = os.path.join(os.path.dirname(__file__),'_freq.pkl')
if os.path.exists(P): freq = pickle.load(open(P,'rb'))
else:
    freq = collections.Counter()
    for f in ('es-gutenberg','es-quijote','es-vasto-memorias'):
        t = open(f'lang/corpora/{f}.txt',encoding='utf8',errors='ignore').read().lower()
        freq.update(re.findall(r"[a-záéíóúñü]+", t))
    pickle.dump(freq,open(P,'wb'))
def ed(a,b):
    p=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        q=[i]
        for j,cb in enumerate(b,1): q.append(min(p[j]+1,q[j-1]+1,p[j-1]+(ca!=cb)))
        p=q
    return p[-1]
if __name__=='__main__':
    tok=sys.argv[1]; md=int(sys.argv[2]) if len(sys.argv)>2 else 1
    res=[]
    for w,c in freq.items():
        if c<3 or abs(len(w)-len(tok))>md: continue
        d=ed(mask(w).replace('ñ','n'),tok.replace('ñ','n'))
        if d<=md: res.append((d,-c,w))
    for d,c,w in sorted(res)[:15]: print(d,-c,w,mask(w))
