"""Download frames of NARA M30 (Despatches from U.S. Ministers to Great Britain) roll 2.
Usage: python dl_m30.py start end   (images go to images/m30/, git-ignored)"""
import sys, os, time, requests
from concurrent.futures import ThreadPoolExecutor
a, b = int(sys.argv[1]), int(sys.argv[2])
out = os.path.join(os.path.dirname(__file__), 'images', 'm30')
os.makedirs(out, exist_ok=True)
URL = 'https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M30/M30-002/M30-002-%04d.jpg'
def get(n):
    p = os.path.join(out, 'M30-002-%04d.jpg' % n)
    if os.path.exists(p) and os.path.getsize(p) > 10000:
        return
    for k in range(4):
        try:
            r = requests.get(URL % n, timeout=180, headers={'User-Agent': 'Mozilla/5.0 (research)'})
            if r.status_code == 200 and len(r.content) > 10000:
                open(p, 'wb').write(r.content); return
        except Exception:
            pass
        time.sleep(5)
    print('FAIL', n, flush=True)
with ThreadPoolExecutor(6) as ex:
    list(ex.map(get, range(a, b + 1)))
print('done')
