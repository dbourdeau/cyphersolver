import json,sys,time
from polona import search
seen={}
for t in sys.argv[1:]:
    d=search(t,cat='Rękopisy',size=48)
    print('##',t,d['totalElements'])
    for h in d['hits']:
        b=h['basicFields'];e=h.get('expandedFields',{})
        title=(b.get('title') or {}).get('values');date=(b.get('dateDescriptive') or {}).get('values');cr=(b.get('creatorForSearch') or {}).get('values')
        oid=h.get('objectId')
        if oid in seen: continue
        seen[oid]=1
        print(oid,date,cr,(title or [''])[0][:110])
    time.sleep(2)
