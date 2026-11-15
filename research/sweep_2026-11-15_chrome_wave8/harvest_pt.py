"""Wave 8: DigitArq search over ALL archives except ANTT (already swept). Writes pt_hits.jsonl."""
import json,sys,time,urllib.parse,urllib.request,collections
BASE="https://digitarq.arquivos.pt/api/docs/search?"
TERMS=["cifra","cifras","cifrada","cifradas","cifrado","cifrados","em cifra","decifrada","decifrado","decifrar","chave da cifra","letra secreta","criptografia","cartas cifradas","carta cifrada","cyfra","zifra","chiffre","cipher","telegramas cifrados","linguagem cifrada","escrita cifrada"]
seen={}
def get(u):
    for i in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"cyphersolver research"}),timeout=90))
        except Exception as e:
            print("retry",e,file=sys.stderr);time.sleep(3*(i+1))
for t in TERMS:
    frm=0;tot=None;n=0
    while True:
        d=get(BASE+urllib.parse.urlencode({"query":t,"fromIndex":frm,"max":100}))
        if not d: break
        tot=d.get("total");rs=d["results"]
        if not rs: break
        for r in rs:
            if r.get("archiveCode")=="ANTT": continue
            if r["id"] not in seen:
                seen[r["id"]]={"id":r["id"],"ref":r["referenceCode"]["value"],"ac":r["archiveCode"],"title":r["titles"][0]["value"] if r.get("titles") else "","d1":r["dateInitial"]["value"] if r.get("dateInitial") else None,"files":r.get("filesCount"),"terms":[t]}
            elif t not in seen[r["id"]]["terms"]: seen[r["id"]]["terms"].append(t)
            n+=1
        frm+=100
        if frm>=min(tot or 0,3000): break
        time.sleep(1)
    print(t,tot,n,len(seen),flush=True)
with open("pt_hits.jsonl","w",encoding="utf8") as f:
    for r in seen.values(): f.write(json.dumps(r,ensure_ascii=False)+"\n")
print(collections.Counter(r["ac"] for r in seen.values()))
