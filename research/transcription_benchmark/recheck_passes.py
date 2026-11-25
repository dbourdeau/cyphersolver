"""Re-check, part B: fresh blind passes against the corpus's own model-made transcriptions (and DECODE's human one
where it exists). Digit streams; disagreement = edit distance / length of our stream.
Usage: python recheck_passes.py PASS_DIR -> recheck_passes.json"""
import glob
import json
import re
import sys
from pathlib import Path

import score
import score2

HERE = Path(__file__).resolve().parent
T = HERE.parent.parent / "targets"


def ours_plain(pattern):
    s = ""
    for f in sorted(glob.glob(str(T / pattern))):
        for l in open(f, encoding="utf-8", errors="replace"):
            if l.lstrip().startswith("#"):
                continue
            s += re.sub(r"<[^>]*>", " ", l)
    return score.digits(s)


def ours_c_lines(name):  # turculet files: 'L1 C: tokens   (comment)'
    s = ""
    for l in open(T / name, encoding="utf-8", errors="replace"):
        m = re.match(r"\s*(?:L\d+\w?\s+)?C:\s*(.*)", l)
        if m:
            s += re.sub(r"\([^)]*\)?", "", m.group(1)) + " "  # notes in brackets, wherever they sit in the line
    return score.digits(s)


DOCS = {"R740": (lambda: ours_plain("papai1706/R740_transcription.txt"), None),
        "R7481": (lambda: ours_c_lines("turculet1709/R7481.txt"), None),
        "R7482": (lambda: ours_c_lines("turculet1709/R7482.txt"), None),
        "R852": (lambda: ours_plain("rakoczi1704/tr/R852_p*.txt").replace("_", ""), "rakoczi1704/DOC_R852_D2171_2171.txt"),
        "R912": (lambda: ours_plain("rakoczi1704/tr/R912_p*.txt"), "rakoczi1704/DOC_R912_D2230_2230.txt")}
out = {}
for d, (get, ref) in DOCS.items():
    p = Path(sys.argv[1]) / f"pass1_{d}.txt"
    if not p.exists():
        continue
    hl = score.hyp_lines(str(p))
    b = score.digits("".join(l.rstrip("! ") for l in hl), keep_q=True)
    a = get()
    row = {"our_signs": len(a), "pass_signs": len(b), "pass_vs_ours": round(score.lev_ops(a, b)[3] / len(a), 4)}
    if ref:
        h = score2.ref_stream(str(T / ref), False)
        row.update({"human_signs": len(h), "ours_vs_human": round(score.lev_ops(h, a)[3] / len(h), 4),
                    "pass_vs_human": round(score.lev_ops(h, b)[3] / len(h), 4)})
    out[d] = row
    print(d, row)
json.dump(out, open(HERE / "recheck_passes.json", "w"), indent=1)
