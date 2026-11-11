#!/usr/bin/env python3
"""Print the full datasheet text of adatbazisokonline records (static HTML; carries the ARK id and every field).
usage: mnl_sheet.py CACHEDIR <db slug> id [id ...]"""
import sys, re, html, os, time, urllib.request, urllib.parse
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
d, slug = sys.argv[1], sys.argv[2]; os.makedirs(d, exist_ok=True)
for i in sys.argv[3:]:
    p = os.path.join(d, re.sub(r"\W", "_", slug)[:30] + "_" + i + ".html")
    if not os.path.exists(p):
        u = "https://adatbazisokonline.mnl.gov.hu/adatbazis/%s/adatlap/%s" % (urllib.parse.quote(slug), i)
        open(p, "wb").write(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=90).read()); time.sleep(2)
    s = open(p, encoding="utf8", errors="replace").read()
    m = re.search(r'<div id="datasheet".*?(?=var treePath|Tartalomgazda)', s, re.S)
    t = re.sub(r"<script.*?</script>", " ", m.group(0) if m else "", flags=re.S)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " | ", t)))
    t = re.sub(r"(\| )+", "| ", t); t = re.sub(r"^.*?Így hivatkozzon erre a tartalomra: ", "", t)
    print(i, "|", t.strip(), flush=True)
