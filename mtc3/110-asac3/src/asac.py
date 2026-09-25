# Reference implementation of Fendt's ASAC (challenge.cpp / polybius.cpp / transposition.cpp).
import random
def keyshifts(pw):
    pw=pw.upper(); k=[pw[i%len(pw)] for i in range(20)]
    return [(ord(c)-65)%10 for c in k[:10]], [(ord(c)-65)%10 for c in k[10:]]  # sX (KeyX, columns), sY (KeyY, rows)
def init_alnum():
    d=[str(i) for i in range(10)]; e='['
    while len(d)<100:
        cnt=2 if e in 'AIOU' else (4 if e=='E' else 1)
        for _ in range(cnt):
            if len(d)<100: d.append(' ' if e=='[' else e)
        e=chr(ord(e)+1)
        if e==chr(92): e='A'
    return d
def init_rng(): return [str(n%10) for n in range(100)]
def transpose(data,sX,sY):
    d=list(data)
    for y in range(10):   # transposeX: rotate rows by sY[y]
        row=d[10*y:10*y+10]; d[10*y:10*y+10]=[row[(x-sY[y])%10] for x in range(10)]
    for x in range(10):   # transposeY: rotate columns by sX[x]
        col=[d[x+10*y] for y in range(10)]
        for y in range(10): d[x+10*y]=col[(y-sX[x])%10]
    return d
def square(sX,sY): return transpose(init_alnum(),sX,sY)
def prng(sX,sY): return [int(c) for c in transpose(init_rng(),sX,sY)]
def trans_order(key):
    k=list(key.upper()); o=list(range(len(k)))
    # C++ bubble on the ORIGINAL (not uppercased) key; keys here are upper already
    for n in range(len(k)):
        for m in range(len(k)-1-n):
            if k[m+1]<k[m]: k[m],k[m+1]=k[m+1],k[m]; o[m],o[m+1]=o[m+1],o[m]
    return o
def trans_enc(s,order):
    L=len(order); return ''.join(s[x::L] for x in order)
def trans_dec(s,order):
    L=len(order); N=len(s); out=[None]*N; i=0
    for x in order:
        n=len(range(x,N,L)); out[x::L]=s[i:i+n]; i+=n
    return ''.join(out)
def poly_enc(text,sq,rng=random):
    out=[]
    for c in text.upper():
        if not (c.isdigit() or 'A'<=c<='Z' or c==' '): continue
        r=rng.randrange(100)
        for n in range(100):
            i=(r+n)%100
            if sq[i]==c: break
        out.append(str(i%10)+str(i//10))
    return ''.join(out)
def add_prng(s,k,reshuffle=None):
    out=[]; k=list(k)
    for n,ch in enumerate(s):
        out.append(str((int(ch)+k[n%100])%10))
        if reshuffle and n%100==99: k=reshuffle(k)
    return ''.join(out)
if __name__=='__main__':
    sX,sY=keyshifts('KRYPTOGRAFENHAUSBOOT'); sq=square(sX,sY)
    for y in range(10): print(''.join(sq[10*y:10*y+10]).replace(' ','_'))
    pX,pY=keyshifts('PASSWORTZWEI'); k=prng(pX,pY)
    for y in range(10): print(''.join(map(str,k[10*y:10*y+10])))
    s1='3107576912422869870906462591217877215647789769430673325706'
    s2=add_prng(s1,k); print(s2)
    ct=trans_enc(trans_enc(s2,trans_order('HALLOWELT')),trans_order('VOGELFEDER')); print(ct)
    # decode check of s1 with sq
    print(''.join(sq[int(s1[i])+10*int(s1[i+1])] for i in range(0,len(s1),2)))
