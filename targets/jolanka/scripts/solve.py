# Substitution search on the TRAINING cards only. Each cipher sign type -> one Hungarian letter (many-to-one allowed).
# python3 -I tools/solve.py <seed> <restarts> <iters> [fold]    fold=1 strips +a/+aa before solving
import sys, gzip, json, random, math, collections, re
B='/home/claude/keyless/postcards/jolanka'
seed=int(sys.argv[1]); R=int(sys.argv[2]); IT=int(sys.argv[3]); fold=len(sys.argv)>4 and sys.argv[4]=='1'
m=json.load(gzip.open(B+'/hu-1900-lit.nospace.json.gz','rt',encoding='utf-8')); lp=m['logp4']; fl=m['floor4']; AL=m['alphabet']
lines=[]
for l in open(B+'/TRANSCRIPTION.tsv',encoding='utf-8').read().split('\n')[1:]:
    if not l: continue
    p=l.split('\t')
    if p[5]=='1': continue          # held-out card never read here
    seg=[]
    for t in re.findall(r'\{[^}]*\}|\[[^\]]*\]|\S+',p[6]):
        if t[0] in '{[' or t in ',.':
            if seg: lines.append(seg); seg=[]
            continue
        t=t.rstrip('?')
        if fold: t=t.split('+')[0]
        seg.append(t)
    if seg: lines.append(seg)
# lines are joined per card in reality; treat each uninterrupted run as a segment
syms=sorted({t for s in lines for t in s}); idx={s:i for i,s in enumerate(syms)}
segs=[[idx[t] for t in s] for s in lines]; n=sum(len(s) for s in segs)
def score(key):
    tot=0.0
    for s in segs:
        x=''.join(key[i] for i in s)
        for i in range(len(x)-3): tot+=lp.get(x[i:i+4],fl)
    return tot
rnd=random.Random(seed); best=(-1e18,None)
freq='eatlnskomzrigáéydvbhjöfupócíőüúűc'
cnt=collections.Counter(i for s in segs for i in s); order=[i for i,_ in cnt.most_common()]
for r in range(R):
    pool=list(AL); rnd.shuffle(pool)
    if r==0:
        pool=[None]*len(AL); rest=[c for c in AL if c not in freq[:len(syms)]]
        for k,i in enumerate(order): pool[i]=freq[k]
        pool=[c for c in pool if c]+[c for c in AL if c not in pool]
    key=pool          # key[i] for i<len(syms) is the letter of sign i; the tail holds unused letters
    sc=score(key)
    for it in range(IT):
        i=rnd.randrange(len(syms)); j=rnd.randrange(len(key))
        if i==j: continue
        key[i],key[j]=key[j],key[i]; s2=score(key); T=0.6*(1-it/IT)+0.01
        if s2>sc or rnd.random()<math.exp((s2-sc)/T): sc=s2
        else: key[i],key[j]=key[j],key[i]
    print('restart',r,'score/sign',round(sc/max(n,1),4), flush=True)
    if sc>best[0]: best=(sc,key[:len(syms)])
sc,key=best
print('BEST',round(sc/n,4),'n',n,'symbols',len(syms))
for s,k in sorted(zip(syms,key)): print(' ',s,'->',k,cnt[idx[s]])
for s in segs[:14]: print(''.join(key[i] for i in s))
json.dump({'seed':seed,'fold':fold,'score_per_sign':sc/n,'key':dict(zip(syms,key))},open(B+'/solve_out_seed%d_fold%d.json'%(seed,int(fold)),'w'),ensure_ascii=False,indent=1)
