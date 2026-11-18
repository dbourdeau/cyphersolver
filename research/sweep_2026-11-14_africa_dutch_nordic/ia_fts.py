"""archive.org full-text queries; usage ia_fts.py out.jsonl 'query' ... ; one request per 3 s"""
import sys,json,time,urllib.parse,urllib.request,re
out=sys.argv[1]
f=open(out,'a')
for q in sys.argv[2:]:
    u="https://archive.org/services/search/beta/page_production/?service_backend=fts&hits_per_page=50&page=1&user_query="+urllib.parse.quote(q)
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=60))
        h=d["response"]["body"]["hits"]
        print(q,'| total',h.get('total'),flush=True)
        for x in h['hits']:
            fl=x['fields']; hl=x.get('highlight') or {}
            sn=' / '.join(hl.get('text',[]) if isinstance(hl,dict) else [])
            rec={'q':q,'id':fl.get('identifier'),'title':fl.get('title'),'year':fl.get('year') or fl.get('date'),'page':fl.get('page_num'),'snip':re.sub(r'\s+',' ',sn)[:400]}
            f.write(json.dumps(rec,ensure_ascii=False)+'\n')
    except Exception as e: print(q,'ERR',e,flush=True)
    f.flush(); time.sleep(3)
