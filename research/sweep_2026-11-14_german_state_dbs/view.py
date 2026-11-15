import json, re, sys
d = json.load(open('new_unknown.json', encoding='utf-8'))
CW = re.compile(r'chiffr|chiffer|cifer|cyffer|zyffer|ziffernschrift|zifferschrift|in ziffern|mit ziffern|geheimschrift|geheimzeichen|geheimalphabet|geheimschl|heimliche[rn]? schrift|geheime[rn]? schrift|kryptogr|entziffer|entschl[üu]ssel|verschl[üu]ssel|nomenk?clator|klarschrift|dechiffr|cifra|cifris|zahlenschl', re.I)
prov_f = sys.argv[1] if len(sys.argv) > 1 else ''
n = 0
for r in d:
    if r['noise']: continue
    if prov_f and prov_f.lower() not in r['prov'].lower(): continue
    t = r['text']
    m = CW.search(t)
    s = max(0, m.start() - 70) if m else 0
    lab = t.split(' || ')[0][:90]
    print(r['id'][:6], '|', r['ref'][:34], '|', lab, '|', t[s:s+150].replace(' | ', ' / '))
    n += 1
print(n)
