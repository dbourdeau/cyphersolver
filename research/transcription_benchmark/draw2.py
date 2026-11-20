"""Second round, step 2: draw the ~50-document sample, one document per correspondence.

Sources: (a) the on-disk pool (frame2/scan.json: one record per target folder, Balbases and Carpio counted as one
series); (b) a random draw from DECODE's 3,692 ciphertext records (research/catalogue_harvest/decode/list.json).
A correspondence is the DECODE author field (sender/recipient) when filled, else the holder shelfmark without folio.
Kept: a manual transcription file labelled [transc] on the record page, page images, symbol set Numerical and/or
Alphabet (records with Graphic signs are excluded: their sign labels are transcriber-specific), at most 4 pages.
Strata: 'letter' if the symbol set includes Alphabet, else 'digit'. Fixed seed; the order of checking is the shuffled
list, so the draw is reproducible.

Usage:
  python draw2.py draw COOKIE_FILE [--digit 30] [--letter 20]   -> frame2/sample2.json
  python draw2.py fetch COOKIE_FILE                             -> decode_cache/R<rec>/ (transcription + images)
"""
import argparse
import html as htmlmod
import json
import random
import re
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / "frame2"
CACHE = HERE / "decode_cache"
LIST = ROOT / "research" / "catalogue_harvest" / "decode" / "list.json"
SEED = 20261120
SAME_SERIES = {"balbases1677": "carpio1677"}


def get(url, cookie):
    req = urllib.request.Request(url, headers={"Cookie": cookie})
    return urllib.request.urlopen(req, timeout=90).read()


def strip(s):
    return re.sub(r"\s+", " ", htmlmod.unescape(re.sub(r"<[^>]*>", " ", s or ""))).strip()


def group_of(row):
    a = strip(row.get("c_author"))
    if a:
        return "author:" + a.lower()
    m = re.search(r"<small>(.*?)</small>", row.get("c_holder") or "", flags=re.S)
    shelf = strip(m.group(1) if m else row.get("c_holder"))
    shelf = re.sub(r"[\s,;.]*(f{1,2}\.?|fol\.?|c\.)?\s*\d+[rv]?(\s*[-–]\s*\d+[rv]?)?\s*$", "", shelf, flags=re.I)
    return "shelf:" + shelf.lower()


# v1 grouped by the exact author string, which let one person in through several spellings (Pallotto x4, Papai x3 ...).
# A correspondence is now a person or series, by this ordered alias table (first match wins); unmatched groups stay as is.
PERSONS = [
    (r"pallotto", "pallotto"), (r"r.k.czi|cesoni|sylver", "rakoczi"), (r"p.pai", "papai"), (r"andr.s bay", "bay"),
    (r"alessandrino", "alessandrino"), (r"ronquillo", "ronquillo"), (r"balbases|carpio|fuenmayor", "carpio-series"),
    (r"ferdinand", "ferdinand-series"), (r"van reede", "vanreede"), (r"schimmelpenninck", "schimmelpenninck"),
    (r"hellen", "hellen"), (r"henrietta", "henrietta-maria"), (r"constantin.*envoys", "constantinople-envoys"),
    (r"affry", "affry"), (r"michell", "michell"), (r"ormanetto", "ormanetto"), (r"bergamo", "bergamo"),
    (r"kauderbach", "kauderbach"), (r"acciaiuoli", "acciaiuoli"), (r"santa ?croce|s croce", "santacroce"),
    (r"chiffrenschl.ssel", "hhsta-chiffrenschluessel"), (r"wessel.nyi", "wesselenyi"), (r"horv.th", "horvath"),
]


def person_key(group):
    for pat, key in PERSONS:
        if re.search(pat, group):
            return "person:" + key
    return group


def record_page(rec, cookie):
    h = get(f"https://de-crypt.org/decrypt-web/RecordsView/{rec}", cookie).decode("utf-8", "replace")
    flat = h.replace("\r", "").replace("\n", "")

    def field(name):
        m = re.search(r'id="el_records_' + name + r'">(.*?)</span>\s*</td>', flat)
        return strip(m.group(1)) if m else ""
    docs = []
    for m in re.finditer(r"(DOC_R" + rec + r"_D\d+_\d+\.(\w+))'[^>]*>((?:<[^>]*>)*)([^<]*)", flat):
        docs.append({"file": m.group(1), "ext": m.group(2), "label": strip(m.group(4))})
    imgs = sorted(set(re.findall(r"TH_(IMG_R" + rec + r"_I\d+_P\d+\.(?:jpg|png|jpeg))", flat)),
                  key=lambda x: int(re.search(r"_P(\d+)", x).group(1)))
    return {"symbol_sets": field("symbol_sets"), "cipher_types": field("cipher_types"), "pages": field("number_of_pages"),
            "start_year": field("start_year"), "end_year": field("end_year"), "status": field("status"),
            "docs": docs, "images": imgs}


def acceptable(meta):
    ss = meta["symbol_sets"].lower()
    transc = [d for d in meta["docs"] if d["ext"] == "txt" and "[transc]" in d["label"].lower()]
    if not transc or not meta["images"]:
        return None, "no transcription or images"
    if "graphic" in ss or not ("numerical" in ss or "alphabet" in ss):
        return None, f"symbol set '{meta['symbol_sets']}'"
    try:
        if int(meta["pages"] or len(meta["images"])) > 4:
            return None, "more than 4 pages"
    except ValueError:
        pass
    return ("letter" if "alphabet" in ss else "digit"), transc[0]["file"]


def draw(cookie_file, n_digit, n_letter):
    cookie = open(cookie_file).read().strip().replace("\n", "").replace("\r", "")
    rows = {r["id"]: r for r in json.load(open(LIST, encoding="utf-8"))}
    scan = json.load(open(OUT / "scan.json"))
    rng = random.Random(SEED)
    sample, used_groups, log = [], set(), []
    # (a) on-disk pool, one record per target folder
    by_target = {}
    for o in scan:
        if not any(d["kind"] == "ciphertext" for d in o["docs"]) or len(o["pages"]) > 4:
            continue
        t = SAME_SERIES.get(o["targets"][0], o["targets"][0])
        by_target.setdefault(t, []).append(o)
    quota = {"digit": n_digit, "letter": n_letter}
    for t in sorted(by_target):
        o = rng.choice(by_target[t])
        meta = record_page(o["rec"], cookie)
        time.sleep(1.1)
        stratum, why = acceptable(meta)
        g = group_of(rows.get(o["rec"], {}))
        used_groups.add(g)
        used_groups.add("target:" + t)
        if stratum is None:
            log.append({"rec": o["rec"], "source": "disk", "rejected": why})
            continue
        doc = next(d["file"] for d in o["docs"] if d["kind"] == "ciphertext")
        sample.append({"rec": o["rec"], "source": "disk", "target": t, "group": g, "stratum": stratum, "transcription": doc,
                       "images": o["pages"], **{k: meta[k] for k in ("symbol_sets", "cipher_types", "start_year", "end_year")}})
        quota[stratum] -= 1
    # (b) DECODE draw
    cands = [r for r in rows.values() if str(r.get("record_type")) == "1"]
    rng.shuffle(cands)
    checked = 0
    for r in cands:
        if quota["digit"] <= 0 and quota["letter"] <= 0:
            break
        g = group_of(r)
        if g in used_groups or g == "author:":
            continue
        checked += 1
        try:
            meta = record_page(r["id"], cookie)
        except Exception as e:
            log.append({"rec": r["id"], "error": str(e)[:80]})
            continue
        finally:
            time.sleep(1.1)
        stratum, why = acceptable(meta)
        if stratum is None:
            log.append({"rec": r["id"], "rejected": why})
            continue
        if quota[stratum] <= 0:
            log.append({"rec": r["id"], "rejected": f"{stratum} quota full"})
            continue
        used_groups.add(g)
        sample.append({"rec": r["id"], "source": "decode", "group": g, "stratum": stratum, "transcription": why,
                       "images": meta["images"], **{k: meta[k] for k in ("symbol_sets", "cipher_types", "start_year", "end_year")}})
        quota[stratum] -= 1
        json.dump({"seed": SEED, "sample": sample, "log": log}, open(OUT / "sample2.json", "w"), indent=1)
    json.dump({"seed": SEED, "checked_decode_candidates": checked, "sample": sample, "log": log},
              open(OUT / "sample2.json", "w"), indent=1)
    print("sample:", len(sample), {s: sum(1 for x in sample if x["stratum"] == s) for s in ("digit", "letter")},
          "| from disk", sum(1 for x in sample if x["source"] == "disk"), "| DECODE candidates checked", checked)


def redraw(cookie_file, n_digit):
    """Dedupe the v1 draw by person_key (keep the first: disk records, then DECODE in drawn order), then refill the digit
    stratum from the candidates v1 passed over as 'digit quota full', in their shuffled order. The letter stratum
    cannot be refilled: v1 exhausted it. v1 is kept as sample2_v1.json."""
    cookie = open(cookie_file).read().strip().replace("\n", "").replace("\r", "")
    v1p = OUT / "sample2_v1.json"
    if not v1p.exists():
        v1p.write_text((OUT / "sample2.json").read_text())
    v1 = json.load(open(v1p))
    rows = {r["id"]: r for r in json.load(open(LIST, encoding="utf-8"))}
    keep, used, dropped = [], set(), []
    for x in v1["sample"]:
        k = person_key(x["group"])
        if k in used:
            dropped.append({"rec": x["rec"], "dropped_as_duplicate_of": k})
            continue
        used.add(k)
        x["person"] = k
        keep.append(x)
    n = sum(1 for x in keep if x["stratum"] == "digit")
    added = []
    for e in v1["log"]:
        if n >= n_digit:
            break
        if not e.get("rejected", "").startswith("digit quota"):
            continue
        k = person_key(group_of(rows[e["rec"]]))
        if k in used or k == "author:":
            continue
        meta = record_page(e["rec"], cookie)
        time.sleep(1.1)
        stratum, why = acceptable(meta)
        if stratum != "digit":
            continue
        used.add(k)
        keep.append({"rec": e["rec"], "source": "decode", "group": group_of(rows[e["rec"]]), "person": k,
                     "stratum": stratum, "transcription": why, "images": meta["images"], "refill": True,
                     **{f: meta[f] for f in ("symbol_sets", "cipher_types", "start_year", "end_year")}})
        added.append(e["rec"])
        n += 1
    json.dump({"seed": SEED, "version": 2, "dedupe": dropped, "refill": added, "sample": keep, "log": v1["log"]},
              open(OUT / "sample2.json", "w"), indent=1)
    print("kept", len(keep), {s: sum(1 for x in keep if x["stratum"] == s) for s in ("digit", "letter")},
          "| dropped", [d["rec"] for d in dropped], "| refilled", added)


def fetch(cookie_file):
    cookie = open(cookie_file).read().strip().replace("\n", "").replace("\r", "")
    s = json.load(open(OUT / "sample2.json"))["sample"]
    for x in s:
        if x["source"] != "decode":
            continue
        d = CACHE / f"R{x['rec']}"
        d.mkdir(parents=True, exist_ok=True)
        for name in [x["transcription"]] + x["images"]:
            p = d / name
            if p.exists() and p.stat().st_size > 20000 or (p.exists() and name.endswith(".txt") and p.stat().st_size > 0):
                continue
            data = get(f"https://de-crypt.org/decrypt-custom/filesrv/?file={name}", cookie)
            if len(data) == 17947 and data[:4] == b"\x89PNG":
                print("forbidden placeholder:", name)
                continue
            p.write_bytes(data)
            time.sleep(2)
        print("R" + x["rec"], "ok")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("step", choices=["draw", "redraw", "fetch"])
    ap.add_argument("cookie")
    ap.add_argument("--digit", type=int, default=30)
    ap.add_argument("--letter", type=int, default=20)
    a = ap.parse_args()
    {"draw": lambda: draw(a.cookie, a.digit, a.letter), "redraw": lambda: redraw(a.cookie, a.digit),
     "fetch": lambda: fetch(a.cookie)}[a.step]()
