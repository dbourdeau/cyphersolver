# Fetch the 8 scans of Gelders Archief 0372 inv. 52 from the archieven.nl viewer (Zoomify tiles the viewer itself loads),
# stitched at a chosen zoom level. One tile request at a time. Output: scans/sNN.jpg (local only, not for git).
import sys, asyncio, re, io, math, time
from playwright.async_api import async_playwright
from PIL import Image
OUT = sys.argv[1]; LEVEL_DROP = int(sys.argv[2]) if len(sys.argv) > 2 else 0
URL = "https://www.archieven.nl/nl/zoeken?mivast=0&mizig=210&miadt=37&miview=inv2&milang=nl&mizk_alle=geheimschrift&micode=0372"
BASE = "https://preserve2.archieven.nl/iipsrv/iipsrv12.fcgi?Zoomify="
async def stitch(p, h, path):
    r = await p.request.get(BASE + h + "/ImageProperties.xml"); x = await r.text()
    W = int(re.search(r'WIDTH="(\d+)"', x).group(1)); H = int(re.search(r'HEIGHT="(\d+)"', x).group(1)); T = int(re.search(r'TILESIZE="(\d+)"', x).group(1))
    dims = []; w, hh = W, H
    while True:
        dims.append((w, hh))
        if w <= T and hh <= T: break
        w, hh = math.ceil(w/2), math.ceil(hh/2)
    dims.reverse()  # level 0 = smallest
    counts = [math.ceil(a/T)*math.ceil(b/T) for a, b in dims]
    NT = int(re.search(r'NUMTILES="(\d+)"', x).group(1))
    while sum(counts) > NT: dims.pop(0); counts.pop(0)  # server keeps fewer small levels
    # iipsrv here serves full resolution at level 4 for every scan of this item (checked: tile 4-11-16 is 184x1 on a 3000x4097 scan)
    lv = 4; lw, lh = W, H; cols, rows = math.ceil(lw/T), math.ceil(lh/T)
    before = sum(counts[:lv]); img = Image.new('RGB', (lw, lh), 'white')
    print('page', path, 'full', W, H, 'level', lv, lw, lh, cols*rows, 'tiles', flush=True)
    for yy in range(rows):
        for xx in range(cols):
            idx = before + yy*cols + xx; g = idx // 256
            rr = await p.request.get(f"{BASE}{h}/TileGroup{g}/{lv}-{xx}-{yy}.jpg")
            if rr.status != 200: print('tile', rr.status, lv, xx, yy); time.sleep(1); continue
            body = await rr.body()
            try: img.paste(Image.open(io.BytesIO(body)), (xx*T, yy*T))
            except Exception: print("bad tile", lv, xx, yy, rr.headers.get("content-type"), body[:120]); return
            await p.wait_for_timeout(150)
    img.save(path, quality=92)
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); p = await b.new_page(viewport={'width':1500,'height':1900})
        hashes = []
        def on_req(r):
            m = re.search(r'Zoomify=(cache%2Ffonc-gea%2F[0-9a-f]+\.jp2)', r.url)
            if m and m.group(1) not in hashes: hashes.append(m.group(1))
        p.on('request', on_req)
        await p.goto(URL, wait_until='networkidle', timeout=90000); await p.wait_for_timeout(3000)
        bt = p.locator('button.mi_btn_toggle').first
        if await bt.count(): await bt.click(); await p.wait_for_timeout(5000)
        await p.locator('.mi_inv_searchresults a.mi_hyperlink').filter(has_text=re.compile(r'^\s*52\s')).first.click(); await p.wait_for_timeout(6000)
        await p.locator('img.mi_stripthumb_img').first.click(); await p.wait_for_timeout(8000)
        fr = None
        for f in p.frames:
            try:
                ok = await f.evaluate(r"() => !!(document.body && /\/\s*\d+/.test(document.body.innerText) && document.querySelector('input'))")
            except Exception: ok = False
            if ok: fr = f
        pages = {1: hashes[-1]}
        for i in range(2, 9):
            n = len(hashes); inp = fr.locator('input').first; await inp.fill(str(i)); await inp.press('Enter')
            for _ in range(30):
                await p.wait_for_timeout(500)
                if len(hashes) > n: break
            pages[i] = hashes[-1]; await p.wait_for_timeout(2000)
        print(pages, flush=True)
        only = [int(a) for a in sys.argv[3].split(',')] if len(sys.argv) > 3 else list(pages)
        for i, h in pages.items():
            if i in only: await stitch(p, h, f"{OUT}/s{i:02d}.jpg")
        await b.close()
asyncio.run(main())
