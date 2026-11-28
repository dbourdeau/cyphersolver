import sys,re,random,difflib,unicodedata
sys.path.insert(0,'.')
from decode import load,decode
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.replace('j','i').replace('v','u').replace('y','i').replace('k','c').replace('h','')
    return re.sub('[^a-z]','',s)
k=load('KEY.tsv')
toks=[]
for l in open('T_V131_final.txt',encoding='utf8'):
    l=l.split('#')[0]
    if ':' in l: toks+= [t.rstrip('?') for t in l.split(':',1)[1].split()]
ref=norm(open('ref_V131_opere6_ocr.txt',encoding='utf8').read())
def score(kk):
    d=norm(decode(toks,kk).replace('[','').replace(']',''))
    n=len(d); w=ref[:round(1.15*n)]
    s=difflib.SequenceMatcher(None,d,w,autojunk=False)
    return sum(b.size for b in s.get_matching_blocks())/n, d
sc,d=score(k)
labels=list(k); vals=[k[x] for x in labels]
ctrl=[]
for seed in range(1,201):
    r=random.Random(seed); v=vals[:]; r.shuffle(v); ctrl.append(score(dict(zip(labels,v)))[0])
print('tokens',len(toks),'decoded chars',len(d))
print('decode:',d)
print('ref   :',ref[:round(1.15*len(d))])
print('SCORE %.3f  best control %.3f  margin %.3f'%(sc,max(ctrl),sc-max(ctrl)))
