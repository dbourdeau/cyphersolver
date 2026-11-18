import json,gzip,random,re,sys,itertools
K=json.load(open(sys.argv[1]))['key']; passB=sys.argv[2]
lex=json.load(gzip.open(sys.argv[3],'rt'))
W=set(w.lower() for w in (lex if isinstance(lex,list) else lex.keys()))
W|={'molly','kimball','newbury','bartlett','bartletts','tivertown','sergt','corpl','inst','capt'}
C={'z':['=','3'],'i':['1','.','\\'],'o':['o','A'],'-':['-'],'t':['t'],'h':['t\\'],'g':['g'],'l':['l'],'.':['.'],'w':['~'],'r':['v','\\'],'8':['B','d','c'],'f':['y'],'+':['+'],'L':['t'],'v':['^','j'],'F':['+','p'],'a':['A'],'p':['p'],'s':['j'],'c':['c'],'u':['A'],'2':['=','3']}
pages={('15','L'),('15','R'),('16','L'),('18','R'),('19','L'),('22','L'),('29','-')}
toks=[]
for line in open(passB):
    p=line.rstrip('\n').split('\t')
    if len(p)<6 or p[0]=='image' or (p[0],p[1]) not in pages: continue
    t=p[5]; t=re.sub(r'\{[^}]*\}','',t); t=re.sub(r'<del:[^>]*>','',t); t=re.sub(r'\([^)]*\)','',t)
    t=t.replace('<ins:','').replace('<box:','').replace('>','')
    for w in t.split():
        w=re.sub(r'\[([^|\]]*)\|[^\]]*\]',r'\1',w).strip(',;=')
        if len(w)>=2 and all(ch in C for ch in w): toks.append(w)
        elif len(w)>=2: toks.append(None)  # contains unmapped sign: counts as miss
def expansions(w):
    opts=[C[ch] for ch in w]
    n=1
    for o in opts: n*=len(o)
    if n>4096: return []
    return [''.join(x) for x in itertools.product(*opts)]
EXP=[expansions(w) if w else [] for w in toks]
def share(k):
    hit=0
    for ex in EXP:
        if any(''.join(k.get(c,'?') for c in e) in W for e in ex): hit+=1
    return hit/len(EXP)
s0=share(K)
rnd=random.Random(1780); g=list(K.keys()); v=list(K.values()); sh=[]
for _ in range(200):
    rnd.shuffle(v); sh.append(share(dict(zip(g,v))))
sh.sort()
print('words',len(EXP),'frozen share %.3f'%s0,'shuffled mean %.3f p99 %.3f max %.3f'%(sum(sh)/200,sh[197],sh[-1]))
print('PASS' if s0>=0.35 and s0>sh[197] else 'FAIL')
