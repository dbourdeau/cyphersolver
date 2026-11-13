import rasearch, json, time, collections
terms = ['chiffer','chifferskrift','chiffre','chiffreret','chiffrerede','chiffrerer','chiffrering','dechiffr','dechifferet','dechiffrering','ciffer','cifferskrift','ciffre','cifre','cifrene','cifferet','krypt','kryptografi','kryptogram','hemmelig skrift','hemmeligt skrift','hemmelige tegn','hemmelighed skrift','lønskrift','ziffer','Ziffern','verschlüsselt','Geheimschrift','geheime Schrift','chifferbrev','chiffer-nøgle','nøgle til','tegnskrift','mærker','cypher','cipher','Nummern','nummerskrift','talskrift','tal i stedet','bogstaver erstattet']
seen = {}
for t in terms:
    for online in (True, False):
        d = rasearch.search(t, online)
        tot = d.get('totalCount')
        rows = d.get('searchResults', [])
        # page through up to 3 pages
        p = 1
        while len(rows) < min(tot or 0, 300):
            rows += rasearch.search(t, online, page=p).get('searchResults', []); p += 1; time.sleep(1)
        print(t, online, tot, len(rows), flush=True)
        for r in rows:
            if 'daisyId' not in r: continue
            e = seen.setdefault(r['daisyId'], dict(id=r['daisyId'], type=r['documentType'], titel=r['titel'], f=(r.get('dateFrom') or '')[:4], t=(r.get('dateTo') or '')[:4], desc=r.get('beskrivelse') or '', creator=r.get('visBedsteArkivskaberNavn'), online=False, terms=[]))
            e['terms'].append(t)
            if online: e['online'] = True
        time.sleep(1)
json.dump(list(seen.values()), open('ra_terms.json', 'w'), ensure_ascii=False, indent=0)
