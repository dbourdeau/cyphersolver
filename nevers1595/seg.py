import sys
from collections import Counter
D=set('0123456789o')
def seg(toks,lead='12'):
    out=[];i=0
    while i<len(toks):
        t=toks[i]
        if t in lead and i+1<len(toks) and toks[i+1] in D:
            out.append(t+toks[i+1].replace('o','0')); i+=2
        else: out.append(t); i+=1
    return out
def load(fn):
    rep={'i':'1'}
    L=[]
    for l in open(fn,encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        L.append([rep.get(t,t) for t in l.split()])
    return L
if __name__=='__main__':
    lines=[x for f in sys.argv[1:] for x in load(f)]
    S=[seg(l) for l in lines]
    for s in S: print(' '.join(s))
    c=Counter(t for s in S for t in s); print(sum(c.values()),len(c)); print(c.most_common())
