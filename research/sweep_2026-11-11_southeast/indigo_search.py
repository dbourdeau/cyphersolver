#!/usr/bin/env python3
"""Search an ArhivX 'Indigo' portal (digitalna.nsk.hr, dizbi.hazu.hr). usage: indigo_search.py BASE term [...]"""
import sys, re, html, time, urllib.request, urllib.parse
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
base = sys.argv[1]
for term in sys.argv[2:]:
    u = base + "?pr=l&ps=50&msq=" + urllib.parse.quote(term)
    try: s = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=60).read().decode("utf8", "replace")
    except Exception as e: print("##", term, "ERR", e); continue
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S))))
    m = re.search(r"Prikazano [\d-]+ od (\d+) zapisa", t)
    print("##", term, "|", m.group(1) if m else "?")
    seen = []
    for href, lab in re.findall(r'<a[^>]+href="([^"]*pr=i[^"]*)"[^>]*>(.*?)</a>', s, re.S):
        lab = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", lab))).strip()
        if lab and (href, lab) not in seen and len(seen) < 40: seen.append((href, lab)); print("   ", lab[:140], "|", href[:60])
    time.sleep(2.5)
