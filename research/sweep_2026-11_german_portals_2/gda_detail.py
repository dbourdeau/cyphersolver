"""Fetch the full record (fonds, signature, whole description, any images) for the selected gda.bayern.de hits.

Selection is by head prefix and year from gda_filter.py's list. Writes gda_selected.json. One request a second."""
import html, json, os, re, time
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'
SEL = ['889 - Korrespondenz der Herzöge', '892 - Berichte und Korr', '893 - Berichte und Korr', 'Dr. Ulrich Zasius',
       '777 -  (Neben)', '793/II', '6286 - Abschriften', '1346 - Übertritt', '1450/1', '4023 - Kriegszüge',
       '80 - Schlüssel zu einer', '29 - Konvente zu Ulm', '38/2 - ', '37/2 - ', '35 - Konvent', '38/1 - ', '37/3 - ',
       '39 - Friedensverhandlungen', '40 - Schriftwechsel', '61/3 - ', '61/25 - ', '15280 - ', '61/32 a', '61/30 - ',
       '61/32 b', '60/38 - ', '62/1 a', '61/42 - ', '59/3 - ', '59/5 - ', '62/9 II', '201 - Chiffrierte', '215 - Berichte Mörmanns',
       '2189 - Misce', '1455 - Vertrauliche', '99 - Acta secretissima', '16091 - ', '16999 - ', '406 - Kurkölnische',
       '125 - Materiam', '165 - 1) Geh', '210 - Geheime Berichte', '14 - \'Invasion', '9 - \'Mission', '13 - \'Affaire',
       '15 - Mission', '16 - Guerre', '59 - Gesandtschaftsberichte', '7174 - ', '1703 - Korrespondenz', '4509 - Fasc',
       '1 - \'Miscellanea\'', '2681 - Sammlung', '2398 - General', '2397 - General', '246 - Korrespondenzen',
       '133/29', '193/IV', '196/8 c', '13/1 - Nachlaß', '807 - Einstweilige', '158 - Politischer']


def text(page):
    page = re.sub(r'<(script|style).*?</\1>', ' ', page, flags=re.S)
    page = re.sub(r'<[^>]+>', ' ', page)
    return re.sub(r'\s+', ' ', html.unescape(page))


def main():
    s = requests.Session()
    s.headers['User-Agent'] = UA
    hits = json.load(open(os.path.join(HERE, 'gda_hits.json'), encoding='utf-8'))['hits']
    out = {}
    for rid, r in hits.items():
        if not any(r['head'].startswith(p) for p in SEL):
            continue
        if not re.search(r'chiffr|geheim|verschl|schlüssel|chiffer', json.dumps(r, ensure_ascii=False), re.I):
            continue
        time.sleep(1)
        url = 'https://www.gda.bayern.de' + r['href'] if r['href'].startswith('/') else r['href']
        try:
            p = s.get(url, timeout=60).text
        except Exception as e:
            print('ERR', rid, e)
            continue
        t = text(p)
        crumbs = [html.unescape(x) for x in re.findall(r'class="ui-menuitem-text">([^<]+)</span>', p.split('stx-breadcrumb-icon', 1)[-1])]
        crumbs = list(dict.fromkeys(c for c in crumbs if 'rechtlichen' not in c))[:10]
        i = t.find('Signatur')
        out[rid] = {'head': r['head'], 'url': url, 'record': r, 'images': r.get('Medium', '')[:1] != 'A',
                    'crumbs': crumbs}
        print(r['head'][:70], '|', out[rid]['images'], '|', crumbs[:7], flush=True)
    json.dump(out, open(os.path.join(HERE, 'gda_selected.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(out))


if __name__ == '__main__':
    main()
