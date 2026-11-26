"""decode_once.py: map BLIND.tsv tokens through the frozen gerlach1252 key, once. No judging, no edits.

Usage:  python3 -I decode_once.py [BLIND.tsv] [decode_once.txt]
Defaults: blind_packet/BLIND.tsv -> decode_once.txt, both beside this script.

- Checks key_frozen.tsv against the sha256 in FREEZE.txt and refuses to run on a mismatch.
- Refuses to overwrite an existing decode_once.txt (the first pass is the figure of record).
- Mapping: each label -> its letter in key_frozen.tsv; "," -> word space; "=" at line end -> word runs on;
  "LABEL?" -> letter + "?" marker kept in the bracketed sign line; "#" -> "#"; "[...]" and "{clear}" copied as is;
  ".", ";", ":" copied as is; any label not in the key -> <LABEL> and counted.
- Writes for every row: the tokens, the decoded letters, and counts; a totals block at the end.
"""
import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.path.join(HERE, "key_frozen.tsv")
FREEZE = os.path.join(HERE, "FREEZE.txt")
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "blind_packet", "BLIND.tsv")
dst = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "decode_once.txt")

want = re.search(r"^sha256:\s*([0-9a-f]{64})", open(FREEZE, encoding="utf-8").read(), re.M).group(1)
have = hashlib.sha256(open(KEY, "rb").read()).hexdigest()
if have != want:
    sys.exit(f"key_frozen.tsv sha256 {have} != FREEZE.txt {want}: refusing to decode")
if os.path.exists(dst):
    sys.exit(f"{dst} exists: decode_once runs once; refusing to overwrite")

key = {}
for line in open(KEY, encoding="utf-8"):
    if not line.strip() or line.startswith("#"):
        continue
    f = line.rstrip("\n").split("\t")
    if f[0] == "letter":
        continue
    key[f[1]] = f[0]

PASS = {".", ";", ":", "#"}
tot = {"rows": 0, "signs": 0, "doubtful": 0, "unknown_hash": 0, "not_in_key": 0}
out = [f"# decode_once of {os.path.basename(src)} with key_frozen.tsv sha256 {have}", ""]
rows = [l.rstrip("\n").split("\t") for l in open(src, encoding="utf-8") if l.strip()]
if rows and rows[0][0].strip().lower() == "page":
    rows = rows[1:]
for r in rows:
    r += [""] * (5 - len(r))
    page, ln, toks, clear, notes = (x.strip() for x in r[:5])
    words, cur = [], ""
    # keep {clear text} and [...] groups whole even if they contain spaces
    for t in re.findall(r"\{[^}]*\}|\[[^\]]*\]|\S+", toks):
        if t == ",":
            words.append(cur); cur = ""
        elif t == "=":
            cur += "="
        elif t in PASS:
            cur += t
            if t == "#":
                tot["unknown_hash"] += 1
        elif t.startswith("{") or t.startswith("["):
            cur += t
        else:
            q = t.endswith("?")
            lab = t[:-1] if q else t
            if lab in key:
                cur += key[lab] + ("?" if q else "")
                tot["signs"] += 1
                tot["doubtful"] += q
            else:
                cur += f"<{t}>"
                tot["not_in_key"] += 1
    words.append(cur)
    tot["rows"] += 1
    out.append(f"p.{page} {ln}" + (f"  clear: {clear}" if clear else ""))
    out.append(f"  signs:  {toks}")
    out.append(f"  letters: {' '.join(w for w in words if w != '')}")
    if notes:
        out.append(f"  notes:  {notes}")
out += ["", "# totals: " + ", ".join(f"{k} {v}" for k, v in tot.items())]
open(dst, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"wrote {dst}: " + ", ".join(f"{k} {v}" for k, v in tot.items()))
