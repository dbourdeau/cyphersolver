"""Fetch Estense IIIF images politely (one request at a time, ~1 s apart).

usage:
  fetch.py MANIFEST OUTDIR overview IDX [WIDTH]          -> scaled full canvas
  fetch.py MANIFEST OUTDIR region IDX X Y W H [NAME]     -> full-size region, fetched in tiles <=1500x640, stitched
Images are CC BY-NC-SA; they stay in scans/ (git-ignored), never committed.
"""
import json, sys, time, io, os, urllib.request
from PIL import Image

UA = {"User-Agent": "WAINUT-research"}
TW, TH = 1500, 640


def get(url):
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            time.sleep(1.0)
            return data
        except Exception as e:
            print("ERR", url, e)
            if "429" in str(e):
                sys.exit("429: stop")
            time.sleep(3)
    raise SystemExit("fetch failed twice: " + url)


def canvases(man):
    m = json.load(open(man, encoding="utf-8"))
    out = []
    for c in m["sequences"][0]["canvases"]:
        svc = c["images"][0]["resource"]["service"]["@id"]
        out.append((c["label"], svc, c["width"], c["height"]))
    return out


def main():
    man, outdir, mode, idx = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
    os.makedirs(outdir, exist_ok=True)
    label, svc, W, H = canvases(man)[idx]
    if mode == "overview":
        w = int(sys.argv[5]) if len(sys.argv) > 5 else 1000
        data = get(f"{svc}/full/{w},/0/default.jpg")
        p = os.path.join(outdir, f"c{idx}_ov{w}.jpg")
        open(p, "wb").write(data)
        print(p, label, W, H)
        return
    x, y, w, h = map(int, sys.argv[5:9])
    name = sys.argv[9] if len(sys.argv) > 9 else f"c{idx}_{x}_{y}_{w}_{h}"
    w = min(w, W - x); h = min(h, H - y)
    img = Image.new("RGB", (w, h), "white")
    for ty in range(y, y + h, TH):
        for tx in range(x, x + w, TW):
            tw, th = min(TW, x + w - tx), min(TH, y + h - ty)
            data = get(f"{svc}/{tx},{ty},{tw},{th}/full/0/default.jpg")
            img.paste(Image.open(io.BytesIO(data)), (tx - x, ty - y))
    p = os.path.join(outdir, name + ".jpg")
    img.save(p, quality=92)
    print(p, label, W, H)


if __name__ == "__main__":
    main()
