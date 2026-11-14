"""Harvest DigitArq search hits for cipher terms, archive-scoped.
usage: harvest.py <archiveCode|ALL> term [term ...]   -> hits_<archive>.jsonl (unique ids, terms matched)
Polite: 2 s between requests, stop on 429/403. Max 2000 hits per term (fuzzy search; noise filtered later)."""
import json, sys, time, urllib.parse, urllib.request, urllib.error, pathlib
HERE = pathlib.Path(__file__).parent
BASE = "https://digitarq.arquivos.pt/api/docs/search?"
arch = sys.argv[1]; TERMS = sys.argv[2:]
OUT = HERE / f"hits_{arch}.jsonl"
CAP = 2000
def get(url):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research sweep)"}), timeout=90) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 403):
                print("STOP", e.code, file=sys.stderr); sys.exit(2)
            time.sleep(4*(i+1))
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(4*(i+1))
seen = {}
if OUT.exists():
    for l in OUT.open(encoding="utf8"):
        r = json.loads(l); seen[r["id"]] = r
for term in TERMS:
    frm = 0; total = None; n = 0
    while True:
        q = {"query": term, "fromIndex": frm, "max": 100}
        if arch != "ALL": q["archiveCode"] = arch
        d = get(BASE + urllib.parse.urlencode(q))
        if not d: break
        total = d.get("total"); res = d.get("results") or []
        for r in res:
            rec = seen.get(r["id"]) or {"id": r["id"], "ref": (r.get("referenceCode") or {}).get("value") or r.get("value"),
                "archive": r.get("archiveCode"), "level": (r.get("descriptionLevel") or {}).get("value"),
                "d1": (r.get("dateInitial") or {}).get("value"), "d2": (r.get("dateFinal") or {}).get("value"),
                "title": " | ".join(t["value"] for t in r.get("titles") or []), "files": r.get("filesCount"), "terms": []}
            if term not in rec["terms"]: rec["terms"].append(term)
            seen[r["id"]] = rec
        n += len(res); frm += len(res)
        if not res or frm >= (total or 0) or frm >= CAP: break
        time.sleep(2)
    print(f"{arch}\t{term}\ttotal={total}\tfetched={n}", flush=True)
    with OUT.open("w", encoding="utf8") as f:
        for r in seen.values(): f.write(json.dumps(r, ensure_ascii=False) + "\n")
    time.sleep(2)
