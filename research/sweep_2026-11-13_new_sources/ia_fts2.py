import json,sys,time
from ia_fts import q
SCR="/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/newsrc/"
out=[]
for qq in sys.argv[1:]:
    try: d=q(qq,size=50)
    except Exception as e: print('ERR',qq,e); continue
    h=d['hits']; print('##',qq,h['total'],flush=True)
    for x in h['hits']:
        f=x['fields']
        out.append({'q':qq,'id':x['_id'].split('|')[0],'year':f.get('meta_year'),'title':(f.get('meta_title') or [''])[0],'hl':x.get('highlight',{}).get('text',[])})
    time.sleep(2)
json.dump(out,open(SCR+'ia_fts2_%d.json'%int(time.time()),'w'),ensure_ascii=False,indent=1)
