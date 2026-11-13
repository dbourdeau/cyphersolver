import sys,string
A=string.ascii_lowercase
def porta(c,k):
    k=A.index(k)//2; c=A.index(c)
    if c<13: return A[13+(c+k)%13]
    return A[(c-13-k)%13]
KEY='constantinopolitanus'
def dec(ct,off=0,key=KEY):
    return ''.join(porta(c,key[(i+off)%len(key)]) if c in A else c for i,c in enumerate(ct))
if __name__=='__main__':
    for ct in sys.argv[1:]:
        print(ct,'->',dec(ct))
