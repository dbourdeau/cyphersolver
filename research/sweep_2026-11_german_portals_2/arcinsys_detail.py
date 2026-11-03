"""Fetch each kept Arcinsys record's full description and whether it has scans. Writes arcinsys_detail.json; resumes.

Kept: dated to 1900, found by a term other than the bare Ziffern ones, not obvious noise, and not the 3036 Gesamtinventar
mirror of a record in another fonds. One request a second."""
import html, json, os, re, time
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'arcinsys_detail.json')
BASE = {'he': 'https://arcinsys.hessen.de/arcinsys/', 'ni': 'https://www.arcinsys.niedersachsen.de/arcinsys/'}
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'
NOISE = re.compile(r'Dose|Tabatiere|Monogramm|Namenschiffre|Schnupftabak|Nadel|Theater|Stickerei|Polizei|Telegramm|'
                   r'Fernschreib|Gestapo|Kriegstagebuch|Wehrmacht', re.I)


def text(page):
    page = re.sub(r'<(script|style).*?</\1>', ' ', page, flags=re.S)
    page = re.sub(r'<[^>]+>', ' ', page)
    return re.sub(r'\s+', ' ', html.unescape(page))


def main():
    hits = json.load(open(os.path.join(HERE, 'arcinsys_hits.json'), encoding='utf-8'))['hits']
    store = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    s = requests.Session()
    s.headers['User-Agent'] = UA
    n = 0
    for key, r in hits.items():
        if key in store or not re.match(r'(he|ni):v\d+', key):
            continue
        y = re.search(r'\b(1[3-9]\d\d)\b', r.get('columnKeyLaufzeit') or '')
        sig, title = r.get('columnKeySignatur') or '', r.get('columnKeyBezeichnung') or ''
        if not y or int(y.group(1)) > 1900 or ', 3036, HHStAW Abt.' in sig or NOISE.search(title):
            continue
        if not [t for t in r.get('terms', []) if t not in ('Ziffern', 'in Ziffern')]:
            continue
        portal, vid = key.split(':v')
        time.sleep(1)
        try:
            p = s.get(BASE[portal] + 'showArchivalDescriptionDetails.action', params={'archivalDescriptionId': vid}, timeout=60).text
        except Exception as e:
            print('ERR', key, repr(e)[:100], flush=True)
            continue
        t = text(p)
        i = t.find('Signatur')
        images = sorted(set(re.findall(r'https?://[^"\'\s]*(?:digitalisate|iiif|dfg-viewer|viewer)[^"\'\s]*', p)))[:6]
        store[key] = {'sig': sig, 'title': title, 'date': r.get('columnKeyLaufzeit'),
                      'preview': bool((r.get('columnKeyPreviewImage') or {}).get('showImage')),
                      'digital': bool(images) or 'Digitalisat' in re.sub(r'Digitalisate? anzeigen\b', 'Digitalisat', t[i:i + 4000] if i >= 0 else ''),
                      'images': images, 'text': t[max(0, i - 50):i + 3000], 'terms': r.get('terms')}
        n += 1
        if n % 20 == 0:
            json.dump(store, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
            print(n, flush=True)
    json.dump(store, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('done', len(store), sum(v['digital'] for v in store.values()), flush=True)


if __name__ == '__main__':
    main()
