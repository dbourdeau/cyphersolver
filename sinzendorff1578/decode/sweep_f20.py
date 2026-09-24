import json,re,os,sys,time,urllib.request
sys.path.insert(0,os.path.dirname(__file__))
from fetch import get
L=json.load(open(r'C:/Users/dbour/cypher/catalogue_harvest/decode/list.json',encoding='utf-8'))
ids=[r["id"] for r in L if 1192<=int(r["id"])<=1555 and 'Chiffrenschl' in (r['c_holder'] or '') and r['record_type']=='2']
print(len(ids),flush=True)
for i in ids:
    p=f'docs/rec{i}.htm'
    if not os.path.exists(p):
        try: open(p,'wb').write(get(f'https://de-crypt.org/decrypt-web/RecordsView/{i}'))
        except Exception as e: print('fail',i,e); continue
        time.sleep(0.3)
    h=open(p,encoding='utf-8',errors='ignore').read()
    for d in sorted(set(re.findall(r'filesrv/\?file=(DOC_[A-Za-z0-9_.]+)',h))):
        o='docs/'+d
        if os.path.exists(o): continue
        b=get('https://de-crypt.org/decrypt-custom/filesrv/?file='+d)
        if len(b)!=17947: open(o,'wb').write(b)
        time.sleep(0.3)
print('done')
