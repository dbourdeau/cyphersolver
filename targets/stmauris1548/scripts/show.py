"""Show decryption per row with a key tsv: python show.py <transcription> <key.tsv> [B]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from compare import load, BMAP
rows = load(sys.argv[1], BMAP if "--B" in sys.argv else None)
K = {}
for l in open(sys.argv[2], encoding="utf-8"):
    if l.strip() and not l.startswith("# "):
        p = l.rstrip("\n").split("\t"); K[p[0]] = p[1]
PAIRS = "--pairs" in sys.argv
for k, t in rows.items():
    if PAIRS: print(f"{k[0]} {k[1]}: " + " ".join(f"{x}={K.get(x,'?')}" for x in t)); continue
    print(f"{k[0]} {k[1]}: " + "".join(K.get(x, "?") if K.get(x, "?") != "-" else "" for x in t))
