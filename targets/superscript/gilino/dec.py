import re,sys
K={}
def rng(base,start,sylls):
    for i,s in enumerate(sylls.split()): K[f'{base}.{start+i}']=s
rng('B',31,'ba be bi bo bu ca ce ci co cu da de di do du ga ge gi go gu')
rng('B',51,'fa fe fi fo fu')
rng('D',51,'la le li lo lu ma me mi mo mu na ne ni no nu')
rng('6',56,'pa pe pi po pu qua que qui quo quu ra re ri ro ru sa se si so su ta te ti to tu')
rng('o',33,'va ve vi vo vu xa xe xi xo xu za ze zi zo zu')
K.update({'A.42':'al','A.43':'am','A.44':'an','H.26':'cosa','H.27':'che','H.28':'come','R.28':'ancora','R.23':'con','D.40':'sara'})
# letters (draft)
L={'a':'ut th A.30 19 28','b':'lam A.31','c':'xo A.32','d':'A.33','e':'+ B.25 ff','f':'gf B.26','g':'mp B.27','h':'dots B.28 H.25','i':'np S D.40 6.48',
   'l':'D.41','m':'pi D.42','n':'6 D.43','o':'o b+ 6.50','p':'6.51','q':'q 6.52','r':'6.53','s':'o.27','t':'m','v':'o.29','x':'o.30'}
for k,v in L.items():
    for t in v.split(): K.setdefault(t,k)
for t in list(K):
    if t[0]=='D': K.setdefault('d'+t[1:],K[t])
n=int(sys.argv[1]) if len(sys.argv)>1 else 20
out=[]
for line in open(r'C:\Users\dbour\cypher\targets\superscript\r8572_tokens.txt',encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    toks=line.split(); s=''
    for t in toks:
        t2=t.rstrip('?')
        s+= K[t2] if t2 in K else f'[{t}]'
    out.append(s)
for s in out[:n]: print(s)
if len(sys.argv)>2:
    i=0
    for line in open(r'C:\Users\dbour\cypher\targets\superscript\r8572_tokens.txt',encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        i+=1
        if i>n: break
        print(' '.join(f'{t}={K.get(t.rstrip("?"),"?")}' for t in line.split()))
