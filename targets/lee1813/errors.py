"""lee1813: how Lee's mistakes produce the garbled letters. Standard library only.

    python errors.py            write error_accounts.txt: for every stretch whose reading differs from the
                                mechanical text, the cheapest set of mistakes that turns the reading into Lee's numerals

The model enciphers the reading (read as, in decryption_*.txt) with WINCHESTER and searches for the cheapest way to
reach the numerals Lee wrote, allowing these mistakes (cost in brackets):
  a figure off by one place (1), a tens figure added or lost, e.g. 17 for 7 (1), two look-alike figures such as 10/16,
  1/7, 3/8, which may be our misreading (1.2), one figure enciphered with the next or previous key letter (1.2),
  two figures run together with no dot, e.g. 17 for 1 7 (1), one figure split by a stray dot, e.g. 1.2 for 12 (1),
  a letter left out with its key letter used up (1.5) or not (1.8), a key letter skipped or used twice (1.5),
  a larger key jump (3), a figure with no letter in the reading (2), any other wrong figure (2.5).
The start of each stretch may use any key position (cost 1 unless it is W). Costs are judgement, not fitted; the
accounts are explanations consistent with the numerals, not proof of what Lee did.
"""
import re, sys, heapq, pathlib
A='ABCDEFGHIKLMNOPQRSTUVWXYZ'; K='WINCHESTER'
D=pathlib.Path(__file__).resolve().parent
SHAPES={(1,7),(7,1),(3,8),(8,3),(10,16),(16,10),(4,9),(9,4),(3,5),(5,3),(11,17),(17,11),(2,7),(7,2),(13,18),(18,13),(14,19),(19,14),(5,6),(6,5)}
def L(n,k): return A[(n-1+A.index(K[k%10]))%25]
def need(p,k): return (A.index(p)-A.index(K[k%10]))%25+1
def subcost(n,p,k):
    m=need(p,k)
    if m==n: return 0,None
    if abs(m-n)==10: return 1,f'wrote {n} for {m} (tens figure added or lost)'
    if abs(m-n)==1 or abs(m-n)==24: return 1,f'wrote {n} for {m} (counted one place off)'
    if (n,m) in SHAPES: return 1.2,f'wrote {n} for {m} (look-alike figures; could be our reading)'
    # wrong key letter for one figure: does a neighbouring key letter give it?
    for d in (1,-1):
        if L(n,k+d)==p: return 1.2,f'{n} enciphered with the {"next" if d==1 else "previous"} key letter ({K[(k+d)%10]} for {K[k%10]})'
    return 2.5,f'wrote {n} for {m} (no simple explanation)'
def target(read):
    t=re.sub(r'\[\.\.\.\]|\[…\]','',read)
    t=re.sub(r'[\[\]<>?]','',t)
    return re.sub(r'[^A-Za-z]','',t).upper().replace('J','I')
def account(ns, read, k0=None):
    T=target(read); N=len(ns); M=len(T)
    start=[(0 if (k0 is None and k==0) or k==k0 else 1.0, k) for k in range(10)]
    pq=[(c,0,0,k,()) for c,k in start]; seen={}
    while pq:
        c,i,j,k,ops=heapq.heappop(pq)
        key=(i,j,k)
        if key in seen: continue
        seen[key]=c
        if i==N and j==M: return c,ops,T
        def push(c2,i2,j2,k2,op):
            if i2<=N and j2<=M and (i2,j2,k2%10) not in seen: heapq.heappush(pq,(c+c2,i2,j2,k2%10,ops+(((op,i,j),) if op else ())))
        if i<N and j<M:
            sc,why=subcost(ns[i],T[j],k); push(sc,i+1,j+1,k+1,why)
        s=str(ns[i]) if i<N else ''
        if i<N and j+1<M and len(s)==2 and s[1]!='0':
            a,b=int(s[0]),int(s[1])
            if L(a,k)==T[j] and L(b,k+1)==T[j+1]: push(1,i+1,j+2,k+2,f'{ns[i]} is two figures {a} and {b} run together (no dot)')
        if i+1<N and j<M and ns[i]<10 and ns[i+1]<10:
            m=int(f'{ns[i]}{ns[i+1]}')
            if 10<=m<=25 and L(m,k)==T[j]: push(1,i+2,j+1,k+1,f'{ns[i]}.{ns[i+1]} is one figure {m} (stray dot)')
        if j<M:
            push(1.5,i,j+1,k+1,f'letter {T[j]} left out (its key letter used up)')
            push(1.8,i,j+1,k,f'letter {T[j]} left out')
        if i<N: push(2,i+1,j,k+1,f'figure {ns[i]} has no letter in the reading (extra letter enciphered)')
        for d in (1,-1):
            push(1.5,i,j,k+d,'key letter skipped' if d==1 else 'key letter used twice')
        for d in (2,3,4,-2,-3,-4):
            push(3,i,j,k+d,f'key jumps {d:+d} places')
    return None
def stretches(date):
    out=[];cur=None
    for line in (D/f'decryption_{date}.txt').read_text().splitlines():
        m=re.match(r'(\S+)  frame (\d+)\s+(\d+) numerals',line)
        if m: cur={'id':m.group(1),'frame':m.group(2)}; out.append(cur); continue
        m=re.match(r'  (read as|\w+)\s+(.*)$',line)
        if cur is not None and m: cur[m.group(1)]=m.group(2)
    return out

KINDS=[('counted one place off','a figure off by one place'),('tens figure','a tens figure added or lost'),
       ('look-alike','look-alike figures (could be our misreading)'),('no simple explanation','other wrong figure'),
       ('run together','two figures run together (no dot)'),('stray dot','one figure split by a stray dot'),
       ('key letter used up','a letter left out (key letter used up)'),('left out','a letter left out'),
       ('key letter skipped','a key letter skipped'),('key letter used twice','a key letter used twice'),
       ('key jumps','a larger key jump'),('enciphered with the','one figure with the next or previous key letter'),
       ('no letter in the reading','a figure with no letter in the reading')]
def classify(op):
    return next(v for k,v in KINDS if k in op)

def main():
    import collections
    lines=[]; tally=collections.Counter(); by_key=collections.Counter(); uses=collections.Counter()
    for date in ('1813-02-01','1813-02-02','1813-02-06'):
        lines.append(f'== {date}')
        for s in stretches(date):
            ns=list(map(int,s['numerals'].split())); read=s.get('read as','')
            runs=[tuple(map(int,x)) for x in re.findall(r'(\d+)-(\d+):(\d+)',s.get('used',''))] or [(1,len(ns),0)]
            for i in range(len(ns)):
                o=next((o for a,b,o in runs if a<=i+1<=b),0); uses[K[(i+o)%10]]+=1
            if not read or read.strip()=='[...]': continue
            r=account(ns,read)
            if r is None: lines.append(f"{s['id']}: no account"); continue
            c,ops,T=r
            if not ops: continue
            lines.append(f"{s['id']} ({len(ns)} figures, cost {c:.1f}): {read}")
            for op,i,j in ops:
                lines.append(f"   figure {i+1}, letter {j+1}: {op}")
                kind=classify(op)
                tally[kind]+=1
                m=re.match(r'wrote (\d+) for (\d+)',op)
                if m:
                    k=[k for k in range(10) if need(T[j],k)==int(m.group(2))][0]; by_key[K[k]]+=1
    out=['# lee1813: error accounts (errors.py). One cheapest explanation per stretch; see the docstring for the model.','',
         '## Tally of mistake types']+[f'  {n:3d}  {k}' for k,n in tally.most_common()]+['',
         '## Single wrong figures by key letter (wrong / figures enciphered with that key letter)']+\
         [f'  {k}: {by_key[k]:3d} / {uses[k]:4d} = {by_key[k]/uses[k]:.3f}' for k in 'WINCHESTR']+['','## Accounts']+lines
    (D/'error_accounts.txt').write_text('\n'.join(out)+'\n',encoding='utf-8')
    print('\n'.join(out[:30]))

if __name__=='__main__':
    main()
