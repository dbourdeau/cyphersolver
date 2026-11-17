import sys, json, urllib.request, urllib.parse
q=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 30
u='https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query='+urllib.parse.quote(q)+'&hits_per_page=%d&page=1'%n
r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60)
d=json.load(r)
hits=d.get('response',{}).get('body',{}).get('hits',{}).get('hits',[])
print('total',d.get('response',{}).get('body',{}).get('hits',{}).get('total'))
for h in hits:
    f=h.get('fields',{})
    hl=h.get('highlight',{}).get('text',[''])
    print(f.get('identifier'),f.get('page_num'),'|',(f.get('title') or '')[:60],'|',' .. '.join(hl)[:300].replace('\n',' '))
