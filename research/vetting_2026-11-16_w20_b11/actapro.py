"""ACTApro (GStA PK) search by plain HTTP: GET the JSF search form, POST it with a term.
Usage: python -I -X utf8 actapro.py "<term>" [startyear endyear]
Prints each hit's header and matched text fragments."""
import re, sys, time, html, urllib.request, urllib.parse, http.cookiejar

BASE = 'https://archive.spk-berlin.de/actaproweb/search.xhtml'
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (research script)')]


def text(s):
    s = re.sub(r'<script.*?</script>', '', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


def search(term, y1='', y2=''):
    page = op.open(BASE, timeout=40).read().decode('utf8', 'replace')
    vs = re.search(r'name="javax.faces.ViewState"[^>]*value="([^"]+)"', page).group(1)
    data = {
        'searchForm': 'searchForm',
        'searchForm:searchTerm_input': term,
        'searchForm:searchDurationStart1': y1,
        'searchForm:searchDurationEnd1': y2,
        'searchForm:searchByType': '',
        'searchForm:Bestande_input': '',
        'searchForm:searchSignature_input': '',
        'searchForm:searchSignature_hinput': '',
        'searchForm:searchRootDocument': '',
        'searchForm:resultsForPage': '100',
        'searchForm:searchButton': 'Suchen',
        'javax.faces.ViewState': vs,
    }
    sel = re.search(r'<select id="searchForm:searchByType".*?</select>', page, re.S)
    if sel:
        o = re.search(r'<option[^>]*selected[^>]*value="([^"]*)"|<option value="([^"]*)"[^>]*selected', sel.group(0))
        if o:
            data['searchForm:searchByType'] = o.group(1) or o.group(2)
    time.sleep(1)
    r = op.open(BASE, urllib.parse.urlencode(data).encode(), timeout=60).read().decode('utf8', 'replace')
    return r


if __name__ == '__main__':
    term = sys.argv[1]
    y1 = sys.argv[2] if len(sys.argv) > 2 else ''
    y2 = sys.argv[3] if len(sys.argv) > 3 else ''
    r = search(term, y1, y2)
    m = re.search(r'(\d[\d.]*)\s*(Treffer|Ergebnisse)', text(r))
    print('hits:', m.group(0) if m else '?')
    # split into entries on the document link
    parts = re.split(r'(?=<a[^>]*id="[^"]*searchDocumentLink")', r)
    for p in parts[1:]:
        uid = re.search(r'document/(Vz_[0-9a-f-]+)', p)
        t = text(p[:6000])
        print('---', uid.group(1) if uid else '')
        print(t[:1500])
