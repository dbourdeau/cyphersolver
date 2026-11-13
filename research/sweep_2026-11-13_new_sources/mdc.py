import json,subprocess,sys,urllib.parse,time,collections
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
SCR="/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/newsrc/"
def get(term,page,n=100):
    u="https://mdc.csuc.cat/digital/api/search/searchterm/%s/maxRecords/%d/page/%d"%(urllib.parse.quote(term),n,page)
    r=subprocess.run(['curl','-s','-m','60','-A',UA,u],capture_output=True,text=True).stdout
    return json.loads(r)
allh={}
for t in sys.argv[1:]:
    p=1;tot=None
    while True:
        d=get(t,p); tot=d['totalResults']
        for it in d['items']:
            md={m['field']:m['value'] for m in it['metadataFields']}
            allh.setdefault((it['collectionAlias'],it['itemId']),{'term':[],'title':it['title'],'coll':md.get('cdmcoll'),'desc':md.get('descri'),'subj':md.get('subjec'),'link':it['itemLink']})['term'].append(t)
        if p*100>=tot or p>=10 or not d['items']: break
        p+=1; time.sleep(1.5)
    print(t,tot,flush=True); time.sleep(1.5)
json.dump({'%s/%s'%k:v for k,v in allh.items()},open(SCR+'mdc_hits.json','w'),ensure_ascii=False,indent=1)
c=collections.Counter(v['coll'] for v in allh.values())
for k,v in c.most_common(): print(v,k)
