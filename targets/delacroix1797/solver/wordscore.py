# Word-bigram Viterbi segmentation score of an unspaced string, trained on Turner's French.
import pickle,math,collections as C
W=r'C:/Users/dbour/cypher/.work/delacroix1797/'
_t=open(W+'turner_fr.txt',encoding='utf8').read().split()
UNI=C.Counter(_t); BI=C.Counter(zip(_t,_t[1:])); N=len(_t)
MAXL=max(len(w) for w,c in UNI.items() if c>=2)
UNI={w:c for w,c in UNI.items() if c>=2 and (len(w)>1 or w in 'adlnsmjcy')}
TOT=sum(UNI.values())
OOV=-14.0
def lp(prev,w):
    u=UNI[w]/TOT
    if prev is None: return math.log(u)
    return math.log((BI.get((prev,w),0)+ 8*u)/(UNI.get(prev,0)+8))
def score(s):
    # states: end position -> {last word: best}
    n=len(s); B=[{} for _ in range(n+1)]; B[0][None]=0.0
    for i in range(n):
        if not B[i]: continue
        # top few prev states
        pv=sorted(B[i].items(),key=lambda x:-x[1])[:6]
        for L in range(1,min(MAXL,n-i)+1):
            w=s[i:i+L]
            if w in UNI:
                for p,v in pv:
                    x=v+lp(p,w)
                    if x>B[i+L].get(w,-1e18): B[i+L][w]=x
        # OOV one char
        p0,v0=pv[0]
        x=v0+OOV
        if x>B[i+1].get(None,-1e18): B[i+1][None]=x
    return max(B[n].values())/n
