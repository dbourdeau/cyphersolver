# heldout.py pass clear key : frozen key on held-out cipher, global alignment to clear text, shuffled-table control
import sys,json,random
S=[x for l in open(sys.argv[1],encoding='utf8') for x in l.split()]
P=''.join(c for c in open(sys.argv[2],encoding='utf8').read() if c.isalpha()).replace('v','u')
key=json.load(open(sys.argv[3],encoding='utf8'))
key={k:v.replace('v','u') for k,v in key.items()}
def nw(a,b):
    n,m=len(a),len(b); prev=list(range(0,-(m+1),-1)); bt=[]
    dp=[[0]*(m+1) for _ in range(n+1)]
    for j in range(m+1): dp[0][j]=-j
    for i in range(1,n+1):
        dp[i][0]=-i
        for j in range(1,m+1):
            dp[i][j]=max(dp[i-1][j-1]+(1 if a[i-1]==b[j-1] else -1),dp[i-1][j]-1,dp[i][j-1]-1)
    i,j=n,m; ops=[]; match=0
    while i>0 or j>0:
        if i>0 and j>0 and dp[i][j]==dp[i-1][j-1]+(1 if a[i-1]==b[j-1] else -1):
            ops.append((a[i-1],b[j-1])); match+= a[i-1]==b[j-1]; i-=1;j-=1
        elif i>0 and dp[i][j]==dp[i-1][j]-1: ops.append((a[i-1],'-')); i-=1
        else: ops.append(('-',b[j-1])); j-=1
    return match,ops[::-1]
D=''.join(key.get(s,'?') for s in S)
m,ops=nw(D,P)
print('signs',len(S),'clear',len(P),'matches',m,'rate over clear',round(m/len(P),4),'rate over signs',round(m/len(S),4))
print(D); 
print('diffs',[o for o in ops if o[0]!=o[1]])
rng=random.Random(1)
vals=list(key.values()); ks=list(key.keys()); R=[]
N=int(sys.argv[4]) if len(sys.argv)>4 else 200
for _ in range(N):
    v=vals[:]; rng.shuffle(v); k2=dict(zip(ks,v)); d=''.join(k2.get(s,'?') for s in S)
    # no-gap comparison and gapped comparison on a subset
    mm,_o=nw(d,P); R.append(mm/len(P))
R.sort(); print('shuffled table: mean',round(sum(R)/N,4),'max',round(R[-1],4),'n',N)
