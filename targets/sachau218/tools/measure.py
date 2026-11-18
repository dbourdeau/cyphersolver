import sys,math,random,re,collections
corp,tr=sys.argv[1],sys.argv[2]
A22='ابجدهوزحطيكلمنسعفصقرشت'
norm={'ث':'ت','خ':'ك','ذ':'د','ض':'ص','ظ':'ط','غ':'ع','ة':'ه','ى':'ي','أ':'ا','إ':'ا','آ':'ا','ء':'ا','ؤ':'و','ئ':'ي'}
txt=open(corp,encoding='utf8').read()
words=[]
for line in txt.splitlines():
    t=line.split('|')[-1]
    for w in t.split():
        w=''.join(norm.get(c,c) for c in w); w=''.join(c for c in w if c in A22)
        if w: words.append(w)
big=collections.Counter(); uni=collections.Counter()
for w in words:
    for a,b in zip(w,w[1:]): big[a+b]+=1; uni[a]+=1
V=len(A22)
lp=lambda a,b: math.log((big[a+b]+1)/(uni[a]+V))
groups=[]
for line in open(tr,encoding='utf8'):
    for g in line.strip().split('/'):
        s=g.split()
        if s: groups.append(s)
abj={1:'ا',2:'ب',3:'ج',4:'د',5:'ه',6:'و',7:'ز',8:'ح',9:'ط',10:'ي',20:'ك',30:'ل',40:'م',50:'ن',60:'س',70:'ع',80:'ف',90:'ص'}
val={c:i for i,c in enumerate(A22)}; 
num={c:k for k,c in abj.items()}
K1={'I':'ا','R':'ب','W':'ج','E':'د','F':'د','O':'ه','L':'ح','N9':'ط'}
def dec(key,dot=True):
    out=[]
    for gi,g in enumerate(groups):
        s=[]
        for si,x in enumerate(g):
            c=key.get(x)
            if c and dot and gi==0 and si==0:  # point rouge sous le 1er F de L1 : x10
                n=num.get(c); c=abj.get(n*10,c) if n and n<10 else c
            s.append(c or '?')
        out.append(''.join(s))
    return out
def score(d):
    t=n=0
    for w in d:
        for a,b in zip(w,w[1:]):
            if a!='?' and b!='?': t+=lp(a,b); n+=1
    return t/n if n else float('-inf'), n
d1=dec(K1); s1,n1=score(d1)
rnd=random.Random(2933); W=[]
for _ in range(200):
    lets=rnd.sample(A22,8); k=dict(zip(K1.keys(),lets)); W.append(score(dec(k))[0])
W.sort()
print('corpus words',len(words))
print('K1 decode (groupes, ? = inconnu):',' | '.join(d1))
print('K1 score %.4f sur %d bigrammes'%(s1,n1))
print('temoins: max %.4f  mediane %.4f  min %.4f'%(W[-1],W[100],W[0]))
print('rang de K1 parmi 201:',1+sum(w>s1 for w in W))
print('seuil score >= max temoin:', s1>=W[-1])
