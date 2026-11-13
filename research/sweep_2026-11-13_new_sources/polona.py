import json,subprocess,sys,urllib.parse,time
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
SCR="/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/newsrc/"
def search(term,cat=None,page=0,size=48):
    f={"copyright":["false"]}
    if cat: f["category"]=[cat]
    u="https://polona.pl/api/search-service/search/simple?"+urllib.parse.urlencode({'query':term,'page':page,'pageSize':size,'sort':'RELEVANCE'})
    r=subprocess.run(['curl','-s','-m','60','-A',UA,'-H','Content-Type: application/json','-X','POST',u,'-d',json.dumps({"keywordFilters":f,"temporalFilters":None})],capture_output=True,text=True).stdout
    return json.loads(r)
def row(h):
    b=h['basicFields']; g=lambda k:(b.get(k) or h.get('expandedFields',{}).get(k) or {}).get('values')
    return {'id':h.get('id') or h.get('uuid'),'title':g('title'),'date':g('dateDescriptive'),'creator':g('creatorForSearch')}
if __name__=='__main__':
    allr={}
    for t in sys.argv[1:]:
        d=search(t)
        cats=d['aggregations']['category']['values']
        print(t,d['totalElements'],[(c['value'],c['count']) for c in cats])
        if d['hits']: print('  keys',list(d['hits'][0].keys())[:8])
        time.sleep(2)
