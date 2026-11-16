import json, urllib.request, urllib.parse, time
BASE='https://archieven.tresoar.nl/api'
def get(p):
    for i in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(BASE+p,headers={'User-Agent':'Mozilla/5.0'}),timeout=60))
        except Exception as e: time.sleep(2*(i+1))
    return {}
TERMS=['cijfer*','cijferschrift','geheimschrift','"in cijfer"','"in cijfers"','ontcijfer*','gecijferd','cijffer*','cyffer*','cyfer*','chijffer*','chiffr*','chiffre','gechiffreerd','dechiffr*','déchiffr*','geheimschrift*','cijfersleutel*','sleutel cijfer','codeboek*','cipher*','cypher*','nomenclator','"geheime tekens"','cijfertekens','ontcijffer*','geheymschrift','"in cyffer"','"in cijffer"','"met cijfer"','decijfer*','gecijffert','"geheime schrijfwijze"','steganograf*','stenografie','cifra','zifra','cijferbrief*']
seen={}
for t in TERMS:
    page=1
    while page<=10:
        d=get('/search?'+urllib.parse.urlencode({'q':t,'page':page,'limit':100}))
        for r in d.get('data',[]):
            x=seen.setdefault(r['id'],{k:r.get(k) for k in ('id','titel','periode','datering','nummer','root_id','scan_count','path','niveau','omvang_aantal','omvang_soort')}|{'snip':r.get('__snippet'),'terms':[]})
            x['terms'].append(t)
        if page*100>=d.get('total',0) or not d.get('data'): break
        page+=1; time.sleep(.3)
    print(t,d.get('total'),len(seen),flush=True)
json.dump(list(seen.values()),open('tres_hits.json','w',encoding='utf8'),ensure_ascii=False)
