#!/usr/bin/env python3
"""List every DECODE record matching a basic search term, all pages. usage: decode_list.py "term" > out.tsv
Columns: id | location/shelfmark | dates | names | languages | type | status | images"""
import sys, re, html, time, urllib.request, urllib.parse, http.cookiejar
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
op.addheaders = [("User-Agent", UA)]
term = sys.argv[1]
u = "https://de-crypt.org/decrypt-web/RecordsList?cmd=search&searchtype=%3D&recperpage=100&search=" + urllib.parse.quote(term)
seen = set(); page = 1
while True:
    s = op.open(u, timeout=90).read().decode("utf8", "replace")
    rows = re.findall(r'<tr[^>]*data-rowindex.*?</tr>', s, re.S); new = 0
    for r in rows:
        cells = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c))).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)]
        cells = [c for c in cells if c and c != "View"]
        if cells and cells[0] not in seen:
            seen.add(cells[0]); new += 1; print(" | ".join(cells))
    if not new or len(rows) < 100: break
    page += 1; u = "https://de-crypt.org/decrypt-web/RecordsList?page=%d" % page
    time.sleep(2.5)
print("# total", len(seen), "for", term, file=sys.stderr)
