"""Fetch the ten cipher pages of BnF fr. 3157 ff. 152r-156v (Gallica btv1b90598645) at full resolution.
Each canvas is a two-page opening; L = left page (verso), R = right page (recto)."""
import os, time, urllib.request
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
ARK = "btv1b90598645"
PAGES = [("152r", 153, "R"), ("152v", 154, "L"), ("153r", 154, "R"), ("153v", 155, "L"), ("154r", 155, "R"),
         ("154v", 156, "L"), ("155r", 156, "R"), ("155v", 157, "L"), ("156r", 157, "R"), ("156v", 158, "L")]
REG = {"L": "pct:12,0,40,100", "R": "pct:51,0,43,100"}
os.makedirs("pages", exist_ok=True)
for fol, c, side in PAGES:
    fn = f"pages/f{fol}.jpg"
    if os.path.exists(fn) and os.path.getsize(fn) > 100000:
        continue
    url = f"https://gallica.bnf.fr/iiif/ark:/12148/{ARK}/f{c}/{REG[side]}/full/0/native.jpg"
    for t in range(5):
        try:
            d = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=180).read()
            open(fn, "wb").write(d); print(fol, len(d), flush=True); break
        except Exception as e:
            print(fol, "fail", e, flush=True); time.sleep(30)
    time.sleep(2)
