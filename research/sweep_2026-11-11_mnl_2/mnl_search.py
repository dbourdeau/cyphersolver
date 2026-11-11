#!/usr/bin/env python3
"""Harvest adatbazisokonline.mnl.gov.hu search results (inline `var searchResults = [...]` JSON).
usage: mnl_search.py OUTDIR term [term ...]   -> OUTDIR/mnl_hits.jsonl (appended), counts on stdout
Copied from sweep_2026-11-11_southeast; page cap raised from 60 to 150 (the site now returns 20 hits a page)."""
import sys, json, base64, re, time, html, urllib.request, urllib.parse, os
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=90).read().decode("utf8", "replace")
def strip(s):
    s = re.sub(r"<br\s*/?>", " | ", s or ""); s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
for term in sys.argv[2:]:
    t = base64.b64encode(json.dumps({"q": term, "fq": [], "sort": "score"}, ensure_ascii=False, separators=(",", ":")).encode()).decode()
    p = 0; n = 0; total = "?"
    while True:
        s = get("https://adatbazisokonline.mnl.gov.hu/search?term=%s&P=%d" % (urllib.parse.quote(t), p))
        m = re.search(r"var searchResults = (\[.*?\]);\s*$", s, re.M)
        mt = re.search(r"([\d ]+) dokumentumban", s)
        if mt: total = mt.group(1).strip()
        rows = json.loads(m.group(1)) if m else []
        if not rows: break
        with open(os.path.join(out, "mnl_hits.jsonl"), "a", encoding="utf8") as f:
            for r in rows:
                f.write(json.dumps({"term": term, "ref": r.get("resultTileFile"), "db": r.get("dbName"), "title": r.get("title"),
                    "date": r.get("date"), "attr": strip(r.get("itemAttribute")), "url": "https://adatbazisokonline.mnl.gov.hu" + r.get("datasheetURL", "").split("?")[0],
                    "doc": r.get("docSRC"), "img": r.get("imgURL")}, ensure_ascii=False) + "\n")
        n += len(rows); p += 1
        if p > 150: break
        time.sleep(2)
    print(term, "total", total, "fetched", n, flush=True)
    time.sleep(2)
