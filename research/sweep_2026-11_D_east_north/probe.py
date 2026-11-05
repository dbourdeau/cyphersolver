import sys, time, requests
requests.packages.urllib3.disable_warnings()
H = {'User-Agent':'Mozilla/5.0 (cyphersolver research sweep; polite)'}
urls = """https://rgada.info/
http://rgada.info/
https://www.rgada.info/
https://archives.ru/
https://rusarchives.ru/
https://prlib.ru/
https://avpri.mid.ru/
https://garf.su/
https://rusneb.ru/
https://www.rsl.ru/
https://f.waldeck.example/
https://katalog.devletarsivleri.gov.tr/
https://www.archivesportaleurope.net/
https://www.nacr.cz/
https://www.mza.cz/
https://www.manuscriptorium.com/
https://kramerius5.nkp.cz/
https://www.mnl.gov.hu/
https://library.hungaricana.hu/
https://archives.hungaricana.hu/
https://adt.arcanum.com/
https://www.minv.sk/
https://www.slovakiana.sk/
https://www.finna.fi/
https://astia.narc.fi/
https://digi.kansalliskirjasto.fi/
https://www.digar.ee/
https://ais.ra.ee/
https://www.raduraksti.lv/
https://dom.lndb.lv/
https://handrit.is/
https://skjalaskrar.is/
https://www.arkivverket.no/
https://www.nb.no/
https://api.nb.no/
https://www.kb.dk/
https://www.kb.dk/e-mat/dod/
https://www.alvin-portal.org/
https://sok.riksarkivet.se/
https://data.riksarkivet.se/api/records?text=chiffer&max=1
https://soeg.rigsarkivet.dk/
https://www.manuscriptorium.com/apps/index.php?direct=search
https://cdiak.archives.gov.ua/
https://archives.gov.ua/
https://www.rada.gov.ua/
https://www.nlb.by/
https://nab.by/
https://e-archives.ee/
https://www.rahvusarhiiv.ee/
https://www.lvva.gov.lv/
https://www.lna.lv/
https://www.liv.lt/
https://www.dlib.si/
https://www.digitalna.nb.rs/
https://www.dubrovnik-archives.org/
https://www.nb.admin.ch/
https://archive.org/advancedsearch.php?q=cipher&rows=1&output=json
https://commons.wikimedia.org/w/api.php?action=query&meta=siteinfo&format=json
https://ru.wikisource.org/w/api.php?action=query&meta=siteinfo&format=json
https://cs.wikisource.org/w/api.php?action=query&meta=siteinfo&format=json
https://hu.wikisource.org/w/api.php?action=query&meta=siteinfo&format=json
https://sv.wikisource.org/w/api.php?action=query&meta=siteinfo&format=json
https://runeberg.org/
https://www.digitale-sammlungen.de/
https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=chiffre&rows=1
""".split()
for u in urls:
    try:
        t=time.time()
        r = requests.get(u, headers=H, timeout=12, verify=False, allow_redirects=True)
        print(r.status_code, round(time.time()-t,1), len(r.content), u, '->', r.url if r.url!=u else '')
    except Exception as e:
        print('ERR', type(e).__name__, str(e)[:70], u)
    time.sleep(0.4)
