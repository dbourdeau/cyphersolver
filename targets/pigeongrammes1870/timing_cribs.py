"""Date/topic profiles of groups across the dated Favre-family letters. Validation first: does a history-only profile
('absent before the Conference question opens in Nov, present after') rank the verified group 1792 at the top?"""
import json,collections,math,sys
sys.stdout.reconfigure(encoding="utf8")
pool=json.load(open("pool.json")); pool["chaudordy"]=json.load(open("chaudordy_nums.json"))
ORDER=["fav701024","s15","s23g","fav701218g","chaudordy","s35","fav711019","fav710126"]
DATE=["24 Oct","14 Nov","28 Nov","18 Dec(34L)","18 Dec(Chaud)","20-21 Dec","19 Jan","26 Jan"]
# drop the Gambetta/R2 sheets of s35: they are another code (keep only A J Favre columns)
import openpyxl
wb=openpyxl.load_workbook(r"C:\Users\dbour\pigeon_dl\data\Dossiers individuels\2emeS-35_ADECHIFFRER\2emeS-35.xlsx",read_only=True,data_only=True)
import re
s35=[]
for ws in wb.worksheets:
    if "Favre" not in ws.title: continue
    for r in ws.iter_rows(values_only=True):
        cells=[v for v in r if v is not None]
        toks=[(int(str(v).strip()) if re.fullmatch(r"\d{1,4}",str(v).strip()) else None) for v in cells]
        if len(cells)>=3 and sum(t is not None for t in toks)>=0.8*len(toks): s35+=[t for t in toks if t is not None]
pool["s35"]=[g for g in s35 if 0<g<=2400]
for k in ORDER: pool[k]=[g for g in pool[k] if 0<g<=2400]
N=[len(pool[k]) for k in ORDER]; print("letters:",dict(zip(DATE,N)))
cnt=[collections.Counter(pool[k]) for k in ORDER]
allg=set().union(*cnt)
def rate(g,i): return cnt[i][g]/N[i]*1000
def score(g,expected):
    """expected: list of 0/1 per letter. log-likelihood-ish: present-letters reward, absent-letters penalty."""
    tot=sum(cnt[i][g] for i in range(8))
    if tot<5: return None
    pbar=tot/sum(N)
    s=0.0
    for i,e in enumerate(expected):
        mu=pbar*N[i]*(1 if e else 0.03)      # expected count if present / nearly absent
        mu=max(mu,0.02); k=cnt[i][g]
        s+= k*math.log(mu)-mu - (k*math.log(max(pbar*N[i],0.02))-pbar*N[i])   # vs flat profile
    return s
CONF=[0,0,1,1,1,1,1,1]       # conference question: not before mid-Nov
res=[(score(g,CONF),g) for g in allg]; res=[(s,g) for s,g in res if s is not None]; res.sort(reverse=True)
print("\nVALIDATION: groups ranked by the history-only 'conference' profile (n groups with >=5 uses: %d)"%len(res))
for r,(s,g) in enumerate(res[:15],1):
    print("%2d. %5d  score %6.1f  counts %s"%(r,g,s,[cnt[i][g] for i in range(8)]))
pos=[r for r,(s,g) in enumerate(res,1) if g==1792]; print("rank of 1792:",pos)
# Other verified values for reference
for g in (2232,1915,977,944,1980):
    print("verified",g,"rank under conference profile:",[r for r,(s,gg) in enumerate(res,1) if gg==g])
json.dump({"order":ORDER,"dates":DATE,"N":N},open("timing_meta.json","w"))

# ---- what do the top 'conference-profile' groups stand for in the Chaudordy plaintext? (word-level HMM alignment, rough)
al=json.load(open("align_hmm2_out.json"))
byg=collections.defaultdict(list)
for r in al:
    if r["w"]: byg[r["g"]].append(r["w"])
print("\nTOP 'conference' groups and the Chaudordy words aligned to them (alignment is rough after ~group 330):")
for s,g in res[:16]:
    print("  %5d  profile %s  chaudordy words: %s"%(g,[cnt[i][g] for i in range(8)],byg.get(g,"-")))
# ---- is the table the same across time? cosine similarity of group-use vectors (groups used >=5 times overall)
import math
G=[g for g in allg if sum(cnt[i][g] for i in range(8))>=5]
vec=[[cnt[i][g]/N[i] for g in G] for i in range(8)]
def cos(a,b):
    d=sum(x*y for x,y in zip(a,b)); return d/math.sqrt(sum(x*x for x in a)*sum(y*y for y in b))
print("\ncosine similarity of group usage between letters (%d groups):"%len(G))
print("              "+"  ".join("%-9s"%d[:9] for d in DATE))
for i in range(8): print("%-13s "%DATE[i][:13]+"  ".join("%9.2f"%cos(vec[i],vec[j]) for j in range(8)))
