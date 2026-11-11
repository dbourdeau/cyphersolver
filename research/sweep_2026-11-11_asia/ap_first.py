"""First-page-only Abhilekh queries (10 hits + total) -> hits/first.jsonl, log to first.log. usage: ap_first.py field=value ..."""
import sys, json, time, urllib.parse, ap
f=open('hits/first.jsonl','a',encoding='utf8'); lg=open('first.log','a')
for a in sys.argv[1:]:
    params=dict(x.split('=',1) for x in a.split('&'))
    params={k:v+',contains' for k,v in params.items()}
    for sort in ('dc.title,asc','dc.title,desc'):
        params['sort']=sort
        qs=urllib.parse.urlencode(params)
        h=ap.get(ap.BASE+'AdvanceSearchV3?'+qs); n=ap.total(h); rs=ap.parse(h)
        for r in rs:
            r['_q']=a; f.write(json.dumps(r,ensure_ascii=False)+'\n')
        if sort.endswith('asc'):
            print('##',a,n,flush=True); lg.write(f'{a}\t{n}\n'); lg.flush()
        for r in rs: print('  ',r.get('Year'),r.get('Identifier'),r.get('No of Pages'),r['title'][:150])
        time.sleep(6)
        if n<=10: break
