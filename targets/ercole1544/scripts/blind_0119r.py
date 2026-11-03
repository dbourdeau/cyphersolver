# usage, from the target folder: python scripts/blind_0119r.py : scores the blind reading of c. 119r and the old transcription, each against the lines settled on crops.
import re,sys
sys.stdout.reconfigure(encoding='utf8')
tok=lambda b: re.findall(r'L\^\w+|\d+|\?|[A-Za-z]',b)
def load(f):
    d={}
    for l in open(f,encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        a,_,b=l.strip().partition(' '); d[a]=tok(b)
    return d
def align(a,b):
    n,m=len(a),len(b); D=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): D[i][0]=i
    for j in range(m+1): D[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            D[i][j]=min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+(a[i-1]!=b[j-1]))
    i,j=n,m; ops=[]
    while i or j:
        if i and j and D[i][j]==D[i-1][j-1]+(a[i-1]!=b[j-1]):
            if a[i-1]!=b[j-1]: ops.append((a[i-1],b[j-1]))
            i-=1;j-=1
        elif i and D[i][j]==D[i-1][j]+1: ops.append((a[i-1],'-')); i-=1
        else: ops.append(('-',b[j-1])); j-=1
    return D[n][m],ops[::-1]
S=load('validation/blind_0119r_settled.txt'); T=load('validation/blind_0119r_before.txt'); P1=load('validation/1554_pass1/0119r.txt')
B=dict(zip(S,load('validation/blind_0119r.txt').values()))
print('line signs blind_v_transcription transcription_v_settled blind_v_settled pass1_v_settled')
tt=[0]*5
for k in S:
    n=len(S[k]); v=(n,align(B[k],T[k])[0],align(T[k],S[k])[0],align(B[k],S[k])[0],align(P1[k],S[k])[0])
    print(k,*v)
    tt=[x+y for x,y in zip(tt,v)]
n=tt[0]; print('all',n,*[f'{x} ({100*x/n:.1f}%)' for x in tt[1:]])
