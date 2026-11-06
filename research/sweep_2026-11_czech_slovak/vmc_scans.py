"""Download scanned finding-aid pages from NA VadeMeCum (Zoomify tiles, tier 3 ~1240 px wide) for OCR.
Usage: python vmc_scans.py <search term> <result index> <out_dir> [max_pages]"""
import io, math, os, re, sys, html, time
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import vmc
sys.stdout.reconfigure(encoding='utf-8')
ROOT = 'https://vademecum.nacr.cz'


def tiers(w, h, ts=256):
    t = [(w, h)]
    while w > ts or h > ts:
        w, h = (w + 1) // 2, (h + 1) // 2
        t.append((w, h))
    return t[::-1]


def page(path, w, h, want=3):
    tl = tiers(w, h)
    want = min(want, len(tl) - 1)
    before = sum(math.ceil(a / 256) * math.ceil(b / 256) for a, b in tl[:want])
    W, H = tl[want]
    nx, ny = math.ceil(W / 256), math.ceil(H / 256)
    img = Image.new('RGB', (W, H), 'white')
    jobs = [(x, y, f'{path}/TileGroup{(before + y * nx + x) // 256}/{want}-{x}-{y}.jpg') for y in range(ny) for x in range(nx)]

    def get(j):
        for _ in range(3):
            try:
                r = vmc.S.get(j[2], timeout=60)
                if r.ok:
                    return j, r.content
            except Exception:
                time.sleep(2)
        return j, None
    with ThreadPoolExecutor(6) as ex:
        for (x, y, _), c in ex.map(get, jobs):
            if c:
                img.paste(Image.open(io.BytesIO(c)), (x * 256, y * 256))
    return img


if __name__ == '__main__':
    term, k, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    maxp = int(sys.argv[4]) if len(sys.argv) > 4 else 9999
    os.makedirs(out, exist_ok=True)
    r = vmc.search('https://vademecum.nacr.cz/vademecum', term)
    blocks = re.findall(r'<aricle class="contentRecordList.*?</aricle>', r.text, re.S)
    z = re.search(r'href="(/vademecum/Zoomify\.action\?[^"]*)"', blocks[k]).group(1)
    p = vmc.S.get(ROOT + html.unescape(z), timeout=60).text
    i = 0
    while i < maxp:
        fn = os.path.join(out, f'p{i:04d}.jpg')
        m = re.search(r'var zoomifyImgPath = "([^"]+)"', p)
        wh = re.search(r"WIDTH='(\d+)' HEIGHT='(\d+)'", p)
        if not m or not wh:
            print('stop at', i); break
        if not os.path.exists(fn):
            page(m.group(1), int(wh.group(1)), int(wh.group(2))).save(fn, quality=85)
            time.sleep(0.2)
        nxt = re.findall(r'href="(/vademecum/PaginatorMedia\.action\?[^"]*row=%d)"' % (i + 1), p)
        if not nxt:
            print('last page', i); break
        p = vmc.S.get(ROOT + html.unescape(nxt[0]), timeout=60).text
        i += 1
    print('done', out, i + 1)
