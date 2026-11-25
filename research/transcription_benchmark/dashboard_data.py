"""Data files for the transcription-benchmark dashboard (JSON {rows, meta}; meta carries this script).

  python dashboard_data.py -> dashboard/round2_docs.json, round2_strata.json, round1_docs.json, round1_models.json,
                              human_ceiling.json
Inputs: scores2.json, scores2_adjusted.json, frame2/sample2.json (round two); scores*.json, stats.json (round one);
human_ceiling_wide.json. Error rate = edits / reference signs.
"""
import html
import json
import random
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "dashboard"
CODE = Path(__file__).read_text(encoding="utf-8")


def meta(inputs):
    return [{"label": "dashboard_data.py", "value": CODE, "type": "code", "lang": "python"},
            {"label": "Input", "value": inputs}]


def label(group):
    g = html.unescape(group.split(":", 1)[1] if ":" in group else group).strip()
    g = re.sub(r"\s*\(.*?\)", "", g).split(",")[0].strip()
    return (g[:1].upper() + g[1:])[:42]


def boot(rows, key, n=10000, seed=20261120):
    rng = random.Random(seed)
    sig = lambda s: sum(r["ref_signs"] for r in s)
    b = sorted(sum(r[key] for r in s) / sig(s) for s in ([rng.choice(rows) for _ in rows] for _ in range(n)))
    return round(b[int(0.025 * n)], 4), round(b[int(0.975 * n) - 1], 4)


def main():
    OUT.mkdir(exist_ok=True)
    plain = {r["doc"]: r for r in json.load(open(HERE / "scores2.json"))["rows"]}
    adj = {r["doc"]: r for r in json.load(open(HERE / "scores2_adjusted.json"))["rows"]}
    smp = {"R" + x["rec"]: x for x in json.load(open(HERE / "frame2" / "sample2.json"))["sample"]}
    zoom = {"R847", "R923", "R928", "R956"}
    rows = []
    for d, a in adj.items():
        p, s = plain[d], smp[d]
        rows.append({"doc": d, "correspondence": label(s["group"]), "year": int(s["start_year"]) if str(s["start_year"]).isdigit() else None,
                     "kind": a["stratum"], "from": "corpus" if s["source"] == "disk" else "DECODE draw",
                     "signs": a["ref_signs"], "edits": a["edits"],
                     "strict": p["cer"], "order_tolerant": p["cer_order_tolerant"], "adjusted": a["cer_adjusted"],
                     "rule": ", ".join(f"{k} = {v}" for k, v in a["rules"].items()).replace("α", "'Infinity'"),
                     "enlarged_crops": d in zoom})
    rows.sort(key=lambda r: r["adjusted"])
    json.dump({"rows": rows, "meta": meta("scores2.json, scores2_adjusted.json, frame2/sample2.json")},
              open(OUT / "round2_docs.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    strata = []
    for name, sel in (("All", rows), ("Digit ciphers", [r for r in rows if r["kind"] == "digit"]),
                      ("Letter ciphers", [r for r in rows if r["kind"] == "letter"])):
        sig = sum(r["signs"] for r in sel)
        lo, hi = boot([{"ref_signs": r["signs"], "e": r["edits"]} for r in sel], "e")
        rates = sorted(r["adjusted"] for r in sel)
        strata.append({"group": name, "documents": len(sel), "signs": sig,
                       "pooled": round(sum(r["edits"] for r in sel) / sig, 4), "ci_low": lo, "ci_high": hi,
                       "median": rates[len(rates) // 2], "under_5pct": sum(x < 0.05 for x in rates),
                       "pooled_strict": round(sum(plain[r["doc"]]["edits"] for r in sel) /
                                              sum(plain[r["doc"]]["ref_signs"] for r in sel), 4)})
    json.dump({"rows": strata, "meta": meta("round2_docs rows (this script)")},
              open(OUT / "round2_strata.json", "w", encoding="utf-8"), indent=1)

    names = {"santacroce_R6": "Santacroce R6", "santacroce_R7": "Santacroce R7", "dandini_R72": "Dandini R72",
             "hellen_R1953": "Hellen R1953", "kauderbach_R2078": "Kauderbach R2078", "hellen_R1049": "Hellen R1049",
             "ferdinand_R1889": "Ferdinand R1889", "ferdinand_R1890": "Ferdinand R1890",
             "carpio_R1009": "Carpio R1009", "carpio_R1010": "Carpio R1010"}
    years = {"santacroce_R6": 1552, "santacroce_R7": 1552, "dandini_R72": 1580, "hellen_R1953": 1752,
             "kauderbach_R2078": 1754, "hellen_R1049": 1756, "ferdinand_R1889": 1635, "ferdinand_R1890": 1640,
             "carpio_R1009": 1677, "carpio_R1010": 1677}
    r1 = {}
    for model, f in (("sonnet", "scores.json"), ("opus", "scores_opus.json"), ("fable", "scores_fable.json")):
        for r in json.load(open(HERE / f)):
            r1.setdefault(r["doc"], {}).setdefault(model, []).append(r["cer"])
            r1[r["doc"]]["signs"] = r["ref_digits"]
    r1rows = [{"document": names[d], "year": years[d], "kind": "letter" if d.startswith(("carpio", "ferdinand")) else "digit",
               "signs": v["signs"], **{m: round(sum(v[m]) / len(v[m]), 4) for m in ("sonnet", "opus", "fable")}}
              for d, v in r1.items()]
    r1rows.sort(key=lambda r: r["fable"])
    json.dump({"rows": r1rows, "meta": meta("scores.json (Sonnet), scores_opus.json, scores_fable.json: mean of 3 passes")},
              open(OUT / "round1_docs.json", "w", encoding="utf-8"), indent=1)

    st = json.load(open(HERE / "stats.json"))
    mrows = [{"subset": {"all": "All 10", "digit-only": "Digit (6)", "letter-and-digit": "Letter (4)"}[k], "model": m.capitalize(),
              "pooled": v["pooled"], "ci_low": v["ci95"][0], "ci_high": v["ci95"][1]}
             for k in ("all", "digit-only", "letter-and-digit") if k in st for m, v in st[k]["models"].items()]
    json.dump({"rows": mrows, "meta": meta("stats.json (hierarchical bootstrap over documents and passes)")},
              open(OUT / "round1_models.json", "w", encoding="utf-8"), indent=1)

    hc = json.load(open(HERE / "human_ceiling_wide.json"))["rows"]  # independent pairs only (see its "excluded")
    hrows = [{"record": v["record"], "transcribers": " vs ".join(v["transcribers"]), "signs": v["signs"], "edits": v["edits"],
              "disagreement": v["disagreement"]} for v in hc if v["used"]]
    hrows.sort(key=lambda r: r["disagreement"])
    json.dump({"rows": hrows, "meta": meta("human_ceiling_wide.json (fitting alignment, two different DECODE transcribers, 16 records)")},
              open(OUT / "human_ceiling.json", "w", encoding="utf-8"), indent=1)
    print(len(rows), "round-two docs;", strata[0], "|", len(r1rows), "round-one docs;", len(mrows), "model rows;", len(hrows), "pairs")


if __name__ == "__main__":
    main()
