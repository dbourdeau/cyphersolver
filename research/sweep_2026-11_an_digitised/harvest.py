import an,json,sys,re
terms=sys.argv[1:] or []
try: store=json.load(open("units.json",encoding="utf8"))
except: store={}
try: counts=json.load(open("counts.json",encoding="utf8"))
except: counts={}
for term in terms:
  for field in ["denominazione-un","contenuto-un"]:
    cur=1; tot=None
    while True:
        try: t=json.loads(an.search(field,term,cur,"on"))
        except Exception as e: print("ERR",term,field,cur,e); break
        d=t["data"]; tot=d["numFound"]
        for c in d.get("cards",[]):
            i=str(c["id"])
            e=store.setdefault(i,{"id":i,"title":c.get("title"),"date":c.get("date"),"route":c.get("route","").split("?")[0],"type":c.get("type"),
              "part":[v.get("text") for v in c.get("valuesArray",{}).get("content",[])],"hits":[]})
            tag=field[:3]+":"+term
            if tag not in e["hits"]: e["hits"].append(tag)
        if cur>=d["pagination"]["max"] or cur>=d["pagination"]["total"]: break
        cur+=1
    counts[field+":"+term]=tot
    print(field,term,tot,flush=True)
  json.dump(store,open("units.json","w",encoding="utf8"),ensure_ascii=False,indent=0)
  json.dump(counts,open("counts.json","w",encoding="utf8"),ensure_ascii=False,indent=0)
print("distinct",len(store))
