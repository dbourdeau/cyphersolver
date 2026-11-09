import json,time,urllib.request,urllib.parse
terms=["cipher","cypher","ciphered","cyphered","cipher letter","in cipher","in cypher","decipher","deciphered","decyphered","cifra","chiffre","chiffres","cipher key","code letter","secret writing","cryptogram","cryptographic","Geheimschrift","Ziffern","enciphered","encoded letter","in figures","cypher letter","letters in cipher","numerals cipher"]
out={}
for t in terms:
    for p in range(1,4):
        u="https://digital.bodleian.ox.ac.uk/search/?q="+urllib.parse.quote(t)+"&format=json&page=%d"%p
        try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0","Accept":"application/json"}),timeout=40))
        except Exception as e: print(t,p,e); break
        for m in d.get("member",[]):
            o=out.setdefault(m["id"],{"shelfmark":m["shelfmark"],"title":m["displayFields"].get("title"),"snip":[],"terms":[],"man":m["manifest"]["id"],"surf":m["surfaceCount"]})
            o["terms"].append(t); o["snip"]+=m["displayFields"].get("snippet",[])
        print(t,p,d["totalItems"],len(out),flush=True)
        if p*len(d.get("member",[]))>=d["totalItems"] or not d["member"]: break
        time.sleep(2.5)
    time.sleep(2.5)
json.dump(out,open("bod_hits.json","w",encoding="utf8"),ensure_ascii=False,indent=1)
