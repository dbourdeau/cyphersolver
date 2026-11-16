"""Fetch full DigitArq records for ids in a hits file -> details.jsonl (incremental). usage: details.py hits_X.jsonl [filter-substring-of-ref ...]"""
import json, sys, time, urllib.request, urllib.error, pathlib
HERE = pathlib.Path(__file__).parent
hits = [json.loads(l) for l in open(sys.argv[1], encoding="utf8")]
if len(sys.argv) > 2:
    hits = [h for h in hits if any(s in h["ref"] for s in sys.argv[2:])]
OUT = HERE / "details.jsonl"
done = {json.loads(l)["id"] for l in OUT.open(encoding="utf8")} if OUT.exists() else set()
v = lambda x: (x or {}).get("value") if isinstance(x, dict) else None
for h in hits:
    if h["id"] in done: continue
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request("https://digitarq.arquivos.pt/api/docs/details/" + h["id"], headers={"User-Agent": "Mozilla/5.0 (research sweep)"}), timeout=90))
    except urllib.error.HTTPError as e:
        if e.code in (429, 403): print("STOP", e.code); sys.exit(2)
        print("err", h["ref"], e); time.sleep(3); continue
    except Exception as e:
        print("err", h["ref"], e); time.sleep(3); continue
    rec = {"id": d["id"], "ref": v(d.get("referenceCode")) or d.get("value"), "level": v(d.get("descriptionLevel")),
           "d1": v(d.get("dateInitial")), "d2": v(d.get("dateFinal")), "titles": [t.get("value") for t in d.get("titles") or []],
           "description": v(d.get("description")), "history": v(d.get("history")), "quota": [i.get("value") for i in d.get("identifiers") or []],
           "languages": [l.get("value") for l in d.get("languages") or []], "hasImages": d.get("hasImages"),
           "nrep": (d.get("relatedRepresentations") or {}).get("total"), "parent": v(d.get("parent")),
           "root": v(d.get("rootParent")), "physLoc": d.get("physLoc"), "typology": [t.get("value") for t in d.get("typology") or []],
           "subject": [t.get("value") for t in d.get("subject") or []], "writing": [t.get("value") for t in d.get("writing") or []],
           "places": str(d.get("relatedPlaces"))[:300], "actors": str(d.get("relatedActors"))[:300]}
    with OUT.open("a", encoding="utf8") as f: f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    time.sleep(2.5)
