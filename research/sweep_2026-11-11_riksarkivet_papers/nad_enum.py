"""Enumerate digitised volumes of the private fonds and chancery series through the NAD API -> enum.json"""
import json, sys, time, requests
H = {'User-Agent': 'curl/8.0'}
SERIES = ['Oxenstiernska samlingen','Tessinska samlingen','Kanslikollegium','De la Gardieska samlingen','Reuterholmska samlingen',
 'S:t Barthélemysamlingen','Stedingkska arkivet','Ericsbergsarkivet','Kungliga arkiv','Skrivelser till konungen',
 'Läckösamlingen','Tidöarkivet','Kungliga handskriftsamlingen','Fredrik Tomas Adlercreutz papper','Utrikesdepartementet med föregångare',
 'Erik Dahlbergs samling','Skoklostersamlingen','Rydboholmssamlingen','Sjöholmsarkivet','Stegeborgssamlingen','Bielkesamlingen','Riksarkivets ämnessamlingar. Miscellanea','Manuskriptsamlingen','Kollegiers m fl, landshövdingars, hovrätters och konsistoriers skrivelser till Kungl Maj:t','Allmänna verks, ämbetsmäns, direktioners m fl skrivelser till Kungl. Maj:t']
out = {}
for ser in SERIES:
    off = 0; tot = 0
    while True:
        try:
            d = requests.get('https://data.riksarkivet.se/api/records', headers=H, timeout=90, params={'text': '*', 'only_digitised_materials': 'true', 'max': 100, 'offset': off, 'facet': 'PartOfArchive:' + ser}).json()
        except Exception as e:
            print('ERR', ser, off, e); break
        for it in d.get('items', []):
            if it.get('type') not in ('Volume', 'Dossier', 'Document'): continue
            m = it.get('metadata', {})
            out[it['id']] = dict(id=it['id'], ref=m.get('referenceCode'), caption=it.get('caption'), date=m.get('date'), note=m.get('note'), series=ser, type=it.get('type'),
                                 path=' / '.join(h['caption'].replace('\n', ' ') for h in m.get('hierarchy', [])))
        tot = d.get('totalHits', 0); off += 100; time.sleep(1.5)
        if off >= tot or off > 1500: break
    print(ser, tot, len(out), flush=True)
    json.dump(list(out.values()), open('enum.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
