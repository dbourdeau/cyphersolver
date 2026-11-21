# score_c14.py = score_c13.py = score_c12.py (critère PREREG-C14 identique : car >= 0,85 ET >= témoin max + 0,30)
import sys,random,re,unicodedata
sys.path.insert(0,'.'); import tools_metric as TM
def nrm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.replace('j','i').replace('y','i').replace('v','u').replace('z','c').replace('h','')
    s=re.sub('[^a-z ]','',s); s=re.sub(r'([a-z])\1+',r'\1',s); return s
ct,ref,kb,seed,segs=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),sys.argv[5]
K={}
for l in open(kb):
    if l.startswith('#') or not l.strip(): continue
    a=l.rstrip('\n').split('\t'); K[a[0]]=a[1]
toks=[]
for l in open(ct):
    if l.startswith('#') or not l.strip(): continue
    if l[0] in segs: toks+=l.split()[1:]
R=' '.join(l.split(' ',1)[1].strip() for l in open(ref) if l[0] in segs and not l.startswith('#'))
def dec(Km): return ''.join(nrm(Km.get(t,'#')) if Km.get(t,'#')!='#' else '#' for t in toks)
def meas(Km):
    d=dec(Km); return TM.metrics(d,nrm(R)),d
(mc,mw),d=meas(K)
cov=sum(t in K for t in toks)/len(toks)
forms=list(K); vals=[K[f] for f in forms]; rnd=random.Random(seed); W=[]
for i in range(200):
    v=vals[:]; rnd.shuffle(v); W.append(meas(dict(zip(forms,v)))[0])
wc=sorted(w[0] for w in W); ww=sorted(w[1] for w in W)
print(f'jetons {len(toks)} couverture {cov:.3f} ; réf. {len(nrm(R).replace(" ",""))} lettres')
print('décodé :',d)
print('réf.   :',nrm(R).replace(' ',''))
print(f'M_car {mc:.3f}  M_mots {mw:.3f} ; témoins car max {wc[-1]:.3f} p99 {wc[197]:.3f} ; mots max {ww[-1]:.3f} p99 {ww[197]:.3f}')
print('rang car', 1+sum(x>=mc for x in wc), '/201 ; rang mots', 1+sum(x>=mw for x in ww),'/201')
print('VALIDÉE' if mc>=0.85 and mc>=wc[-1]+0.30 else ('PARTIELLE (rang 1, sous seuil)' if mc>wc[-1] else 'NON VALIDÉE'))
