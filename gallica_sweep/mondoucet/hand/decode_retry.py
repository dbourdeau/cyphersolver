# Retry decode of 13 July 1572 with the a/alpha split (21 Sept 2026).
# Beam over the whole block as one stream (as f1573/decode1573.py), P(letter|glyph) from key counts x period-French 5-gram.
# usage: python hand/decode_retry.py KEYNAME file...   KEYNAME in base | ext | k1573
#   base  = hand/key2.json (1572 key, as before)
#   ext   = key2 with '@' (alpha) given the 1573 alpha counts (r 123) and r removed from round 'a'
#   k1573 = f1573/key1573_split2.json directly ('@'->'α'), key2 counts only for signs the 1573 key lacks
# LM: f1573/fr5.npy (git-ignored; set FR5 to its path).
import sys, json, math, collections, os
import numpy as np
H=os.path.dirname(os.path.abspath(__file__)); M=os.path.dirname(H)
ALPHA='abcdefghiklmnopqrstuvxyz'; K=len(ALPHA)
tab=np.load(os.environ.get('FR5',os.path.join(M,'f1573','fr5.npy')))
SM=float(os.environ.get('SM','0.3')); NP=float(os.environ.get('NP','3.5')); W=int(os.environ.get('W','300'))
k2=json.load(open(os.path.join(H,'key2.json')))
k3=json.load(open(os.path.join(M,'f1573','key1573_split2.json'),encoding='utf-8'))
def load(name):
    c={t:collections.Counter(v) for t,v in k2['key'].items()}; n=collections.Counter(k2['nulls'])
    for t in ('*','C','mq','j'): n[t]+=20          # hard nulls of the 1572 key
    if name=='ext':
        c['@']=c.get('@',collections.Counter())+collections.Counter(k3['counts']['α'])
        c['a'].pop('r',None)
    elif name=='k1573':
        c3={('@' if t=='α' else t):collections.Counter(v) for t,v in k3['counts'].items()}
        n3=collections.Counter({('@' if t=='α' else t):v for t,v in k3['nulls'].items()})
        for t in c:
            if t not in c3: c3[t]=c[t]; n3[t]=n.get(t,0)
        for t in ('*','C','mq','j'): n3[t]+=20
        c,n=c3,n3
    return c,n
def emis(t,c,n):
    cc=c.get(t,collections.Counter()); nn=n.get(t,0); S=sum(cc.values())+nn+SM*K
    res=[(ALPHA.index(ch),math.log((v+SM)/S)) for ch,v in cc.items() if ch in ALPHA]
    seen={i for i,_ in res}; res+=[(i,math.log(SM/S)) for i in range(K) if i not in seen]
    res.append((-1,math.log((nn+0.2)/S))); return res
def beam(toks,c,n):
    e=ALPHA.index('e'); beams={(e,e,e,e):(0.0,'')}
    for t in toks:
        E=emis(t,c,n); nb={}
        for ctx,(sc,txt) in beams.items():
            for li,lp in E:
                if li==-1: ns=sc+lp-NP; kk=ctx; ch='·'
                else: ns=sc+lp+tab[ctx[0],ctx[1],ctx[2],ctx[3],li]; kk=(ctx[1],ctx[2],ctx[3],li); ch=ALPHA[li]
                if kk not in nb or nb[kk][0]<ns: nb[kk]=(ns,txt+ch)
        beams=dict(sorted(nb.items(),key=lambda kv:-kv[1][0])[:W])
    return max(beams.values(),key=lambda v:v[0])[1]
def run(name,files):
    c,n=load(name); lines=[]
    for f in files:
        for l in open(f,encoding='utf-8'):
            if l.startswith('#') or ':' not in l: continue
            lab,rest=l.split(':',1); lines.append((lab.strip(),[('O' if t=='ð' else t) for t in rest.split() if t not in('/','.')]))
    txt=beam([t for _,ts in lines for t in ts],c,n); out=[]; i=0
    for lab,ts in lines: out.append((lab,txt[i:i+len(ts)],ts)); i+=len(ts)
    return out
if __name__=='__main__':
    for lab,s,_ in run(sys.argv[1],sys.argv[2:]): print('%4s  %s'%(lab,s))
