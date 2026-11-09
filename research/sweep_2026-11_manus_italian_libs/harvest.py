"""Manus Online harvest: all pages of each query (ONLY mode) -> _dl/hits.json {id:{id,title,info,snippet,queries}}."""
import json, os, sys, time, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://manus.iccu.sbn.it/o/manus-api/titles-search-post"
P = os.path.join(HERE, "_dl", "hits.json")
def page(q, mode, n):
    body = urllib.parse.urlencode({"monocampo": q, "n": "v", "monocampo:tipo": mode, "page": n}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0"})
    for k in range(3):
        try:
            time.sleep(1.0)
            return json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf8", "replace"), strict=False)
        except Exception as e:
            print("retry", k, e, file=sys.stderr); time.sleep(8)
    return {}
QS = sys.argv[1:]
hits = json.load(open(P, encoding="utf8")) if os.path.exists(P) else {}
for q in QS:
    r = page(q, "ONLY", 1).get("data", {})
    pages = r.get("pagination", {}).get("total", 1)
    print(f"## {q}: {r.get('total')} records, {pages} pages", flush=True)
    for n in range(1, pages + 1):
        d = r if n == 1 else page(q, "ONLY", n).get("data", {})
        for it in d.get("results", []):
            h = hits.setdefault(it["id"], {"id": it["id"], "title": it["title"]["text"], "info": it["title"].get("info"), "snippet": it.get("snippet"), "queries": []})
            if q not in h["queries"]: h["queries"].append(q)
        if n % 10 == 0: json.dump(hits, open(P, "w", encoding="utf8"), ensure_ascii=False)
    json.dump(hits, open(P, "w", encoding="utf8"), ensure_ascii=False)
    print("   stored", len(hits), flush=True)
