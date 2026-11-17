"""Download the 96 images of ANC1-1-T-7519 (Arxius en linia static host) into img/t7519/, one request a second."""
import json, os, time, urllib.request
B = "https://backend.arxiusenlinia.cultura.gencat.cat/unitat/objects?codiReferencia=ANC1-1-T-7519"
H = {"User-Agent": "Mozilla/5.0", "Origin": "https://arxiusenlinia.cultura.gencat.cat"}
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img", "t7519")
os.makedirs(D, exist_ok=True)
objs = json.load(urllib.request.urlopen(urllib.request.Request(B, headers=H), timeout=60))
json.dump(objs, open(os.path.join(D, "objects.json"), "w"), indent=0)
for i, o in enumerate(objs, 1):
    p = os.path.join(D, f"{i:03d}.jpg")
    if os.path.exists(p): continue
    data = urllib.request.urlopen(urllib.request.Request(o["mediaUrl"], headers=H), timeout=90).read()
    open(p, "wb").write(data); time.sleep(1)
print(len(objs), "objects")
