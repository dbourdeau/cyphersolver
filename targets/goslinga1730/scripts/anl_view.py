# archieven.nl viewer screenshots (Python port of Dan's research/sweep_2026-11-11_dutch_2/anl_view2.js),
# set for Gelders Archief 0613 inv. 3889. usage: python anl_view.py <outdir> <page> [<page> ...]
# env: DSF (device scale factor), WAIT (ms per page), ZOOM (number of zoom-in clicks, default 0)
import sys, os, re
from playwright.sync_api import sync_playwright
ADT, CODE, TERM, UID = '37', '0613', 'Goslinga', '3889'
out = sys.argv[1]; pages = [int(x) for x in sys.argv[2:]]
os.makedirs(out, exist_ok=True)
W = int(os.environ.get('VW', '1500')); H = int(os.environ.get('VH', '1900'))
with sync_playwright() as pw:
    b = pw.chromium.launch()
    p = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=float(os.environ.get('DSF', '1')), user_agent='WAINUT-research')
    p.goto(f'https://www.archieven.nl/nl/zoeken?mivast=0&mizig=210&miadt={ADT}&miview=inv2&milang=nl&mizk_alle={TERM}&micode={CODE}', wait_until='networkidle', timeout=90000)
    p.wait_for_timeout(3000)
    bt = p.locator('button.mi_btn_toggle').first
    if bt.count():
        try: bt.click()
        except Exception: pass
        p.wait_for_timeout(5000)
    a = p.locator('.mi_inv_searchresults a.mi_hyperlink').filter(has_text=re.compile(r'^\s*' + UID + r'\s')).first
    try: a.click()
    except Exception as e: print('item not found', e)
    p.wait_for_timeout(6000)
    try: p.locator('img.mi_stripthumb_img').first.click()
    except Exception as e: print('no thumbs', e)
    p.wait_for_timeout(8000)
    fr, total = None, 0
    for f in p.frames:
        try:
            m = f.evaluate("() => { const m = document.body ? document.body.innerText.match(/\/\s*(\d+)/) : null; return m && document.querySelector('input') ? parseInt(m[1]) : 0; }")
        except Exception: m = 0
        if m: fr, total = f, m
    print('pages', total, fr.url[:150] if fr else 'no frame')
    if os.environ.get('DUMP'):
        p.screenshot(path=os.path.join(out, 'full_dump.png'))
        open(os.path.join(out, 'frame_dump.html'), 'w', encoding='utf8').write(fr.content() if fr else '')
    for i in pages:
        fn = os.path.join(out, f'p{i:04d}.png')
        if os.path.exists(fn): continue
        inp = fr.locator('input').first; inp.fill(str(i)); inp.press('Enter')
        p.wait_for_timeout(int(os.environ.get('WAIT', '6000')))
        p.screenshot(path=fn, clip={'x': 70, 'y': 100, 'width': W - 255, 'height': H - 200})
        print('saved', fn, flush=True)
    b.close()
