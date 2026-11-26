"""after_judge.py [FOLDER]: re-add the judge's figures from judge/judge.tsv, check each row's unit count against
judge/decode.txt, then run the 5,000-shuffle control at seeds 20261112 and 7 (shuffle.py, once).
Adapted (copied and parameterised) from /home/claude/gerlach_next/tools/after_judge.py for the Klingenberg unit format.

  python3 -I /home/claude/next_round2/kling72/tools/after_judge.py [/home/claude/next_round2/kling72]

Writes judge/RECOUNT.txt and shuffle_out.txt (refuses to overwrite shuffle_out.txt).
Pass rule (both must hold): strict S/(S+E+N) >= 65% (our line), and fewer than 5 of 5,000 shuffles at or above the
real decode at every seed. Declared before any read: ~120 cipher tokens, so the shuffle may fail on length alone;
a failure is recorded as a failure, not explained away.
REPO: a cyphersolver checkout whose lang/ has de-1640s built (built 24 Nov 2026 in /home/claude/wt-gerlach-next).
"""
import os, re, subprocess, sys
D = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "/home/claude/wt-gerlach-next"
UNIT = re.compile(r"^\[(\d+|\?.*)\]$")

def units(s):
    """count units in a decode string: tokens outside <struck>, {...} and non-hole [marks]."""
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1; continue
        if c in "[{":
            close = "]" if c == "[" else "}"; d = 0; j = i
            while j < len(s):
                if s[j] == c: d += 1
                elif s[j] == close:
                    d -= 1
                    if d == 0: break
                j += 1
            tok = s[i:j + 1]; i = j + 1
            if c == "[" and UNIT.match(tok): out.append(tok)
            continue
        j = i
        while j < len(s) and not s[j].isspace() and s[j] not in "[{": j += 1
        tok = s[i:j]; i = j
        if tok != "<struck>": out.append(tok)
    return out

dec = {}
for n, l in enumerate(open(os.path.join(D, "judge", "decode.txt"), encoding="utf-8").read().splitlines()[1:], 1):
    f = l.split("\t")
    if len(f) >= 3: dec[n] = len(units(f[2]))
cnt, per = {}, {}
for i, l in enumerate(open(os.path.join(D, "judge", "judge.tsv"), encoding="utf-8")):
    f = l.rstrip("\n").split("\t")
    if i == 0 or len(f) < 7 or not f[2].strip().isdigit(): continue
    r, lab = int(f[2]), f[6].strip().upper()
    if lab not in ("S", "E", "N"): continue
    cnt[r] = cnt.get(r, 0) + 1; per[lab] = per.get(lab, 0) + 1
S, E, N = per.get("S", 0), per.get("E", 0), per.get("N", 0); T = S + E + N
mism = [f"row {r}: judge {cnt.get(r, 0)} vs decode {dec[r]}" for r in dec if cnt.get(r, 0) != dec[r]]
out = [f"ALL: S {S} E {E} N {N} = {T}; strict {S}/{T} = {100 * S / T:.2f}%; (S+E)/all {S + E}/{T} = {100 * (S + E) / T:.2f}%" if T else "no units judged",
       f"rows in decode {len(dec)}; rows judged {len(cnt)}; unit-count mismatches {len(mism)} {mism[:5]}",
       f"65% line: {'PASS' if T and S / T >= 0.65 else 'FAIL'}"]
open(os.path.join(D, "judge", "RECOUNT.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
so = os.path.join(D, "shuffle_out.txt")
if os.path.exists(so): sys.exit("shuffle_out.txt exists: not re-run")
r = subprocess.run([sys.executable, "-I", os.path.join(D, "shuffle.py"), REPO, "5000", "20261112", "7"], capture_output=True, text=True)
open(so, "w").write(r.stdout + (("\nSTDERR:\n" + r.stderr) if r.returncode else ""))
print(r.stdout, r.stderr[-2000:] if r.returncode else "")
