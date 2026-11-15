import json, re, sys
d = json.load(open('short.json', encoding='utf-8'))
STRONG = re.compile(r'chiffriert|chiffrierte|chiffrierung|chiffren|chiffres|chiffre[- ]|chiffer|cifer|geheimschrift|dechiffr|entzifferung|entziffert|verschl[üu]ssel|kryptogr|schl[üu]ssel zu|ziffern|zahlenschl|nomenclator|nomenklator|aufl[öo]sung|heimlich\w* schrift|geheime[rn]? schrift|entschl[üu]ssel', re.I)
f = sys.argv[1]
for r in d:
    if f.lower() not in r['prov'].lower(): continue
    t = r['text']; m = STRONG.search(t); s = max(0, m.start()-60)
    lab = t.split(' || ')[0][:100]
    ref = re.sub(r'\s*\(Benutzungsort.*', '', r['ref'])[:40]
    b = r.get('begin'); 
    print(r['id'][:5], '|', ref, '|', lab, '|', t[s:s+120].replace(' | ',' / ') if lab[:40] not in t[s:s+120] else '')
