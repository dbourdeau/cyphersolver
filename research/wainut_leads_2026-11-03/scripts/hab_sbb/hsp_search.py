"""Handschriftenportal (handschriftenportal.de) JSON search for cipher terms; keeps HAB Wolfenbuettel and SBB Berlin.
GET /api/hspobjects/search, one request at a time, 1.1 s apart, UA WAINUT-research. Stops on 403/429."""
import sys, time, json, re, urllib.request, urllib.parse
UA = {"User-Agent": "WAINUT-research"}
OUT = sys.argv[1]
TERMS = sys.argv[2:] or ["Chiffre", "Chiffren", "chiffriert", "chiffrirt", "Chiffreschrift", "Chiffernschrift", "Chiffern",
    "Zifferschrift", "Ziffernschrift", "Ziffernbrief", "Geheimschrift", "Geheimalphabet", "Geheimschriften", "dechiffriert",
    "Dechiffrierung", "Dechiffrement", "Chiffrenschlüssel", "Chiffrierschlüssel", "cifra", "cifre", "\"en chiffre\"",
    "chiffré", "dechiffré", "Nomenklator", "nomenclator", "Geheimzeichen", "Kryptogramm", "Geheimcode", "Ziffernalphabet"]
KEEP = ("Herzog August Bibliothek", "Staatsbibliothek zu Berlin")
res, log = {}, []
def get(params):
    url = "https://handschriftenportal.de/api/hspobjects/search?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return json.load(r)
for term in TERMS:
    start = 0
    while True:
        try:
            d = get({"q": term, "start": start, "rows": 100, "sort": "score-desc", "fq": "{}", "hl": "true", "isExtended": "false"})
        except urllib.error.HTTPError as e:
            print("HTTP", e.code, term); 
            if e.code in (403, 429): json.dump(list(res.values()), open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1); sys.exit(1)
            break
        md = d["metadata"]; hl = md.get("highlighting", {})
        kept = 0
        for p in d["payload"]:
            o = p["hspObject"]
            if o.get("repository-display") not in KEEP: continue
            kept += 1
            r = res.setdefault(o["id"], {"id": o["id"], "terms": [], "hl": []})
            r["terms"].append(term)
            r.update({"repo": o.get("repository-display"), "idno": o.get("idno-display"), "title": o.get("title-display"),
                      "date": o.get("orig-date-lang-display"), "url": o.get("persistent-url-display"),
                      "digitized": [x.get("manifest-url-display") or x.get("id") for x in p.get("hspDigitizeds", [])],
                      "digi_raw": p.get("hspDigitizeds", [])[:2]})
            for x in [o["id"]] + [x["id"] for x in p.get("hspDescriptions", [])]:
                for k, v in hl.get(x, {}).items():
                    for s in v:
                        s = re.sub(r"\s+", " ", s)
                        if s not in r["hl"]: r["hl"].append(s)
        log.append((term, start, md["numFound"], kept))
        print(term, start, md["numFound"], "kept", kept, flush=True)
        start += 100
        time.sleep(1.1)
        if start >= md["numFound"] or start >= 1500: break
json.dump(list(res.values()), open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(log, open(OUT + ".log.json", "w"), ensure_ascii=False)
print("kept", len(res))
