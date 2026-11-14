# Line-level EM: each gloss line is attached to the cipher line just above or just below it
# (choice re-estimated by likelihood). Soft EM over code->substring emissions.
import sys, math, json, collections
import numpy as np
sys.path.insert(0,__file__.rsplit('/',1)[0])
from parse import load, norm
from em2 import emis_matrix, fb, LMAX
def units(blocks):
    """return list of blocks as sequences of ('C',codes) / ('G',text) skipping X"""
    out=[]
    for b in blocks:
        seq=[(t,v) for t,v in b['lines'] if t in 'CG']
        out.append((b['id'],seq))
    return out
def build_pairs(us,assign):
    pairs=[]
    for bid,seq in us:
        Cidx=[k for k,(t,v) in enumerate(seq) if t=='C']
        gl={k:'' for k in Cidx}
        for k,(t,v) in enumerate(seq):
            if t!='G': continue
            above=[c for c in Cidx if c<k]; below=[c for c in Cidx if c>k]
            a=assign.get((bid,k),'up')
            if a=='up' and above: gl[above[-1]]+=norm(v)
            elif below: gl[below[0]]+=norm(v)
            elif above: gl[above[-1]]+=norm(v)
        for c in Cidx:
            pairs.append({'id':'%s:%d'%(bid,c),'C':seq[c][1],'G':gl[c]})
    return pairs
def line_ll(C,S,E,lu,bc,skipc,skips):
    if not S: return len(C)*skipc
    EM=emis_matrix(C,S,E,bc,lu); F,B,Z=fb(C,S,EM,skipc,skips); return Z
def train(path,iters=30,rounds=4,skipc=math.log(0.05),skips=math.log(0.02),init_assign=None):
    blocks=load(path); us=units(blocks)
    allg=''.join(norm(v) for _,seq in us for t,v in seq if t=='G')
    uni=collections.Counter(allg); tot=sum(uni.values())
    lu={ch:math.log(v/tot) for ch,v in uni.items()}
    assign=dict(init_assign or {})
    E={}
    from em2 import run
    for r in range(rounds):
        pairs=build_pairs(us,assign)
        E,counts,LL=run(pairs,iters=iters,skipc=skipc,skips=skips,E=E,verbose=False)
        print('round',r,'LL',round(LL,1),flush=True)
        bc={}
        changed=0
        for bid,seq in us:
            for k,(t,v) in enumerate(seq):
                if t!='G': continue
                best=None
                for a in ('up','down'):
                    trial=dict(assign); trial[(bid,k)]=a
                    # only affected lines
                    pp=[p for p in build_pairs([(bid,seq)],trial)]
                    ll=sum(line_ll(p['C'],p['G'],E,lu,bc,skipc,skips) for p in pp)
                    if best is None or ll>best[0]: best=(ll,a)
                if assign.get((bid,k),'up')!=best[1]: changed+=1
                assign[(bid,k)]=best[1]
        print(' reassigned',changed,flush=True)
        if changed==0 and r>0: break
    pairs=build_pairs(us,assign)
    E,counts,LL=run(pairs,iters=iters,skipc=skipc,skips=skips,E=E,verbose=False)
    return E,counts,assign,pairs,us
if __name__=='__main__':
    E,counts,assign,pairs,us=train(sys.argv[1],iters=int(sys.argv[2]))
    json.dump({'E':E,'assign':{'%s|%d'%k:v for k,v in assign.items()}},open(sys.argv[3],'w'))
    for bid,seq in us:
        for k,(t,v) in enumerate(seq):
            if t=='G': print('ASSIGN',bid,k,assign.get((bid,k)),v[:50])
    for c,d in sorted(counts.items(),key=lambda x:-sum(x[1].values())):
        tt=sum(d.values()); top=sorted(d.items(),key=lambda x:-x[1])[:4]
        print(c,round(tt,1),' '.join('%s:%.2f'%(t,v/tt) for t,v in top))
