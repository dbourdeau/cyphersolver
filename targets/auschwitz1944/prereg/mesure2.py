import re,sys,random,math,collections
D=sys.argv[1]
T=open(D+'/TRANSCRIPTION-GELEE.txt',encoding='utf-8').read().split('# DOUTES')[0]
G={}
for m in re.finditer(r'#G(\d+)\(([^)]*)\)',T):
    G[int(m.group(1))]=['?' if '«?»' in x else int(re.match(r'\d+',x).group()) for x in m.group(2).split('-')]
lex=set(open(D+'/essais/lexique_pl.txt',encoding='utf-8').read().split())
words=re.findall(r'[a-ząćęłńóśźż]+',open(sys.argv[2],encoding='utf-8',errors='ignore').read().lower())
bg=collections.Counter(); ug=collections.Counter()
for w in words:
    w='^'+w+'$'
    for a,b in zip(w,w[1:]): bg[a+b]+=1; ug[a]+=1
NA=len(set(''.join(words)))+2
def lp(a,b): return math.log((bg[a+b]+0.5)/(ug[a]+0.5*NA))
def letters(t): return [c for c in t.lower() if c.isalpha()]
def distinct(t,shift_from_p=False):
    k={};n=1
    for c in letters(t):
        if c in k.values(): continue
        if shift_from_p and c=='p': n+=1
        k[n]=c;n+=1
    for num,c in ((28,'h'),(30,'ó')):
        if num not in k and c not in k.values(): k[num]=c
    return {a:b for a,b in k.items() if a<=30}
s1="Kto się w opiekę poda Panu swemu, A całem sercem szczerze ufa jemu, Śmiele rzec może: mam obrońcę Boga, Nie przypadnie na mię żadna trwoga"
KEYS={'K1':distinct(s1),'K2':distinct(s1.replace('całem','całym')),
'K3':distinct("Kto się w opiekę odda Panu swemu, A całem sercem zaufa jemu, Śmiele rzec może: mam obrońcę Boga, Nie przypadnie na mię żadna trwoga"),
'K4':distinct(s1.replace('poda','poddał')),'K5':distinct(s1,True)}
def dec(k,g): return ''.join('?' if x=='?' else k.get(x,'#') for x in g)
def score(k,ids):
    ll=[]
    for i in ids:
        s='^'+dec(k,G[i]).replace('?','').replace('#','')+'$'
        ll+=[lp(a,b) for a,b in zip(s,s[1:])]
    return sum(ll)/len(ll)
def lexn(k,ids): return sum(1 for i in ids if len(G[i])>=2 and dec(k,G[i]) in lex)
def wit(k,ids,n=200,seed=19440904):
    r=random.Random(seed); ks=sorted(k); v0=[k[x] for x in ks]; o=[]
    for _ in range(n):
        v=v0[:]; r.shuffle(v); o.append(score(dict(zip(ks,v)),ids))
    return o
burn=list(range(20,40)); fresh=list(range(1,20))
for n,k in KEYS.items(): print('GRILLE',n,round(score(k,burn),3),[dec(k,G[i]) for i in burn])
best=max(KEYS,key=lambda n:score(KEYS[n],burn)); k=KEYS[best]
print('CLE CHOISIE',best,sorted(k.items()))
s=score(k,fresh); w=wit(k,fresh)
print('MESURE G1-G19',best,'score',round(s,3),'temoins>=',sum(1 for x in w if x>=s),'max temoin',round(max(w),3),'lexique',lexn(k,fresh),'/',sum(1 for i in fresh if len(G[i])>=2))
for i in fresh: print('G%d'%i,G[i],dec(k,G[i]))
print('STAT', 'OK' if sum(1 for x in w if x>=s)==0 else 'ECHEC')
