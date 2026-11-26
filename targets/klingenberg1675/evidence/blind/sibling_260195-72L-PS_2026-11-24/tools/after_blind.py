"""after_blind.py [FOLDER]: freeze BLIND.tsv, run decode_once once, build the judge packet. Runs once.
Adapted (copied and parameterised) from /home/claude/gerlach_next/tools/after_blind.py for the Klingenberg format.

  python3 -I /home/claude/next_round2/kling72/tools/after_blind.py [/home/claude/next_round2/kling72]

1. Refuses if FREEZE_blind.txt or decode_once.txt already exists (first pass is the figure of record).
2. Checks every hash line of FREEZE.txt (key_frozen/*, sheet_to_key.tsv, decode_once.py, shuffle.py, tools, packet/*).
3. Writes FREEZE_blind.txt (first token = sha256 of BLIND.tsv, as decode_once.py reads it; then md5, UTC time).
4. Runs decode_once.py once (writes decode_once.txt, DECODE_RUN.txt).
5. Writes judge/decode.txt (image, line, decode only: no clear words, no key) and judge/BRIEF.txt.
   The judge agent is given only those two files.
"""
import datetime, hashlib, os, re, subprocess, sys
D = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
blind = os.path.join(D, "BLIND.tsv")
for f in ("FREEZE_blind.txt", "decode_once.txt"):
    if os.path.exists(os.path.join(D, f)):
        sys.exit(f"{f} exists in {D}: refusing (runs once)")
if not os.path.exists(blind):
    sys.exit("no BLIND.tsv")
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
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
    "frozen before decode_once; FREEZE.txt hashes re-checked: all match\n")
subprocess.run([sys.executable, "-I", os.path.join(D, "decode_once.py")], check=True, cwd=D)
os.makedirs(os.path.join(D, "judge"), exist_ok=True)
rows = []
for l in open(os.path.join(D, "decode_once.txt"), encoding="utf-8").read().splitlines()[1:]:
    f = l.split("\t")
    if len(f) >= 4:
        rows.append(f"{f[0]}\t{f[1]}\t{f[3]}")
open(os.path.join(D, "judge", "decode.txt"), "w", encoding="utf-8").write("image\tline\tdecode\n" + "\n".join(rows) + "\n")
brief = (
    "decode.txt: one mechanical decode (no edits) of the cipher runs of a short postscript in a German letter draft of 1675 "
    "(Danish-Swedish war period). Each row: image, line, then the decoded units separated by spaces. A unit is a syllable, "
    "letter or whole word as the code gives it. '[n]' (a number in brackets) = code number with no value in the key; "
    "'[?...]' or '<?...>' = unread or unvalued token; '<struck>' = a deleted group (not a unit); '{...}' = a drawn mark "
    "(not a unit); other bracketed marks such as [edge] or [gloss] are not units.\n"
    "Task (strict judge, one pass, no second tries): join the units of each row into words, then label EVERY unit S (part of "
    "a word that reads as sense in 17th-c. German, period spellings and Latin/French loanwords allowed; proper names S only "
    "if well formed), E (wrong but plausibly a one-letter slip), N (no sense, and every '[n]' or unread token). "
    "Write judge.tsv with header: image, line, row, word_no, word, unit, label, gloss (one row per unit; 'row' = the row "
    "number in decode.txt counting from 1 after the header; gloss = your reading of the row, on its first unit only). "
    "Then JUDGE_NOTES.txt: unit rules, totals S, E, N and the strict share S/(S+E+N) with the arithmetic, recurring slips, "
    "and a 3-line gist. Write both files in this folder. Do not open any other file.\n")
open(os.path.join(D, "judge", "BRIEF.txt"), "w", encoding="utf-8").write(brief)
print(f"FREEZE_blind {hashlib.sha256(data).hexdigest()[:16]}... at {now}; judge packet: {len(rows)} rows")
