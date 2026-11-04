# Noisy version of control_matched.py (cardona1517): same Lazarillo text and encipherment, plus
#   NOUT  extra code groups for frequent words of 5+ letters that are NOT in the option list (wide_words.txt)
#   NOISE fraction of tokens replaced by another token of the same kind (misreadings)
# Prints sign / group accuracy of the best runs and the true key's score.
import os,random,collections,multiprocessing as mp,re,subprocess
from drv import norm_words, A
import syl
NW=int(os.environ.get('NW','600')); PS=float(os.environ.get('PS','0.22')); NCW=int(os.environ.get('NCW','45'))
NCS=int(os.environ.get('NCS','70')); NLET=int(os.environ.get('NLET','68')); NOUT=int(os.environ.get('NOUT','35'))
NOISE=float(os.environ.get('NOISE','0.05')); ITERS=int(os.environ.get('ITERS','10000000')); RUNS=int(os.environ.get('RUNS','16'))
ws=[l.strip() for l in open('wide_words.txt') if l.strip()]; WS=set(ws)
def build():
    rnd=random.Random(1)
    t=open('corp/g320.txt',encoding='utf-8',errors='ignore').read(); t=t[t.find('*** START'):t.find('*** END')]
    W=norm_words(t)[6402:6402+NW]
    cw=[w for w,_ in collections.Counter(W).most_common(NCW)]
    out=[w for w,_ in collections.Counter(w for w in W if len(w)>=5 and w not in WS and w not in cw).most_common(NOUT)]
    sub=collections.Counter()
    for w in W:
        if w in cw or w in out: continue
        for L in (1,2,3):
            for i in range(len(w)-L+1): sub[w[i:i+L]]+=1
    cs=[s for s,_ in sub.most_common(400) if s not in cw][:NCS]
    code={x:f'g{i}' for i,x in enumerate(cw+out+cs)}; pairs=syl.PAIRS[:8]
    lc=collections.Counter(c for w in W if w not in cw and w not in out for c in w); own={}; n=0
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
    S=sorted({x for x in toks if not x.startswith('g')}); G=sorted({x for x in toks if x.startswith('g')})
    clean=list(toks); nerr=0
    for i,x in enumerate(toks):
        if rnd.random()<NOISE:
            pool=G if x.startswith('g') else S; toks[i]=rnd.choice([y for y in pool if y!=x]); nerr+=1
    return clean,toks,truth,nerr
def main():
    clean,toks,truth,nerr=build()
    groups=sorted({x for x in toks if x.startswith('g')}); signs=sorted({x for x in toks if not x.startswith('g')})
    tv={};gv={}
    for x,tr in zip(clean,truth): (gv if x.startswith('g') else tv)[x]=tr
    ns=sum(1 for x in toks if not x.startswith('g'))
    gin=sum(1 for g in groups if gv.get(g) in WS)
    print(f'noisy control: tokens {len(toks)} signs {ns} sign types {len(signs)} groups {len(toks)-ns} group types {len(groups)}; '
          f'group types with value in list {gin}/{len(groups)}; tokens altered {nerr}',flush=True)
    tk=syl.task2(toks,signs,groups,ws)
    # true key score (on the noisy tokens)
    tt=tk+''.join(f'FIXS {i} {A.index(tv[s]) if len(tv[s])==1 else len(A)+syl.PAIRS.index(tv[s])}\n' for i,s in enumerate(signs))
    tt+=''.join(f'FIX {i} {ws.index(gv[g]) if gv[g] in WS else len(ws)}\n' for i,g in enumerate(groups))
    open('task_noisy_true.txt','w').write(tt)
    o=subprocess.run(['./wsa4','es.lm','task_noisy_true.txt','1','1','1','-12'],capture_output=True,text=True).stdout
    print(f'true key: {float(re.search(r"BEST (\S+)",o).group(1))/len(toks):.3f} per token',flush=True)
    with mp.Pool(8) as p: res=sorted(p.map(syl.runone,[(tk,s,ITERS,3,[],f'n{s}') for s in range(RUNS)]),reverse=True)
    for best,seed,sm,gw in res[:6]:
        sacc=sum(1 for x,c in zip(toks,clean) if x==c and not x.startswith('g') and syl.unit(sm[signs.index(x)]).lower()==tv[x])/ns
        gacc=sum(1 for x,c in zip(toks,clean) if x==c and x.startswith('g') and gw[groups.index(x)]<len(ws) and ws[gw[groups.index(x)]]==gv[x])/(len(toks)-ns)
        print(f'{best/len(toks):.3f}  sign tokens right {sacc:.2f}  group tokens right {gacc:.2f}',flush=True)
if __name__=='__main__': main()
