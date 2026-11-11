"""DECODE basic keyword search (one polite request per term).

    python3 decode_search.py "<term>" ["<term>" ...]

Prints the number of result pages (20 records a page) and the first rows. The DECODE dump is not in this checkout,
so this is the DECODE check used by the 11 Nov 2026 German sweep.
"""
import html, re, sys, time, urllib.parse, urllib.request

UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36'


def search(term, rows=5):
    url = 'https://de-crypt.org/decrypt-web/RecordsList?' + urllib.parse.urlencode({'cmd': 'search', 'search': term, 'searchtype': ''})
    page = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60).read().decode('utf-8', 'replace')
    m = re.search(r'data-pagecount="(\d+)"', page)
    out = []
    for r in re.findall(r'<tr[^>]*data-rowindex.*?</tr>', page, flags=re.S)[:rows]:
        out.append(re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', r))).strip()[:220])
    return (m.group(1) if m else '0'), out


if __name__ == '__main__':
    for t in sys.argv[1:]:
        pages, rows = search(t)
        print('DECODE "%s": %s page(s), %d row(s) shown' % (t, pages, len(rows)))
        for r in rows:
            print('   ', r)
        time.sleep(2.5)
