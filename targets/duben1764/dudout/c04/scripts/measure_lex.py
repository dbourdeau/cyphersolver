"""C04 — mesure lexicale unique (PREREG.md). Usage : python3 -I measure_lex.py N_key.json
K0 = key_c03 + c03b_ajouts (gelés le 12/11) ; N = valeurs nouvelles/corrigées dérivées de C (121-122R) seulement.
Mesure sur H = 123R + 124L (transcription de Daniel gelée)."""
import sys,json,re,gzip,random,statistics
BASE='/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/lovisa-ulrika-1764/cryptanalysis/'
LEX='/Users/bdudout/Documents/Veille cyber/_shared/cyphersolver/lang/lexicons/fr.json.gz'
K0=json.load(open(BASE+'c03/construction/key_c03.json')); K0.update(json.load(open(BASE+'c03/construction/c03b_ajouts.json')))
N=json.load(open(sys.argv[1]))
lex={w for w,c in json.load(gzip.open(LEX)).items() if len(w)>=4 and c>=2}
H=[]
for l in open(BASE+'c03/transcr/lecture_121-124L.txt'):
    if l.startswith('#') or not l.strip(): continue
    lab,rest=l.split(' ',1)
    if not lab.startswith(('123R','124L')): continue
    rest=re.sub(r'\[del:[^\]]*\]','',rest)
    for t in rest.split():
        g=re.sub(r"[?'`]",'',t)
        if g.isdigit(): H.append(g)
Nm={v:s for v,s in N.items() if s}          # valeurs mesurables (non nulles)
occ=[i for i,g in enumerate(H) if g in Nm]
def norm(s): return re.sub(r'[^a-z]','',s.lower())
def score(key):
    hits=0
    for i in occ:
        parts=[];a=b=None;pos=0
        for j in range(max(0,i-3),min(len(H),i+4)):
            s=key.get(H[j]); s='#' if s is None else norm(s)
            if j==i: a=pos;b=pos+len(s)
            parts.append(s);pos+=len(s)
        w=''.join(parts); ok=False
        for st in range(0,a+1):
            for en in range(b,len(w)+1):
                if en-st>=4 and '#' not in w[st:en] and w[st:en] in lex: ok=True;break
            if ok: break
        hits+=ok
    return hits/len(occ)
def mk(sub):
    k=dict(K0); k.update({v:s for v,s in N.items()}); k.update(sub); return k
M=score(mk({}))
rnd=random.Random(4504); vals=sorted(Nm); strs=[Nm[v] for v in vals]
pool=[norm(s) for s in K0.values() if s]
W1=[];W2=[]
for _ in range(200):
    p=strs[:]; rnd.shuffle(p); W1.append(score(mk(dict(zip(vals,p)))))
for _ in range(200):
    W2.append(score(mk({v:rnd.choice(pool) for v in vals})))
W=W1+W2
res={'H_groups':len(H),'N_values':len(N),'N_measurable':len(Nm),'H_occurrences':len(occ),'M':round(M,4),
     'perm_max':max(W1),'perm_mean':round(statistics.mean(W1),4),'rand_max':max(W2),'rand_mean':round(statistics.mean(W2),4)}
ok=len(occ)>=12 and M>=0.60 and M>max(W) and M-statistics.mean(W)>=0.25
res['verdict']=('VALIDEE' if ok else 'NON VALIDEE') if len(occ)>=12 else 'MESURE NON CONDUITE (<12 occurrences)'
print(json.dumps(res,ensure_ascii=False,indent=1))
