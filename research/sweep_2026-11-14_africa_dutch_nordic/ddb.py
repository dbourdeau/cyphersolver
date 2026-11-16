"""DDB Solr (no key): Africa x cipher boolean queries; usage ddb.py 'query' ... ; prints hits"""
import sys,json,time,urllib.parse,urllib.request,re
for q in sys.argv[1:]:
    u='https://api.deutsche-digitale-bibliothek.de/2/search/index/search/select?q=%s&rows=40&start=0&wt=json'%urllib.parse.quote(q)
    try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'curl/8.0'}),timeout=60))
    except Exception as e: print(q,'ERR',e); time.sleep(3); continue
    r=d['response']; print(q,'| total',r['numFound'],flush=True)
    for x in r['docs'][:40]:
        print('   ',x.get('id'),'|',str(x.get('label') or x.get('title'))[:110],'|',str(x.get('provider_fct') or x.get('provider'))[:40],'|',x.get('sector_fct'),'|',str(x.get('subtitle') or '')[:80])
    time.sleep(3)
