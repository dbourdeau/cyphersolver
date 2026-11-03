# Held-out test. Train the annealer on c. 15r only (pass 1b signs, no words supplied). Freeze. Decrypt cc. 15v-16r, which played no part.
# Score: mean 4-gram log prob per letter of the held-out text, against tables with the sign->letter values shuffled.
import sys,re,random,json;sys.path.insert(0,'work')
from hsolve import *
lp=load4();pr=freqprior()
CODES=['F r','b u r','b o r','b a r','m u r','Q u a n','u l i r','i m a','s e d','L u s']
def strip(t):
    o=[]
    for x in t:
        if x in('_8','_9'):
            if o:o.pop()
            continue
        o.append(x)
    return o
def runs(files):
    R=[]
    for f in files:
        for ln in open(f,encoding='utf8'):
            if ln.startswith('#') or ' ' not in ln.strip():continue
            for p in re.split(r'\[[^\]]*\]',ln.split(' ',1)[1]):
                s=' '+' '.join(strip(p.split()))+' '
                s=s.replace(' e r ',' ER ')
                for c in CODES:s=s.replace(' '+c+' ',' | ')
                for q in s.split('|'):
                    q=q.split()
                    if q:R.append(q)
    return R
tr=runs(['cc15_16/transcription_c15r_pass1b.txt']);te=runs(['cc15_16/transcription_c15v_pass1b.txt','cc15_16/transcription_c16r_pass1b.txt'])
seq,toks=encode(tr);L=int((seq>=0).sum());print('train letters',L,'signs',len(toks))
res=[anneal(seq,len(toks),lp,1000000,6.0,0.3,s+1,pr,3.0) for s in range(16)];res.sort(key=lambda x:-x[0]);b=res[0]
print('train per letter',round(float(b[0])/L,3),[round(float(r[0])/L,2) for r in res[:6]])
key={t:AL[b[1][i]] for i,t in enumerate(toks)}
json.dump(key,open('work/key_frozen_c15r.json','w'),indent=0)
te2=[[x for x in r] for r in te]
known=[x for r in te2 for x in r if x in key];tot=sum(len(r) for r in te2)
print('held-out letters',tot,'covered by frozen table',len(known))
alltoks=sorted(key);ix={t:i for i,t in enumerate(alltoks)}
sq=[]
for r in te2:
    for x in r:
        sq.append(ix[x] if x in ix else -1)
    sq.append(-1)
sq=np.array(sq,dtype=np.int32)
mp=np.array([IDX[key[t]] for t in alltoks],dtype=np.int32)
def s(m):return float(score(sq,m,lp,pr,0.0))
n=int((sq>=0).sum());real=s(mp)/n
ctrl=[]
for i in range(200):
    m=mp.copy();np.random.shuffle(m);ctrl.append(s(m)/n)
print('held-out per letter',round(real,3),'shuffled mean',round(float(np.mean(ctrl)),3),'best',round(float(np.max(ctrl)),3),'sd',round(float(np.std(ctrl)),3))
print(plain(sq,mp)[:700])
# agreement of frozen table with the table reached on all pages
full=json.load(open('work/key_v4.json'))
agree=[(t,key[t],full.get(t)) for t in key if t in full]
print('agree',sum(a==c for _,a,c in agree),'of',len(agree),[x for x in agree if x[1]!=x[2]])
