import re,json,collections,sys
sys.stdout.reconfigure(encoding="utf8")
seg=open("chaudordy_18dec_plain.txt",encoding="utf8").read()
W=[x.replace("’","'") for x in re.findall(r"[\wéèêëàâîïôùûüçœ'’]+",seg.lower())]
C=json.load(open("chaudordy_nums.json"))
N,T=len(W),len(C); ratio=T/N
pg=collections.defaultdict(list); pw=collections.defaultdict(list)
for i,g in enumerate(C): pg[g].append(i)
for j,w in enumerate(W): pw[w].append(j)
TOL=70
def fits(cp,wp):
    """each cipher pos matched to a distinct plaintext pos in order, |cp-ratio*wp|<TOL (monotone subsequence of wp)"""
    k=0
    for c in cp:
        while k<len(wp) and abs(c-ratio*wp[k])>=TOL+0.0*c: 
            if ratio*wp[k]>c+TOL: return False
            k+=1
        if k>=len(wp): return False
        k+=1
    return True
res=[]
for g,cp in pg.items():
    if not 3<=len(cp)<=12: continue
    for w,wp in pw.items():
        if len(wp)<len(cp) or len(wp)>len(cp)+3 or len(w)<4: continue
        if fits(cp,wp): res.append((g,w,len(cp),len(wp)))
# rank: by count then rarity
from collections import defaultdict
byg=defaultdict(list)
for g,w,a,b in res: byg[g].append((w,a,b))
print("groups with candidate word(s):",len(byg))
for g in sorted(byg,key=lambda g:-len(pg[g])): print(g,len(pg[g]),byg[g][:6])
