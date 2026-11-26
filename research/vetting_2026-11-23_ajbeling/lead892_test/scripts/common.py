import re
import os
O=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')+os.sep
def load(path):
    L={}
    for line in open(path,encoding='utf-8'):
        m=re.match(r'^([AB]\d\d):\s*(.*)$',line.strip())
        if m: L[m.group(1)]=m.group(2).split()
    return L
def norm(t):
    t=t.strip()
    if t.startswith('{'): return t.strip('{}?').lower()
    t=t.split('/')[0]
    if t!='??' : t=t.rstrip('?')
    return t
def align(a,b):
    n,m=len(a),len(b); D=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): D[i][0]=i
    for j in range(m+1): D[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            D[i][j]=min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+(a[i-1]!=b[j-1]))
    i,j=n,m; pairs=[]
    while i>0 or j>0:
        if i>0 and j>0 and D[i][j]==D[i-1][j-1]+(a[i-1]!=b[j-1]): pairs.append((a[i-1],b[j-1])); i-=1; j-=1
        elif i>0 and D[i][j]==D[i-1][j]+1: pairs.append((a[i-1],None)); i-=1
        else: pairs.append((None,b[j-1])); j-=1
    return pairs[::-1]
