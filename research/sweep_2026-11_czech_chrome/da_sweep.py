"""Run the term list through DigiArchiv (SOA Třeboň) and save every result block to da_hits.jsonl."""
import json, re, sys, time
from digiarchiv import search, text

TERMS = sys.argv[1:] or ['šifr*', 'šifrovan*', 'šifrovaně', 'šifrový', 'dešifr*', 'chiffr*', 'Chiffre*', 'Ziffer*', 'cifra',
                         'cifre', 'tajné písmo', 'tajným písmem', 'Geheimschrift', 'cifrato', 'chiffré', 'nomenklátor', 'kryptogra*',
                         'zifra', 'ciffer*', 'Zifern']
out = open('da_hits.jsonl', 'a', encoding='utf-8')
for term in TERMS:
    start, seen, pages = 0, 0, None
    while True:
        t = text(search(term, start))
        m = re.search(r'Strana\s*(\d*)\s*/\s*(\d+)', t)
        pages = int(m.group(2)) if m else 0
        blocks = re.split(r'\n(?=(?:Inventární záznam|Archivní soubor|Kniha v archivní knihovně|Archivní pomůcka|Digitalizovan|Matrika|Listina|Kronika|Mapa)[^\n]*Poslední aktualizace)', t)
        blocks = [b.strip() for b in blocks[1:]]
        for b in blocks:
            out.write(json.dumps({'term': term, 'start': start, 'text': b}, ensure_ascii=False) + '\n')
        seen += len(blocks)
        print(term, 'start', start, 'pages', pages, 'blocks', len(blocks), flush=True)
        start += 10
        if start >= pages * 10 or not blocks or start > 400:
            break
        time.sleep(1.5)
    time.sleep(1.5)
