"""Find DECODE records transcribed by two different people (for the human-to-human ceiling).

  python scan_doubles.py scan COOKIE_FILE   -> frame2/doubles_scan.json: every ciphertext record whose page lists two or
                                              more transcription files ([transc], .txt). Resumable; ~1 request/s.
  python scan_doubles.py fetch COOKIE_FILE  -> decode_cache/doubles/<file>.txt for those records
  python scan_doubles.py compare            -> frame2/doubles_compare.json: for each record, pairs of transcriptions by
                                              different transcribers, compared by fitting alignment (the shorter
                                              stream against the best-matching stretch of the longer, which may be a
                                              bulk file covering several records); a pair counts only when the
                                              stretch length is within 15% of the shorter stream.
"""
import json
import re
import sys
import time
from pathlib import Path

import draw2
import frame2
import human_ceiling
import score

HERE = Path(__file__).resolve().parent
OUT = HERE / "frame2" / "doubles_scan.json"
CMP = HERE / "frame2" / "doubles_compare.json"
DL = HERE / "decode_cache" / "doubles"


def scan(cookie_file):
    cookie = open(cookie_file).read().strip().replace("\n", "").replace("\r", "")
    rows = [r for r in json.load(open(draw2.LIST, encoding="utf-8")) if str(r.get("record_type")) == "1"]
    state = json.load(open(OUT)) if OUT.exists() else {"criterion": 2, "done": [], "hits": {}}
    if state.get("criterion") != 2:  # v1 kept only [transc] files and missed second transcriptions filed as [dec]
        state = {"criterion": 2, "done": [], "hits": {}}
    done = set(state["done"])
    for k, r in enumerate(rows):
        if r["id"] in done:
            continue
        try:
            meta = draw2.record_page(r["id"], cookie)
            # any text file except keys: a second transcriber's ciphertext is often inside a [dec] file
            tx = {d["file"]: d["label"] for d in meta["docs"] if d["ext"] == "txt" and "[key" not in d["label"].lower()}
            if len(tx) >= 2:
                state["hits"][r["id"]] = {"files": sorted(tx), "labels": tx, "symbol_sets": meta["symbol_sets"],
                                          "images": len(meta["images"])}
        except Exception as e:
            state.setdefault("errors", {})[r["id"]] = str(e)[:80]
        state["done"].append(r["id"])
        if k % 25 == 0:
            json.dump(state, open(OUT, "w"))
            print(f"{len(state['done'])}/{len(rows)} scanned, {len(state['hits'])} with 2+ transcriptions", flush=True)
        time.sleep(1.0)
    json.dump(state, open(OUT, "w"))
    print("done:", len(state["done"]), "scanned,", len(state["hits"]), "records with 2+ transcriptions")


def fetch(cookie_file):
    cookie = open(cookie_file).read().strip().replace("\n", "").replace("\r", "")
    DL.mkdir(parents=True, exist_ok=True)
    hits = json.load(open(OUT))["hits"]
    for rec, h in hits.items():
        for f in h["files"]:
            p = DL / f
            if p.exists() and p.stat().st_size > 0:
                continue
            data = draw2.get(f"https://de-crypt.org/decrypt-custom/filesrv/?file={f}", cookie)
            if len(data) == 17947 and data[:4] == b"\x89PNG":
                continue
            p.write_bytes(data)
            time.sleep(1.5)
    print("fetched", len(list(DL.glob("*.txt"))), "files")


def header(path, field):
    t = open(path, encoding="utf-8-sig", errors="replace").read(3000)
    m = re.search(field + r"\s*:\s*(.*)", t, re.I)
    return m.group(1).strip() if m else ""


def compare():
    hits = json.load(open(OUT))["hits"]
    out = {}
    for rec, h in hits.items():
        files = [DL / f for f in h["files"] if (DL / f).exists()]
        alnum = "alphabet" in h["symbol_sets"].lower()
        streams = []
        for p in files:
            if frame2.classify(p)[0] in ("key", "plaintext"):
                continue
            who = header(p, "TRANSCRIBER NAME")
            st = score.digits("".join(score.ref_lines(str(p))), alnum=alnum)
            if st:
                streams.append((p.name, who, st))
        res = []
        for i in range(len(streams)):
            for j in range(i + 1, len(streams)):
                (na, wa, a), (nb, wb, b) = streams[i], streams[j]
                if not wa or not wb or wa.lower() == wb.lower():
                    continue
                if len(a) > len(b):
                    (na, wa, a), (nb, wb, b) = (nb, wb, b), (na, wa, a)
                if len(a) < 50 or len(a) * len(b) > 4e7:
                    continue
                e, s, t = human_ceiling.fit(a, b)
                ok = abs((t - s) - len(a)) <= 0.15 * len(a)
                res.append({"a": na, "b": nb, "transcribers": [wa, wb], "signs": len(a), "stretch": t - s,
                            "edits": e, "disagreement": round(e / len(a), 4), "used": ok})
        if res:
            out[rec] = {"symbol_sets": h["symbol_sets"], "pairs": res}
    json.dump(out, open(CMP, "w"), indent=1)
    used = [(rec, p) for rec, v in out.items() for p in v["pairs"] if p["used"]]
    best = {}
    for rec, p in used:  # one pair per record (the longest)
        if rec not in best or p["signs"] > best[rec]["signs"]:
            best[rec] = p
    if best:
        e = sum(p["edits"] for p in best.values())
        n = sum(p["signs"] for p in best.values())
        print(f"records with a usable pair by different transcribers: {len(best)}; pooled disagreement {100 * e / n:.2f}% "
              f"over {n} signs")
        rates = sorted(p["disagreement"] for p in best.values())
        print("per-record disagreement, median %.2f%%, range %.2f%% to %.2f%%" %
              (100 * rates[len(rates) // 2], 100 * rates[0], 100 * rates[-1]))


if __name__ == "__main__":
    {"scan": lambda: scan(sys.argv[2]), "fetch": lambda: fetch(sys.argv[2]), "compare": compare}[sys.argv[1]]()
