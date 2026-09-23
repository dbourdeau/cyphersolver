# seg.py "tokens..." [k] : top-k segmentations of a sign string into lexicon words under key (KEY env)
import sys,json,re,os,math,heapq
K=json.load(open(os.environ.get('KEY','key_v6.json'),encoding='utf8'))
L=json.load(open('lex2.json',encoding='utf8'))
toks=sys.argv[1].split(); k=int(sys.argv[2]) if len(sys.argv)>2 else 15
tot=sum(L.values())
def alt(t):
    if t=='?': return '[a-z]{0,2}'
    vs=K.get(t,'*').split(',')
    if '*' in vs: return '[a-z]{1,6}'
    opts=[v for v in vs if v]
    r='(?:'+'|'.join(re.escape(v) for v in opts)+')'
    return r+('?' if '' in vs else '')
words=[w for w in L if L[w]>=3 and len(w)<=16]
n=len(toks); span={}
for i in range(n):
    for j in range(i+1,min(n,i+12)+1):
        p=re.compile('^'+''.join(alt(t) for t in toks[i:j])+'$')
        span[(i,j)]=[(math.log(L[w]/tot),w) for w in words if p.match(w)]
        span[(i,j)].sort(reverse=True); span[(i,j)]=span[(i,j)][:8]
best=[[] for _ in range(n+1)]; best[0]=[(0.0,'')]
for j in range(1,n+1):
    c=[]
    for i in range(max(0,j-12),j):
        for s,txt in best[i]:
            for ls,w in span[(i,j)]:
                c.append((s+ls-3,txt+' '+w))
        # unknown single sign as '?'
        if j==i+1:
            for s,txt in best[i]: c.append((s-22,txt+' ?'))
    best[j]=heapq.nlargest(k,c)
for s,t in best[n]: print(round(s,1),t)
