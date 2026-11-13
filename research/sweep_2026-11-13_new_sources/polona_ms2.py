import json,sys,time,subprocess
from polona import search,UA
cache={}
def note(oid):
    r=subprocess.run(['curl','-s','-m','30','-A',UA,'https://polona.pl/api/search-service/search/'+oid],capture_output=True,text=True).stdout
    d=json.loads(r); e=d['expandedFields']
    return ' | '.join(' '.join(e[k]['values']) for k in ('note','description','physicalDescription','callNumber','provenance') if k in e)
seen={}
for t in sys.argv[1:]:
    d=search(t,cat='Rękopisy',size=48)
    print('##',t,d['totalElements'],flush=True)
    for h in d['hits']:
        oid=h['objectId']
        if oid in seen: continue
        b=h['basicFields']
        title=(b.get('title') or {}).get('values',[''])[0]
        if 'Górecki' in json.dumps(b,ensure_ascii=False) or 'Ficowski' in json.dumps(b,ensure_ascii=False): continue
        seen[oid]=1
        n=note(oid); time.sleep(1)
        print(oid,(b.get('dateDescriptive') or {}).get('values'),title[:90],'\n     NOTE:',n[:350],flush=True)
    time.sleep(2)
