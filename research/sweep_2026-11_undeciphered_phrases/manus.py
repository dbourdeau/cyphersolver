import json,sys,time,urllib.parse,urllib.request
sys.stdout.reconfigure(encoding='utf-8')
API="https://manus.iccu.sbn.it/o/manus-api/titles-search-post"
def page(q,mode,n):
    body=urllib.parse.urlencode({"monocampo":q,"n":"v","monocampo:tipo":mode,"page":n}).encode()
    req=urllib.request.Request(API,data=body,headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0"})
    time.sleep(1.2)
    return json.loads(urllib.request.urlopen(req,timeout=60).read().decode('utf8','replace'),strict=False)
for q in sys.argv[1:]:
    for mode in ('ONLY',):
        try: d=page(q,mode,1)['data']
        except Exception as e: print(q,'ERR',e);continue
        print('##',q,d.get('total'))
        for it in d.get('results',[])[:20]:
            print('  ',it['id'],it['title']['text'][:100],'|',(it.get('snippet') or '')[:160].replace('\n',' '))
