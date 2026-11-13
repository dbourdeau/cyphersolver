import sys,string
A=string.ascii_lowercase
def porta(c,k):
    k=A.index(k)//2; c=A.index(c)
    if c<13: return A[13+(c+k)%13]
    return A[(c-13-k)%13]
def vig(c,k,alph=A): n=len(alph); return alph[(alph.index(c)-alph.index(k))%n]
def beau(c,k,alph=A): n=len(alph); return alph[(alph.index(k)-alph.index(c))%n]
def var(c,k,alph=A): n=len(alph); return alph[(alph.index(c)+alph.index(k))%n]
ct=sys.argv[1]; key=sys.argv[2]
for name,f in [('porta',porta),('vig',vig),('beau',beau),('var',var)]:
    for off in range(len(key)):
        try: out=''.join(f(c,key[(i+off)%len(key)]) for i,c in enumerate(ct))
        except ValueError: continue
        print(name,off,out)
