"""Fetch Riksarkivet IIIF images one at a time, >=1.6 s apart, UA WAINUT-research.
usage: python fetch.py <vol> <size> <img> [<img>|lo-hi ...]   (vol e.g. R0003590; size width or max)
       python fetch.py <vol> region <img> x,y,w,h <width>
Stops on 429/403 or non-image reply."""
import sys, time, urllib.request, urllib.error, os
UA = "WAINUT-research"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scans")
def get(url, path):
    if os.path.exists(path): return True
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            ct = r.headers.get("Content-Type", ""); data = r.read()
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, url)
        if e.code in (429, 403): sys.exit("blocked: stop")
        return False
    if "image" not in ct: sys.exit("non-image reply (%s): stop" % ct)
    open(path, "wb").write(data); print("ok", os.path.basename(path), len(data)); time.sleep(1.6); return True
if __name__ == "__main__":
    vol = sys.argv[1]; BASE = "https://lbiiif.riksarkivet.se/v3/arkis!" + vol + "_{:05d}"
    os.makedirs(OUT, exist_ok=True)
    if sys.argv[2] == "region":
        n, reg, w = int(sys.argv[3]), sys.argv[4], sys.argv[5]
        get(BASE.format(n) + "/%s/%s,/0/default.jpg" % (reg, w), os.path.join(OUT, "%s_%05d_%s_%s.jpg" % (vol, n, reg.replace(",", "-"), w)))
    else:
        size = sys.argv[2]; sz = "max" if size == "max" else size + ","
        for a in sys.argv[3:]:
            if "-" in a:
                lo, hi = map(int, a.split("-")); rng = range(lo, hi + 1)
            else: rng = [int(a)]
            for n in rng:
                get(BASE.format(n) + "/full/%s/0/default.jpg" % sz, os.path.join(OUT, "%s_%05d_w%s.jpg" % (vol, n, size)))
