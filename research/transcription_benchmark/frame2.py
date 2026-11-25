"""Second round, step 1: the frame of DECODE records that have both a manual ciphertext transcription and page images
on disk (downloaded during earlier target work), with DECODE metadata from the API.

Usage:
  python frame2.py scan                -> frame2/scan.json (records, target folders, transcription files, page images)
  python frame2.py meta COOKIE_FILE    -> frame2/meta.json (DECODE API view per record: symbol sets, cipher types,
                                          century, language), polite (about 1 request per second)
"""
import collections
import glob
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / "frame2"


def classify(path):
    t = open(path, encoding="utf-8-sig", errors="replace").read(4000)
    head = t[:500].upper()
    if "#KEY" in head:
        kind = "key"
    elif "#CIPHERTEXT" in head or "#IMAGE NAME" in head:
        kind = "ciphertext"
    elif "#PLAINTEXT" in head or "#DECRYPT" in head or "#TRANSLATION" in head:
        kind = "plaintext"
    else:
        kind = "other"
    m = re.search(r"TRANSCRIPTION METHOD\s*:\s*(.*)", t, re.I)
    who = re.search(r"TRANSCRIBER NAME\s*:\s*(.*)", t, re.I)
    return kind, (m.group(1).strip()[:40] if m else ""), (who.group(1).strip()[:40] if who else "")


def scan():
    recs = collections.defaultdict(lambda: {"docs": set(), "imgs": set(), "targets": set()})
    for f in glob.glob(str(ROOT / "targets" / "**" / "DOC_R*_D*.txt"), recursive=True):
        m = re.search(r"DOC_R(\d+)_D(\d+)", os.path.basename(f))
        if m:
            p = Path(f).relative_to(ROOT).as_posix()
            recs[m.group(1)]["docs"].add(p)
            recs[m.group(1)]["targets"].add(p.split("/")[1])
    for f in glob.glob(str(ROOT / "targets" / "**" / "IMG_R*_I*_P*.*"), recursive=True):
        m = re.search(r"IMG_R(\d+)_I(\d+)_P(\d+)\.(png|jpg|jpeg)$", os.path.basename(f), re.I)
        if m and m.group(1) in recs:
            recs[m.group(1)]["imgs"].add(Path(f).relative_to(ROOT).as_posix())
    out = []
    for rec, v in sorted(recs.items(), key=lambda x: int(x[0])):
        if not v["imgs"]:
            continue
        docs = [{"file": f, "kind": k, "method": meth, "transcriber": who}
                for f in sorted(v["docs"]) for k, meth, who in [classify(ROOT / f)]]
        pages = {}
        for i in sorted(v["imgs"]):
            m = re.search(r"_I(\d+)_P(\d+)", os.path.basename(i))
            pages.setdefault(m.group(1), (int(m.group(2)), i))  # one file per image id
        out.append({"rec": rec, "targets": sorted(v["targets"]), "docs": docs,
                    "pages": [p for _, p in sorted(pages.values())]})
    OUT.mkdir(exist_ok=True)
    json.dump(out, open(OUT / "scan.json", "w"), indent=1)
    ct = [o for o in out if any(d["kind"] == "ciphertext" for d in o["docs"])]
    multi = [o for o in ct if sum(d["kind"] == "ciphertext" for d in o["docs"]) > 1]
    print("records with images:", len(out), "| with a ciphertext transcription:", len(ct),
          "| target folders:", len({t for o in ct for t in o["targets"]}))
    print("records with 2+ ciphertext transcriptions:", len(multi), [o["rec"] for o in multi])


def meta(cookie_file):
    cookie = open(cookie_file).read().strip().replace("\n", "").replace("\r", "")
    scan_ = json.load(open(OUT / "scan.json"))
    out = {}
    if (OUT / "meta.json").exists():
        out = json.load(open(OUT / "meta.json"))
    jwt = None
    for o in scan_:
        rec = o["rec"]
        if rec in out:
            continue
        if jwt is None:
            req = urllib.request.Request(f"https://de-crypt.org/decrypt-web/RecordsView/{rec}", headers={"Cookie": cookie})
            html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
            m = re.search(r'"API_JWT_TOKEN"\s*:\s*"([^"]+)"', html)
            jwt = m.group(1) if m else ""
        req = urllib.request.Request(f"https://de-crypt.org/decrypt-web/api/view/Records/{rec}",
                                     headers={"Cookie": cookie, "X-Authorization": f"Bearer {jwt}"})
        try:
            data = json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace"))
            r = data.get("Records") or data.get("records") or data
            if isinstance(r, list):
                r = r[0] if r else {}
            keep = {k: r.get(k) for k in ("name", "record_type", "status", "symbol_sets", "cipher_types",
                                          "start_year", "end_year", "language", "access_mode", "number_of_pages")}
            out[rec] = keep
        except Exception as e:
            out[rec] = {"error": str(e)[:120]}
        json.dump(out, open(OUT / "meta.json", "w"), indent=1)
        time.sleep(1.1)
    print("metadata for", len(out), "records;", sum(1 for v in out.values() if "error" in v), "errors")


if __name__ == "__main__":
    {"scan": lambda: scan(), "meta": lambda: meta(sys.argv[2])}[sys.argv[1]]()
