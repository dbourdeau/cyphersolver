"""archive.org full-text (page-level) search. python ia_fts.py "<query>" ... ; appends hits to ia_hits.jsonl, prints total and first 8 (id | title | year | snippet)"""
import sys, json, urllib.parse, urllib.request, time, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
def fts(q, n=50, page=1):
    u = "https://archive.org/services/search/beta/page_production/?service_backend=fts&hits_per_page=%d&page=%d&user_query=%s" % (n, page, urllib.parse.quote(q))
    for i in range(3):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=90))
        except Exception as e:
            time.sleep(4)
if __name__ == "__main__":
    out = open(os.path.join(HERE, "ia_hits.jsonl"), "a", encoding="utf8")
    show = int(os.environ.get("SHOW", "8"))
    for q in sys.argv[1:]:
        d = fts(q)
        if not d: print(repr(q), "ERR"); continue
        h = d["response"]["body"]["hits"]
        print(f"{q!r}: total {h.get('total')}", flush=True)
        for i, x in enumerate(h["hits"]):
            f = x["fields"]; sn = ((x.get("highlight") or {}).get("text") or [""])[0]
            row = {"q": q, "id": f.get("identifier"), "title": f.get("title"), "year": f.get("year") or f.get("date"), "page": f.get("page_num"), "snip": sn}
            out.write(json.dumps(row, ensure_ascii=False) + "\n")
            if i < show: print("  ", row["id"], "|", str(row["title"])[:60], "|", row["year"], "|", re.sub(r"\s+", " ", sn)[:230])
        time.sleep(2.5)
