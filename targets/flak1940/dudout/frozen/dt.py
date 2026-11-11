def undo(ct, ord_):
    n,k=len(ct),len(ord_); rows=-(-n//k); full=n%k or k
    pt=[None]*n; p=0
    for c in ord_:
        ln=rows if c<full else rows-1
        for r in range(ln): pt[r*k+c]=ct[p]; p+=1
    return ''.join(pt)
def enc(pt, ord_):
    n,k=len(pt),len(ord_)
    return ''.join(pt[r*k+c] for c in ord_ for r in range(-(-n//k)) if r*k+c<n)
def key_to_order(key): return sorted(range(len(key)), key=lambda i:(key[i],i))
def order_to_key(o):
    k=[0]*len(o)
    for r,c in enumerate(o): k[c]=r+1
    return k
