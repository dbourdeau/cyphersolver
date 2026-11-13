"""Fetch the raw PDF of a JACAR item (path is embedded in /das/image/<ref>) -> pdf/<ref>.pdf; render pages with --png."""
import sys, re, os, jacar, urllib.request
os.makedirs("pdf", exist_ok=True)
for ref in [a for a in sys.argv[1:] if not a.startswith("--")]:
    p = "pdf/%s.pdf" % ref
    if not os.path.exists(p):
        t = jacar.get(jacar.BASE + "/das/image/" + ref)
        m = re.search(r'"path":"([^"]+?\.pdf)"', t)
        if not m:
            print(ref, "no pdf path"); continue
        u = jacar.BASE + m.group(1).replace(chr(92), "")
        open(p, "wb").write(urllib.request.urlopen(urllib.request.Request(u, headers=jacar.UA), timeout=180).read())
    print(ref, os.path.getsize(p))
    if "--png" in sys.argv:
        import fitz
        os.makedirs("png", exist_ok=True)
        d = fitz.open(p)
        for i in range(min(len(d), 3)):
            d[i].get_pixmap(dpi=90).save("png/%s_%d.png" % (ref, i + 1))
