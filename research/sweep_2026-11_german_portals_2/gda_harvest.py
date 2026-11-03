"""Harvest the Staatliche Archive Bayerns finding aids (www.gda.bayern.de/gvl/search.xhtml) for cipher words.

JSF/PrimeFaces: GET the search page for the ViewState, POST searchForm (full page) for hits, then POST pagingTopForm with
the page link's name for each next page. One request a second. Writes gda_hits.json, keyed by the archive's record id.

    python gda_harvest.py            # all TERMS, resumes from gda_hits.json
    python gda_harvest.py --probe X  # one term, first page only, print what came back
"""
import html, json, os, re, sys, time
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'gda_hits.json')
URL = 'https://www.gda.bayern.de/gvl/search.xhtml'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'
TERMS = ['Geheimschrift', 'chiffr*', 'Chiffre*', 'dechiffr*', 'dechiffriert', 'Ziffernschrift', 'verschlüsselt*',
         'Geheimzeichen', 'Geheimsprache', 'Zifferschrift', 'Zahlenschrift', 'Chiffern', 'Ziffer*',
         'Geheimschlüssel', 'Geheimalphabet', 'Geheimcode', 'Kryptogra*', 'Entzifferung', 'entziffert', 'Zifferbrief',
         'en chiffre', 'in chiffris', 'Geheimziffer', 'Decifrierung', 'Dechiffrierung', 'Chiffrierung', 'verziffert',
         'Geheimkorrespondenz', 'geheime Zeichen', 'Kanzleichiffre', 'Chiffrenschlüssel', 'Geheimbrief']


def hidden(form):
    return {html.unescape(n): html.unescape(v) for n, v in re.findall(
        r'<input[^>]*name="([^"]+)"[^>]*type="hidden"[^>]*value="([^"]*)"', form)} | {
        html.unescape(n): html.unescape(v) for n, v in re.findall(
        r'<input[^>]*type="hidden"[^>]*name="([^"]+)"[^>]*value="([^"]*)"', form)}


def form_of(page, fid):
    m = re.search(r'<form id="%s".*?</form>' % re.escape(fid), page, re.S)
    return m.group(0) if m else ''


def parse(page):
    rows = []
    for block in re.split(r'<div id="singleSearchResult"', page)[1:]:
        a = re.search(r'id="searchEntry:\d+:docForm:searchDocumentLink"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)
        if not a:
            continue
        rec = {'href': html.unescape(a.group(1)), 'head': html.unescape(re.sub(r'<[^>]+>', '', a.group(2))).strip()}
        for k, v in re.findall(r'<td class="doc-header">(.*?)</td>\s*<td class="doc-text"[^>]*>(.*?)</td>', block, re.S):
            rec[html.unescape(k).rstrip(':')] = html.unescape(re.sub(r'<[^>]+>', '', v)).strip()
        mid = re.search(r'id=(Vz[^&"#]+)', rec['href'])
        rec['id'] = mid.group(1) if mid else rec['href']
        rows.append(rec)
    return rows


def count(page):
    m = re.search(r'([\d.]+)\s+Datens', page)
    return int(m.group(1).replace('.', '')) if m else 0


def next_link(page):
    f = form_of(page, 'pagingTopForm')
    m = re.search(r'<a id="(pagingTopForm:[^"]+)"[^>]*>\s*(?:&gt;|>)\s*</a>', f)
    return m.group(1) if m else None


def nonce(page):
    m = re.search(r"PrimeFaces\.csp\.init\('([^']+)'\)", page) or re.search(r'nonce="([^"]+)"', page)
    return m.group(1) if m else ''


def search(s, term, limit=None):
    page = s.get(URL, timeout=60).text
    f = form_of(page, 'searchForm')
    data = hidden(f)
    data.update({'searchForm:searchTerm_input': term, 'searchForm:searchButton': 'Suchen',
                 'searchForm:valuesRecordPerpage': '100', 'primefaces.nonce': nonce(page)})
    for name in ('searchForm:searchByType_input', 'searchForm:searchRootDocument_input'):
        sel = re.search(r'<select[^>]*name="%s".*?</select>' % name, f, re.S)
        opt = re.search(r'<option value="([^"]*)"[^>]*selected', sel.group(0)) if sel else None
        if opt:
            data[name] = html.unescape(opt.group(1))
    time.sleep(1)
    page = s.post(URL, data=data, timeout=90).text
    n = count(page)
    rows = parse(page)
    p = 1
    while True:
        if limit and p >= limit:
            break
        link = next_link(page)
        if not link or len(rows) >= n:
            break
        d = hidden(form_of(page, 'pagingTopForm'))
        d[link] = link
        d['primefaces.nonce'] = nonce(page)
        time.sleep(1)
        page = s.post(URL, data=d, timeout=90).text
        got = parse(page)
        if not got:
            break
        rows += got
        p += 1
    return n, rows


def main():
    s = requests.Session()
    s.headers['User-Agent'] = UA
    if len(sys.argv) > 2 and sys.argv[1] == '--probe':
        n, rows = search(s, sys.argv[2], limit=1)
        print(n, len(rows))
        for r in rows[:5]:
            print(r['head'][:100], '|', r['id'], '|', r.get('Laufzeit'))
        return
    store = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {'terms': {}, 'hits': {}}
    for t in TERMS:
        if t in store['terms']:
            continue
        try:
            n, rows = search(s, t)
        except Exception as e:
            print(t, 'ERROR', e, flush=True)
            continue
        store['terms'][t] = {'count': n, 'got': len(rows)}
        for r in rows:
            store['hits'].setdefault(r['id'], r).setdefault('terms', []).append(t)
        json.dump(store, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print(t, n, len(rows), 'unique', len(store['hits']), flush=True)


if __name__ == '__main__':
    main()
