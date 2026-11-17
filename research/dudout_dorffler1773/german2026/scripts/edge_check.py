"""Edge check on the strip transcription, for the question: does any half lose numbers at the left or right edge?

  CIPHER_DATA=transcription python3 scripts/edge_check.py [../training/T-train-v1.txt ../training/T476-cipher-v1.txt]
1. Against B. Dudout's blind cipher transcriptions of 470, 475 and 476 (training/): for each of his lines of 6+ numbers,
   the longest run of numbers shared with any line of the same half, and where in his line that run starts.
   Numbers lost at the left edge show as a run starting at index 7-8 instead of 0.
2. Key-free: median numbers per cipher line (8+ numbers) in each half. A half far under the other halves is cut.
"""
import collections, difflib, os, re, statistics, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p5

nums = lambda t: re.findall(r"\d+", t)
rows = collections.defaultdict(list)
for r in p5.load_lines():
    if r["tag"] == "L" and len(nums(r["text"])) >= 8:
        rows[r["half"]].append(nums(r["text"]))

args = sys.argv[1:] or ["../training/T-train-v1.txt", "../training/T476-cipher-v1.txt"]
ref = collections.defaultdict(list)
for path in args:
    cur = None
    for l in open(path):
        m = re.match(r"@(\d{3})([LR])", l)
        if m:
            cur = "dorffler-19-102/p0%s%s" % (m.group(1), m.group(2))
        elif l.startswith("C ") and cur:
            g = l[2:].replace("?+", "").replace(":", " ").split()
            g = [x for x in g if x.isdigit()]
            if len(g) >= 6:
                ref[cur].append(g)

print("1. against Dudout's blind transcriptions (lines of 6+ numbers)")
print("%-26s %6s %12s %14s" % ("half", "lines", "shared share", "median start"))
for half, lines in sorted(ref.items()):
    run = tot = 0
    starts = []
    for b in lines:
        best = (0, 0)
        for o in rows.get(half, []):
            m = difflib.SequenceMatcher(None, b, o, autojunk=False).find_longest_match(0, len(b), 0, len(o))
            if m.size > best[0]:
                best = (m.size, m.a)
        run += best[0]; tot += len(b); starts.append(best[1])
    print("%-26s %6d %11.1f%% %14s" % (half, len(lines), 100 * run / tot, statistics.median(starts)))

print("\n2. median numbers per cipher line (8+ numbers), halves under 14 listed")
med = {h: statistics.median(len(x) for x in ls) for h, ls in rows.items()}
print("all halves: median of medians %.1f, %d halves with cipher lines" % (statistics.median(med.values()), len(med)))
for h in sorted(med):
    if med[h] < 14:
        print("  %-26s %5.1f (%d lines)" % (h, med[h], len(rows[h])))
