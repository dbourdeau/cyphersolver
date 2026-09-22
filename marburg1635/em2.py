import collections,math
T="6 0 9 6 F T 4 M 6 1 2 9 0 3 6 0 7 T 4 X 3 9 1 7 6 F 6 F 8 1 2 W F 4 5 D 9 6 1 2 2 5 F W 9 6 3".split()
L="daskanndiesesorthsselberobservirendagegenauchselbst"
P1=collections.defaultdict(lambda:.05);P2=collections.defaultdict(lambda:.001)
PS=.05;PN=.05
n,m=len(L),len(T)
for it in range(60):
    F=[[0.0]*(m+1) for _ in range(n+1)];F[0][0]=1
    for i in range(n+1):
        for j in range(m+1):
            if i==j==0: continue
            v=0
            if i and j: v+=F[i-1][j-1]*P1[(L[i-1],T[j-1])]
            if i and j>1: v+=F[i-1][j-2]*P2[(L[i-1],T[j-2]+T[j-1])]
            if i: v+=F[i-1][j]*PS
            if j: v+=F[i][j-1]*PN
            F[i][j]=v
    B=[[0.0]*(m+2) for _ in range(n+2)];B[n][m]=1
    for i in range(n,-1,-1):
        for j in range(m,-1,-1):
            if i==n and j==m: continue
            v=0
            if i<n and j<m: v+=B[i+1][j+1]*P1[(L[i],T[j])]
            if i<n and j<m-1: v+=B[i+1][j+2]*P2[(L[i],T[j]+T[j+1])]
            if i<n: v+=B[i+1][j]*PS
            if j<m: v+=B[i][j+1]*PN
            B[i][j]=v
    Z=F[n][m];C1=collections.defaultdict(float);C2=collections.defaultdict(float)
    for i in range(1,n+1):
        for j in range(1,m+1):
            C1[(L[i-1],T[j-1])]+=F[i-1][j-1]*P1[(L[i-1],T[j-1])]*B[i][j]/Z
            if j>1: C2[(L[i-1],T[j-2]+T[j-1])]+=F[i-1][j-2]*P2[(L[i-1],T[j-2]+T[j-1])]*B[i][j]/Z
    tot=collections.defaultdict(float)
    for (a,t),v in list(C1.items())+list(C2.items()): tot[a]+=v
    P1=collections.defaultdict(lambda:1e-4,{k:v/tot[k[0]]+1e-4 for k,v in C1.items()})
    P2=collections.defaultdict(lambda:1e-5,{k:v/tot[k[0]]*0.5+1e-5 for k,v in C2.items()})
# viterbi
import itertools
V=[[(-1e9,None)]*(m+1) for _ in range(n+1)];V[0][0]=(0,None)
for i in range(n+1):
    for j in range(m+1):
        if i==j==0: continue
        c=[]
        if i and j: c.append((V[i-1][j-1][0]+math.log(P1[(L[i-1],T[j-1])]),(i-1,j-1,L[i-1]+'='+T[j-1])))
        if i and j>1: c.append((V[i-1][j-2][0]+math.log(P2[(L[i-1],T[j-2]+T[j-1])]),(i-1,j-2,L[i-1]+'='+T[j-2]+T[j-1])))
        if i: c.append((V[i-1][j][0]+math.log(PS),(i-1,j,L[i-1]+'=-')))
        if j: c.append((V[i][j-1][0]+math.log(PN),(i,j-1,'-='+T[j-1])))
        V[i][j]=max(c)
out=[];i,j=n,m
while (i,j)!=(0,0):
    s,b=V[i][j];out.append(b[2]);i,j=b[0],b[1]
print(' '.join(reversed(out)))
