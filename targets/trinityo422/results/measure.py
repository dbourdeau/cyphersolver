import random, sys
V=[2,22,10,30,18,7,27,15,4,24,12,1,21,9,29,17,5,25,13]
def expected(n,off):
    gn=((n+off-1)%19)+1; d=(19*(gn-1)+15)%30; day=21+d
    return day if day<=31 else day-31
def score(vals,off=3): return sum(vals[n-1]==expected(n,off) for n in range(1,20))/19
s=score(V); print("score",s, "attendu",[expected(n,3) for n in range(1,20)])
rng=random.Random(20261116); ctr=[]
for _ in range(200):
    w=V[:]; rng.shuffle(w); ctr.append(score(w))
print("temoins max",max(ctr),"moy",sum(ctr)/200)
print("decalages",{o:round(score(V,o),3) for o in range(19) if o!=3})
print("PASS" if s>=0.85 and s>=max(ctr)+0.30 else "FAIL")
