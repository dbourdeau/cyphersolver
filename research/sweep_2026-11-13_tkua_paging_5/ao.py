"""Rigsarkivet Arkivalieronline helpers (works with curl-type requests from the cloud network, 11 Nov 2026).
  Daisy series page  https://daisy.rigsarkivet.dk/arkivserie_detaljer?heid=<daisyId>   -> link billedviser?epid=<epid>
  tree               https://api.rigsarkivet.dk/ao/v1/billedviser/indeks-top?epid=<epid>   (units: key = bsid, title)
  image list         https://api.rigsarkivet.dk/ao/v1/billedviser/billed-reference-lister?bsid=<bsid>
  image              https://api.rigsarkivet.dk/ao/v1/images/<bid>   (full size JPEG, about 1 MB)
  viewer link        https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=<epid>#<bsid>,<bid>
usage:
  python3 ao.py epid <daisyId> ...            print epid and unit tree with image counts
  python3 ao.py sheet <bsid> <outdir> [stride] [width]   contact sheets (12 per sheet) of every <stride>th image
  python3 ao.py get <bid> <out.jpg> [width]
"""
import sys, re, os, json, time, io, urllib.request
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/126.0 Safari/537.36", "Referer": "https://arkivalieronline.rigsarkivet.dk/"}
def get(u, binary=False):
    for a in range(5):
        try:
            b = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
            return b if binary else b.decode("utf-8", "replace")
        except Exception as e:
            err = e; time.sleep(6)
    raise RuntimeError("%s: %s" % (u, err))
def epid(heid):
    m = re.search(r"billedviser\?epid=(\d+)", get("https://daisy.rigsarkivet.dk/arkivserie_detaljer?heid=%s" % heid))
    return m.group(1) if m else None
def top(ep): return json.loads(get("https://api.rigsarkivet.dk/ao/v1/billedviser/indeks-top?epid=%s" % ep))
def refs(bsid): return [g.split(",")[1] for g in json.loads(get("https://api.rigsarkivet.dk/ao/v1/billedviser/billed-reference-lister?bsid=%s" % bsid))["SA_GUIDs"]]
def image(bid, width=None):
    from PIL import Image
    im = Image.open(io.BytesIO(get("https://api.rigsarkivet.dk/ao/v1/images/%s" % bid, True)))
    if width: im.draft("RGB", (width * 2, width * 2))   # decode at reduced scale: much faster for sheets
    im = im.convert("RGB")
    if width: im = im.resize((width, int(im.height * width / im.width)))
    return im
def sheet(bsid, out, stride=15, width=620, cols=4, rows=3, start=0, stop=None):
    from PIL import Image, ImageDraw
    os.makedirs(out, exist_ok=True); ids = refs(bsid); pick = list(range(start, min(stop or len(ids), len(ids)), stride)); made = []
    for s in range(0, len(pick), cols * rows):
        fn = os.path.join(out, "%s_s%d_%04d.jpg" % (bsid, stride, pick[s]))
        made.append(fn)
        if os.path.exists(fn): continue
        ims = []
        for i in pick[s:s + cols * rows]:
            try: im = image(ids[i], width)
            except Exception as e: print("fail", i, e); continue
            ImageDraw.Draw(im).rectangle([0, 0, 110, 26], fill="white"); ImageDraw.Draw(im).text((4, 6), "img %d" % (i + 1), fill="red")
            ims.append(im); time.sleep(0.8)
        if not ims: continue
        h = max(i.height for i in ims); S = Image.new("RGB", (cols * width, ((len(ims) + cols - 1) // cols) * h), "white")
        for k, im in enumerate(ims): S.paste(im, ((k % cols) * width, (k // cols) * h))
        S.save(fn, quality=70)
    print(len(ids), "images;", "\n".join(made))
if __name__ == "__main__":
    c = sys.argv[1]
    if c == "epid":
        for h in sys.argv[2:]:
            ep = epid(h); print(h, "epid", ep, flush=True)
            if ep:
                for u in top(ep):
                    try: n = len(refs(u["key"]))
                    except Exception: n = "?"
                    print("  ", u["key"], n, u["title"].strip(), flush=True); time.sleep(1)
            time.sleep(1)
    elif c == "sheet": sheet(sys.argv[2], sys.argv[3], *(int(x) for x in sys.argv[4:]))
    elif c == "get": image(sys.argv[2], int(sys.argv[4]) if len(sys.argv) > 4 else None).save(sys.argv[3], quality=85)
