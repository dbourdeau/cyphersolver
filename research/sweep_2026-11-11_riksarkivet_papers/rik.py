"""Helpers: resolve NAD id -> image series, count images (info.json bisection), contact sheets.
python rik.py resolve <refsubstr> ...   resolve every enum.json unit whose ref contains a substring -> units.json
python rik.py sheet <man> [k=24] [start] [end]   k evenly spaced images, 12 a sheet (3 cols, 520 px) -> scratch
python rik.py pick <man> <px> i j ...   single images
python rik.py range <man> a b [step]    every step-th image of a..b as sheets"""
import io, json, os, re, sys, time, requests
from PIL import Image, ImageDraw
H = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://sok.riksarkivet.se/'}
SP = os.environ.get('RIK_SP', '/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a2')
HERE = os.path.dirname(os.path.abspath(__file__)); U = HERE + '/units.json'
S = requests.Session(); S.headers.update(H)
def ok(man, i):
    for a in range(3):
        try:
            return S.get(f'https://lbiiif.riksarkivet.se/arkis!{man}_{i:05d}/info.json', timeout=40).status_code == 200
        except Exception: time.sleep(2)
    return False
def count(man):
    lo, hi = 1, 64
    if not ok(man, 1): return 0
    while ok(man, hi): lo = hi; hi *= 2
    while hi - lo > 1:
        m = (lo + hi) // 2
        if ok(man, m): lo = m
        else: hi = m
    return lo
def man_of(i, ref):
    r = requests.get(f'https://data.riksarkivet.se/archive/{i}.jsonld', headers={'User-Agent': 'curl/8.0'}, timeout=60).text
    m = re.search(r'arkis!([0-9A-Z]+)/manifest', r)
    if m: return m.group(1)
    r = requests.get('https://oai-pmh.riksarkivet.se/OAI/?verb=GetRecord&identifier=' + ref + '&metadataPrefix=oai_ape_ead', headers=H, timeout=60).text
    m = re.search(r'bildvisning/([0-9A-Z]+)', r)
    return m.group(1) if m else None
def units(): return json.load(open(U, encoding='utf-8')) if os.path.exists(U) else {}
def img(man, i, tw):
    u = f'https://lbiiif.riksarkivet.se/arkis!{man}_{i:05d}/full/{tw},/0/default.jpg'
    for a in range(3):
        try:
            r = S.get(u, timeout=90)
            if r.status_code == 200: return Image.open(io.BytesIO(r.content)).convert('L')
        except Exception: pass
        time.sleep(2)
    return Image.new('L', (tw, int(tw * 0.75)), 255)
def grid(tiles, labels, cols, tw, path):
    cap = int(tw * 0.78)
    tiles = [t if t.size[1] <= cap else t.resize((max(1, int(t.size[0] * cap / t.size[1])), cap)) for t in tiles]
    th = max(t.size[1] for t in tiles); rows = (len(tiles) + cols - 1) // cols
    out = Image.new('L', (cols * tw, rows * th), 200)
    for k, (t, lab) in enumerate(zip(tiles, labels)):
        d = ImageDraw.Draw(t); d.rectangle([0, 0, 40, 14], fill=255); d.text((2, 2), str(lab), fill=0)
        out.paste(t, ((k % cols) * tw, (k // cols) * th))
    out.save(path, quality=72); return path
def sheets(man, idx, tag, tw=520, per=12):
    for a in range(0, len(idx), per):
        ch = idx[a:a + per]; tiles = []
        for i in ch: tiles.append(img(man, i, tw)); time.sleep(0.5)
        print(grid(tiles, ch, 3, tw, f'{SP}/{man}_{tag}_{ch[0]}-{ch[-1]}.jpg'), flush=True)
if __name__ == '__main__':
    c = sys.argv[1]
    if c == 'resolve':
        e = json.load(open(HERE + '/enum.json', encoding='utf-8')); u = units()
        for x in e:
            if any(s in x['ref'] for s in sys.argv[2:]) and x['ref'] not in u:
                try:
                    man = man_of(x['id'], x['ref']); n = count(man) if man else 0
                except Exception as ex: man, n = None, str(ex)[:60]
                u[x['ref']] = dict(id=x['id'], man=man, n=n, caption=x['caption'], date=x['date'], note=(x['note'] or '')[:400], series=x['series'])
                print(x['ref'], man, n, flush=True); time.sleep(1.5)
                json.dump(u, open(U, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    elif c == 'sheet':
        man = sys.argv[2]; k = int(sys.argv[3]) if len(sys.argv) > 3 else 24
        n = next(v['n'] for v in units().values() if v['man'] == man)
        a = int(sys.argv[4]) if len(sys.argv) > 4 else 2; b = int(sys.argv[5]) if len(sys.argv) > 5 else n
        step = max(1, (b - a) / k); idx = sorted({int(round(a + i * step)) for i in range(k) if a + i * step <= b})
        sheets(man, idx, 's')
    elif c == 'range':
        man, a, b = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); st = int(sys.argv[5]) if len(sys.argv) > 5 else 1
        sheets(man, list(range(a, b + 1, st)), 'r')
    elif c == 'pick':
        man, px = sys.argv[2], int(sys.argv[3])
        for i in sys.argv[4:]:
            p = f'{SP}/{man}_{int(i):05d}_{px}.jpg'; img(man, int(i), px).save(p, quality=80); print(p); time.sleep(0.5)
