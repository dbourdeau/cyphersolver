"""Fetch Riksarkivet IIIF images for R0003582 (Diplomatica Turcica I/9/21), one at a time, ~1.2 s apart.

usage: python fetch.py <size> <img> [<img> ...]     size e.g. 1400 (width), or max
       python fetch.py region <img> x,y,w,h <width>  (crop of the full-size image)
Stops on 429 or any non-image reply.
"""
import sys, time, urllib.request, os

UA = "WAINUT-research"
BASE = "https://lbiiif.riksarkivet.se/v3/arkis!R0003582_{:05d}"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scans")


def get(url, path):
    if os.path.exists(path):
        return True
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            ct = r.headers.get("Content-Type", "")
            data = r.read()
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, url)
        if e.code == 429:
            sys.exit("429: stop")
        return False
    if "image" not in ct:
        sys.exit("non-image reply (%s): stop" % ct)
    open(path, "wb").write(data)
    print("ok", path, len(data))
    time.sleep(1.2)
    return True


if __name__ == "__main__":
    if sys.argv[1] == "region":
        n, reg, w = int(sys.argv[2]), sys.argv[3], sys.argv[4]
        get(BASE.format(n) + "/%s/%s,/0/default.jpg" % (reg, w),
            os.path.join(OUT, "%05d_%s_%s.jpg" % (n, reg.replace(",", "-"), w)))
    else:
        size = sys.argv[1]
        sz = "max" if size == "max" else size + ","
        for a in sys.argv[2:]:
            if "-" in a:
                lo, hi = map(int, a.split("-"))
                rng = range(lo, hi + 1)
            else:
                rng = [int(a)]
            for n in rng:
                get(BASE.format(n) + "/full/%s/0/default.jpg" % sz, os.path.join(OUT, "%05d_w%s.jpg" % (n, size)))
