import json,re,urllib.request,sys
rows=json.load(open('tres_hits.json',encoding='utf8'))
roots={}
def root(i):
    if i not in roots:
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(f'https://archieven.tresoar.nl/api/toegangen/{i}',headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
            d=d.get('data',d); roots[i]=(d.get('code'),d.get('titel'))
        except Exception as e: roots[i]=('?',str(e)[:30])
    return roots[i]
rx=re.compile(r'cijferschrift|geheimschrift|geheymschrift|in cijfers?\b|cijffer|cyffer|chijffer|ontcijffer|ontcijfer|gecijfer|chiffr|cipher|cypher|codeboek|zifra|cifra|sleutel|decijfer',re.I)
for r in rows:
    t=r['titel'] or ''
    if rx.search(t) and not re.search(r'statistiek|jaarcijfers',t,re.I):
        c=root(r['root_id'])
        print(f"{r['periode']}|{c[0]} {str(c[1])[:40]}|inv {r['nummer']}|sc{r['scan_count']}|{t[:330]}")
