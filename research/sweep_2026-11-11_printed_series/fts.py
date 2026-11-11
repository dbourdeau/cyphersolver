import sys, json, urllib.parse, urllib.request
def fts(q, n=20, page=1):
    u="https://archive.org/services/search/beta/page_production/?service_backend=fts&hits_per_page=%d&page=%d&user_query=%s"%(n,page,urllib.parse.quote(q))
    r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=60)
    return json.load(r)
if __name__=="__main__":
    d=fts(sys.argv[1], int(sys.argv[2]) if len(sys.argv)>2 else 10)
    hits=d["response"]["body"]["hits"]["hits"]
    print(d["response"]["body"]["hits"].get("total"))
    for h in hits:
        f=h["fields"]
        print(f.get("identifier"),"|",f.get("title"),"|",f.get("year") or f.get("date"))
        for s in (h.get("highlight") or {}).get("text",[])[:3] if isinstance(h.get("highlight"),dict) else []:
            print("   ",s[:300].replace("\n"," "))
