# python3 fetch_all.py <scratch>  -- sequential openapi.bnf.fr IIIF fetch at 800 px, volumes in priority order; resumable
import sys, os, time, urllib.request
S = sys.argv[1]
VOLS = [('15905b','btv1b9063808z',363),('15905a','btv1b90638227',341),('15911','btv1b52521582d',907),('15904','btv1b9064051h',480),
        ('15903b','btv1b9064052x',436),('15903a','btv1b10501677p',858),('15902','btv1b9063602s',627),('15894','btv1b525216318',1168),
        ('15897','btv1b9057357p',580),('15898a','btv1b90643252',422),('15898b','btv1b9064324n',412),('15890','btv1b105073513',988)]
if len(sys.argv) > 2: VOLS = [v for v in VOLS if v[0] in sys.argv[2:]]
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36', 'Accept': 'image/jpeg'}
for name, ark, n in VOLS:
    out = f'{S}/{name}'; os.makedirs(out, exist_ok=True)
    for i in range(1, n + 1):
        fn = f'{out}/c{i:04d}.jpg'
        if os.path.exists(fn) and os.path.getsize(fn) > 3000: continue
        url = f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ark}/f{i}/full/800,/0/default.jpg'
        for t in range(4):
            try:
                d = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
                open(fn + '.tmp', 'wb').write(d); os.rename(fn + '.tmp', fn); break
            except Exception as e:
                if '429' in str(e) or '403' in str(e): print('BLOCK', name, i, e, flush=True); sys.exit()
                print('fail', name, i, str(e)[:60], flush=True); time.sleep(8 * (t + 1))
        time.sleep(1.0)
    print('DONE', name, flush=True)
