"""shuffle_A.py: frozen code A key vs 5000 shuffled keys (letters permuted among the values that carry a letter;
word codes stay word codes), seeds 20261112 and 7. Scored with the solver's own LM (lm/da1620.bin: 5-gram,
runs anchored at word starts/ends; word codes and '?' split runs). Held-out = A1P + A2; training = A1."""
import sys,random,numpy as np
R='/home/claude/keyless/rosenkrantz1629/pass2'
sys.path.insert(0,R+'/tools'); from numlib import load
A=27;H=26
raw=np.fromfile(R+'/lm/da1620.bin',dtype=np.float32,offset=8)
n4=A**4; mainT=raw[:n4*26].reshape(n4,26); o=n4*26
pendT=raw[o:o+n4]; o+=n4
un=[raw[o:o+26]]; o+=26; un.append(raw[o:o+676]); o+=676; un.append(raw[o:o+17576]); o+=17576; un.append(raw[o:o+456976])
def run_score(b):
    if not b: return 0.0
    ctx=((H*A+H)*A+H)*A+H; s=0.0
    for x in b: s+=mainT[ctx,x]; ctx=(ctx%(A**3))*A+x
    return s+pendT[ctx]
key={}
for l in open(R+'/codeA/KEY_A.tsv').read().splitlines()[1:]:
    f=l.split('\t'); key[int(f[0])]=f[2]
letvals=[v for v,L in key.items() if L!='WORD']
def mk_letter(k):
    lows={}
    for v,L in k.items():
        if v<200: lows.setdefault(v%9,[]).append(v)
    for r in lows: lows[r].sort()
    def f(v):
        if isinstance(v,str): return None
        if v in k: return None if k[v]=='WORD' else k[v]
        if v>=200: return None
        row=lows.get(v%9,[]); lo=[u for u in row if u<v]; hi=[u for u in row if u>v]
        if lo and hi and k[lo[-1]]==k[hi[0]]: return k[lo[-1]]
        return None
    return f
def runs(which):
    out=[]; cur=[]
    for let,img,ln,items in load(R+'/tx/CODE_A_FROZEN.tsv'):
        if let not in which: continue
        for it in items:
            if it[0]=='n': cur.append(it[1])
            elif it[0]=='c':
                if cur: out.append(cur); cur=[]
    if cur: out.append(cur)
    return out
def score(k,rs):
    f=mk_letter(k); tot=0.0; n=0
    for r in rs:
        b=[]
        for v in r:
            x=f(v)
            if x is None: tot+=run_score(b); n+=len(b); b=[]
            else: b.append(ord(x)-97)
        tot+=run_score(b); n+=len(b)
    return tot,n
for which,name in (({'A1P','A2'},'held-out A1P+A2'),({'A1'},'training A1')):
    rs=runs(which); real,n=score(key,rs)
    for seed in (20261112,7):
        rnd=random.Random(seed); ge=0; best=-1e18; tot=0.0
        for i in range(5000):
            vals=[key[v] for v in letvals]; rnd.shuffle(vals); k=dict(key); k.update(zip(letvals,vals))
            s,_=score(k,rs); tot+=s; best=max(best,s); ge+=s>=real
        print(f'{name}: letters {n}, real {real:.1f} ({real/n:.3f}/letter); seed {seed}: shuffles >= real {ge}/5000, best shuffle {best:.1f}, mean {tot/5000:.1f}',flush=True)
