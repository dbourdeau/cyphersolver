import re, sys, random, math, json
FREQ = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]))
LP = {k: math.log10(v/100) for k,v in FREQ.items()}
KEYS = ["COMERETRIBUTION","COMPLETEVICTORY","MANCHESTERBLUFF","THENAVYOURPRIDE","OURNAVYOURPRIDE"]
def load(path):
    s=open(path).read(); out={}
    for blk in s.split('## ')[1:]:
        name=blk[:2]
        L=[l for l in blk.splitlines()[1:] if l and not l.startswith(('«','#'))]
        t=re.sub(r'\[(.)\|.\]',r'\1',' '.join(L)).replace('/','')
        out[name]=t.split()
    return out
def dec(letters,key,off=0):
    return ''.join(chr((ord(c)-ord(key[(i+off)%len(key)]))%26+65) for i,c in enumerate(letters))
def S(p): return sum(LP[c] for c in p)/len(p)
if __name__=="__main__":
    T=load(sys.argv[1]); rnd=random.Random(681)
    ctrl=[''.join(rnd.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(15)) for _ in range(200)]
    tel={k:''.join(v) for k,v in T.items()}
    res={}
    for name in list(tel)+["ALL"]:
        def score(key,off=0):
            if name=="ALL":
                ps=''.join(dec(tel[n],key,off) for n in tel); return S(ps)
            return S(dec(tel[name],key,off))
        cs=sorted(score(k) for k in ctrl)
        row={"n_letters": sum(map(len,tel.values())) if name=="ALL" else len(tel[name]),
             "controls_max":round(cs[-1],4),"controls_median":round(cs[100],4)}
        for k in KEYS:
            s0=score(k); rank=1+sum(c>=s0 for c in cs)
            row[k]={"S":round(s0,4),"rank_of_201":rank,"fits":rank==1,
                    "other_offsets_max":round(max(score(k,o) for o in range(1,15)),4)}
        res[name]=row
    print(json.dumps(res,indent=1))
