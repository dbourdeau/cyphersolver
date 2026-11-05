import requests, json, sys, re, time
sys.stdout.reconfigure(encoding='utf-8')
H={'User-Agent':'curl/8.0'}
u=[x for x in json.load(open('rik_units.json',encoding='utf-8')) if x['type']=='Volume']
try: done={x['id']:x for x in json.load(open('rik_vols.json',encoding='utf-8'))}
except Exception: done={}
for i,x in enumerate(u):
    if x['id'] in done: continue
    try:
        r=requests.get(f"https://data.riksarkivet.se/archive/{x['id']}.jsonld",headers=H,timeout=60)
        m=re.search(r'lbiiif\.riksarkivet\.se/arkis!(R\d+)/manifest',r.text)
        x['man']=m.group(1) if m else None
        time.sleep(1.0)
        if x['man']:
            mr=requests.get(f"https://lbiiif.riksarkivet.se/arkis!{x['man']}/manifest",headers=H,timeout=60)
            j=mr.json()
            seq=j.get('sequences',[{}])[0].get('canvases') or j.get('items') or []
            x['n']=len(seq)
            time.sleep(1.0)
    except Exception as e:
        x['err']=str(e)[:80]
    done[x['id']]=x
    if i%10==0:
        json.dump(list(done.values()),open('rik_vols.json','w',encoding='utf-8'),ensure_ascii=False)
        print(i,len(done),flush=True)
json.dump(list(done.values()),open('rik_vols.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print('done',len(done))
