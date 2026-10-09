"""Spearman between ct usage of Zifra Prima codes and corpus frequency of their values, against a structured
null (base-letter permutations x cyclic offsets of the ct usage table). Arg: min,max value length."""
import sys,collections,re,itertools
import numpy as np
sys.path.insert(0,'../..')
from lang import lm
lo,hi=int(sys.argv[1]),int(sys.argv[2])
key={}
for l in open('keys/zifra_prima_R1789.tsv',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k,v=l.rstrip('\n').split('\t'); key[k]=v
C=collections.Counter(open('ct_all.txt',encoding='utf8').read().split())
txt=re.sub('[^a-z]','',lm.norm(open('../../lang/corpora/it-renaissance.txt',encoding='utf8',errors='ignore').read()[:3000000],'early'))
codes=[k for k,v in key.items() if v.islower() and lo<=len(v)<=hi and v.isalpha()]
ys=np.array([txt.count(lm.norm(key[k],'early')) for k in codes])
def spear(a,b):
    ra=np.argsort(np.argsort(a)); rb=np.argsort(np.argsort(b)); return np.corrcoef(ra,rb)[0,1]
def cnt(perm,off):
    return np.array([C.get(perm[k[0]]+str((int(k[1:])-1+off)%99+1),0) for k in codes])
B='acdfgh'
real=spear(cnt({b:b for b in B},0),ys)
vals=np.array([spear(cnt(dict(zip(B,p)),off),ys) for p in itertools.permutations(B) for off in range(0,99,3) if not (p==tuple(B) and off==0)])
print('len %d-%d codes %d real %.3f null mean %.3f 99%% %.3f max %.3f frac>=real %.4f'%(lo,hi,len(codes),real,vals.mean(),np.percentile(vals,99),vals.max(),(vals>=real).mean()))
