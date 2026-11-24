import csv, sys, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "judge_A.tsv")
rows = list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
def agg(sel):
    L = sum(int(r["letters"]) for r in sel); S = sum(int(r["S"]) for r in sel)
    E = sum(int(r["E"]) for r in sel); N = sum(int(r["N"]) for r in sel)
    return L, S, E, N
bad = [r["line"] for r in rows if int(r["letters"]) != int(r["S"]) + int(r["E"]) + int(r["N"])]
if bad: print("ROW SUM ERROR:", bad); sys.exit(1)
groups = {
    "A1 training (T)": [r for r in rows if r["set"] == "T"],
    "A1P held-out": [r for r in rows if r["line"].startswith("A1P")],
    "A2 held-out": [r for r in rows if r["line"].startswith("A2")],
    "Held-out total (H)": [r for r in rows if r["set"] == "H"],
    "All": rows,
}
for k, sel in groups.items():
    L, S, E, N = agg(sel)
    print(f"{k}: letters {L} = S {S} + E {E} + N {N}; S {S}/{L} = {100*S/L:.1f}%; S+E {S+E}/{L} = {100*(S+E)/L:.1f}%")
low = min(rows, key=lambda r: (int(r["S"]) / int(r["letters"]), -int(r["letters"])))
print("lowest line:", low["line"], low["set"], f"S {low['S']}/{low['letters']}", low["reading"])
for s in "TH":
    sel = [r for r in rows if r["set"] == s]
    low = min(sel, key=lambda r: (int(r["S"]) / int(r["letters"]), -int(r["letters"])))
    print(f"lowest {s} line:", low["line"], f"S {low['S']}/{low['letters']}", low["reading"])
