import sys,re,random,difflib,unicodedata
sys.path.insert(0,sys.argv[0].rsplit('/',1)[0])
from dec import run
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.replace('ł','l').replace('j','i').replace('y','i')
    return re.sub('[^a-z]','',s)
keyf,cipf,clearf=sys.argv[1:4]; stop=int(sys.argv[4]) if len(sys.argv)>4 else None

rows=run(cipf,show=False)
toks=[v for _,o in rows for v in o]
if stop: toks=toks[:stop]
clear=''.join(l for l in open(clearf,encoding='utf-8') if not l.startswith('#'))
words=[w for w in re.findall(r"[^\s,.:;()!?]+",clear) if norm(w)]
def score(toks):
    dec_s=''.join('#' if t.startswith('‹') else norm(t) for t in toks)
    cl=''.join(norm(w) for w in words)
    sm=difflib.SequenceMatcher(None,cl,dec_s,autojunk=False)
    ok=[False]*len(cl)
    for a,b,n in sm.get_matching_blocks():
        for i in range(n): ok[a+i]=True
    pos=0; wok=0
    for w in words:
        n=len(norm(w)); wok+=all(ok[pos:pos+n]); pos+=n
    return wok/len(words), sum(ok)/len(cl), len(words), len(cl)
w,c,nw,nc=score(toks); print(f'real: words {w:.3f} ({nw}), characters {c:.3f} ({nc})')
random.seed(1); ws=[];cs=[]
for i in range(200):
    t=toks[:]; random.shuffle(t); a,b,_,_=score(t); ws.append(a); cs.append(b)
ws.sort();cs.sort(); print(f'200 shuffled controls: words max {ws[-1]:.3f} p50 {ws[100]:.3f} ; chars max {cs[-1]:.3f} p50 {cs[100]:.3f}')
