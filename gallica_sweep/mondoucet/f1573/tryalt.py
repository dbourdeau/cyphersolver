# tryalt.py ct.txt "LAB:tokidx:new" ...  (tokidx = 0-based index among non-separator tokens of that line; new may be 'x y' for 2 tokens)
import sys,os
os.environ.setdefault('KEY','key1573_split2.json')
sys.argv=[sys.argv[0]]+sys.argv[1:]
src=open('decode1573.py',encoding='utf-8').read().split('W=int(')[0]
__file__=os.path.abspath('decode1573.py'); exec(src)
def load(fn):
    L=[]
    for l in open(fn,encoding='utf-8'):
        if l.startswith('#') or ':' not in l: continue
        a,b=l.split(':',1); L.append((a.strip(),[t for t in b.split() if t not in('/','.')]))
    return L
def run(L):
    allt=[t for _,ts in L for t in ts]; sc,txt=beam(allt,600); out={};i=0
    for lab,ts in L:
        o=''
        for t in ts:
            if t.startswith('['): j=txt.index(']',i)+1;o+=txt[i:j];i=j
            else:o+=txt[i];i+=1
        out[lab]=o
    return sc,out
L=load(sys.argv[1]); sc0,o0=run(L)
for spec in sys.argv[2:]:
    lab,idx,new=spec.split(':'); idx=int(idx)
    L2=[(a,list(ts)) for a,ts in L]
    for a,ts in L2:
        if a==lab: old=ts[idx]; ts[idx:idx+1]=new.split()
    sc,o=run(L2)
    print('%-18s %s->%s  dscore %+.1f\n   old %s\n   new %s'%(spec,old,new,sc-sc0,o0[lab],o[lab]),flush=True)
