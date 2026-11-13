"""Pillon's suggestions of 13 Nov 2026 (6819 3412 = PIERR-ET, 5511 = messieurs, 3412 = et, VIN-OY, DUC-ROT) against the
alphabetical rule and the telegram's own structure. Vocabulary: wiki/topic_counts.json (words used >= 2 times; the Favre/Enquete
corpus of alpha_test.py is not in the repo, so errors differ slightly from the earlier sections)."""
import json,bisect,re,os
H=os.path.dirname(os.path.abspath(__file__))
D=json.load(open(os.path.join(H,"wiki","topic_counts.json"),encoding="utf8"))["counts"]
V=sorted(w for w,n in D.items() if n>=2 and re.fullmatch("[a-z]+",w))
print("vocabulary %d words"%len(V))
for s,v in [("est",3407),("et",3412),("messieurs",5511),("m",5511),("monsieur",5711),("madame",5218),("mademoiselle",5219),("pi",6816),
            ("pierre",6819),("on",6129),("oy",6124),("oi",6124),("vin",9802),("duc",2722),("ro",8317),("rot",7802),("r",7802),("re",7802),
            ("le",5006),("les",5019),("inspecteur",4821),("inspecteurs",4822)]:
    f=bisect.bisect_left(V,s)/len(V); print("  %-12s %04d  value %.3f  position %.3f  diff %+.3f"%(s,v,v/9999,f,f-v/9999))
T=open(os.path.join(H,"inspecteurs_2nov_partial.txt"),encoding="utf8").read().split()
for g in ("5511","5711","3412","7802","5219"):
    print("\n"+g)
    for i,t in enumerate(T):
        if t==g: print("   "+" ".join(T[max(0,i-6):i+9]))
