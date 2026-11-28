"""after_blind.py BATCH: freeze BLIND.tsv, run decode_once once, build the judge packet. Run once per batch.

  python3 -I /home/claude/gerlach_next/tools/after_blind.py A

1. Refuses if FREEZE_blind.txt or decode_once.txt already exists (first pass is the figure of record).
2. Checks FREEZE.txt hashes (key_frozen.tsv, decode_once.py, packet files) are unchanged.
3. Writes FREEZE_blind.txt (sha256 + md5 of BLIND.tsv, UTC time).
4. Runs decode_once.py BLIND.tsv decode_once.txt (once).
5. Writes judge/decode.txt (letters only: '[...n]' -> n x '_', '[...]' -> '_', '<LABEL>' -> '#')
   and judge/BRIEF.txt. The judge agent is given only those two files.
"""
import datetime
import hashlib
import os
import re
import subprocess
import sys

B = sys.argv[1]
D = os.path.join("/home/claude/gerlach_next", B)
blind = os.path.join(D, "BLIND.tsv")
for f in ("FREEZE_blind.txt", "decode_once.txt"):
    if os.path.exists(os.path.join(D, f)):
        sys.exit(f"{f} exists in {D}: refusing (runs once)")
if not os.path.exists(blind):
    sys.exit("no BLIND.tsv")

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

bad = []
for line in open(os.path.join(D, "FREEZE.txt"), encoding="utf-8"):
    m = re.match(r"^([0-9a-f]{64})  (\S+)$", line.rstrip("\n"))
    if m and sha(os.path.join(D, m.group(2))) != m.group(1):
        bad.append(m.group(2))
if bad:
    sys.exit(f"FREEZE.txt mismatch: {bad}")

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
data = open(blind, "rb").read()
open(os.path.join(D, "FREEZE_blind.txt"), "w").write(
    f"{hashlib.sha256(data).hexdigest()}  BLIND.tsv\nmd5 {hashlib.md5(data).hexdigest()}\n{now}\n"
    f"frozen before decode_once; FREEZE.txt hashes re-checked: all match\n")

subprocess.run([sys.executable, "-I", os.path.join(D, "decode_once.py"), blind, os.path.join(D, "decode_once.txt")], check=True)

os.makedirs(os.path.join(D, "judge"), exist_ok=True)
rows, pages, cur = [], [], None
for l in open(os.path.join(D, "decode_once.txt"), encoding="utf-8"):
    if l.startswith("p."):
        cur = l.split("  clear:")[0].strip()
        pg = cur.split()[0][2:]
        if pg not in pages:
            pages.append(pg)
    elif l.startswith("  letters: ") and cur:
        s = l[len("  letters: "):].rstrip("\n")
        s = re.sub(r"\[\.\.\.(\d+)\]", lambda m: "_" * int(m.group(1)), s)
        s = s.replace("[...]", "_")
        s = re.sub(r"<[^>]*>", "#", s)
        rows.append(f"{cur}\t{s}")
        cur = None
open(os.path.join(D, "judge", "decode.txt"), "w", encoding="utf-8").write("\n".join(rows) + "\n")
pl = ", ".join(pages)
brief = (
    f"decode.txt: one decode (no edits) of {len(pages)} cipher pages (pp.{pl}) of Johann Gerlach's 'Occulta scripta "
    "chymica' (Wellcome MS.309), 16th-century Early New High German alchemical recipes. Each row: page and line, then "
    "decoded letters; word breaks are the transcriber's ',' dividers turned to spaces, so approximate; '?' after a letter "
    "= doubtful sign (judge the letter); '_' or '#' = unknown sign (1 unit, N); text in { } is clear script, not cipher "
    "(exclude it from the counts).\n"
    "Task (strict judge, one pass, no second tries): segment into words and mark each letter S (part of a word that reads "
    "as sense in 16th-c. German, period spellings and Latin chemical terms allowed), E (wrong but plausibly a one-letter "
    "slip), N (no sense). Write judge.tsv (page, line, segmented reading, S, E, N). Totals PER PAGE and overall, strict "
    "share S/(S+E+N) with arithmetic. Then a 3-line gist per page, describing recipes only at the level 'a recipe for X' "
    "(no quantities, no how-to). Write judge.tsv and JUDGE_NOTES.txt (unit rules, totals, recurring slips, gists) in this "
    "folder. Do not open any other file.\n")
open(os.path.join(D, "judge", "BRIEF.txt"), "w", encoding="utf-8").write(brief)
print(f"batch {B}: FREEZE_blind {hashlib.sha256(data).hexdigest()[:16]}... at {now}; judge packet: {len(rows)} rows, pages {pl}")
