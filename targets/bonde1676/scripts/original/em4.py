import sys,re,math,collections
# em2.py file : test hypothesis H (about 1 letter per 2-digit group; gloss runs ahead). Free end.
lines=open(sys.argv[1],encoding='utf-8').read().split('\n')
G=[];P=''
for l in lines:
    m=re.match(r'L\d+\s+G:\s*(.*)',l)
    if m: P+=re.sub(r'[^a-zåäö#]','',m.group(1).replace('EKM','#').lower().replace('(?)',''))
    m=re.match(r'L\d+\s+N:\s*(.*)',l)
    if m: G+=re.findall(r'\d+',m.group(1))
P=P[:P.find('audience')+8]
n=len(G);L=len(P)
def maxk(g): return 12 if int(g)>=200 else 3
def prior(g,k):
    if int(g)>=200: return 1.0/13
    return {0:0.0,1:1.0,2:0.06,3:0.0}[k]
prob={}
def p(g,s,it):
    if it==0 or int(g)>=200: return prior(g,len(s))
    return prob.get(g,{}).get(s,0)*0.97+0.03*prior(g,len(s))/ (24**len(s))
lo=lambda i:max(0,int(i*0.7)-30); hi=lambda i:min(L,int(i*1.5)+40)
ll=0
for it in range(60):
    A=[dict() for _ in range(n+1)]; A[0][0]=1.0; ll=0
    for i in range(1,n+1):
        g=G[i-1]; s_=0; row={}
        for j in range(lo(i),hi(i)+1):
            v=0
            for k in range(0,maxk(g)+1):
                a=A[i-1].get(j-k)
                if a: v+=a*p(g,P[j-k:j],it)
            if v: row[j]=v; s_+=v
        ll+=math.log(s_); A[i]={j:v/s_ for j,v in row.items()}
    B=[dict() for _ in range(n+1)]; B[n]={L:1.0}
    for i in range(n-1,-1,-1):
        g=G[i]; row={}; s_=0
        for j in A[i]:
            v=0
            for k in range(0,maxk(g)+1):
                b=B[i+1].get(j+k)
                if b: v+=b*p(g,P[j:j+k],it)
            if v: row[j]=v; s_+=v
        B[i]={j:v/s_ for j,v in row.items()}
    new=collections.defaultdict(lambda:collections.defaultdict(float))
    for i in range(1,n+1):
        g=G[i-1]; tmp={}; tot=0
        for j,b in B[i].items():
            for k in range(0,maxk(g)+1):
                a=A[i-1].get(j-k)
                if a:
                    w=a*p(g,P[j-k:j],it)*b
                    if w: tmp[(j-k,j)]=w; tot+=w
        for (a_,b_),w in tmp.items(): new[g][P[a_:b_]]+=w/tot
    prob={g:{s:w/sum(d.values()) for s,w in d.items()} for g,d in new.items()}
print('groups',n,'letters',L,'loglik/group %.3f'%(ll/n))
end=max(A[n],key=A[n].get); print('most likely end letter index',end,'of',L)
cnt=collections.Counter(G); crisp=0
for g,c in sorted(cnt.items(),key=lambda x:-x[1]):
    top=sorted(prob[g].items(),key=lambda x:-x[1])[:3]
    if c>=5: print(g,c,' '.join('%s:%.2f'%(s or '-',w) for s,w in top))
    if c>=5 and top[0][1]>=0.7: crisp+=1
print('types with n>=5:',sum(1 for c in cnt.values() if c>=5),'crisp(top>=0.7):',crisp)
# Viterbi print
V=[dict() for _ in range(n+1)]; V[0][0]=(0.0,None)
for i in range(1,n+1):
    g=G[i-1]
    for j in range(lo(i),hi(i)+1):
        best=None
        for k in range(0,maxk(g)+1):
            a=V[i-1].get(j-k)
            if a is None: continue
            q=p(g,P[j-k:j],1)
            if q<=0: continue
            s=a[0]+math.log(q)
            if best is None or s>best[0]: best=(s,k)
        if best: V[i][j]=best
j=L; out=[]
for i in range(n,0,-1):
    k=V[i][j][1]; out.append((G[i-1],P[j-k:j])); j-=k
out.reverse()
print(' '.join('%s=%s'%(g,s) for g,s in out))
import json
key={g:max(d.items(),key=lambda x:x[1]) for g,d in prob.items()}
json.dump({g:[s,round(w,2),cnt[g]] for g,(s,w) in key.items()},open('work/key_em.json','w'),ensure_ascii=False,indent=0)
print('DECODE:',''.join((key[g][0] if int(g)<200 else '['+g+']') for g in G))
print('GLOSS :',P[:620])
