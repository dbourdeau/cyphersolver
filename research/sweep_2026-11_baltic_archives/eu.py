import requests,json,time,sys
S=requests.Session()
terms=['cipher','cypher','Chiffre','chiffriert','Geheimschrift','Ziffer','Ziffern','chiffre','cifra','cifra','šifr*','šifrēt*','šifreeri*','salakiri','slepenraksts','шифр*','тайнопись','цифирью','krypt*','secret writing','decipher*','dechiffr*','Zifferschrift','cipher letter','in Ziffern']
out={}
for c in ['estonia','latvia']:
    for t in terms:
        for k in range(3):
            try:
                r=S.get("https://api.europeana.eu/record/v2/search.json",params=dict(wskey='api2demo',query=t,qf='COUNTRY:'+c,rows=100,profile='standard'),timeout=60);d=r.json();break
            except Exception: time.sleep(3); d={}
        its=d.get('items',[]);print(c,t,d.get('totalResults'),flush=True)
        for i in its:
            f=lambda v:' | '.join(map(str,v)) if isinstance(v,list) else str(v or '')
            out[i['id']]=dict(id=i['id'],c=c,t=t,title=f(i.get('title')),desc=f(i.get('dcDescription')),year=f(i.get('year')),type=f(i.get('dcType')),prov=f(i.get('dataProvider')),link=i.get('guid'))
        time.sleep(1.5)
json.dump(list(out.values()),open('eu_hits.json','w',encoding='utf8'),ensure_ascii=False)
print(len(out))
