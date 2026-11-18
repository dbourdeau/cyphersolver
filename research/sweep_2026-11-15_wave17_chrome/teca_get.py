"""BNCF Teca: list a folder's images (azione=readBook) and download some (azione=showImg) to img/.
Usage: python -I -X utf8 teca_get.py BNCF0003856980 [first last]"""
import os, re, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
B = "https://teca.bncf.firenze.sbn.it/ImageViewer/servlet/ImageViewer?idr=%s&azione=%s"
def get(u):
    time.sleep(1.1)
    return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=90).read()
idr = sys.argv[1]
xml = get(B % (idr, "readBook")).decode("utf8", "replace")
ims = re.findall(r'<immagine ID="(\S+)\s*" mx-libro:sequenza="(\d+)"[^>]*><mx-libro:nomenclatura>([^<]*)<', xml)
for i, s, n in ims: print(s, i, n)
if len(sys.argv) > 3:
    a, b = int(sys.argv[2]), int(sys.argv[3])
    for i, s, n in ims:
        if a <= int(s) <= b:
            p = os.path.join(HERE, "img", f"{idr}_{int(s):02d}.jpg")
            if not os.path.exists(p):
                open(p, "wb").write(get(B % (i, "showImg")))
            print("saved", p, os.path.getsize(p))
