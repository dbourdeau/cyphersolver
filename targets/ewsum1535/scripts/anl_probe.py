# archieven.nl viewer probe for Groninger Archieven 696 inv. 595 (port of Dan's anl_view2.js); logs image requests.
import sys, os, re, json
from playwright.sync_api import sync_playwright
ADT, CODE, TERM, UID = '5', '696', 'geheimschrift', '595'
out = sys.argv[1]; pages = [int(x) for x in sys.argv[2:]]
os.makedirs(out, exist_ok=True)
reqs = []
with sync_playwright() as pw:
    b = pw.chromium.launch()
    p = b.new_page(viewport={'width': 1500, 'height': 1900}, user_agent='WAINUT-research')
    p.on('request', lambda r: reqs.append(r.url) if r.resource_type in ('image','fetch','xhr') else None)
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
    print('pages', total, fr.url if fr else 'no frame')
    for i in pages:
        fn = os.path.join(out, f'p{i:04d}.png')
        if i > 1:
            inp = fr.locator('input').first; inp.fill(str(i)); inp.press('Enter')
            p.wait_for_timeout(7000)
        p.screenshot(path=fn, clip={'x': 70, 'y': 100, 'width': 1245, 'height': 1700})
        print('saved', fn)
    b.close()
json.dump(reqs, open(os.path.join(out,'reqs.json'),'w'), indent=0)
print(len(reqs))
