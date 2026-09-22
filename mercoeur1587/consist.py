import sys,random
sys.path.insert(0,'..');from lang import lm
M=lm.load('fr-1600-letters',order=5,spaces=False)
exec(open('cands.py',encoding='utf8').read())
lines=[l.split() for l in open(sys.argv[1],encoding='utf8') if l.strip()]
toks=[t for L in lines for t in L]
labs=sorted({t for t in toks if not t.startswith('{')})
# allow any letter for each label but prior bonus for key candidate
A='abcdefghilmnopqrstuvxyz'
def opts(l):
    c=list(C.get(l,''))
    return c+[x for x in A if x not in c]
O={l:opts(l) for l in labs}
def dec(asg):
    return ''.join(W.get(t[1:-1],'') if t.startswith('{') else asg[t] for t in toks)
def score(asg):
    s=dec(asg);pen=sum(0 if asg[l] in C.get(l,'') else 6 for l in labs)
    return M.score_idx(M.encode(lm.norm(s,'early',spaces=False)))-pen
best=None
for r in range(4):
    asg={l:O[l][0] if O[l] else 'e' for l in labs};cur=score(asg);T=3.0
    for it in range(6000):
        l=random.choice(labs);old=asg[l];asg[l]=random.choice(O[l][:len(C.get(l,''))] if random.random()<.7 and C.get(l) else O[l])
        n=score(asg)
        if n>=cur or random.random()<pow(2.718,(n-cur)/T):cur=n
        else:asg[l]=old
        T=max(.05,T*.9993)
    if not best or cur>best[0]:best=(cur,dict(asg))
cur,asg=best
print(cur);print({l:asg[l] for l in labs})
p=0
for i,L in enumerate(lines):
    print('%02d'%(i+1),''.join(W.get(t[1:-1],'['+t[1:-1]+']') if t.startswith('{') else asg[t] for t in L))
