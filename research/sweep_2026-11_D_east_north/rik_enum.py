"""Enumerate digitised Volumes of Riksarkivet Diplomatica series through data.riksarkivet.se/api/records (facet PartOfArchive)."""
import requests, json, sys, time, re
sys.stdout.reconfigure(encoding='utf-8')
H={'User-Agent':'curl/8.0'}
series = ['Diplomatica Turcica','Diplomatica Polonica','Diplomatica Muscovitica','Diplomatica Gallica','Diplomatica Hollandica','Diplomatica Anglica','Diplomatica Germanica','Diplomatica Italica','Diplomatica Danica','Diplomatica Hispanica','Diplomatica Lusitanica','Diplomatica Maroccana','Diplomatica Tunisica','Diplomatica Algerica','Diplomatica Cosacica','Diplomatica Tatarica','Diplomatica Transsylvanica','Diplomatica Svecica','Diplomatica Persica','Diplomatica Ragusana']
words = ['*','Brev','Depescher','Relationer','Koncept','Kungl','Envoyen','Chiffer','Original','Skrivelser','Memorial','Handlingar','Acta']
units = {}
def run(ser, w, offset=0):
    r=requests.get('https://data.riksarkivet.se/api/records',params={'text':w,'only_digitised_materials':'true','max':100,'offset':offset,'facet':'PartOfArchive:'+ser},headers=H,timeout=90)
    if r.status_code!=200: return None
    return r.json()
for ser in series:
    for w in words:
        off=0
        while True:
            try: d=run(ser,w,off)
            except Exception as e: print('ERR',ser,w,e); break
            if not d: break
            for it in d.get('items',[]):
                m=it.get('metadata',{})
                units[it['id']]={'id':it['id'],'ref':m.get('referenceCode'),'caption':it.get('caption'),'date':m.get('date'),'note':m.get('note'),'series':ser,'type':it.get('type'),'html':it['_links'].get('html')}
            tot=d.get('totalHits',0)
            off+=100
            time.sleep(1.2)
            if off>=tot: break
        print(ser,w,len(units),flush=True)
json.dump(list(units.values()),open('rik_units.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
