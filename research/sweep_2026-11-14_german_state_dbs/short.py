import json, re
d = json.load(open('new_unknown.json', encoding='utf-8'))
STRONG = re.compile(r'chiffriert|chiffrierte|chiffrierung|chiffren|chiffres|chiffre[- ]|chiffer|cifer|geheimschrift|dechiffr|entzifferung|entziffert|verschl[üu]ssel|kryptogr|schl[üu]ssel zu|ziffern|zahlenschl|nomenclator|nomenklator|aufl[öo]sung|heimlich\w* schrift|geheime[rn]? schrift|entschl[üu]ssel', re.I)
MOD = re.compile(r'\(WK\)|Druckvorschrift|Plansammlung|Kriegsministerium|MKr|Stv\. GK|Generalkommando|Telegraph|Funk|Fernsprech|Dampf|Zeichnungskatalog|Chiffre-Nummer|Kinospielfilm|Lichtbild|Theaterzettel|Kästchen mit der Chiffer|Freimarke|Inschrift|Siegel|Sprengstoff|Kriegsgefangene|Postüberwachung', re.I)
out = []
for r in d:
    if r['noise']: continue
    b = r.get('begin')
    b = b[0] if isinstance(b, list) and b else b
    if b is not None and b > 679000: continue   # after about 1860
    t = r['text']
    if MOD.search(t): continue
    if not STRONG.search(t): continue
    out.append(r)
print(len(out))
from collections import Counter
print(Counter(r['prov'][:45] for r in out).most_common(30))
json.dump(out, open('short.json', 'w', encoding='utf-8'), ensure_ascii=False)
