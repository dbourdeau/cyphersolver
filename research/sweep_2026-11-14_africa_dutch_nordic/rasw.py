"""Riksarkivet (Sweden) record search; usage rasw.py 'text' ..."""
import sys,json,time,urllib.parse,urllib.request,re
for q in sys.argv[1:]:
    u='https://data.riksarkivet.se/api/records?text=%s&max=50&offset=0'%urllib.parse.quote(q)
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'curl/8.0'}),timeout=60))
    except Exception as e: print(q,'ERR',e); time.sleep(3); continue
    items=d.get('items') or []
    print(q,'| total',d.get('totalHits'),flush=True)
    for it in items[:15]:
        print('   ',it.get('referenceCode'),'|',(it.get('caption') or it.get('title') or '')[:90],'|',it.get('dateText') or it.get('date'),'|',str(it.get('description') or it.get('note') or '')[:120])
    time.sleep(3)
