import json,re,requests,time,os,sys
d=json.load(open('hpbk_all.json',encoding='utf-8'))
old=json.load(open('../sweep_2026-11-14_russia_ottoman_nordic/koc_items.json',encoding='utf-8'))
ids=set()
rx=re.compile(r'şifr|encrypt|cipher|encod',re.I)
for k,v in d.items():
    if k.endswith('HPBK'):
        t=' '.join(m['value'] for m in v['metadataFields'])
        if rx.search(t): ids.add(int(k.split('|')[0]))
for k in old:
    if k.endswith('HPBK'): ids.add(int(k.split('|')[0]))
ids=sorted(ids);print(len(ids),flush=True)
os.makedirs('img',exist_ok=True)
for i in ids:
    p='img/HPBK_%d.jpg'%i
    if os.path.exists(p) and os.path.getsize(p)>1000: continue
    for t in range(4):
        try:
            r=requests.get('https://cdm21054.contentdm.oclc.org/digital/api/singleitem/image/HPBK/%d/default.jpg'%i,headers={'User-Agent':'Mozilla/5.0'},timeout=60)
            if r.status_code==200 and len(r.content)>1000:
                open(p,'wb').write(r.content);break
        except Exception: pass
        time.sleep(3)
    else: print('fail',i,flush=True)
    time.sleep(.6)
print('done',flush=True)
