"""Manus Online (ICCU) harvest, all cities. POST /o/manus-api/titles-search-post. Saves _dl/manus_all.json {id: {...}}.
Usage: python manus_all.py "<query>" [AND|ONLY|OR]"""
import json, os, sys, time, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://manus.iccu.sbn.it/o/manus-api/titles-search-post"
def page(q, mode, n):
    body = urllib.parse.urlencode({"monocampo": q, "n": "v", "monocampo:tipo": mode, "page": n}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0"})
    for k in range(3):
        try:
            time.sleep(1.2)
            return json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf8", "replace"), strict=False)
        except Exception as e:
            print("retry", k, e, file=sys.stderr); time.sleep(8)
    return {}
def main():
    q = sys.argv[1]; mode = sys.argv[2] if len(sys.argv) > 2 else "AND"
    path = os.path.join(HERE, "_dl", "manus_all.json")
    hits = json.load(open(path, encoding="utf8")) if os.path.exists(path) else {}
    r = page(q, mode, 1); d = r.get("data", {})
    pages = d.get("pagination", {}).get("total", 1); total = d.get("total")
    print(f"## {q} [{mode}]: {total} records, {pages} pages", flush=True)
    for n in range(1, min(pages, 60) + 1):
        if n > 1: d = page(q, mode, n).get("data", {})
        for it in d.get("results", []):
            h = hits.setdefault(it["id"], {"id": it["id"], "title": it["title"]["text"], "info": it["title"].get("info"), "queries": []})
            if q not in h["queries"]: h["queries"].append(q)
    json.dump(hits, open(path, "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print("   total stored", len(hits))
if __name__ == "__main__":
    main()
