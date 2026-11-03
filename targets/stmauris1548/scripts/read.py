"""Print the decryption row by row; letters from signs seen <= 8 times in upper case; unknown '?'.
python read.py <transcription> <key.tsv>"""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from compare import load
rows = load(sys.argv[1]); K = {}
for l in open(sys.argv[2], encoding="utf-8"):
    if l.strip() and not l.startswith("# "):
        p = l.rstrip("\n").split("\t"); K[p[0]] = p[1]
f = collections.Counter(t for r in rows.values() for t in r)
for k, r in rows.items():
    s = ""
    for t in r:
        v = K.get(t, "?"); v = "" if v == "-" else v
        s += (f"[{t}={v}]" if "--names" in sys.argv else v.upper()) if f[t] <= 8 else v
    print(f"{k[0]} {k[1]}: {s}")
