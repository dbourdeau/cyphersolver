"""Engine for the Favre / delegation code (not alphabetical, no clear words).  Run from the target folder:  python wiki/tools/favre_engine.py
What it can test there: TOPIC clusters. For an anchor group a with a verified reading (1792 conference, 1915 armistice, 2232 Bruxelles, 977 sauf), a group g belongs to the anchor's topic if g occurs within +-W positions of a
far more often than chance, in the dated letters. Gate: Poisson p-value with Bonferroni over all groups used >= 4 times, and >= 3 co-occurrences.
Validation: the Chaudordy plaintext (word-level alignment of the first ~330 groups): the words aligned to the cluster groups should be topical."""
import sys,os,io,json,math,collections,contextlib,re
sys.path.insert(0,os.getcwd())
sys.stdout.reconfigure(encoding="utf8")
class Buf(io.StringIO):
    def reconfigure(self,**k): pass
buf=Buf()
with contextlib.redirect_stdout(buf):
    import timing_cribs as T
POOL=T.pool; ORDER=T.ORDER
W=12
ANCHORS={"conference":1792,"armistice":1915,"bruxelles":2232,"sauf-conduit":977}
tot=sum(len(POOL[k]) for k in ORDER)
cnt=collections.Counter(g for k in ORDER for g in POOL[k])
def cooc(anchor):
    obs=collections.Counter(); wins=0
    for k in ORDER:
        s=POOL[k]; idx=[i for i,g in enumerate(s) if g==anchor]
        covered=set()
        for i in idx:
            for j in range(max(0,i-W),min(len(s),i+W+1)):
                if j!=i: covered.add(j)
        wins+=len(covered)
        for j in covered: obs[s[j]]+=1
    return obs,wins
def poisson_sf(k,mu):
    # P(X>=k)
    if k<=0: return 1.0
    p=0.0;term=math.exp(-mu)
    for i in range(k): p+=term; term*=mu/(i+1)
    return max(0.0,1.0-p)
al=json.load(open("align_hmm2_out.json",encoding="cp1252"))
words_of=collections.defaultdict(list)
for r in al:
    if r["w"] and r["i"]<330: words_of[r["g"]].append(r["w"])
ngroups=len([g for g,c in cnt.items() if c>=4])
results={}
for topic,a in ANCHORS.items():
    obs,wins=cooc(a)
    frac=wins/tot
    rows=[]
    for g,c in cnt.items():
        if g==a or c<4 or obs[g]<3: continue
        mu=c*frac; p=poisson_sf(obs[g],mu)*ngroups   # Bonferroni
        rows.append((p,g,obs[g],c,mu))
    rows.sort()
    results[topic]=rows
    sel=[r for r in rows if r[0]<0.05]
    print("TOPIC %-13s anchor %-5d occurrences %d, window covers %.1f%% of positions; %d groups with Bonferroni p<0.05"%(topic,a,cnt[a],100*frac,len(sel)))
    for p,g,o,c,mu in rows[:12]:
        print("   group %-5d co-occurs %2d of %2d uses (expected %.1f)  Bonferroni p=%.3g   Chaudordy words: %s"%(g,o,c,mu,p,words_of.get(g,"-")))
json.dump({t:[(float(p),int(g),int(o),int(c)) for p,g,o,c,mu in rows[:30]] for t,rows in results.items()},open("favre_topics.json","w"))
