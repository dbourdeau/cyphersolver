"""Second round, step 5: score the blind passes on the drawn sample against the DECODE transcriptions.

  python score2.py OUT_DIR [PASS]  -> scores2.json (PASS default pass1)
Scoring as round one (score.py): edit distance between sign streams, separators and clear text ignored, '?' in the
hypothesis always an error. Digit stratum: digits only. Letter stratum: digits and letters (case-folded).
Pooled rate = all edits / all reference signs. 95% interval: bootstrap over documents (10,000 resamples, seed fixed),
since documents, not signs, are the sampling unit.
"""
import json
import random
import re
import sys
from pathlib import Path

import score

HERE = Path(__file__).resolve().parent


def ref_stream(path, alnum):
    """Reference sign stream. DECODE codes a mark over or under a digit as '^' plus one character (3^1, 7^~, 8^., 2^_):
    in the digit stratum that is a mark, not a sign, and is removed. In the letter stratum '^' introduces a real
    superscript number (c^227) and is kept. Stray un-hashed header labels (CIPHERTEXT2) are removed."""
    t = "".join(score.ref_lines(path))
    t = re.sub(r"CIPHERTEXT\s*\d*", "", t, flags=re.I)
    if not alnum:
        t = re.sub(r"\^\S", "", t)
    return score.digits(t, alnum=alnum)


def order_tolerant(a, hl, alnum, block=10):
    """Secondary score that forgives block order (two-page spreads transcribed right half first, pages photographed out
    of order). The hypothesis is cut into blocks of `block` lines; each block is fitted to its best-matching stretch of
    the reference (free ends); edits = sum of block edits + reference signs covered by no block (deletions)."""
    import human_ceiling
    covered = bytearray(len(a))
    edits = 0
    for i in range(0, len(hl), block):
        b = score.digits("".join(l.rstrip("! ") for l in hl[i:i + block]), keep_q=True, alnum=alnum)
        if not b:
            continue
        e, s, t = human_ceiling.fit(b, a)
        edits += e
        for k in range(s, t):
            covered[k] = 1
    return edits + covered.count(0)


def main(out_dir, pas="pass1"):
    pages = json.load(open(HERE / "frame2" / "pages2.json"))
    rows, missing = [], []
    for d, v in sorted(pages.items(), key=lambda x: int(x[0][1:])):
        hyp = Path(out_dir) / f"{pas}_{d}.txt"
        if not hyp.exists():
            missing.append(d)
            continue
        al = v["stratum"] == "letter"
        a = ref_stream(v["reference"], al)
        hl = score.hyp_lines(str(hyp))
        b = score.digits("".join(l.rstrip("! ") for l in hl), keep_q=True, alnum=al)
        s, ins, dl, e = score.lev_ops(a, b)
        eo = min(e, order_tolerant(a, hl, al))
        rows.append({"doc": d, "stratum": v["stratum"], "source": v["source"], "ref_signs": len(a), "hyp_signs": len(b),
                     "edits": e, "subs": s, "ins": ins, "dels": dl, "cer": round(e / max(1, len(a)), 4),
                     "edits_order_tolerant": eo, "cer_order_tolerant": round(eo / max(1, len(a)), 4),
                     "length_ratio": round(len(b) / max(1, len(a)), 3),
                     "flagged_lines": sum(1 for l in hl if l.rstrip().endswith("!")), "unreadable_marks": b.count("?")})
    summary = {}
    rng = random.Random(20261120)
    for name, sel in (("all", rows), ("digit", [r for r in rows if r["stratum"] == "digit"]),
                      ("letter", [r for r in rows if r["stratum"] == "letter"])):
        if not sel:
            continue
        pooled = sum(r["edits"] for r in sel) / sum(r["ref_signs"] for r in sel)
        boots = []
        for _ in range(10000):
            smp = [rng.choice(sel) for _ in sel]
            boots.append(sum(r["edits"] for r in smp) / sum(r["ref_signs"] for r in smp))
        boots.sort()
        cers = sorted(r["cer"] for r in sel)
        pooled_ot = sum(r["edits_order_tolerant"] for r in sel) / sum(r["ref_signs"] for r in sel)
        summary[name] = {"documents": len(sel), "signs": sum(r["ref_signs"] for r in sel), "pooled_cer": round(pooled, 4),
                         "ci95": [round(boots[250], 4), round(boots[9749], 4)], "median_doc_cer": cers[len(cers) // 2],
                         "pooled_cer_order_tolerant": round(pooled_ot, 4)}
    json.dump({"pass": pas, "rows": rows, "summary": summary, "missing": missing},
              open(HERE / "scores2.json", "w"), indent=1)
    for r in rows:
        print(f"{r['doc']:7} {r['stratum']:6} ref {r['ref_signs']:5} hyp {r['hyp_signs']:5} cer {100 * r['cer']:6.2f}%"
              f"  order-tolerant {100 * r['cer_order_tolerant']:6.2f}%  len {r['length_ratio']}")
    for k, v in summary.items():
        print(k, v)
    if missing:
        print("missing:", missing)


if __name__ == "__main__":
    main(sys.argv[1], *(sys.argv[2:3]))
