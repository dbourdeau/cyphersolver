"""after_judge.py BATCH: re-add the judge's figures from judge.tsv, check each row's S+E+N against the letters of
judge/decode.txt, then run the 5,000-shuffle control at seeds 20261112 and 7 (shuffle.py, once).

  python3 -I /home/claude/gerlach_next/tools/after_judge.py A

Writes judge/RECOUNT.txt and shuffle_out.txt (refuses to overwrite shuffle_out.txt).
Pass rule (both must hold): strict S/(S+E+N) >= 65% for the batch (our line), and fewer than 5 of 5,000
shuffles at or above the real decode at every seed.
"""
import os
import re
import subprocess
import sys

B = sys.argv[1]
D = os.path.join("/home/claude/gerlach_next", B)
REPO = "/home/claude/wt-gerlach-next"

dec = {}
for l in open(os.path.join(D, "judge", "decode.txt"), encoding="utf-8"):
    if l.strip():
        k, s = l.rstrip("\n").split("\t", 1)
        s = re.sub(r"\{[^}]*\}", "", s)
        dec[k] = sum(1 for c in s if c.isalpha() or c in "#_")

tot, out, mism, seen = {}, [], [], set()
for i, l in enumerate(open(os.path.join(D, "judge", "judge.tsv"), encoding="utf-8")):
    f = l.rstrip("\n").split("\t")
    if i == 0 or len(f) < 6 or not f[3].strip().isdigit() or not re.match(r"^L\d+", f[1].strip()):
        continue
    p = f[0].strip()
    p = p if p.startswith("p.") else "p." + p
    key = f"{p} {f[1].strip()}"
    S, E, N = (int(x) for x in f[3:6])
    seen.add(key)
    if key in dec and S + E + N != dec[key]:
        mism.append(f"{key}: judge {S + E + N} vs decode {dec[key]}")
    t = tot.setdefault(p, [0, 0, 0])
    t[0] += S; t[1] += E; t[2] += N
missing = [k for k in dec if k not in seen]
a = [0, 0, 0]
for p, t in tot.items():
    n = sum(t); a = [x + y for x, y in zip(a, t)]
    out.append(f"{p}: S {t[0]} E {t[1]} N {t[2]} = {n}; strict {t[0]}/{n} = {100 * t[0] / n:.1f}%")
n = sum(a)
out.append(f"ALL: S {a[0]} E {a[1]} N {a[2]} = {n}; strict {a[0]}/{n} = {100 * a[0] / n:.1f}%; "
           f"(S+E)/all {a[0] + a[1]}/{n} = {100 * (a[0] + a[1]) / n:.1f}%")
out.append("check: " + " + ".join(str(t[0]) for t in tot.values()) + f" = {sum(t[0] for t in tot.values())}")
out.append(f"rows judged {len(seen)}; decode rows {len(dec)}; rows missing from judge {len(missing)} {missing[:5]}; "
           f"S+E+N != decode letters on {len(mism)} rows {mism[:5]}")
out.append(f"65% line: {'PASS' if a[0] / n >= 0.65 else 'FAIL'}")
open(os.path.join(D, "judge", "RECOUNT.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out))

so = os.path.join(D, "shuffle_out.txt")
if os.path.exists(so):
    sys.exit("shuffle_out.txt exists: not re-run")
r = subprocess.run([sys.executable, "-I", os.path.join(D, "shuffle.py"), REPO, "5000", "20261112", "7"],
                   capture_output=True, text=True)
open(so, "w").write(r.stdout + (("\nSTDERR:\n" + r.stderr) if r.returncode else ""))
print(r.stdout, r.stderr[-2000:] if r.returncode else "")
