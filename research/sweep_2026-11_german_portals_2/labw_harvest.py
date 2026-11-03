"""Harvest the Landesarchiv BW online finding aids (ofs21/suche/ergebnis1.php) for cipher words, without a browser.

Unlike the 2 Nov Chrome pass this keeps 1750-1900 and adds terms and the old spellings. One request a second. Writes labw_hits.json.

    python labw_harvest.py --probe Geheimschrift
"""
import html, json, os, re, sys, time
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'labw_hits.json')
URL = 'https://www2.landesarchiv-bw.de/ofs21/suche/ergebnis1.php'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'
TERMS = ['chiffriert', 'chiffrierte', 'chiffrierter', 'chiffrierten', 'chiffriertes', 'Chiffre', 'Chiffren', 'Chiffern',
         'Chiffer', 'chiffrirt', 'chiffrirte', 'dechiffriert', 'Dechiffrierung', 'Dechiffrat', 'Geheimschrift', 'Geheimschriften',
         'Geheimzeichen', 'Geheimsprache', 'Geheimalphabet', 'Geheimschlüssel', 'Geheimcode', 'Geheimziffern', 'verschlüsselt',
         'verschlüsselte', 'verschlüsselter', 'verschlüsselten', 'Verschlüsselung', 'Entzifferung', 'entziffert', 'Kryptographie',
         'Kryptogramm', 'Ziffernschrift', 'Zifferschrift', 'Ziffernbrief', 'Zahlenschrift', 'en chiffre', 'Chiffreschlüssel',
         'Chiffrenschlüssel', 'Chiffrierschlüssel', 'in Ziffern', 'mit Auflösung', 'Geheimbrief', 'Geheimkorrespondenz']


def text(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def search(s, term):
    data = {'joker': 'zeichenfolge', 'sortierung': 'archivort asc, klassifi_bestand asc, bereich asc, klassifi asc',
            'trefferausgabe': '500', 'listeZeichenfolge': '', 'sucheAusgangspunkt': 'index', 'suche': term,
            'archive[8]': 'alle', 'suchMaschine': 'lucene', 'logik': 'und', 'pruefzahl': ''}
    r = s.post(URL, data=data, timeout=120, headers={'Referer': 'https://www2.landesarchiv-bw.de/ofs21/suche/index.php'})
    r.encoding = r.apparent_encoding if 'charset' not in r.headers.get('content-type', '') else r.encoding
    return r.text


def rows(page):
    out = {}
    for m in re.finditer(r'id_titlaufn=(\d+)', page):
        i = m.group(1)
        if i in out:
            continue
        start = page.rfind('<tr', 0, m.start())
        end = page.find('</tr>', m.end())
        out[i] = text(page[start:end])[:600]
    return out


def main():
    s = requests.Session()
    s.headers['User-Agent'] = UA
    if sys.argv[1:2] == ['--probe']:
        p = search(s, sys.argv[2])
        print(len(p), re.findall(r'[\d.]+\s+Treffer', p)[:3], re.findall(r'href="([^"]+)"', p)[10:20])
        rr = rows(p)
        print(len(rr))
        for k in list(rr)[:4]:
            print(k, rr[k][:300])
        if not rr:
            print(text(p)[:800])
        return
    store = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {'terms': {}, 'hits': {}}
    for t in TERMS:
        if t in store['terms']:
            continue
        time.sleep(1)
        try:
            rr = rows(search(s, t))
        except Exception as e:
            print(t, 'ERROR', repr(e)[:150], flush=True)
            continue
        store['terms'][t] = len(rr)
        for k, v in rr.items():
            store['hits'].setdefault(k, {'text': v, 'terms': []})['terms'].append(t)
        json.dump(store, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print(t, len(rr), 'unique', len(store['hits']), flush=True)


if __name__ == '__main__':
    main()
