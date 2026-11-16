"""Fetch one image politely and write a reduced copy for viewing.
   python -I -X utf8 fetch.py <name> <url> [maxpx] [referer]"""
import sys, time, urllib.request, io, os
from PIL import Image
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'
def get(url, referer=None):
    h = {'User-Agent': UA}
    if referer: h['Referer'] = referer
    r = urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=90)
    return r.read()
if __name__ == '__main__':
    name, url = sys.argv[1], sys.argv[2]
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 1800
    ref = sys.argv[4] if len(sys.argv) > 4 else None
    here = os.path.dirname(os.path.abspath(__file__))
    p = os.path.join(here, 'img', name + '.jpg')
    if not os.path.exists(p):
        open(p, 'wb').write(get(url, ref)); time.sleep(1)
    im = Image.open(p); print(name, im.size)
    im.thumbnail((mx, mx)); im.convert('RGB').save(os.path.join(here, 'img', name + '_v.jpg'), quality=85)
