"""Manus Online: run extra cipher terms (ONLY mode) -> raw/manus_hits.json. Usage: python -I -X utf8 manus_terms.py term ..."""
import json, os, sys, time, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://manus.iccu.sbn.it/o/manus-api/titles-search-post"
P = os.path.join(HERE, "raw", "manus_hits.json")
def page(q, n, mode="ONLY"):
    body = urllib.parse.urlencode({"monocampo": q, "n": "v", "monocampo:tipo": mode, "page": n}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0"})
    time.sleep(1.1)
    return json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf8", "replace"), strict=False).get("data", {})
hits = json.load(open(P, encoding="utf8")) if os.path.exists(P) else {}
for q in sys.argv[1:]:
    try:
        r = page(q, 1)
    except Exception as e:
        print("##", q, "ERR", e); continue
    pages = min(r.get("pagination", {}).get("total", 1), 15)
    print(f"## {q}: {r.get('total')} records", flush=True)
    for n in range(1, pages + 1):
        d = r if n == 1 else page(q, n)
        for it in d.get("results", []):
            h = hits.setdefault(it["id"], {"id": it["id"], "title": it["title"]["text"], "info": it["title"].get("info"), "snippet": it.get("snippet"), "queries": []})
            if q not in h["queries"]: h["queries"].append(q)
    json.dump(hits, open(P, "w", encoding="utf8"), ensure_ascii=False)
