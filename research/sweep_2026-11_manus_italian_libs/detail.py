"""Fetch Manus detail records for harvested ids, append to _dl/detail.jsonl {id, text}. Priority: specific-term hits, then cifra, then cifre."""
import json, os, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
hits = json.load(open(os.path.join(HERE, "_dl", "hits.json"), encoding="utf8"))
OUT = os.path.join(HERE, "_dl", "detail.jsonl")
done = set()
if os.path.exists(OUT):
    for l in open(OUT, encoding="utf8"):
        try: done.add(json.loads(l)["id"])
        except Exception: pass
def prio(h):
    q = set(h["queries"])
    if q - {"cifra", "cifre"}: return 0
    if "cifra" in q: return 1
    return 2
def strings(o, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("href", "icon", "linkType", "type", "id", "status", "hasMore", "src", "alt"): continue
            strings(v, acc)
    elif isinstance(o, list):
        for v in o: strings(v, acc)
    elif isinstance(o, str) and o.strip(): acc.append(o.strip())
ids = sorted((k for k in hits if k not in done), key=lambda k: prio(hits[k]))
print("to fetch", len(ids), flush=True)
f = open(OUT, "a", encoding="utf8")
for i, k in enumerate(ids):
    u = f"https://manus.iccu.sbn.it/o/manus-api/title?id={k}"
    for a in range(3):
        try:
            time.sleep(1.0)
            j = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0", "X-Requested-With": "XMLHttpRequest"}), timeout=60).read().decode("utf8", "replace"), strict=False)
            acc = []; strings(j.get("data", {}), acc)
            f.write(json.dumps({"id": k, "text": " || ".join(acc)}, ensure_ascii=False) + "\n"); f.flush(); break
        except Exception as e:
            time.sleep(6)
    if i % 200 == 0: print(i, flush=True)
