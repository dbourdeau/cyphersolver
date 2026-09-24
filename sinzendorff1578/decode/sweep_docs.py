import json,re,os,sys,time,urllib.request
sys.path.insert(0,os.path.dirname(__file__))
from fetch import get as _get
def get(u):
    for k in range(5):
        try: return _get(u)
        except Exception as e: print('retry',u[-40:],e,flush=True); time.sleep(10*(k+1))
    raise RuntimeError(u)
L=json.load(open(r'C:/Users/dbour/cypher/catalogue_harvest/decode/list.json',encoding='utf-8'))
ids=[r['id'] for r in L if 'Chiffrenschl' in (r['c_holder'] or '') and r['record_type']=='2']
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
        try: b=get('https://de-crypt.org/decrypt-custom/filesrv/?file='+d)
        except Exception as e: print('fail',d); continue
        if len(b)!=17947: open(o,'wb').write(b)
        time.sleep(0.3)
print('done')
