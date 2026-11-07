import json, time, sys
from an import units
terms="cifra cifre cifrata cifrate cifrato cifrati cifrario cifrari zifra zifre ziffra ziffre ciffra ciffre chiffre decifrazione decifrato decifrata decifrati cifrare cifrado descifrado crittografia crittografico cifras criptografia".split()
terms+=["in cifra","lettere cifrate","chiave cifrata","cartella cifrata"]
out={}
for f in ("denominazione-un","contenuto-un"):
    for t in terms:
        cur=1
        while True:
            try: j=json.loads(units(f,t,cur,50))
            except Exception as e:
                print("ERR",f,t,cur,e); time.sleep(5); break
            d=j.get("data",{})
            cards=d.get("cards",[])
            if cur==1: print(f,t,d.get("numFound"),flush=True)
            for c in cards:
                r=out.setdefault(c["id"],{"id":c["id"],"title":c["title"],"date":c.get("date"),"subtype":c.get("subtype"),"content":c["valuesArray"].get("content",[]),"hits":[]})
                r["hits"].append(f+":"+t)
            if len(cards)<50 or cur>=40: break
            cur+=1; time.sleep(1.2)
        time.sleep(1.2)
    json.dump(out,open("an_units_raw.json","w"),ensure_ascii=False)
json.dump(out,open("an_units_raw.json","w"),ensure_ascii=False)
print(len(out))
