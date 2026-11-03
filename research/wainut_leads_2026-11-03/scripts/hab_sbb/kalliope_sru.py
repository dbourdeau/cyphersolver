"""Kalliope SRU sweep: cipher terms, keep records held by HAB Wolfenbuettel or Staatsbibliothek zu Berlin.
One request at a time, 1.1 s apart, UA WAINUT-research. Stops on 429/403."""
import sys, time, json, urllib.request, urllib.parse, xml.etree.ElementTree as ET
UA = {"User-Agent": "WAINUT-research"}
NS = {"srw": "http://www.loc.gov/zing/srw/", "m": "http://www.loc.gov/mods/v3"}
TERMS = sys.argv[2:] or ["chiffr*", "Chiffre", "Chiffern", "Ziffer", "Ziffern", "Zifferschrift", "Geheimschrift",
         "dechiffr*", "Dechiffrierung", "Chiffrenschlüssel", "cifra", "\"en chiffre\"", "chiffré", "verschlüsselt", "Geheimschrift*"]
OUT = sys.argv[1]
KEEP = ("herzog august", "staatsbibliothek zu berlin", "staatsbibliothek berlin")
seen = {}
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()
def txt(el):
    return " ".join("".join(el.itertext()).split()) if el is not None else ""
for term in TERMS:
    start, total = 1, None
    while True:
        q = urllib.parse.urlencode({"version": "1.2", "operation": "searchRetrieve", "query": term,
                                    "maximumRecords": 100, "startRecord": start, "recordSchema": "mods"})
        try:
            data = get("https://kalliope-verbund.info/sru?" + q)
        except urllib.error.HTTPError as e:
            print("HTTP", e.code, term, start); sys.exit(1) if e.code in (403, 429) else None; break
        root = ET.fromstring(data)
        total = int(root.findtext("srw:numberOfRecords", "0", NS))
        recs = root.findall(".//m:mods", NS)
        for m in recs:
            src = txt(m.find("m:recordInfo/m:recordContentSource", NS))
            loc = " | ".join(txt(x) for x in m.findall(".//m:location/m:physicalLocation", NS))
            hay = (src + " " + loc).lower()
            rid = m.findtext("m:recordInfo/m:recordIdentifier", "", NS)
            if not any(k in hay for k in KEEP):
                continue
            rec = seen.setdefault(rid, {"id": rid, "terms": []})
            rec["terms"].append(term)
            rec.update({
                "src": src, "loc": loc,
                "shelf": " | ".join(txt(x) for x in m.findall(".//m:location/m:shelfLocator", NS)),
                "title": " | ".join(txt(x) for x in m.findall("m:titleInfo/m:title", NS)),
                "parent": " | ".join(txt(x) for x in m.findall("m:relatedItem/m:titleInfo/m:title", NS)),
                "names": " ; ".join(txt(x) for x in m.findall("m:name", NS))[:400],
                "date": " ".join(txt(x) for x in m.findall("m:originInfo/*", NS))[:120],
                "place": txt(m.find("m:originInfo/m:place", NS)),
                "notes": " | ".join(txt(x) for x in m.findall("m:note", NS))[:1200],
                "phys": txt(m.find("m:physicalDescription", NS))[:300],
                "urls": [x.text for x in m.findall(".//m:location/m:url", NS)],
                "lang": txt(m.find("m:language", NS)),
            })
        print(term, start, total, len(recs), "kept so far", len(seen), flush=True)
        start += 100
        time.sleep(1.1)
        if start > total or not recs or start > 2000:
            break
json.dump(list(seen.values()), open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("kept", len(seen))
