"""build_lm27.py corpus.txt out.bin [order=5]
Character LM over a-z (26) + '#' (26 = word boundary, used only as left padding at a word-anchored segment start).
Spaces are removed inside the stream (the cipher runs carry no word breaks). Witten-Bell interpolation 5->4->3->2->1->uniform.
Tables written (float32, natural log): main[27^4*26]  P(x | c1 c2 c3 c4), contexts may start with '#' padding (anchored at a word start)
                                       pend[27^4]     log P(word ends here | last 4 symbols, '#'-padded if the run is shorter)
                                       un1[26], un2[26*26], un3[26^3], un4[26^4]  unanchored lower orders for runs not starting at a word boundary
"""
import sys, numpy as np
src,out=sys.argv[1],sys.argv[2]
txt=open(src,encoding='utf-8').read().lower()
words=[w for w in ''.join(ch if 'a'<=ch<='z' else ' ' for ch in txt).split() if w]
S=np.frombuffer(''.join(words).encode(),dtype=np.uint8)-97
L=len(S); ws=np.zeros(L,bool); we=np.zeros(L,bool); p=0
for w in words:
    ws[p]=True; p+=len(w); we[p-1]=True
A=27; H=26
def counts(order):
    """counts[ctx(order-1 symbols over 27), x(26)] with '#'-padded anchored contexts added"""
    n=order-1
    C=np.zeros((A**n,26),np.float64)
    if n==0:
        C[0]=np.bincount(S,minlength=26); return C
    # internal
    idx=np.zeros(L-n,np.int64)
    for k in range(n): idx=idx*A+S[k:L-n+k]
    np.add.at(C,(idx,S[n:]),1)
    # anchored: context = '#'*(n-j) + S[i..i+j-1], predicts S[i+j], for j=0..n-1, i word start
    st=np.where(ws)[0]
    for j in range(0,n):
        ii=st[st+j<L]
        idx=np.zeros(len(ii),np.int64)
        for k in range(n-j): idx=idx*A+H
        for k in range(j): idx=idx*A+S[ii+k]
        np.add.at(C,(idx,S[ii+j]),1)
    return C
order=int(sys.argv[3]) if len(sys.argv)>3 else 5
P=np.full((1,26),1/26.0)
tabs={}
for o in range(1,order+1):
    C=counts(o); N=C.sum(1,keepdims=True); T=(C>0).sum(1,keepdims=True).astype(np.float64)
    n=o-1
    # lower-order prob for each context: drop leftmost symbol
    if n==0: low=np.full((1,26),1/26.0)
    else:
        ctx=np.arange(A**n); lowidx=ctx % (A**(n-1)); low=P[lowidx]
    lam=np.where(N+T>0,N/np.maximum(N+T,1e-12),0.0)
    # Witten-Bell: P = (C + T*low)/(N+T); if N==0 -> low
    P=np.where(N>0,(C+T*low)/np.maximum(N+T,1e-12),low)
    tabs[o]=P
main=np.log(tabs[order]).astype(np.float32)
# end probability: P(word end | last 4 symbols), backoff WB over context length
def endtab():
    Pe=np.full(1,we.mean())
    for n in range(1,5):
        Cn=np.zeros(A**n); En=np.zeros(A**n)
        idx=np.zeros(L-n+1,np.int64)
        for k in range(n): idx=idx*A+S[k:L-n+1+k]
        np.add.at(Cn,idx,1); np.add.at(En,idx[we[n-1:]],1)
        # anchored short runs: '#'*(n-j)+S[i..i+j-1], j=1..n-1, i a word start; end flag = we[i+j-1]
        st=np.where(ws)[0]
        for j in range(1,n):
            ii=st[st+j-1<L]
            ix=np.zeros(len(ii),np.int64)
            for k in range(n-j): ix=ix*A+H
            for k in range(j): ix=ix*A+S[ii+k]
            np.add.at(Cn,ix,1); np.add.at(En,ix[we[ii+j-1]],1)
        low=Pe[np.arange(A**n)%(A**(n-1))]
        K=3.0
        Pe=(En+K*low)/(Cn+K)
    return Pe
pend=np.log(np.maximum(endtab(),1e-6)).astype(np.float32)
def unanch(o):
    n=o-1; C=np.zeros((26**n,26))
    if n==0: C[0]=np.bincount(S,minlength=26)
    else:
        idx=np.zeros(L-n,np.int64)
        for k in range(n): idx=idx*26+S[k:L-n+k]
        np.add.at(C,(idx,S[n:]),1)
    return C
un=[]; Pl=np.full((1,26),1/26.0)
for o in range(1,5):
    C=unanch(o); N=C.sum(1,keepdims=True); T=(C>0).sum(1,keepdims=True).astype(float); n=o-1
    low=Pl[np.arange(26**n)%(26**max(n-1,0))] if n>0 else np.full((1,26),1/26.0)
    Pl=np.where(N>0,(C+T*low)/np.maximum(N+T,1e-12),low); un.append(np.log(Pl).astype(np.float32))
with open(out,'wb') as f:
    np.array([order,A],np.int32).tofile(f); main.tofile(f); pend.tofile(f)
    for u in un: u.tofile(f)
freq=np.bincount(S,minlength=26)/L
np.save(out+'.freq.npy',freq)
print('letters',L,'words',len(words),'order',order,'main',main.shape,'pend',pend.shape, 'bytes',main.nbytes+pend.nbytes)
# quick perplexity on held-out tail
