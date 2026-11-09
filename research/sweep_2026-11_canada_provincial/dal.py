import json,urllib.request,urllib.parse,time,sys
out=[]
for term in ["cipher","cypher","ciphered","cryptogram","secret writing","code letter","chiffre","enciphered","decipher"]:
    for page in range(0,3):
        u="https://dalspace.library.dal.ca/server/api/discover/search/objects?size=20&page=%d&query=%s"%(page,urllib.parse.quote(term))
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30))
        except Exception as e: print(term,e);break
        objs=d["_embedded"]["searchResult"]["_embedded"]["objects"]
        tot=d["_embedded"]["searchResult"]["page"]["totalElements"]
        if page==0:print(term,tot)
        for o in objs:
            it=o["_embedded"]["indexableObject"]
            out.append((term,it.get("handle"),it.get("name")))
        if len(objs)<20:break
        time.sleep(2)
    time.sleep(2)
seen=set()
for t,h,n in out:
    if h in seen:continue
    seen.add(h);print(t,h,n)
