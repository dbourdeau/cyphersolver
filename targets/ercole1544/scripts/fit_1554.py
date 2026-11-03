# usage, from the target folder: python scripts/fit_1554.py validation/1554_pass1/*.txt
# Fit test of the frozen 1556 letter table, with shuffled tables as control. Letter signs only; digits and L signs are skipped and
# break runs. Score: mean log-probability per letter under Italian letter bigrams trained on the clear decipherment cc. 104r and c. 107
# of the sibling target (a text not used to build anything here), and the count of hits of common Italian 4+ letter words.
import re,sys,random,math,collections
sys.stdout.reconfigure(encoding='utf8')
T=dict(zip('abcdefghnopqrstuxyzk','nopqrstuabcdefghilmz'))
txt=''
for f in ['transcription_0104r.txt','transcription_0107.txt']:
    for l in open(f,encoding='utf8'):
        if not l.startswith('#'): txt+=l
txt=re.sub(r'[^a-z]','',txt.lower().replace('v','u').replace('j','i').replace('y','i'))
A='abcdefghilmnopqrstuz'
bg=collections.Counter(zip(txt,txt[1:])); ug=collections.Counter(txt)
def lp(a,b): return math.log((bg[(a,b)]+.5)/(ug[a]+.5*len(A)))
WORDS=set('della nella alla quello questo sono essere fare sopra dire dalla anco hauer hauere papa tutto tutti ogni quale quali mandato loro altro altri parte detto perche cosi molto grande fatto come uuole sapere conte cardinal duca imperatore francia'.split())
def segs(path):
    out=[]
    for l in open(path,encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        b=l.strip().partition(' ')[2]
        for s in re.split(r'L\^\w+|\d+|L|S|\?',b): 
            s=s.replace(' ','')
            if s: out.append(s)
    return out
def score(ss,t):
    n=0;v=0;h=0
    for s in ss:
        d=''.join(t.get(c,'?') for c in s)
        for a,b in zip(d,d[1:]):
            if a!='?' and b!='?': v+=lp(a,b);n+=1
        h+=sum(d.count(w) for w in WORDS)
    return v/max(n,1),h,n
random.seed(1554)
for p in sys.argv[1:]:
    ss=segs(p); r,h,n=score(ss,T)
    ctl=[]
    keys=list(T); vals=list(T.values())
    for _ in range(500):
        v=vals[:]; random.shuffle(v); ctl.append(score(ss,dict(zip(keys,v))))
    m=sum(c[0] for c in ctl)/len(ctl); mx=max(c[0] for c in ctl); hm=sum(c[1] for c in ctl)/len(ctl); hx=max(c[1] for c in ctl)
    print(f'{p}: letters pairs {n}; bigram log-prob table {r:.3f}; shuffled mean {m:.3f} max {mx:.3f}; word hits table {h}; shuffled mean {hm:.1f} max {hx}')
