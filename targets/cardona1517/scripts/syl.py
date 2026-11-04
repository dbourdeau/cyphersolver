# Syllable test: signs may stand for a letter or one of the 40 commonest letter pairs; groups for a word or syllable.
import math,sys,os,re,random,collections,subprocess,multiprocessing as mp; from drv import *
WC=[l.split() for l in open('words.txt')]
bg=collections.Counter(); tg=collections.Counter()
for w,lp in WC[:600]:
    c=math.exp(float(lp))
    for i in range(len(w)-1): bg[w[i:i+2]]+=c
    for i in range(len(w)-2): tg[w[i:i+3]]+=c
PAIRS=[b for b,_ in bg.most_common(40)]; SYLS=PAIRS+[t for t,_ in tg.most_common(30)]
def task2(tokens,signs,groups,ws,fix={}):
    t=task(tokens,signs,groups,ws,fix)
    return t+''.join(f'UNIT 2 {IX[b[0]]} {IX[b[1]]}\n' for b in PAIRS)
def unit(u): return A[u] if u<len(A) else (PAIRS[u-len(A)].upper() if u<len(A)+len(PAIRS) else '_')
def runone(args):
    tk,seed,iters,R,extra,d=args
    os.makedirs(d,exist_ok=True); open(f'{d}/task.txt','w').write(tk)
    o=subprocess.run([os.environ.get('SOLVER','./wsa2'),'es.lm',f'{d}/task.txt',str(iters),str(R),str(seed),'-12']+extra,capture_output=True,text=True).stdout
    best=float(re.search(r'BEST (\S+)',o).group(1)); sm=list(map(int,o.split('\nSM')[1].split('\n')[0].split())); gw=list(map(int,o.split('\nGW')[1].split('\n')[0].split()))
    return best,seed,sm,gw
def control(nw=int(os.environ.get('NW','450')),npairs=8,runs=16,iters=int(os.environ.get('ITERS','300000')),R=3):
    rnd=random.Random(1)
    t=open('corp/g320.txt',encoding='utf-8',errors='ignore').read(); t=t[t.find('*** START'):t.find('*** END')]
    W=norm_words(t); st=rnd.randrange(2000,len(W)-700); W=W[st:st+nw]
    wc=collections.Counter(W); codew=[w for w,_ in wc.most_common(int(os.environ.get('NCODE','70')))]; code={w:f'g{i}' for i,w in enumerate(codew)}
    sp=[b for b in PAIRS[:npairs]]
    lc=collections.Counter(c for w in W if w not in code for c in w); signs=[];own={}
    for c,n in lc.most_common(): k=max(1,round(int(os.environ.get('NLET','31'))*n/sum(lc.values()))); own[c]=[f's{len(signs)+i}' for i in range(k)]; signs+=own[c]
    for b in sp: own[b]=[f'b{b}']; signs.append(f'b{b}')
    signs_all=signs
    toks=[];truth=[]
    for w in W:
        if w in code: toks.append(code[w]); continue
        i=0
        while i<len(w):
            if w[i:i+2] in sp: toks.append(own[w[i:i+2]][0]); truth.append(w[i:i+2]); i+=2
            else: toks.append(rnd.choice(own[w[i]])); truth.append(w[i]); i+=1
    groups=[code[w] for w in codew]; ws=words_file()+[s for s in SYLS if s not in words_file()]
    tk=task2(toks,signs,groups,ws)
    with mp.Pool(8) as p: res=sorted(p.map(runone,[(tk,s,iters,R,[],f'y{s}') for s in range(runs)]),reverse=True)
    ntok=len(toks); stoks=[x for x in toks if x in signs]
    print('control: tokens',ntok,'signs',len(stoks),'sign types',len(signs),'group tokens',ntok-len(stoks),'group types',len(set(toks)-set(signs)))
    for best,seed,sm,gw in res[:5]:
        dec=[unit(sm[signs.index(x)]).lower() for x in stoks]
        npair_used=sum(1 for x in signs if sm[signs.index(x)]>=len(A))
        print('pair values used by the key:',npair_used, end='  ')
        print(f'{best/ntok:.3f} letters right {sum(a==b for a,b in zip("".join(truth),"".join(dec)))/len("".join(truth)):.2f}',
              'pair signs:',' '.join(f'{x[1:]}={unit(sm[signs.index(x)])}' for x in signs if x.startswith('b')))
def real(fn,runs=int(os.environ.get("RUNS","16")),iters=int(os.environ.get('ITERS','300000')),R=3,extra=[]):
    L=[l.split() for l in open(fn) if l.strip() and not l.startswith('#')]; toks=[x for l in L for x in l]
    isg=lambda t: len(t)>1 and t.islower() and t.isalpha()
    signs=sorted({t for t in toks if not isg(t)}); groups=sorted({t for t in toks if isg(t)})
    ws=words_file()+[s for s in SYLS if s not in words_file()]
    if os.environ.get('GLET'): ws+=[c for c in A if c not in ws]
    if os.environ.get('WIDE'): ws=[l.strip() for l in open('wide_words.txt') if l.strip()]
    fixg={}
    for kv in os.environ.get('FIXG','').split():
        g,w=kv.split('=')
        if w not in ws: ws.append(w)
        fixg[g]=w
    tk=task2(toks,signs,groups,ws,fixg)
    for kv in os.environ.get('FIXS','').split():
        sg,val=kv.split('='); u=A.index(val) if len(val)==1 else len(A)+PAIRS.index(val.lower())
        tk+=f'FIXS {signs.index(sg)} {u}\n'
    with mp.Pool(8) as p: res=sorted(p.map(runone,[(tk,s,iters,R,extra,f'z{s}') for s in range(int(os.environ.get('SEEDOFF','0')),int(os.environ.get('SEEDOFF','0'))+runs)]),reverse=True)
    import json; json.dump([(b,s,sm,gw) for b,s,sm,gw in res],open(os.environ.get('DUMP','last.json'),'w')); json.dump([signs,groups,ws],open(os.environ.get('DUMP','last.json')+'.meta','w'))
    for best,seed,sm,gw in res[:3]:
        print(f'{best/len(toks):.3f}',' '.join(f'{s}={unit(sm[i])}' for i,s in enumerate(signs)))
        out=[]
        for t in toks:
            out.append(unit(sm[signs.index(t)]) if t in signs else ' ['+(ws[gw[groups.index(t)]] if gw[groups.index(t)]<len(ws) else '?')+'] ')
        print('  ',re.sub(' +',' ',''.join(out))[:400])
if __name__=='__main__':
    import math
    if sys.argv[1]=='control': control(npairs=int(os.environ.get('NPAIRS','8')))
    else: real(sys.argv[2],extra=sys.argv[3:])
