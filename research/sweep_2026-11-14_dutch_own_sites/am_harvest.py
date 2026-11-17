import am_search as a, json, time, re
TERMS=['cijfer*','cijferschrift','geheimschrift*','"in cijfer"','"in cijfers"','ontcijfer*','gecijferd','cijffer*','cyffer*','cyfer*','chiffr*','chiffre*','gechiffreerd','dechiffr*','déchiffr*','"geheime schrift"','cijfersleutel*','codeboek*','cipher*','cypher*','nomenclator','stenografie','steganografie','"geheime tekens"','cijfertekens','cijferalfabet','"in cijfer geschreven"']
seen={}
for t in TERMS:
    for ty in ['File','Series','Fonds']:
        page=1
        while True:
            d=a.q(t,ty,page=page,per=100)
            for r in d['rows']:
                s=(r['data'].get('date') or {}).get('start') or ''
                if s and s[:4]>'1920': continue
                x=seen.setdefault(r['id'],{'id':r['id'],'title':r['title'],'desc':r['description'],'date':r['data'].get('date'),'parents':[p['title'] for p in r['data'].get('parents',[])],'type':ty,'terms':[]})
                x['terms'].append(t)
            if page*100>=d['total'] or not d['rows']: break
            page+=1; time.sleep(0.4)
        time.sleep(0.3)
    print(t,len(seen),flush=True)
json.dump(list(seen.values()),open('am_hits.json','w',encoding='utf8'),ensure_ascii=False,indent=0)
