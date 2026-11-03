"""Merge pass A and pass B into transcription_l2_merged.txt: A's tokens, with finer B distinctions kept
(A fs + B N21 -> fz; A Le + B N24 -> eo; A y + B N25 -> phi; A N1 + B N9 -> N1b). Disagreements are written as
A-token and logged to merge_log.tsv for settling by eye."""
import re, difflib, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compare import load, BMAP
A = load("transcription_l2_passA.txt"); Braw = load("transcription_l2_passB.txt")
SPLIT = {("fs", "N21"): "fz", ("Le", "N24"): "eo", ("y", "N25"): "phi", ("N1", "N9"): "N1b"}
out = []; log = []
for k, a in A.items():
    b = Braw.get(k, []); bm = [BMAP.get(t, t) for t in b]
    sm = difflib.SequenceMatcher(None, a, bm, autojunk=False); toks = list(a)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for i, j in zip(range(i1, i2), range(j1, j2)):
                if (a[i], b[j]) in SPLIT: toks[i] = SPLIT[(a[i], b[j])]
        else:
            log.append(f"{k[0]} {k[1]}\t{i1}\tA: {' '.join(a[i1:i2])}\tB: {' '.join(b[j1:j2])}")
    out.append(f"{k[0]} {k[1]}: " + " ".join(toks))
open("transcription_l2_merged.txt", "w", encoding="utf-8").write("# merged A/B, see scripts/merge.py and merge_log.tsv\n" + "\n".join(out) + "\n")
open("merge_log.tsv", "w", encoding="utf-8").write("row\tpos\tpass A\tpass B\tsettled\n" + "\n".join(log) + "\n")
print(len(out), "rows;", len(log), "disagreements")
