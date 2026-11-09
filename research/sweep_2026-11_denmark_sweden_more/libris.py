import requests,json,time,sys
H={'User-Agent':'curl/8.0'}
terms=sys.argv[1:]
out={}
for t in terms:
    s=1;tot=None
    while True:
        r=requests.get('https://libris.kb.se/xsearch',params={'query':t,'format':'json','n':200,'start':s},headers=H,timeout=60)
        try:j=r.json()['xsearch']
        except Exception as e: print(t,'err',r.status_code);break
        tot=j['records']
        for x in j['list']:
            out.setdefault(x['identifier'],x)['q']=t
        s+=200
        time.sleep(2.5)
        if s>tot or s>1000:break
    print(t,tot)
json.dump(out,open('libris_hits.json','w'),ensure_ascii=False,indent=0)
types={}
for x in out.values(): types[x.get('type')]=types.get(x.get('type'),0)+1
print(types)
