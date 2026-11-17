"""Mechanical reconciliation of two helper transcriptions (PLAN.md step 1).
usage: reconcile.py A.txt B.txt out_reconciled.txt"""
import sys, re, difflib, json
def load(p):
    lines = {}
    for ln in open(p, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln or ln.startswith("#!"): continue
        k, v = ln.split(":", 1)
        line = k.split("_w")[0]
        v = re.sub(r"\?\([^)]*\)", "?", v)
        toks = [t for t in v.split() if t != "/"]
        lines.setdefault(line, []).extend(toks)
    return lines
A, B = load(sys.argv[1]), load(sys.argv[2])
order = ["L1","L2","L3","L4","L5","L6","L7","L8a","L8b"]
out, agree, total, rows = [], 0, 0, []
for L in order:
    a, b = A.get(L, []), B.get(L, [])
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    rec = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for t in a[i1:i2]:
                if t in ("?", "#"): rec.append("D"); rows.append((L, "both-unclear", t, t)); total += 1
                else: rec.append(t); agree += 1; total += 1
        else:
            n = max(i2-i1, j2-j1)
            aa = a[i1:i2] + ["-"]*(n-(i2-i1)); bb = b[j1:j2] + ["-"]*(n-(j2-j1))
            for x, y in zip(aa, bb):
                rec.append("D"); total += 1; rows.append((L, op, x, y))
    out.append(f"{L}: " + " ".join(rec))
open(sys.argv[3], "w").write("\n".join(out) + "\n")
print(f"agreed {agree} of {total} aligned positions; A {sum(len(v) for v in A.values())} signs, B {sum(len(v) for v in B.values())} signs")
for r in rows: print("\t".join(r))
