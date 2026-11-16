import json, os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
RX = re.compile(r"(?<!de)(?<!inde)cifr|bcritt|bcript|zifer|furtiv|scrittura segreta|convenzional", re.I)
def flat(o, out):
    if isinstance(o, dict):
        for v in o.values(): flat(v, out)
    elif isinstance(o, list):
        for v in o: flat(v, out)
    elif isinstance(o, str) and len(o) > 12 and not o.startswith(("table-", "http")): out.append(o)
ids = sys.argv[1:] or [os.path.basename(p)[:-5] for p in glob.glob(os.path.join(HERE, "raw", "manus_detail", "*.json"))]
for i in ids:
    out = []; flat(json.load(open(os.path.join(HERE, "raw", "manus_detail", i + ".json"), encoding="utf8"), strict=False), out)
    print("=====", i, out[0][:110] if out else "")
    seen = set()
    for s in out:
        s = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))
        for m in RX.finditer(s):
            x = s[max(0, m.start() - 160): m.end() + 200]
            if x[:60] in seen: continue
            seen.add(x[:60]); print("   ..", x); break
