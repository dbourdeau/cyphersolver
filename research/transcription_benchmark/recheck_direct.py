"""Re-check, part A: the corpus's own model-made transcriptions scored against DECODE's human transcription of the same
record (digit streams, as score2: mark codes and clear text removed; strict and order-tolerant).
Usage: python recheck_direct.py -> recheck_direct.json"""
import glob
import json
import re
from pathlib import Path

import score
import score2

HERE = Path(__file__).resolve().parent
T = HERE.parent.parent / "targets"
PAIRS = {  # record: (our page files, DECODE human transcription)
    "R922": ("rakoczi1704/tr/R922_p*.txt", "rakoczi1704/DOC_R922_D1861_1861.txt"),
    "R852": ("rakoczi1704/tr/R852_p*.txt", "rakoczi1704/DOC_R852_D2171_2171.txt"),
    "R912": ("rakoczi1704/tr/R912_p*.txt", "rakoczi1704/DOC_R912_D2230_2230.txt"),
    "R483": ("rakoczi1711/tr/R483_p*.txt", "rakoczi1704/DOC_R483_D2172_2172.txt"),
}
out = {}
for rec, (ours, ref) in PAIRS.items():
    a = score2.ref_stream(str(T / ref), False)
    hl = []
    for f in sorted(glob.glob(str(T / ours))):
        hl += [re.sub(r"[_?]", "", l) for l in score.hyp_lines(f)]  # our own mark and doubt signs are not digits
    b = score.digits("".join(hl))
    e = score.lev_ops(a, b)[3]
    eo = min(e, score2.order_tolerant(a, hl, False))
    out[rec] = {"ref_signs": len(a), "our_signs": len(b), "edits": e, "cer": round(e / len(a), 4),
                "edits_order_tolerant": eo, "cer_order_tolerant": round(eo / len(a), 4)}
    print(rec, out[rec])
json.dump(out, open(HERE / "recheck_direct.json", "w"), indent=1)
