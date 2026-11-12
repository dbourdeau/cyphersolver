import sys, json, time, urllib.request, os
UA = {"User-Agent": "WAINUT-research", "Referer": "https://arkivalieronline.rigsarkivet.dk/"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
cmd = sys.argv[1]
if cmd == "refs":
    d = json.loads(get("https://api.rigsarkivet.dk/ao/v1/billedviser/billed-reference-lister?bsid=%s" % sys.argv[2]))
    ids = [g.split(",")[1] for g in d["SA_GUIDs"]]
    open(sys.argv[3], "w").write("\n".join(ids)); print(len(ids))
elif cmd == "img":
    ids = open(sys.argv[2]).read().split()
    out = sys.argv[3]
    for n in sys.argv[4:]:
        fn = os.path.join(out, "img%03d.jpg" % int(n))
        if os.path.exists(fn): continue
        b = get("https://api.rigsarkivet.dk/ao/v1/images/%s" % ids[int(n) - 1])
        open(fn, "wb").write(b); print(n, ids[int(n)-1], len(b)); time.sleep(1.6)
