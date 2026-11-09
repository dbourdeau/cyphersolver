import json,time,urllib.request,urllib.parse,sys
terms=["Chiffre","chiffriert","chiffrirt","Chiffern","Geheimschrift","Geheimschriften","Ziffern","Zifferschrift","Zifferbrief","cifra","cifre","cifrato","cifrata","chiffre","chiffres","chiffré","cipher","cypher","in Ziffern","Dechiffrierung","Entzifferung","dechiffriert","Schlüssel Chiffre","Kryptographie","Geheimschrift Brief","Korrespondenz Chiffre"]
out={}
for t in terms:
    for p in range(0,6):
        u="https://www.digitale-sammlungen.de/api/search?handler=simple-metadata&query="+urllib.parse.quote(t)+"&pageSize=100&startPage=%d"%p
        try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=40))
        except Exception as e: print(t,p,e); break
        for x in d.get("docs",[]):
            if x.get("manufacturingType")!="print": out.setdefault(x["id"],x)["term"]=t
        print(t,p,d["numTotal"],len(out),flush=True)
        if (p+1)*100>=d["numTotal"]: break
        time.sleep(2.5)
    time.sleep(2.5)
json.dump(out,open("bsb_hits.json","w"),ensure_ascii=False,indent=1)
