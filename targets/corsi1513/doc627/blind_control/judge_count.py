"""Recount judge.tsv and check it reproduces the decode lines L1-L5.
Usage: python3 -I judge_count.py <judge.tsv> <decode_once.txt>"""
import sys, collections

tsv, dec = sys.argv[1], sys.argv[2]
decode = {}
for line in open(dec, encoding="utf-8"):
    if line[:1] == "L" and "\t" in line:
        k, v = line.rstrip("\n").split("\t", 1)
        if k[1:].isdigit():
            decode.setdefault(int(k[1:]), v)  # first L1-L5 block only
    if line.startswith("#"):
        break

cnt = collections.defaultdict(collections.Counter)
text = collections.defaultdict(str)
rows = list(open(tsv, encoding="utf-8"))[1:]
for r in rows:
    ln, unit, d, ref, tag, note = r.rstrip("\n").split("\t")
    ln = int(ln)
    assert tag in "MXHO" and len(tag) == 1, r
    assert (tag == "O") == (d == ""), r
    if tag == "M" and note != "code unit":
        assert d == ref.lower(), r
    cnt[ln][tag] += 1
    text[ln] += d

ok = True
for ln in sorted(decode):
    same = text[ln] == decode[ln]
    ok &= same
    print(f"L{ln} concat matches decode: {same}")

def show(name, c):
    m, x, h, o = (c[t] for t in "MXHO")
    print(f"{name}: M={m} X={x} H={h} O={o} | strict {m}/({m}+{x}+{h}+{o})={m}/{m+x+h+o}="
          f"{m/(m+x+h+o):.1%} | accuracy {m}/({m}+{x})={m}/{m+x}={m/(m+x):.1%}")

tot = collections.Counter()
for ln in sorted(cnt):
    show(f"L{ln}", cnt[ln]); tot += cnt[ln]
show("Block", tot)
print("result:", "consistent" if ok else "MISMATCH")
