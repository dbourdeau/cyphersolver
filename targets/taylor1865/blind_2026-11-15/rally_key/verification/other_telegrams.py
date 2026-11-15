# Try RALLYTOTHEFRONT (Vigenere, plain = cipher - key) at all 15 phases on every Taylor cipher stream we hold.
# Language model: letter trigrams from the Official Records ser. I vol. 49 pt. 2 OCR text (period military English).
# Control per stream: 400 random 15-letter English-like keys (same generator as run_verify.py) x 15 phases; a stream
# "hits" if RALLY's best whole-stream score beats every control. Windows of 20 letters are also listed when RALLY's best
# phase beats every control on that window (many windows -> chance hits expected; each is read by eye).
import csv, glob, math, os, random, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TGT = os.path.join(ROOT, "output/push_2026-11-15/wt-main-readonly/targets/taylor1865")
OPEN = os.path.join(ROOT, "output/taylor1865_open_2026-11-15")
ORT = os.path.join(ROOT, "sources/raw/taylor1865_open_2026-11-15/or_text/warofrebellion014902rootrich_djvu.txt")
KEY = "RALLYTOTHEFRONT"

txt = re.sub("[^A-Z]", "", open(ORT, encoding="utf-8", errors="ignore").read().upper())
from collections import Counter
tri = Counter(txt[i:i+3] for i in range(len(txt)-2)); bi = Counter(txt[i:i+2] for i in range(len(txt)-1))
def lp(a, b, c): return math.log((tri[a+b+c] + 0.1) / (bi[a+b] + 2.6))
def score(p): return sum(lp(p[i], p[i+1], p[i+2]) for i in range(len(p)-2)) / max(1, len(p)-2)
def dec(c, k, off): return "".join(chr((ord(x) - ord(k[(i+off) % len(k)])) % 26 + 65) for i, x in enumerate(c))

WORDS = sorted(w.strip().upper() for w in open("/usr/share/dict/words") if w.strip().isalpha() and 2 <= len(w.strip()) <= 8)
rng = random.Random(20261115); rkeys = []
while len(rkeys) < 400:
    s = ""
    while len(s) < 15: s += rng.choice(WORDS)
    rkeys.append(s[:15])

def first(s):  # "[A/B]" -> A ; strip other marks
    return re.sub(r"\[([A-Z])/[^\]]*\]", r"\1", s)

streams = {}
for f in sorted(glob.glob(os.path.join(TGT, "*_cipher.txt"))):
    body = "\n".join(l for l in open(f, encoding="utf-8") if not l.startswith("#"))
    streams["target:" + os.path.basename(f)] = re.sub("[^A-Z]", "", first(body))
for f in ["v11-0044a_transcription.txt", "v11-0045b_transcription.txt"]:
    t = open(os.path.join(TGT, f), encoding="utf-8").read()
    runs = re.findall(r"(?:\b[A-Z]{2,}\b\s*-?\s*){3,}", t)
    for j, r in enumerate(runs):
        r2 = re.sub("[^A-Z]", "", r)
        if len(r2) >= 15 and not r2.startswith(("NARA", "PROVISIONAL", "COME")): streams[f"target:{f}:run{j+1}"] = r2
for rd in ["B1", "B2"]:
    rows = [r for r in csv.DictReader(open(os.path.join(OPEN, f"transcriptions/reader{rd}_transcription.tsv"), encoding="utf-8"), delimiter="\t")]
    t10 = [first(r["group"]) for r in rows if r["frame"] == "v11_0046" and "telegram 1" in r["telegram"]]
    allg = re.sub("[^A-Z]", "", "".join(t10)); mid = re.sub("[^A-Z]", "", "".join(t10[4:13]))
    streams[f"T10 whole, reader {rd}"] = allg; streams[f"T10 groups 5-13, reader {rd}"] = mid
v = [r for r in csv.DictReader(open(os.path.join(OPEN, "verify/mine/verifier_transcription.tsv"), encoding="utf-8"), delimiter="\t") if r["telegram"] == "M"]
streams["T10 groups 5-13, earlier verifier"] = "".join(r["letters"] for r in v[4:13])
streams["T11 (this telegram), helper A: positive control"] = "".join(r["first"] for r in csv.DictReader(open(os.path.join(HERE, "helperA/transcription.tsv")), delimiter="\t"))

out = []
for name, c in streams.items():
    if len(c) < 10: continue
    rs = [(score(dec(c, KEY, o)), o) for o in range(15)]; best, bo = max(rs)
    ctl = max(score(dec(c, k, o)) for k in rkeys for o in range(15))
    hit = best > ctl
    out.append(f"{name}: {len(c)} letters; RALLY best {best:.3f} at phase {bo}; control max {ctl:.3f}; {'HIT' if hit else 'no hit'}")
    out.append(f"    phase {bo}: {dec(c, KEY, bo)}")
    W = 20
    if len(c) >= W:
        for i in range(0, len(c) - W + 1, 5):
            w = c[i:i+W]; rb = max((score(dec(w, KEY, (o + i) % 15)), o) for o in range(15))
            cm = max(score(dec(w, k, o)) for k in rkeys[:100] for o in range(15))
            if rb[0] > cm: out.append(f"    window {i+1}-{i+W}: RALLY phase {rb[1]} {dec(w, KEY, (rb[1]+i) % 15)} ({rb[0]:.2f} > {cm:.2f})")
open(os.path.join(HERE, "other_telegrams_results.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
