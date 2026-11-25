"""Part A of PLAN_round2.md: close round-2 holes with a third blind reading (helpers C and D).
usage: reconcile_round3.py A.txt B.txt C.txt D.txt map.json out_dir"""
import sys, re, difflib, json
def load(p):
    lines = {}
    for ln in open(p, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln or ln.startswith("#!") or ":" not in ln: continue
        k, v = ln.split(":", 1)
        line = k.split("_w")[0].strip()
        v = re.sub(r"\?\([^)]*\)", "?", v)
        lines.setdefault(line, []).extend(t for t in v.split() if t != "/")
    return lines
def rec2(a, b):
    """round-2 rule: list of (agreed_token_or_None, a_tok, b_tok)"""
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if op == "equal":
            for t in a[i1:i2]: out.append((None if t in ("?", "#") else t, t, t))
        else:
            n = max(i2-i1, j2-j1)
            aa = a[i1:i2] + ["-"]*(n-(i2-i1)); bb = b[j1:j2] + ["-"]*(n-(j2-j1))
            for x, y in zip(aa, bb): out.append((None, x, y))
    return out
A, B, C, D = (load(p) for p in sys.argv[1:5]); M = json.load(open(sys.argv[5])); od = sys.argv[6]
order = ["L1","L2","L3","L4","L5","L6","L7","L8a","L8b"]
rows = []; strict = []; cnt = dict(holes=0, closed=0, dropped=0, left=0)
for L in order:
    ab = rec2(A.get(L, []), B.get(L, [])); cd = rec2(C.get(L, []), D.get(L, []))
    ka = [t if t else f"H{i}" for i, (t, _, _) in enumerate(ab)]
    kc = [t if t else f"h{j}" for j, (t, _, _) in enumerate(cd)]
    newl = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=ka, b=kc, autojunk=False).get_opcodes():
        if op == "equal":
            for i in range(i1, i2): newl.append(ab[i][0])
            continue
        same_len = (i2-i1) == (j2-j1)
        for k, i in enumerate(range(i1, i2)):
            t, x, y = ab[i]
            if t is not None: newl.append(t); continue
            cnt["holes"] += 1
            res, val = "left", None
            if op == "replace" and same_len:
                ct, cx, cy = cd[j1+k]
                if ct is not None and ct in (x, y): res, val = "closed", ct
                why = f"C={cx} D={cy}"
            elif op == "delete" and "-" in (x, y):
                res = "dropped"; why = "C and D: no sign here"
            else:
                why = f"alignment not one-to-one ({op}); C/D here: " + " ".join(f"{cd[j][1]}/{cd[j][2]}" for j in range(j1, j2))
            cnt[res] += 1
            rows.append((L, str(len(newl)+1), x, y, why, res, val or ""))
            if res == "closed": newl.append(val)
            elif res == "left": newl.append("#")
    strict.append((L, newl))
with open(f"{od}/holes_table.tsv", "w") as f:
    f.write("line\tposition_in_new_line\treader_A\treader_B\treaders_C_D\tresult\tsign\tlasry_name\n")
    for r in rows: f.write("\t".join(r) + "\t" + (M.get(r[6], "") if r[6] else "") + "\n")
with open(f"{od}/transcription_strict_round3_ids.txt", "w") as f:
    for L, s in strict: f.write(f"{L}: " + " ".join(x if x else "#" for x in s) + "\n")
print(cnt)
