# count_c14.py = count_c13.py (KB5, T14, segments L+M ; fichier de référence en argument) — descriptif, après la mesure
import sys,re,unicodedata
sys.path.insert(0,'.'); import tools_metric as TM
def nrm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.replace('j','i').replace('y','i').replace('v','u').replace('z','c').replace('h','')
    s=re.sub('[^a-z ]','',s); s=re.sub(r'([a-z])\1+',r'\1',s); return s
K={}
for l in open('key_dudout_kb5.tsv'):
    if l.startswith('#') or not l.strip(): continue
    a=l.rstrip('\n').split('\t'); K[a[0]]=a[1]
toks=[t for l in open('27may1549_31v_tokens.txt') if not l.startswith('#') for t in l.split()[1:]]
dec=''.join(nrm(K[t]) if t in K else '#' for t in toks)
R=' '.join(l.split(' ',1)[1].strip() for l in open(sys.argv[1]) if l[0] in 'LM' and not l.startswith('#'))
words=[nrm(w) for w in R.split()]; words=[w for w in words if w]
ref=''.join(words); d,ok=TM.align(dec,ref)
pos=0; out=[]; c={'sure':0,'probable':0,'restored':0}
for w in words:
    f=sum(ok[pos:pos+len(w)])/len(w); pos+=len(w)
    k='sure' if f==1 else ('probable' if f>=2/3 else 'restored'); c[k]+=1
    out.append(w if k=='sure' else ('{'+w+'}' if k=='probable' else '['+w+']'))
n=len(words); print(' '.join(out)); print(c, n, 'sûrs+probables = %.3f'%((c['sure']+c['probable'])/n))
