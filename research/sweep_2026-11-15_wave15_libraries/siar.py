"""SIAR Veneto free-text search. python -I -X utf8 siar.py term ...  -> raw/siar.jsonl
GET https://siar.regione.veneto.it/serverSiar/json/searchMetadata?request=<json>"""
import json, sys, time, urllib.request, urllib.parse, os
HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, 'raw', 'siar.jsonl'), 'a', encoding='utf-8')
for term in sys.argv[1:]:
    for tipo in (['descrizione', 'unita', 'lettera', 'cartografia'],):
        req = {'caseInsensitive': True, 'text': term, 'actorId': '', 'archivi': {'tipo': tipo, 'denominazione': '', 'archiviFotografici': False, 'conAlberoArchivistico': False, 'conInventarioDigitale': False, 'conDocumentoDigitalizzato': False, 'conImmagini': False, 'conFilmati': False, 'progetto': ''}}
        u = 'https://siar.regione.veneto.it/serverSiar/json/searchMetadata?request=' + urllib.parse.quote(json.dumps(req))
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=120) as f:
                j = json.load(f)
        except Exception as e:
            print(term, tipo, 'ERR', e); continue
        data = j.get('data') or []
        print('##', term, tipo, j.get('message'), len(data), j.get('error'))
        for d in data:
            d['_term'] = term; d['_tipo'] = 'units'
            out.write(json.dumps(d, ensure_ascii=False) + '\n')
        out.flush(); time.sleep(1.2)
