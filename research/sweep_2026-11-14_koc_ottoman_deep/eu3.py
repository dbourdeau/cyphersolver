import requests,json,time,sys,urllib.parse
sys.stdout.reconfigure(encoding='utf-8')
terms=['şifreli','şifre telgraf','cipher telegram','ramz','rumuz','chiffre','chiffré','télégramme chiffré','dépêche chiffrée','code secret','geheimschrift','Ottoman cipher','Persian cipher','Qajar cipher','Khedive cipher','ciphered despatch','cipher key Turkey','encoded letter Ottoman','telegram in cipher','çözülemeyen']
seen={}
for t in terms:
    for extra in ['','&qf=COUNTRY:Turkey','&qf=YEAR:[1800 TO 1920]']:
        u='https://api.europeana.eu/record/v2/search.json?wskey=api2demo&rows=50&query='+urllib.parse.quote(t+(' AND (Ottoman OR Turkey OR Istanbul OR Constantinople OR Persia OR Egypt OR Tehran OR Cairo)' if not extra else ''))+extra.replace(' ','%20')
        try: r=requests.get(u,timeout=40).json()
        except Exception as e: print('err',t,extra);continue
        for it in r.get('items',[]):
            seen.setdefault(it['id'],(t,it.get('title',[''])[0][:110],it.get('year',[''])[0] if it.get('year') else '',it.get('dataProvider',[''])[0][:40],it.get('guid','')))
        time.sleep(.8)
print(len(seen))
json.dump(seen,open('eu3.json','w',encoding='utf-8'),ensure_ascii=False)
for k,v in seen.items(): print(v[0],'|',v[1],'|',v[2],'|',v[3])
