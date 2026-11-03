"""Align pass 1 (a pairs tsv) and pass 2 (a digits txt) per image and list disagreements: python compare_passes.py p1.tsv [p1b.tsv] p2.txt"""
import re, difflib, collections, sys
p1 = collections.defaultdict(list)
for ln in open(sys.argv[1], encoding="utf-8"):
    if ln.startswith("#") or not ln.strip(): continue
    img, run, use, groups, gloss = ln.rstrip("\n").split("\t")
    p1[img] += groups.split()
p2 = collections.defaultdict(list); cur = None; seen = set()
for ln in open(sys.argv[2], encoding="utf-8"):
    m = re.match(r"## c(\d{3})", ln)
    if m: cur = m.group(1); continue
    m = re.match(r"L\d+:\s*(.*)", ln)
    if m and cur:
        toks = re.findall(r"\d{4}\??", m.group(1))
        key = " ".join(toks)
        if key in seen: continue   # overlapping crops
        seen.add(key); p2[cur] += toks
for img in sorted(p1):
    a = p1[img]; b = [t.rstrip("?") for t in p2[img]]
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    print(f"== {img}: pass1 {len(a)} groups, pass2 {len(b)} groups, ratio {sm.ratio():.3f}")
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(f"  {op:8s} p1[{i1}:{i2}]={' '.join(a[i1:i2])} | p2={' '.join(b[j1:j2])}  ctx: {' '.join(a[max(0,i1-3):i1])}")
