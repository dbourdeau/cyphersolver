# Build page/column/line index from line records. Usage: index_ed.py lines.tsv out.tsv
import sys, re, statistics, collections
rows = collections.defaultdict(list)
for l in open(sys.argv[1]):
    leaf, W, H, x0, y0, x1, y1, txt = l.rstrip('\n').split('\t', 7)
    rows[int(leaf)].append((int(W), int(H), int(x0), int(y0), int(x1), int(y1), txt))
# printed page number per leaf: digits-only token in top 15% of page
pn = {}
for leaf, segs in rows.items():
    W, H = segs[0][0], segs[0][1]
    for s in segs:
        if s[3] < H * 0.16 and re.fullmatch(r'\d{1,3}', s[6].strip()):
            pn[leaf] = int(s[6].strip())
# offsets: mode of pn-leaf
offs = collections.Counter(p - l for l, p in pn.items())
out = open(sys.argv[2], 'w')
for leaf in sorted(rows):
    segs = rows[leaf]; W, H = segs[0][0], segs[0][1]
    # local offset: nearest leaves with detected page numbers
    near = sorted((abs(l - leaf), p - l) for l, p in pn.items() if abs(l - leaf) <= 6)
    if not near: continue
    oc = collections.Counter(o for d, o in near).most_common(1)[0][0]
    page = leaf + oc
    # find header y: segments with caps/digits at top; body starts below
    body = [s for s in segs if s[3] > H * 0.10 and len(s[6].strip()) > 2]
    if not body: continue
    mid = statistics.median([s[2] for s in body])  # rough
    xs = sorted(s[2] for s in body)
    # column split: largest gap in sorted x0 among the middle
    if len(xs) < 2: continue
    gaps = [(xs[i+1]-xs[i], (xs[i+1]+xs[i])/2) for i in range(len(xs)-1)]
    split = max(gaps)[1]
    for c, sel in (('a', [s for s in body if s[2] < split]), ('b', [s for s in body if s[2] >= split])):
        if not sel: continue
        left = statistics.median([s[2] for s in sel])
        heads = [s for s in sel if abs(s[2] - left) < W * 0.03]
        heads.sort(key=lambda s: (s[3]+s[5])/2)
        ycs = [(s[3]+s[5])/2 for s in heads]
        diffs = [ycs[i+1]-ycs[i] for i in range(len(ycs)-1)]
        if not diffs: continue
        pitch = statistics.median([d for d in diffs if d > 10] or [1])
        y0 = ycs[0]
        for s, yc in zip(heads, ycs):
            ln = round((yc - y0) / pitch) + 1
            out.write(f"{page}\t{c}\t{ln}\t{leaf}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}\n")
print(sys.argv[1], 'page offsets', offs.most_common(4))
