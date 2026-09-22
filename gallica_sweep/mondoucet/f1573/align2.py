# Hard-EM alignment of hand-transcribed 1573 cipher pages to the Court's decipherment.
# usage: python align.py ct1.txt:pt1.txt [ct2.txt:pt2.txt ...]  -> key1573.json, align_out.txt
# Moves: token->letter, token->null, plaintext letter skipped, token->2..8 letters (code sign).
import sys, json, math, collections, re, os
HERE=os.path.dirname(os.path.abspath(__file__)); OUT=os.environ.get('OUT',os.path.join(HERE,'key_out'))
ALPHA='abcdefghiklmnopqrstuvxyz'
def norm(s):
    s=s.lower().replace('j','i').replace('v','u').replace('w','u')
    s=re.sub('[çc]','c',s)
    return ''.join(ch for ch in s if ch in ALPHA)
def read_ct(fn):
    toks=[]
    for l in open(fn,encoding='utf-8'):
        if l.startswith('#') or ':' not in l: continue
        lab,rest=l.split(':',1)
        for t in rest.split():
            if t in ('.','/',':'): continue
            if t.startswith('['): toks.append(('CLEAR',norm(t),lab.strip())); continue
            toks.append((t,None,lab.strip()))
    return toks
def read_pt(fn):
    s=''
    for l in open(fn,encoding='utf-8'):
        if l.startswith('#') or ':' not in l: continue
        s+=norm(l.split(':',1)[1])
    return s
# prior from the 1572 key
k1572=json.load(open(os.path.join(HERE,'..','hand','key_counts.json')))
prior=collections.defaultdict(collections.Counter)
for t,c in k1572.items():
    for ch,v in c.items():
        if ch in ALPHA: prior[t][ch]+=min(v,5)*0.6
NULLP={'*':0.9,'+':0.5}
SKIP=5.0; CODE0=9.0; CODEL=0.6; FLOOR=0.05
def model(counts,nulls):
    P={}
    toks=set(counts)|set(prior)|set(nulls)
    for t in toks:
        c=collections.Counter(prior.get(t,{}))
        for ch,v in counts.get(t,{}).items(): c[ch]+=v
        nn=nulls.get(t,0)+ (3*NULLP[t] if t in NULLP else 0.05)
        S=sum(c.values())+nn+FLOOR*len(ALPHA)
        P[t]=({ch:-math.log((c.get(ch,0)+FLOOR)/S) for ch in ALPHA}, -math.log(nn/S))
    return P
def cost(P,t,ch):
    if t not in P: return -math.log(1/24)+0.5
    return P[t][0][ch]
def nullc(P,t):
    if t not in P: return 4.0
    return P[t][1]
def align(toks,pt,P,band=260):
    n,m=len(toks),len(pt); INF=1e18
    D=[dict() for _ in range(n+1)]; B=[dict() for _ in range(n+1)]
    D[0][0]=0.0
    for j in range(1,min(m,band)+1): D[0][j]=j*SKIP; B[0][j]=('skip',)
    for i in range(1,n+1):
        t,clear,_=toks[i-1]; c=i*m/n
        lo=max(0,int(c-band)); hi=min(m,int(c+band))
        Di=D[i]; Bi=B[i]; Dp=D[i-1]
        for j in range(lo,hi+1):
            best=INF; bb=None
            if clear is not None:
                L=len(clear)
                if j-L in Dp:
                    v=Dp[j-L]+ (0 if pt[j-L:j]==clear else 3.0*L)
                    if v<best: best,bb=v,('clear',L)
                if j in Dp and Dp[j]+3.0*L<best: best,bb=Dp[j]+3.0*L,('clearnull',)
            else:
                if j-1 in Dp:
                    v=Dp[j-1]+cost(P,t,pt[j-1])
                    if v<best: best,bb=v,('emit',)
                if j in Dp:
                    v=Dp[j]+nullc(P,t)
                    if v<best: best,bb=v,('null',)
                for L in range(2,9):
                    if j-L in Dp:
                        v=Dp[j-L]+CODE0+CODEL*L
                        if v<best: best,bb=v,('code',L)
            if j-1 in Di:
                v=Di[j-1]+SKIP
                if v<best: best,bb=v,('skip',)
            if bb: Di[j]=best; Bi[j]=bb
    # backtrace
    i,j=n,m; path=[]
    if m not in D[n]: j=min(D[n],key=lambda k:D[n][k]+abs(m-k)*SKIP)
    while i>0 or j>0:
        mv=B[i].get(j) if i>=0 else None
        if mv is None: # only skips remain at i=0
            path.append(('skip',None,pt[j-1])); j-=1; continue
        if mv[0]=='emit': path.append(('emit',toks[i-1],pt[j-1])); i-=1; j-=1
        elif mv[0]=='null': path.append(('null',toks[i-1],'')); i-=1
        elif mv[0]=='skip': path.append(('skip',None,pt[j-1])); j-=1
        elif mv[0]=='code': L=mv[1]; path.append(('code',toks[i-1],pt[j-L:j])); i-=1; j-=L
        elif mv[0]=='clear': L=mv[1]; path.append(('clear',toks[i-1],pt[j-L:j])); i-=1; j-=L
        elif mv[0]=='clearnull': path.append(('clearnull',toks[i-1],'')); i-=1
    path.reverse()
    return D[n].get(m,min(D[n].values())),path
pairs=[a.split(':') for a in sys.argv[1:]]
data=[(read_ct(os.path.join(HERE,c)),read_pt(os.path.join(HERE,p))) for c,p in pairs]
counts=collections.defaultdict(collections.Counter); nulls=collections.Counter()
for it in range(6):
    P=model(counts,nulls)
    nc=collections.defaultdict(collections.Counter); nn=collections.Counter(); tot=0; paths=[]
    for toks,pt in data:
        sc,path=align(toks,pt,P); tot+=sc; paths.append(path)
        for mv,tk,ch in path:
            if mv=='emit': nc[tk[0]][ch]+=1
            elif mv=='null': nn[tk[0]]+=1
    counts,nulls=nc,nn
    print('iter',it,'cost %.0f'%tot, 'emits',sum(1 for p in paths for x in p if x[0]=='emit'),
          'nulls',sum(nn.values()),'skips',sum(1 for p in paths for x in p if x[0]=='skip'),
          'codes',sum(1 for p in paths for x in p if x[0]=='code'),flush=True)
json.dump({'counts':{t:dict(c) for t,c in counts.items()},'nulls':dict(nulls)},open(OUT+'.json','w'),indent=0)
with open(OUT+'_align.txt','w',encoding='utf-8') as f:
    for t in sorted(counts,key=lambda t:-sum(counts[t].values())):
        f.write('%-4s n=%3d null=%2d  %s\n'%(t,sum(counts[t].values()),nulls.get(t,0),' '.join('%s%d'%(c,v) for c,v in counts[t].most_common(6))))
    for p in paths:
        f.write('\n'); lab=None; ct=''; pl=''
        for mv,tk,ch in p:
            if tk and tk[2]!=lab:
                if lab: f.write('%s | %s\n   | %s\n'%(lab,ct,pl))
                lab=tk[2]; ct=''; pl=''
            g=tk[0] if tk else '-'
            if mv=='emit': ct+=g+' '; pl+=ch+' '*len(g)
            elif mv=='null': ct+=g+' '; pl+='_'+' '*len(g)
            elif mv=='skip': ct+='- '; pl+=ch.upper()+' '
            elif mv in('code','clear'): ct+=g+' '; pl+='{'+ch+'}'+' '
            elif mv=='clearnull': ct+=g+' '; pl+='{?}'
        f.write('%s | %s\n   | %s\n'%(lab,ct,pl))
