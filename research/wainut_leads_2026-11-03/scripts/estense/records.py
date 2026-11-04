"""Fetch Lodovico record pages for ids in a JSON list; write records.json (id -> fields)."""
import json, re, sys, html, os
from fetch import get
OUT = os.path.join(os.path.dirname(__file__), "records.json")
recs = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
def parse(b):
    b = re.sub(r"<script.*?</script>|<style.*?</style>", "", b, flags=re.S)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " | ", b)))
    t = re.sub(r"(\s*\|\s*)+", " | ", t)
    def f(lbl, stop=r" \| [A-Z][A-Z ]{3,} :"):
        m = re.search(lbl + r" :? \| (.*?)(?=" + stop + "| \| Chiudi)", t)
        return m.group(1).strip(" |") if m else ""
    d = {}
    m = re.search(r"\| DESCRIZIONE \| (.*?) \| DETTAGLI", t); d["desc"] = m.group(1) if m else ""
    for k, lbl in [("shelf", "SEGNATURA"), ("persons", "PERSONE"), ("date", "DATAZIONE"), ("place", "DATA TOPICA"), ("recipient", "DESTINATARIO"), ("lang", "LINGUA"), ("coll", "COLLEZIONE DIGITALE")]:
        d[k] = f(lbl)
    m = re.search(r"\| Lettera[^|]*|\| Manoscritto[^|]*", t); d["title"] = m.group(0).strip(" |") if m else ""
    return d
ids = json.load(open(sys.argv[1]))
for i in ids:
    if i in recs: continue
    recs[i] = parse(get("https://lodovico.medialibrary.it/media/schedadl.aspx?id=" + i))
    json.dump(recs, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(recs))
