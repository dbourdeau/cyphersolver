# Control matched to vich1515: a held-out Spanish text (Lazarillo, Gutenberg 320) enciphered with letter signs
# (homophones, plus 8 letter-pair signs) and code groups for the commonest words AND for common syllables/letters
# inside spelled words. Defaults give about vich1515's size: 3,280 tokens, 1,910 signs (38 types), 1,375 group
# tokens (158 types). Solved with the same pipeline (wsa4, wide group options, nothing fixed); prints how many sign
# and group tokens come out right. Run as a file: python3 control_matched.py
import os,sys,random,collections,multiprocessing as mp
from drv import norm_words
import syl
NW=int(os.environ.get('NW','1180')); PS=float(os.environ.get('PS','0.22')); NCW=int(os.environ.get('NCW','60'))
NCS=int(os.environ.get('NCS','99')); NLET=int(os.environ.get('NLET','23')); SEED=int(os.environ.get('SEED','1'))
ITERS=int(os.environ.get('ITERS','300000')); RUNS=int(os.environ.get('RUNS','16'))
def build():
    rnd=random.Random(SEED)
    t=open('corp/g320.txt',encoding='utf-8',errors='ignore').read(); t=t[t.find('*** START'):t.find('*** END')]
    W=norm_words(t)[6402:6402+NW]
    cw=[w for w,_ in collections.Counter(W).most_common(NCW)]
    sub=collections.Counter()
    for w in W:
        if w in cw: continue
        for L in (1,2,3):
            for i in range(len(w)-L+1): sub[w[i:i+L]]+=1
    cs=[s for s,_ in sub.most_common(400) if s not in cw][:NCS]
    code={x:f'g{i}' for i,x in enumerate(cw+cs)}; pairs=syl.PAIRS[:8]
    lc=collections.Counter(c for w in W if w not in cw for c in w); own={}; n=0
    for c,k in lc.most_common():
        m=max(1,round(NLET*k/sum(lc.values()))); own[c]=[f's{n+i}' for i in range(m)]; n+=m
    for b in pairs: own[b]=[f'b{b}']
    toks=[];truth=[]
    for w in W:
        if w in code: toks.append(code[w]); truth.append(w); continue
        i=0
        while i<len(w):
            hit=None
            for L in (3,2,1):
                s=w[i:i+L]
                if len(s)==L and s in cs and rnd.random()<PS: hit=s; break
            if hit: toks.append(code[hit]); truth.append(hit); i+=len(hit); continue
            if w[i:i+2] in pairs: toks.append(own[w[i:i+2]][0]); truth.append(w[i:i+2]); i+=2; continue
            toks.append(rnd.choice(own[w[i]])); truth.append(w[i]); i+=1
    return toks,truth
def main():
    toks,truth=build()
    groups=sorted({x for x in toks if x.startswith('g')}); signs=sorted({x for x in toks if not x.startswith('g')})
    ns=sum(1 for x in toks if not x.startswith('g'))
    print('control: tokens',len(toks),'signs',ns,'sign types',len(signs),'groups',len(toks)-ns,'group types',len(groups),flush=True)
    if os.environ.get('SIZEONLY'): return
    ws=[l.strip() for l in open('wide_words.txt') if l.strip()]
    tv={};gv={}
    for x,tr in zip(toks,truth): (gv if x.startswith('g') else tv)[x]=tr
    print('group values in the option list',sum(v in ws for v in gv.values()),'/',len(gv),flush=True)
    tk=syl.task2(toks,signs,groups,ws)
    with mp.Pool(8) as p: res=sorted(p.map(syl.runone,[(tk,s,ITERS,3,[],f'q{s}') for s in range(RUNS)]),reverse=True)
    for best,seed,sm,gw in res[:5]:
        sacc=sum(1 for x in toks if not x.startswith('g') and syl.unit(sm[signs.index(x)]).lower()==tv[x])/ns
        gacc=sum(1 for x in toks if x.startswith('g') and gw[groups.index(x)]<len(ws) and ws[gw[groups.index(x)]]==gv[x])/(len(toks)-ns)
        print(f'{best/len(toks):.3f}  sign tokens right {sacc:.2f}  group tokens right {gacc:.2f}',flush=True)
if __name__=='__main__':
    main()
