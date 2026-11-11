# run fts phrase queries, several pages, save hits; usage: q.py out.json pages "query" ...
import sys,json,time
from fts import fts
out=sys.argv[1]; pages=int(sys.argv[2])
try: res=json.load(open(out))
except Exception: res={}
for q in sys.argv[3:]:
    if q in res: continue
    hs=[];tot=None
    for p in range(1,pages+1):
        try:
            d=fts(q,50,p)
        except Exception as e:
            print("ERR",q,e); break
        b=d["response"]["body"]["hits"]; tot=b.get("total")
        for h in b["hits"]:
            f=h["fields"]; hl=h.get("highlight") or {}
            hs.append({"id":f.get("identifier"),"title":f.get("title"),"page":f.get("page_num"),"year":f.get("year") or f.get("date"),"snip":(hl.get("text") or [""])[:2] if isinstance(hl,dict) else []})
        if len(b["hits"])<50: break
        time.sleep(2)
    res[q]={"total":tot,"hits":hs}
    print(tot,len(hs),q,flush=True)
    json.dump(res,open(out,"w"),indent=0)
    time.sleep(2)
