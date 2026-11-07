"""Fill the coded 4-digit groups of the inspectors' telegram (Tours, 2 Nov 1870) by word-bigram LM + one word per group.
Clear words are fixed. Output: inspecteurs_cloze_out.txt"""
import re,collections,math,random,sys,unicodedata
sys.stdout.reconfigure(encoding="utf8")
def strip(s): return "".join(c for c in unicodedata.normalize("NFD",s) if unicodedata.category(c)!="Mn")
def toks(t): return [re.sub(r"[^a-z0-9]","",strip(x)) for x in re.findall(r"[\wéèêëàâîïôùûüçœ]+",t.lower().replace("'"," ").replace("’"," "))]
corp=[]
for f in ("gouvernementdela01favr","gouvernementdela02favr"):
    corp+=[w for w in toks(open(r"C:\Users\dbour\enquete\%s.txt"%f,encoding="utf8",errors="replace").read()) if w]
uni=collections.Counter(corp); bi=collections.Counter(zip(corp,corp[1:])); NT=len(corp); V=len(uni)
raw=open("inspecteurs_2nov_partial.txt",encoding="utf8").read()
seq=[]
for w in raw.replace("’","'").replace("'"," ").split():
    if re.fullmatch(r"\d{4}",w): seq.append(("G",w))
    else:
        ww=re.sub(r"[^a-z0-9]","",strip(w.lower()))
        if ww and not ww.isdigit(): seq.append(("W",ww))
        elif ww: seq.append(("W",ww))
groups=sorted({w for t,w in seq if t=="G"})
clear=[w for t,w in seq if t=="W"]
cand=[w for w,_ in uni.most_common(1800)]+[w for w in set(clear) if w not in uni]
cand=list(dict.fromkeys(cand))
lam=0.72
def lp(a,b):
    ca=uni[a]; p1=(uni[b]+0.5)/(NT+0.5*V)
    p2=bi[(a,b)]/ca if ca else 0
    return math.log(lam*p2+(1-lam)*p1)
pos=collections.defaultdict(list)
for i,(t,w) in enumerate(seq):
    if t=="G": pos[w].append(i)
words=[w if t=="W" else None for t,w in seq]
def total(m):
    s=0.0; prev=None
    for i,(t,w) in enumerate(seq):
        cur=w if t=="W" else m[w]
        if prev is not None: s+=lp(prev,cur)
        prev=cur
    return s
def local(m,g,val):
    s=0.0
    for i in pos[g]:
        a=(seq[i-1][1] if seq[i-1][0]=="W" else m[seq[i-1][1]]) if i>0 else None
        b=(seq[i+1][1] if seq[i+1][0]=="W" else m[seq[i+1][1]]) if i+1<len(seq) else None
        if a is not None: s+=lp(a,val)
        if b is not None: s+=lp(val,b)
    return s
random.seed(5)
def run(m,sweeps=6):
    for sw in range(sweeps):
        order=sorted(groups,key=lambda g:-len(pos[g])); ch=0
        for g in order:
            cur=m[g]; best=cur; bs=local(m,g,cur)
            for c in cand:
                s=local(m,g,c)
                if s>bs+1e-9: bs=s; best=c
            if best!=cur: m[g]=best; ch+=1
        if ch==0: break
    return m
freq=[w for w,_ in uni.most_common(60)]
m={g:random.choice(freq) for g in groups}
t0=total(m); m=run(m); t1=total(m)
print("log-prob random start %.0f -> optimised %.0f over %d tokens (%d groups, %d clear)"%(t0,t1,len(seq),len(groups),len(clear)))
# baseline: same clear words, groups replaced by random frequent words
rs=[]
for _ in range(5):
    mm={g:random.choice(freq) for g in groups}; rs.append(total(mm))
print("random-mapping baseline %.0f"%(sum(rs)/len(rs)))
out=[]
for t,w in seq: out.append(w if t=="W" else "[%s=%s]"%(w,m[w]))
open("inspecteurs_cloze_out.txt","w",encoding="utf8").write(" ".join(out))
print("most frequent groups:",[(g,len(pos[g]),m[g]) for g in sorted(groups,key=lambda g:-len(pos[g]))[:20]])
print(" ".join(out[:260]))
