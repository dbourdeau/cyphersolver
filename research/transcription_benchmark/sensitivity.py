"""Check 4: how much does the setup move the score? One Fable 5.2 pass per variant on three documents, against the
spread of Fable's three baseline passes (passes_fable/, 1000-px bands, the standard prompt).

Variants (transcriptions in runs_sensitivity/): fullpage (whole page as one image), band600 (600-px bands),
reworded (baseline tiles, prompt rewritten). Scored against the original DECODE reference and against the adjudicated
reference (adjudication/verdicts.jsonl applied as in adjudicate.py).
Usage: python sensitivity.py     -> sensitivity.json
"""
import json
import os

import adjudicate as A
import score

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = ["santacroce_R7", "hellen_R1049", "carpio_R1009"]
VARIANTS = ["fullpage", "band600", "reworded"]


def adjudicated_refs():
    items = {it["id"]: it for it in json.load(open(os.path.join(A.ADJ, "items.json"), encoding="utf-8"))["items"]}
    vs = [json.loads(l) for l in open(os.path.join(A.ADJ, "verdicts.jsonl"), encoding="utf-8")]
    out = {}
    for doc in DOCS:
        ref, _, _ = A.ref_structure(doc)
        s = ref
        for a, b, ai in sorted(((items[v["id"]]["pos"][0], items[v["id"]]["pos"][1], items[v["id"]]["ai"]) for v in vs
                                if v["side"] == "ai" and items[v["id"]]["doc"] == doc), reverse=True):
            s = s[:a] + ai + s[b:]
        out[doc] = (ref, s)
    return out


def stream(doc, path):
    hl = score.hyp_lines(path)
    return score.digits("".join(l.rstrip("! ") for l in hl), keep_q=True, alnum=doc in score.ALNUM_DOCS)


def main():
    refs = adjudicated_refs()
    res = {}
    for doc in DOCS:
        ref, adj = refs[doc]
        base = [stream(doc, os.path.join(HERE, "passes_fable", f"pass{p}_{doc}.txt")) for p in (1, 2, 3)]
        e = {"baseline_orig": [round(score.lev_ops(ref, h)[3] / len(ref), 4) for h in base],
             "baseline_adj": [round(score.lev_ops(adj, h)[3] / len(adj), 4) for h in base]}
        for v in VARIANTS:
            h = stream(doc, os.path.join(HERE, "runs_sensitivity", f"{v}_{doc}.txt"))
            e[v] = {"orig": round(score.lev_ops(ref, h)[3] / len(ref), 4), "adj": round(score.lev_ops(adj, h)[3] / len(adj), 4)}
        res[doc] = e
        bo, ba = e["baseline_orig"], e["baseline_adj"]
        print(f"{doc:15s} baseline orig {100 * min(bo):.1f}-{100 * max(bo):.1f}%  adj {100 * min(ba):.1f}-{100 * max(ba):.1f}%  | "
              + "  ".join(f"{v} {100 * e[v]['orig']:.1f}%/{100 * e[v]['adj']:.1f}%" for v in VARIANTS))
    json.dump(res, open(os.path.join(HERE, "sensitivity.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
