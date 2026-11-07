"""Does the inspectors' numbering follow alphabetical position? Place the known syllables/words in an alphabetical French word list
and compare their fractional position with value/9999."""
import re,collections,bisect,sys,unicodedata
sys.stdout.reconfigure(encoding="utf8")
def strip(s): return "".join(c for c in unicodedata.normalize("NFD",s) if unicodedata.category(c)!="Mn")
def toks(t): return [re.sub(r"[^a-z]","",strip(x)) for x in re.findall(r"[\wéèêëàâîïôùûüçœ]+",t.lower().replace("'"," ").replace("’"," "))]
corp=[]
for f in ("gouvernementdela01favr","gouvernementdela02favr","sc_0001326967_0000001317479","sc_0001326967_00000001739290"):
    corp+=[w for w in toks(open(r"C:\Users\dbour\enquete\%s.txt"%f,encoding="utf8",errors="replace").read()) if w]
c=collections.Counter(corp)
for MIN in (2,3,5):
    V=sorted(w for w,n in c.items() if n>=MIN and len(w)>=2)
    print("\nvocabulary: words with >=%d uses: %d entries"%(MIN,len(V)))
    anchors=[("a",218),("bal",919),("ca",1122),("di",2514),("er",3316),("ge",4001),("ke",4906),("l",5121),("mer",5504),("on",6129),("pi",6816),("s",8328),("teen",9214),("recu",5926),("depeche",603)]
    err=[]
    for s,v in anchors:
        f=bisect.bisect_left(V,s)/len(V)
        print("  %-8s value %4d -> %.3f   alphabetical position %.3f   diff %+.3f"%(s,v,v/9999,f,f-v/9999))
        if s not in ("recu","depeche"): err.append(abs(f-v/9999))
    print("  mean |diff| over the 13 syllable anchors: %.3f"%(sum(err)/len(err)))
