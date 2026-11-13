"""valscore.py KEY PAIRS : encipher each clear word with the key (m=x added from the involution, stated), compare with the reader's cipher word.
Letters agreeing = longest common subsequence; denominator = max(len(enciphered), len(read)). Also exact words."""
import sys
k={}
for l in open(sys.argv[1]):
    if l.startswith('#'): continue
    for p in l.split(): x,y=p.split('='); k[x]=y
inv={v:c for c,v in k.items()}; inv['m']='x'
def lcs(a,b):
    D=[[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): D[i+1][j+1]=D[i][j]+1 if x==y else max(D[i][j+1],D[i+1][j])
    return D[-1][-1]
A=T=W=X=skip=0; rows=[]
for l in open(sys.argv[2]):
    if l.startswith('#') or not l.strip(): continue
    c,p=l.rstrip('\n').split('\t'); c=c.replace('+','')
    if p=='-': skip+=1; continue
    e=''.join(inv[ch] for ch in p); m=lcs(c,e); d=max(len(c),len(e)); A+=m; T+=d; W+=1; X+=(c==e)
    rows.append('%-14s %-14s %-14s %d/%d%s'%(c,p,e,m,d,'' if c==e else '  <<'))
print('\n'.join(rows))
print('pairs counted %d ; not counted %d ; exact words %d/%d = %.2f%% ; letters %d/%d = %.2f%%'%(W,skip,X,W,100*X/W,A,T,100*A/T))
print('sum check: '+' + '.join(r.split()[3].split('/')[0] for r in rows)+' = %d'%A)
print('den check: '+' + '.join(r.split()[3].split('/')[1] for r in rows)+' = %d'%T)
