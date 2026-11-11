#!/usr/bin/env python3
"""Search DECODE RecordsList (basic search). usage: decode_search.py "term" [...]"""
import sys, re, html, time, urllib.request, urllib.parse, http.cookiejar
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
op.addheaders = [("User-Agent", UA)]
for term in sys.argv[1:]:
    u = "https://de-crypt.org/decrypt-web/RecordsList?cmd=search&searchtype=%3D&recperpage=100&search=" + urllib.parse.quote(term)
    s = op.open(u, timeout=90).read().decode("utf8", "replace")
    rows = re.findall(r'<tr[^>]*data-rowindex.*?</tr>', s, re.S)
    print("##", term, "rows on page:", len(rows), re.findall(r'Records? \d+ to \d+ of (\d+)', re.sub(r"<[^>]+>", "", s))[:1])
    for r in rows:
        cells = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c))).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)]
        print("  ", " | ".join(c for c in cells if c)[:400])
    time.sleep(2.5)
