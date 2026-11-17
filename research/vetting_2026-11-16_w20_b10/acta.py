"""ACTApro (archive.spk-berlin.de/actaproweb) search by script: GET search.xhtml, POST searchForm, then
fetch each hit's archive.xhtml?id= page in the same session and print the record text.
Usage: python -I -X utf8 acta.py "<search term>" [outfile]"""
import re, sys, time, html, urllib.request, urllib.parse, http.cookiejar

BASE = 'https://archive.spk-berlin.de/actaproweb/'
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]


def get(url, data=None):
    time.sleep(1.2)
    r = op.open(url, data=urllib.parse.urlencode(data).encode() if data else None, timeout=60)
    return r.read().decode('utf-8', 'replace')


def text(h):
    h = re.sub(r'(?s)<script.*?</script>|<style.*?</style>', ' ', h)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()


def form_fields(h, form='searchForm'):
    m = re.search(r'(?s)<form id="%s".*?</form>' % form, h)
    f = {}
    for inp in re.finditer(r'<input[^>]*>', m.group(0)):
        t = inp.group(0)
        n = re.search(r'name="([^"]*)"', t)
        if not n:
            continue
        typ = (re.search(r'type="([^"]*)"', t) or [None, 'text'])[1]
        v = (re.search(r'value="([^"]*)"', t) or [None, ''])[1]
        if typ in ('checkbox', 'radio') and 'checked' not in t:
            continue
        if typ in ('submit', 'button'):
            continue
        f[n.group(1)] = html.unescape(v)
    return f


def search(term, sig=''):
    h = get(BASE + 'search.xhtml')
    f = form_fields(h)
    f['searchForm:searchTerm_input'] = term
    f['searchForm:searchDurationStart1'] = ''
    f['searchForm:searchDurationEnd1'] = ''
    f['searchForm:resultsForPage'] = '500'
    f['searchForm:searchByType'] = '3'
    f['searchForm:searchRootDocument'] = ''
    if sig:
        f['searchForm:searchSignature_input'] = sig
    f['searchForm:searchButton'] = ''
    f['searchForm'] = 'searchForm'
    return get(BASE + 'search.xhtml', f)


def hits(r):
    """(id, header text) per hit, in order."""
    out = []
    for m in re.finditer(r'<a[^>]*href="[^"]*archive\.xhtml\?id=([^"&]+)[^"]*"[^>]*>(.*?)</a>', r, re.S):
        out.append((m.group(1), text(m.group(2))))
    return list(dict.fromkeys(out))


def record(i):
    t = text(get(BASE + 'archive.xhtml?id=' + i))
    k = t.find('Vollansicht')
    e = t.find('Impressum des GStA', k)
    return t[k:e if e > 0 else k + 6000]


if __name__ == '__main__':
    term, pat = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else '')
    r = search(term)
    hs = hits(r)
    out = ['SEARCH %r: %d hits' % (term, len(hs))]
    for i, hd in hs:
        out.append('  HIT ' + hd[:160])
    for i, hd in hs:
        if pat and not re.search(pat, hd):
            continue
        out.append('=== ' + hd + '\n' + record(i))
    s = '\n'.join(out)
    if len(sys.argv) > 3:
        open(sys.argv[3], 'w', encoding='utf8').write(s)
    print(s[:12000])
