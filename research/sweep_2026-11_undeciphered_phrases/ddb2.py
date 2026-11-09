import json,sys,time,urllib.parse,urllib.request
sys.stdout.reconfigure(encoding='utf-8')
B='https://api.deutsche-digitale-bibliothek.de/2/search/index/search/select'
def get(p):
    u=B+'?'+urllib.parse.urlencode(p)
    for i in range(3):
        try: return json.load(urllib.request.urlopen(u,timeout=60))
        except Exception as e: print('retry',e,file=sys.stderr);time.sleep(4)
seen=set()
out=open('ddb_hits2.jsonl','a',encoding='utf-8')
for q in sys.argv[1:]:
    d=get({'q':q,'rows':100,'start':0,'wt':'json','fq':'sector_fct:sec_01','sort':'id asc'})
    r=d['response'];print('##',q,r['numFound'])
    for doc in r['docs']:
        if doc['id'] in seen: continue
        seen.add(doc['id']);doc.pop('preview_store',None);doc['_q']=q
        out.write(json.dumps(doc,ensure_ascii=False)+'\n')
        v=doc.get('view') or []
        print('  ',doc['id'][:8],'|',(doc.get('begin_time') or [''])[0],'|',(doc.get('provider_fct') or [''])[-1][:30],'|',str(doc.get('label'))[:110],'|',' / '.join(v[:2])[:60],'|',' '.join(str(x) for x in v if 'chiffr' in str(x).lower() or 'dechiff' in str(x).lower())[:200])
    time.sleep(1.5)
