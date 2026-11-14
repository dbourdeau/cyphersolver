"""archive.org advancedsearch on metadata. python ia_meta.py '<lucene query>' ... prints count and rows (id | year | title)"""
import sys, json, urllib.parse, urllib.request, time
for q in sys.argv[1:]:
    u = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode({"q": q, "fl[]": ["identifier","title","year","creator","mediatype"], "rows": 60, "output": "json"}, doseq=True)
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=90))
    r = d["response"]
    print(f"{q!r}: {r['numFound']}", flush=True)
    for x in r["docs"][:int(__import__('os').environ.get('SHOW','25'))]:
        print("  ", x.get("identifier"), "|", x.get("year"), "|", str(x.get("title"))[:90], "|", str(x.get("creator"))[:40])
    time.sleep(2.5)
