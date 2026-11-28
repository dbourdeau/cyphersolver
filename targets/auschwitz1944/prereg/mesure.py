import re,sys,random,math,collections,json
D=sys.argv[1]
T=open(D+'/TRANSCRIPTION-GELEE.txt',encoding='utf-8').read().split('# DOUTES')[0]
G={}
for m in re.finditer(r'#G(\d+)\(([^)]*)\)',T):
    toks=[]
    for x in m.group(2).split('-'):
        if '«?»' in x or x.strip()=='?': toks.append('?')
        else: toks.append(int(re.match(r'\d+',x).group()))
    G[int(m.group(1))]=toks
lex=set(open(D+'/essais/lexique_pl.txt',encoding='utf-8').read().split())
corp=open(sys.argv[2],encoding='utf-8',errors='ignore').read().lower()
words=re.findall(r'[a-ząćęłńóśźż]+',corp)
bg=collections.Counter(); ug=collections.Counter()
for w in words:
    w='^'+w+'$'
    for a,b in zip(w,w[1:]): bg[a+b]+=1; ug[a]+=1
A=set(''.join(words))|{'^','$'}
def lp(a,b): return math.log((bg[a+b]+0.5)/(ug[a]+0.5*len(A)))
def L(s): return [c for c in s.lower() if c.isalpha()]
v1579="Kto się w opiekę poda Panu swemu, A całym sercem szczerze ufa jemu, Śmiele rzec może: Mam obrońcę Boga"
vchant="Kto się w opiekę odda Panu swemu, A całym sercem zaufa jemu, Śmiele rzec może: Mam obrońcę Boga"
vklod="Kto się w opiekę podda Pany swemu, A całym sercem szczerze ufa jemu, Śmiele rzec może: Mam obrońcę Boga"
vkomu="Komu w opiekę poda Panu swemu, A całym sercem szczerze ufa jemu, Śmiele rzec może: Mam obrońcę Boga"
def pos(t,off=1):
    l=L(t); return {i+off:c for i,c in enumerate(l) if 0<=i+off<=40}
def dedup(t):
    k={};n=1
    for c in L(t):
        if c not in k.values(): k[n]=c;n+=1
    return k
KEYS={'F1-a':pos(v1579),'F1-b':pos(vchant),'F1-c':pos(vklod),'F2':dedup(v1579),'F3':pos(vkomu),'V1':pos(v1579,0)}
def dec(k,g): return ''.join('?' if x=='?' else k.get(x,'#') for x in g)
def inlex(s):
    if '#' in s: return False
    if '?' not in s: return s in lex
    r=re.compile('^'+s.replace('?','.')+'$'); return any(r.match(w) for w in lex)
def score(k,ids):
    p=sum(1 for i in ids if len(G[i])>=2 and inlex(dec(k,G[i])))
    ll=[];
    for i in ids:
        s='^'+dec(k,G[i]).replace('?','').replace('#','')+'$'
        ll+= [lp(a,b) for a,b in zip(s,s[1:])]
    return p, sum(ll)/max(1,len(ll))
def wit(k,ids,n=200,seed=19440904):
    rnd=random.Random(seed); ks=sorted(k); vals=[k[x] for x in ks]; out=[]
    for _ in range(n):
        v=vals[:]; rnd.shuffle(v); out.append(score(dict(zip(ks,v)),ids))
    return out
dev=[i for i in sorted(G) if i<=19]; val=[i for i in sorted(G) if i>=20]
res={}
for name,k in KEYS.items():
    s=score(k,dev); w=wit(k,dev)
    res[name]=(s,sum(1 for x in w if x[0]>=s[0]),max(x[0] for x in w))
    print('DEV',name,s,'temoins>=:',res[name][1],'max temoin:',res[name][2], [dec(k,G[i]) for i in dev])
best=max(KEYS,key=lambda n:res[n][0])
print('MEILLEURE (dev):',best)
k=KEYS[best]; s=score(k,val); w=wit(k,val)
n2=sum(1 for i in val if len(G[i])>=2)
print('VAL',best,s,'n>=2:',n2,'temoins>=:',sum(1 for x in w if x[0]>=s[0]),'max temoin:',max(x[0] for x in w))
print('VAL dechiffre:',[dec(k,G[i]) for i in val])
print('SUCCES' if (sum(1 for x in w if x[0]>=s[0])==0 and s[0]>=0.3*n2) else 'ECHEC')
