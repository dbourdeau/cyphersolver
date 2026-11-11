"""DDB Solr, archives sector, digitised only: python3 ddb_digi.py OUT.jsonl"""
import json, sys, time, urllib.parse, urllib.request
B='https://api.deutsche-digitale-bibliothek.de/2/search/index/search/select'
TERMS=['chiffr*','dechiffr*','Chiffer*','Ziffernschrift','Zifferschrift','Zifferbrief*','Geheimschrift*','verschlüssel*','entziffer*','unentziffert',
 '"in Ziffern"','"mit Ziffern"','"in Zahlen"','"en chiffres"','"en chiffre"','cifra','cifre','Zifra','Ziffra','Ziffre*','Geheimzeichen','Kryptogramm*','"in Chiffern"',
 'Chiffre','Chiffren','chiffriert','Zahlenschrift','Geheimalphabet','Nomenklator','Ziffernschlüssel','Chiffrenschlüssel','Geheimcode','Zeichenschrift','Ziffernkanzlei','"geheime Schrift"','"geheimer Schrift"','cipher','ciphered','zifferiert','beziffert','"in Charakteren"','Characteren','Caracteren','Charakterschrift','Ziffer']
def get(p):
    u=B+'?'+urllib.parse.urlencode(p,doseq=True)
    for i in range(4):
        try:
            with urllib.request.urlopen(u,timeout=60) as r: return json.load(r)
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(4*(i+1))
    raise RuntimeError(u)
recs={};counts={}
for t in TERMS:
    s=0
    while True:
        d=get({'q':t,'rows':500,'start':s,'wt':'json','sort':'id asc','fq':['sector_fct:sec_01','digitalisat:true']})
        n=d['response']['numFound']; docs=d['response']['docs']
        for doc in docs:
            doc.pop('preview_store',None)
            if doc['id'] in recs: recs[doc['id']]['_terms'].append(t)
            else: doc['_terms']=[t]; recs[doc['id']]=doc
        s+=500; time.sleep(1.5)
        if s>=n or not docs or s>=5000: break
    counts[t]=n; print(t,n,file=sys.stderr)
with open(sys.argv[1],'w') as f:
    for r in recs.values(): f.write(json.dumps(r,ensure_ascii=False)+'\n')
json.dump(counts,open(sys.argv[1]+'.counts.json','w'),ensure_ascii=False,indent=1)
print(len(recs),'unique',file=sys.stderr)
