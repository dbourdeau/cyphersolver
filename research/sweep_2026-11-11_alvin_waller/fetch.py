"""Fetch Alvin 600-px previews for a list made by select_*.py. usage: python3 fetch.py <list.json> <imgdir>
One request every 2 s; stops at the first 403/429."""
import sys, json, os, time, urllib.request, urllib.error
L = json.load(open(sys.argv[1])); D = sys.argv[2]; os.makedirs(D, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"}
for o in L:
    for n in o['take']:
        f = "%s/%s_%04d.jpg" % (D, o['id'], n)
        if os.path.exists(f): continue
        u = "https://www.alvin-portal.org/alvin/attachment/preview/alvin-record:%s/ATTACHMENT-%04d" % (o['id'], n)
        for a in range(3):
            try:
                b = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90).read()
                open(f, 'wb').write(b); break
            except urllib.error.HTTPError as e:
                print("HTTP", e.code, u, flush=True)
                if e.code in (403, 429): sys.exit("blocked")
                break
            except Exception as e:
                print("err", e, u, flush=True); time.sleep(15)
        time.sleep(2)
print("done", flush=True)
