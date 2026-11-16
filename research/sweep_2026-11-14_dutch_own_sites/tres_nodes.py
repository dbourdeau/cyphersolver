import json,urllib.request,sys,re
def node(i):
    d=json.load(urllib.request.urlopen(urllib.request.Request(f'https://archieven.tresoar.nl/api/nodes/{i}',headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
    return d.get('data',d)
for i in sys.argv[1:]:
    n=node(i)
    print('==',i,n.get('periode'),n.get('nummer'),n.get('niveau'),'scan',n.get('scan_count'),'iiif',bool(n.get('iiif')))
    t=n.get('titel') or ''
    print(re.sub(r'\s+',' ',t)[:1500])
    for k in ('nb','omvang_aantal','omvang_soort','taal','trefwoorden'):
        if n.get(k): print(' ',k,str(n[k])[:400])
