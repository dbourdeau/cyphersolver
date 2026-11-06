"""Fetch Riksarkivet images of series 40008933, one at a time, >=1.5 s apart.
usage: python fetch.py <outdir> <width|max> <n> [<n> ...]"""
import sys, os, time, urllib.request
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass
out, w = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for n in sys.argv[3:]:
    n = int(n)
    fn = os.path.join(out, f"{n:03d}.jpg")
    if os.path.exists(fn) and os.path.getsize(fn) > 1000:
        continue
    size = "max" if w == "max" else f"{w},"
    url = f"https://lbiiif.riksarkivet.se/arkis!40008933_{n:05d}/full/{size}/0/default.jpg"
    req = urllib.request.Request(url, headers={"User-Agent": "WAINUT-research", "Referer": "https://sok.riksarkivet.se/"})
    try:
        data = urllib.request.urlopen(req, timeout=60).read()
    except Exception as e:
        print(n, "ERROR", e, flush=True)
        if "429" in str(e) or "403" in str(e):
            sys.exit(1)
        time.sleep(3); continue
    open(fn, "wb").write(data)
    print(n, len(data), flush=True)
    time.sleep(1.6)
