import difflib,random,re
key={}
for l in open('KEY.tsv'):
    if l.startswith('#'): continue
    c,ch,*_=l.split('\t'); key[c]=ch
H=[]
for l in open('H-CHIFFRE.txt'):
    H+= [t for t in l.split()[1:] if re.fullmatch(r'\d\d',t)]
ref=re.sub('[^a-z]','',[l for l in open('H-CLAIR.txt') if not l.startswith('#')][0].lower().replace('ij','y'))
def car(k):
    dec=''.join(k.get(c,'') for c in H)
    m=difflib.SequenceMatcher(None,dec,ref,autojunk=False)
    return sum(b.size for b in m.get_matching_blocks())/len(ref),dec
c0,dec=car(key)
cov=sum(1 for c in H if c in key)/len(H)
rnd=random.Random(1801); codes=list(key); vals=list(key.values()); tem=[]
for i in range(200):
    v=vals[:]; rnd.shuffle(v); tem.append(car(dict(zip(codes,v)))[0])
mx=max(tem); marge=c0-mx
verdict='VALIDÉ' if c0>=0.85 and marge>=0.30 else ('PARTIEL' if marge>=0.30 else 'ÉCHEC')
print(f"groupes H={len(H)} lettres réf={len(ref)}\ndécodage : {dec}\nréférence: {ref}\ncar={c0:.3f} couverture={cov:.3f} max_témoins={mx:.3f} marge={marge:.3f} rang=1/{1+sum(t>=c0 for t in tem)+0}\nVERDICT : {verdict}")
