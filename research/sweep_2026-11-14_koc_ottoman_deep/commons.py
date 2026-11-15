import requests,json,time,sys,urllib.parse
sys.stdout.reconfigure(encoding='utf-8')
H={'User-Agent':'cyphersolver-sweep/1.0 (research; contact via repo)'}
terms=['şifreli telgraf','şifre telgraf Osmanlı','Ottoman cipher telegram','Ottoman cipher','Ottoman code telegram','şifre defteri','Osmanlı şifre','Ottoman encrypted','cipher Constantinople 19th century','Qajar cipher','ramz Qajar letter','Persian cipher letter','Persian code telegram','Khedive cipher','Egypt cipher telegram 1882','Urabi cipher','Arabic cipher manuscript','Arabic cryptography manuscript','Ibn Dunaynir','al-Kindi cryptanalysis','ciphered letter Istanbul','code book Ottoman','Telegramme Ottoman Yemen','Hilmi Pasha telegram','Yıldız telegram şifre','cipher key Ottoman Bank','şifre cetveli','ta\'miye','mu\'amma cipher','Abdul Hamid telegraph code']
seen={}
for t in terms:
    for ns in (6,):
        u='https://commons.wikimedia.org/w/api.php?action=query&list=search&srnamespace=6&srlimit=30&format=json&srsearch='+urllib.parse.quote(t)
        try: r=requests.get(u,headers=H,timeout=30).json()
        except Exception as e: print('err',t,e);continue
        for h in r.get('query',{}).get('search',[]):
            if h['title'] not in seen: seen[h['title']]=(t,h.get('snippet','')[:100])
    time.sleep(.5)
print(len(seen))
json.dump(seen,open('commons_hits.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
for k,v in seen.items(): print(v[0],'|',k)
