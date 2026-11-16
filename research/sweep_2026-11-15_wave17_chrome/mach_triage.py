"""Triage all Carte Machiavelli hits in raw/manus_hits.json: cipher sentence, decipherment words, bibliography, summary."""
import json, os, re, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "raw", "manus_detail")
h = json.load(open(os.path.join(HERE, "raw", "manus_hits.json"), encoding="utf8"))
def strings(o, out):
    if isinstance(o, dict):
        for v in o.values(): strings(v, out)
    elif isinstance(o, list):
        for v in o: strings(v, out)
    elif isinstance(o, str): out.append(o)
rows = []
for k, v in h.items():
    if "Machiavelli" not in v["title"]: continue
    p = os.path.join(D, k + ".json")
    if not os.path.exists(p):
        time.sleep(1.1)
        req = urllib.request.Request("https://manus.iccu.sbn.it/o/manus-api/title?id=" + k, headers={"User-Agent": "Mozilla/5.0", "X-Requested-With": "XMLHttpRequest"})
        open(p, "wb").write(urllib.request.urlopen(req, timeout=60).read())
    out = []; strings(json.load(open(p, encoding="utf8"), strict=False), out)
    out = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)) for s in out]
    full = " ¦ ".join(out)
    shelf = v["title"].split("Machiavelli ")[-1]
    ciph = "; ".join(sorted({m.group(0)[:160] for m in re.finditer(r"[^.¦]*(?<!de)cifr[^.¦]*", full)}))[:420]
    bib = re.search(r"Bibliografia:([^¦]{0,160})", full)
    date = re.search(r"1[45]\d\d-\d\d-\d\d", full)
    rows.append((shelf, date.group(0) if date else "?", ciph, bib.group(1).strip()[:120] if bib else "NO BIBL"))
for r in sorted(rows): print(" | ".join(r))
