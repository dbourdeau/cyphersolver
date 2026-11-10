"""Key from word-level pairs: each K line gives groups and a segmentation with one piece per group.
usage: python scripts/make_key.py out.tsv wordpairs_a.tsv [wordpairs_b.tsv ...]
value = most frequent piece (a/å/ä and o/ö folded, lower case); status confirmed = seen >= 2 and >= 2/3 agree."""
import sys, collections, unicodedata
def fold(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if c.isalpha() or c.isdigit())
cnt = collections.defaultdict(collections.Counter); bad = 0
for path in sys.argv[2:]:
    for ln in open(path, encoding="utf-8"):
        if ln.startswith("#"): continue
        f = ln.rstrip("\n").split("\t")
        if len(f) < 6 or f[2] != "K": continue
        gs = f[3].split(); ps = f[5].split("|")
        if len(gs) != len(ps) or any("?" in g for g in gs): bad += 1; continue
        for g, p in zip(gs, ps): cnt[g][fold(p)] += 1
st = collections.Counter()
with open(sys.argv[1], "w", encoding="utf-8") as o:
    o.write("# group\tvalue\tseen\tagree\tstatus\tother\n")
    for g in sorted(cnt):
        c = cnt[g]; v, a = c.most_common(1)[0]; n = sum(c.values())
        s = "single" if n == 1 else ("confirmed" if a >= 2 and a * 3 >= n * 2 else "mixed")
        st[s] += 1
        o.write(f"{g}\t{v}\t{n}\t{a}\t{s}\t" + " ".join(f"{k}:{x}" for k, x in c.most_common()[1:]) + "\n")
print(dict(st), "lines skipped:", bad)
