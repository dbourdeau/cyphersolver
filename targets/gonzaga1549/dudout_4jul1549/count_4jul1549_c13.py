# Compte strict (après la mesure, descriptif) : mots de la référence classés par l'alignement du décodé.
import sys,re,unicodedata
sys.path.insert(0,'.'); import tools_metric as TM
def nrm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.replace('j','i').replace('y','i').replace('v','u').replace('z','c').replace('h','')
    s=re.sub('[^a-z ]','',s); s=re.sub(r'([a-z])\1+',r'\1',s); return s
K={}
for l in open('key_dudout_kb4.tsv'):
    if l.startswith('#') or not l.strip(): continue
    a=l.rstrip('\n').split('\t'); K[a[0]]=a[1]
toks=[t for l in open('4jul1549_c13_tokens.txt') if not l.startswith('#') for t in l.split()[1:]]
dec=''.join(nrm(K[t]) if t in K else '#' for t in toks)
R=[l.split(' ',1)[1] for l in open('4jul1549_44r_decipherment_passage.txt') if l.startswith('A ')][0]
words=[nrm(w) for w in R.split()]; words=[w for w in words if w]
ref=''.join(words); d,ok=TM.align(dec,ref)
pos=0; out=[]; c={'sure':0,'probable':0,'restored':0}
for w in words:
    f=sum(ok[pos:pos+len(w)])/len(w); pos+=len(w)
    k='sure' if f==1 else ('probable' if f>=2/3 else 'restored'); c[k]+=1
    out.append(w if k=='sure' else ('{'+w+'}' if k=='probable' else '['+w+']'))
n=len(words); print(' '.join(out)); print(c, n, 'sûrs+probables = %.3f'%((c['sure']+c['probable'])/n))
