"""Human-to-human disagreement: records transcribed independently by two DECODE transcribers.

The second transcription is often part of a bulk file covering several records, so the comparison is a fitting
alignment: the best-matching stretch of the bulk stream (free leading and trailing characters) against the whole
single-record stream. Disagreement = edits / length of the single-record stream, on digits only (all four are digit
ciphers). A pair is used only if the fitted stretch is close in length to the single record (within 15%), which
guards against matching the wrong record.
Usage: python human_ceiling.py  -> human_ceiling.json
"""
import json
from pathlib import Path

import score

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
PAIRS = {  # record: (single-record transcription D-id, other transcriber's D-id), transcribers differ
    "72": ("1824", "3191"),
    "197": ("1659", "3237"),
    "198": ("1660", "3238"),
    "199": ("1661", "3240"),
}


def fit(a, b):
    """Edits to turn a into the best-matching substring of b; returns (edits, b_start, b_end)."""
    n, m = len(a), len(b)
    prev = [0] * (m + 1)  # free start in b
    start = list(range(m + 1))
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        cst = [0] * (m + 1)
        ai = a[i - 1]
        for j in range(1, m + 1):
            d = prev[j - 1] + (ai != b[j - 1])
            u = prev[j] + 1
            l = cur[j - 1] + 1
            if d <= u and d <= l:
                cur[j], cst[j] = d, start[j - 1]
            elif u <= l:
                cur[j], cst[j] = u, start[j]
            else:
                cur[j], cst[j] = l, cst[j - 1]
        prev, start = cur, cst
    j = min(range(m + 1), key=lambda k: prev[k])  # free end in b
    return prev[j], start[j], j


def main():
    scan = {o["rec"]: o for o in json.load(open(HERE / "frame2" / "scan.json"))}
    out = {}
    for rec, (da, db) in PAIRS.items():
        docs = scan[rec]["docs"]
        fa = next(d for d in docs if f"_D{da}_" in d["file"])
        fb = next(d for d in docs if f"_D{db}_" in d["file"])
        a = score.digits("".join(score.ref_lines(fa["file"])))
        b = score.digits("".join(score.ref_lines(fb["file"])))
        e, s, t = fit(a, b)
        ok = abs((t - s) - len(a)) <= 0.15 * len(a)
        out[rec] = {"transcribers": [fa["transcriber"], fb["transcriber"]], "signs": len(a), "matched_stretch": t - s,
                    "edits": e, "disagreement": round(e / len(a), 4), "used": ok}
        print(f"R{rec}: {fa['transcriber']} vs {fb['transcriber']}  {len(a)} signs, stretch {t - s}, edits {e}, "
              f"disagreement {100 * e / len(a):.2f}%  {'used' if ok else 'NOT used (stretch length mismatch)'}")
    used = [v for v in out.values() if v["used"]]
    if used:
        tot = sum(v["edits"] for v in used) / sum(v["signs"] for v in used)
        print(f"pooled human-human disagreement over {len(used)} records: {100 * tot:.2f}%")
    json.dump(out, open(HERE / "human_ceiling.json", "w"), indent=1)


if __name__ == "__main__":
    import os
    os.chdir(ROOT)
    main()
