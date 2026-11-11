"""python man.py <scratch> <Shelfmark>... : fetch IIIF manifests (3 s apart), print canvas count and labels summary"""
import sys,json,os,urllib.request,time,urllib.error
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
S=sys.argv[1]
for sm in sys.argv[2:]:
    mp=f'{S}/m_{sm}.json'
    if not os.path.exists(mp):
        req=urllib.request.Request(f'https://digi.vatlib.it/iiif/MSS_{sm}/manifest.json',headers={'User-Agent':UA,'Referer':'https://digi.vatlib.it/'})
        try: d=urllib.request.urlopen(req,timeout=90).read()
        except urllib.error.HTTPError as e:
            print(sm,'HTTP',e.code,flush=True)
            if e.code in(429,403): sys.exit(1)
            time.sleep(3); continue
        open(mp,'wb').write(d); time.sleep(3)
    m=json.load(open(mp,encoding='utf8'))
    cv=m['sequences'][0]['canvases']
    md={x['label']:x['value'] for x in m.get('metadata',[]) if isinstance(x.get('value'),str)}
    print(sm,len(cv),m.get('label'),json.dumps(md,ensure_ascii=False)[:400],flush=True)
