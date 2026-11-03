"""Fetch Estense IIIF pages by tiles (<=1500x640 regions), one request at a time, ~1.1 s apart, UA WAINUT-research.
Usage: python fetch.py manifests            -> writes scans/manifests.json (canvas list)
       python fetch.py page <uuid> <idx> <name> [scale]  -> stitched scans/<name>.jpg
Images are CC BY-NC-SA: kept in scans/ (git-ignored), never committed."""
import sys, json, time, io, os, urllib.request, urllib.error
from PIL import Image
UA = {"User-Agent": "WAINUT-research"}
HERE = os.path.dirname(os.path.abspath(__file__)); SC = os.path.join(HERE, "..", "scans")
UUIDS = {"c01-02": "b70e7528-3bf3-46cd-b78d-a956fd528f6f", "c03-04": "7320ae85-1d75-4b1f-81ae-662ebae08782",
         "c05-08": "65514839-924d-447b-962f-547fa30c0f7f", "c09-11": "430bc92b-78c5-49be-b3c4-37e39090847d",
         "c22-23": "cb2a1bd0-5e3c-457a-88b4-088942578c2d"}
def get(url, binary=False):
    time.sleep(1.1)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code == 429: sys.exit("STOP 429")
        raise
def manifests():
    out = {}
    for k, u in UUIDS.items():
        m = json.loads(get(f"https://edl-jarvis.cultura.gov.it/meta/iiif/{u}/manifest"))
        cans = m.get("sequences", [{}])[0].get("canvases") or m.get("items")
        rows = []
        for c in cans:
            if "images" in c:
                svc = c["images"][0]["resource"]["service"]["@id"]
            else:
                body = c["items"][0]["items"][0]["body"]; s = body["service"]; s = s[0] if isinstance(s, list) else s
                svc = s.get("@id") or s.get("id")
            lab = c.get("label"); lab = lab if isinstance(lab, str) else json.dumps(lab, ensure_ascii=False)
            rows.append({"label": lab, "w": c["width"], "h": c["height"], "svc": svc})
        out[k] = rows
    json.dump(out, open(os.path.join(SC, "manifests.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    for k, rows in out.items():
        for i, r in enumerate(rows): print(k, i, r["label"], r["w"], r["h"])
def page(key, idx, name, scale=1.0):
    rows = json.load(open(os.path.join(SC, "manifests.json"), encoding="utf-8"))[key]
    r = rows[int(idx)]; W, H, svc = r["w"], r["h"], r["svc"]
    tw, th = 1500, 640
    canvas = Image.new("RGB", (int(W*scale), int(H*scale)), "white")
    for y in range(0, H, th):
        for x in range(0, W, tw):
            w, h = min(tw, W-x), min(th, H-y)
            ow = max(1, int(round(w*scale)))
            data = get(f"{svc}/{x},{y},{w},{h}/{ow},/0/default.jpg")
            im = Image.open(io.BytesIO(data)).convert("RGB")
            canvas.paste(im, (int(x*scale), int(y*scale)))
    p = os.path.join(SC, name + ".jpg"); canvas.save(p, quality=92); print(p, canvas.size)
if __name__ == "__main__":
    if sys.argv[1] == "manifests": manifests()
    elif sys.argv[1] == "page": page(sys.argv[2], sys.argv[3], sys.argv[4], float(sys.argv[5]) if len(sys.argv) > 5 else 1.0)

def crop(key, idx, name, X0, Y0, X1, Y1, scale=1.0):
    """Stitch a full-resolution region (canvas coords) from tiles of at most 1500x640."""
    rows = json.load(open(os.path.join(SC, "manifests.json"), encoding="utf-8"))[key]
    svc = rows[int(idx)]["svc"]
    W, H = X1 - X0, Y1 - Y0
    out = Image.new("RGB", (int(W*scale), int(H*scale)), "white")
    for y in range(Y0, Y1, 640):
        for x in range(X0, X1, 1500):
            w, h = min(1500, X1-x), min(640, Y1-y)
            data = get(f"{svc}/{x},{y},{w},{h}/{max(1,int(round(w*scale)))},/0/default.jpg")
            out.paste(Image.open(io.BytesIO(data)).convert("RGB"), (int((x-X0)*scale), int((y-Y0)*scale)))
    p = os.path.join(SC, name + ".jpg"); out.save(p, quality=92); print(p, out.size)
if __name__ == "__main__" and sys.argv[1] == "crop":
    a = sys.argv; crop(a[2], a[3], a[4], *map(int, a[5:9]), float(a[9]) if len(a) > 9 else 1.0)
