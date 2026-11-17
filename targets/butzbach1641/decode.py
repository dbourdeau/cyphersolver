# Decode the arbitrated digits of HStAD D 4 Nr. 76/6, view 13, with key.tsv.
# Usage: python3 decode.py transcription/digits_arbitrated.txt > decryption.txt
import sys, collections
from pathlib import Path
KEY, MAIN = {}, set()
for row in (Path(__file__).parent / "key.tsv").read_text(encoding="utf-8").splitlines():
    if row.startswith("#") or not row.strip(): continue
    n, c, src = row.split("\t")
    KEY[int(n)] = c
    if src.startswith("view 11"): MAIN.add(int(n))
nums = collections.Counter(); out = []
for line in open(sys.argv[1], encoding="utf-8"):
    if not line.strip() or line.startswith("#"): continue
    tag, body = line.split(":", 1)
    words = []
    for w in body.split("/"):
        s = ""
        for tok in w.split():
            if tok.isdigit():
                n = int(tok); nums[n] += 1
                s += KEY.get(n, f"<{n}>")
            elif tok == "||": s += "-"
            else: s += tok
        words.append(s)
    out.append(f"{tag}: " + " ".join(words))
print("\n".join(out))
tot = sum(nums.values()); inkey = sum(c for n, c in nums.items() if n in MAIN)
print(f"\n# numbers read: {tot}; on the view 11 strip (11-34): {inkey} ({inkey/tot:.1%}); off the strip: "
      + ", ".join(f"{n} x{c}" for n, c in sorted(nums.items()) if n not in MAIN))
