"""Finna API sweep: terms x archive/manuscript/letter formats, year <= 1950. usage: python3 finna.py <out.jsonl>"""
import sys, json, time, urllib.request, urllib.parse
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/126.0 Safari/537.36"}
TERMS = ["salakirjoitus", "salakirjoituksella", "salakirjoitettu", "salakirjoitusavain", "salakieli", "kryptattu", "chiffer", "chiffre", "chiffré", "chifferbrev",
         "chifferskrift", "chiffernyckel", "chiffrerad", "chiffrerat", "chiffrerade", "lönnskrift", "\"hemlig skrift\"", "\"i chiffer\"", "\"en chiffre\"", "\"en chiffres\"",
         "ziffer", "chiffren", "Geheimschrift", "cipher", "cypher", "cifra", "dechiffrerad", "dechiffrering", "шифр", "шифрованный", "цифирь", "\"i siffror\"", "sifferskrift", "koodi salakirjoitus", "salakirjain", "salakirjaimin", "tolkad chiffer", "nyckel chiffer", "chiffre-clef", "krypto"]
FIELDS = ["id", "title", "year", "formats", "buildings", "summary", "nonPresenterAuthors", "hierarchyParentTitle", "identifierString", "images", "onlineUrls", "physicalDescriptions", "generalNotes", "humanReadablePublicationDates", "collections", "institutions", "hierarchyTopTitle", "rawData"]
def q(term, page, extra):
    p = [("lookfor", term), ("type", "AllFields"), ("limit", "100"), ("page", str(page))] + [("field[]", f) for f in FIELDS if f != "rawData"] + extra
    u = "https://api.finna.fi/v1/search?" + urllib.parse.urlencode(p)
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
seen = set()
with open(sys.argv[1], "w") as f:
    for t in TERMS:
        for fmt in ["0/Document/", "0/Manuscript/", "0/Letter/", "0/OtherText/", "0/Other/"]:
            extra = [("filter[]", 'format:"%s"' % fmt), ("filter[]", 'search_daterange_mv:"[-2000 TO 1950]"')]
            page = 1; tot = 0
            while True:
                try: d = q(t, page, extra)
                except Exception as e: print("err", t, fmt, e); break
                tot = d.get("resultCount", 0)
                for r in d.get("records", []):
                    if r["id"] not in seen:
                        seen.add(r["id"]); r["_term"] = t; f.write(json.dumps(r, ensure_ascii=False) + "\n")
                time.sleep(1.2)
                if page * 100 >= min(tot, 1500): break
                page += 1
            if tot: print(t, fmt, tot, flush=True)
