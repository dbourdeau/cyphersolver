# Structured noisy control for wsa5 (cardona1517): control_noisy.build() (Lazarillo at Cardona's size, 35% of group
# types outside the option list, 5.5% misreadings), with each code group given a Lannoy-style code: initial by the
# word's first-letter bucket, a final reserved per first letter, a random vowel. Groups sharing initial+final form a
# class (GCLS). Runs wsa5 (SOLVER) and prints sign/group accuracy.
import os,random,collections,multiprocessing as mp,re,subprocess
os.environ.setdefault('NW','700'); os.environ.setdefault('NOUT','40')
import control_noisy as cn, syl
from drv import A
BUCKET={}
for letters,ini in (('ab','z'),('cd','n'),('ef','m'),('ghijy','g'),('lmno','f'),('pq','p'),('rs','t'),('tuvxz','s')):
    for c in letters: BUCKET[c]=ini
FINALS='bcdfghklmnpqrstxzaeoy'; CAP=int(os.environ.get('CAP','2'))
def classes(gv,rnd):
    by=collections.defaultdict(list)
    for g,w in gv.items(): by[(BUCKET.get(w[0],'s'),w[0] if w[0]!='y' else 'i')].append(g)
    used=collections.defaultdict(int); code={}; cls={}
    for (ini,first),gs in sorted(by.items()):
        k=-(-len(gs)//CAP); fs=[FINALS[(used[ini]+i)%len(FINALS)]+('' if used[ini]+i<len(FINALS) else str((used[ini]+i)//len(FINALS))) for i in range(k)]; used[ini]+=k
        for j,g in enumerate(gs):
            f=fs[j//CAP]; code[g]=ini+'aeiou'[j%CAP]+f; cls[g]=(ini,f)
    return code,cls
def main():
    clean,toks,truth,nerr=cn.build()
    groups=sorted({x for x in toks if x.startswith('g')}); signs=sorted({x for x in toks if not x.startswith('g')})
    tv={};gv={}
    for x,tr in zip(clean,truth): (gv if x.startswith('g') else tv)[x]=tr
    code,cls=classes({g:gv[g] for g in groups},random.Random(2))
    cid={c:i for i,c in enumerate(sorted(set(cls.values())))}
    sizes=collections.Counter(cls.values())
    print(f'structured control: tokens {len(toks)}; classes {len(cid)}, groups in classes of 2+: {sum(1 for g in groups if sizes[cls[g]]>1)}/{len(groups)}',flush=True)
    ws=cn.ws; tk=syl.task2(toks,signs,groups,ws)+''.join(f'GCLS {i} {cid[cls[g]]}\n' for i,g in enumerate(groups))
    if os.environ.get('NOCLS'): tk=syl.task2(toks,signs,groups,ws)
    ns=sum(1 for x in toks if not x.startswith('g'))
    with mp.Pool(8) as p: res=sorted(p.map(syl.runone,[(tk,s,int(os.environ.get('ITERS','10000000')),3,[],f'c{s}') for s in range(int(os.environ.get('RUNS','16')))]),reverse=True)
    for best,seed,sm,gw in res[:8]:
        sacc=sum(1 for x,c in zip(toks,clean) if x==c and not x.startswith('g') and syl.unit(sm[signs.index(x)]).lower()==tv[x])/ns
        gacc=sum(1 for x,c in zip(toks,clean) if x==c and x.startswith('g') and gw[groups.index(x)]<len(ws) and ws[gw[groups.index(x)]]==gv[x])/(len(toks)-ns)
        print(f'{best/len(toks):.3f}  sign tokens right {sacc:.2f}  group tokens right {gacc:.2f}',flush=True)
if __name__=='__main__': main()
