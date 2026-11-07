import json,urllib.parse,time,sys
from an import get,B
terms=["cifra","cifre","in cifra","cifrata","cifrati","cifrario","cifrari","cifrato","decifrazione","decifrare","zifra","ziffra","chiavi cifrate","cifrate","corrispondenza cifrata","cifrare","cifrario diplomatico","lettere in cifra"]
out={}
for t in terms:
    cur=1
    while True:
        q=urllib.parse.urlencode({"p_p_id":"it_inera_icar_search_complessi_SearchComplessiPortlet","p_p_lifecycle":"2","p_p_state":"normal","p_p_mode":"view","p_p_resource_id":"/search","p_p_cacheability":"cacheLevelPage","keywords":t,"cur":cur,"pageSize":50})
        try: j=json.loads(get(B+"/it/patrimoni-documentari?"+q))
        except Exception as e: print("ERR",t,e); break
        d=j.get("data",{}); cards=d.get("cards") or d.get("items") or []
        if cur==1: print(t,d.get("numFound"),len(cards),list(d.keys())[:8],flush=True)
        for c in cards:
            out.setdefault(c["id"],{"id":c["id"],"title":c.get("title"),"date":c.get("date"),"type":c.get("type"),"content":c.get("valuesArray",{}).get("content",[]),"hits":[]})["hits"].append(t)
        if len(cards)<50 or cur>=20: break
        cur+=1; time.sleep(1.2)
    time.sleep(1.2)
json.dump(out,open("an_fonds_raw.json","w"),ensure_ascii=False)
print(len(out))
