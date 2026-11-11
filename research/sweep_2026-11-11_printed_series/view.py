# print fts hits whose snippet has a cipher word; usage: view.py hits.json [skip-first-n-queries]
import json,sys,re
r=json.load(open(sys.argv[1])); seen=set()
C=re.compile(r"c[iy]pher|chiffr|cifr|Ziffer|Chiffer|cijfer",re.I)
bad=re.compile(r"^sim_|DTIC|cia-|CIA-|dictionar|novel|crypt|magazine|numismat|manualzilla",re.I)
for q,v in list(r.items())[int(sys.argv[2]) if len(sys.argv)>2 else 0:]:
    print("==",q,v["total"])
    for h in v["hits"]:
        s=" ".join(h["snip"]).replace("\n"," ")
        if h["id"] in seen or not C.search(s) or bad.search(h["id"]+(h["title"] or "")): continue
        try:
            y=int(str(h["year"])[:4])
            if y>1975: continue
        except Exception: pass
        seen.add(h["id"]); print(" ",h["id"],"|",(h["title"] or "")[:55],"|",h["year"],"|",s[:260])
