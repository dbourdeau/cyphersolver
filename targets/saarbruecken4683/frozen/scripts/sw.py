# Smith-Waterman (+1 / -1 / -1) : nombre de caractères de a alignés sur un caractère identique de b dans le meilleur alignement local
def sw_match(a,b):
    n,m=len(a),len(b)
    if n==0: return 0
    prev=[0]*(m+1); best=(0,0,0); ptrs=[]
    for i in range(1,n+1):
        cur=[0]*(m+1); p=bytearray(m+1); ai=a[i-1]
        for j in range(1,m+1):
            d=prev[j-1]+(1 if ai==b[j-1] else -1); u=prev[j]-1; l=cur[j-1]-1
            v=max(0,d,u,l); cur[j]=v
            p[j]=0 if v==0 else (1 if v==d else (2 if v==u else 3))
            if v>best[0]: best=(v,i,j)
        ptrs.append(p); prev=cur
    _,i,j=best; ok=0
    while i>0 and j>0:
        p=ptrs[i-1][j]
        if p==0: break
        if p==1: ok+= a[i-1]==b[j-1]; i-=1; j-=1
        elif p==2: i-=1
        else: j-=1
    return ok
