"""Summarise the saved DECODE views (decode/view*.json) into decode_records.tsv."""
import os, re, json, glob, html
HERE = os.path.dirname(os.path.abspath(__file__))
rows = []
for p in glob.glob(os.path.join(HERE, "decode", "view*.json")):
    r = json.load(open(p, encoding="utf-8"))["records"]
    t = open(p.replace("view", "rec").replace(".json", ".htm"), encoding="utf-8", errors="replace").read()
    nimg = len(set(re.findall(r"TH_(IMG_[A-Za-z0-9_.]+)", t)))
    info = html.unescape(re.sub(r"<[^>]+>", " ", r.get("additional_information") or ""))
    info = re.sub(r"\s+", " ", info.replace("The image is not in the public domain. Publishing it is only possible with the permission of the Library.", "")).strip()
    au = re.sub(r"<[^>]+>", " ", r.get("c_author") or ""); au = re.sub(r"\s+", " ", au).strip()
    rows.append((int(r["id"]), {"1": "CT", "2": "KEY"}.get(r["record_type"], r["record_type"]), r["status"], r["current_holder"],
                 "%s-%s-%s" % (r.get("start_year"), r.get("start_month"), r.get("start_day")), r.get("end_year") or "",
                 au, r.get("cipher_types") or "", r.get("symbol_sets") or "", r.get("private_ciphertext") or "", nimg, info[:300]))
rows.sort()
with open(os.path.join(HERE, "decode_records.tsv"), "w", encoding="utf-8") as f:
    f.write("rec\ttype\tstatus\tholder\tstart\tend\tauthor\tcipher_types\tsymbols\tprivate\timgs\tinfo\n")
    for r in rows: f.write("\t".join(map(str, r)) + "\n")
print(len(rows))
