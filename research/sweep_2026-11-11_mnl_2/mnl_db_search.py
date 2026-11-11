#!/usr/bin/env python3
"""Search ONE database of adatbazisokonline.mnl.gov.hu (keeps the 20th-century databases out of the hits).
URL: /adatbazis/<slug>?term=<base64 {"q":..,"fq":{"db_id":[]},"sort":"score"}>&P=<page>; 20 hits a page.
usage: mnl_db_search.py OUTDIR slug[,slug...] term [term ...]  -> OUTDIR/db_hits.jsonl (appended), counts on stdout"""
import sys, json, base64, re, time, html, urllib.request, urllib.parse, os
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
def get(url):
    for k in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=90).read().decode("utf8", "replace")
        except Exception as e:
            err = e; time.sleep(8)
    raise err
def strip(s):
    s = re.sub(r"<br\s*/?>", " | ", s or ""); s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
for slug in sys.argv[2].split(","):
    for term in sys.argv[3:]:
        t = base64.b64encode(json.dumps({"q": term, "fq": {"db_id": []}, "sort": "score"}, ensure_ascii=False, separators=(",", ":")).encode()).decode()
        p = 0; n = 0; total = "0"
        while True:
            s = get("https://adatbazisokonline.mnl.gov.hu/adatbazis/%s?term=%s&P=%d" % (urllib.parse.quote(slug), urllib.parse.quote(t), p))
            m = re.search(r"var searchResults = (\[.*?\]);\s*$", s, re.M)
            mt = re.search(r"([\d ]+) dokumentumban", s)
            if mt: total = mt.group(1).strip()
            rows = json.loads(m.group(1)) if m else []
            if not rows: break
            with open(os.path.join(out, "db_hits.jsonl"), "a", encoding="utf8") as f:
                for r in rows:
                    f.write(json.dumps({"slug": slug, "term": term, "ref": r.get("resultTileFile"), "db": r.get("dbName"), "title": r.get("title"),
                        "date": r.get("date"), "attr": strip(r.get("itemAttribute")), "url": "https://adatbazisokonline.mnl.gov.hu" + r.get("datasheetURL", "").split("?")[0],
                        "img": r.get("imgURL"), "more": r.get("moreHitsNum")}, ensure_ascii=False) + "\n")
            n += len(rows); p += 1
            if p > 120 or len(rows) < 20: break
            time.sleep(2)
        print(slug[:40], "|", term, "| total", total, "fetched", n, flush=True)
        time.sleep(2)
