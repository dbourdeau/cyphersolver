# One process, 3 s between images, 800 px. Order set by the coordinator 9 Nov 2026.
import sys, os, time, urllib.request
SC = sys.argv[1]
Q = [('btv1b90638227','15905a'),('btv1b9063808z','15905b'),('btv1b52521582d','15911'),('btv1b9064051h','15904'),
     ('btv1b10501677p','15903a'),('btv1b9064052x','15903b'),('btv1b525216318','15894'),('btv1b9063602s','15902'),
     ('btv1b9057357p','15897'),('btv1b90643252','15898a'),('btv1b9064324n','15898b')]
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) cyphersolver research', 'Accept': 'image/jpeg'}
for ark, name in Q:
    out = f'{SC}/w_{name}'; os.makedirs(out, exist_ok=True)
    i = 4
    while True:
        i += 1
        fn = f'{out}/c{i:03d}.jpg'
        if os.path.exists(fn) and os.path.getsize(fn) > 3000: continue
        url = f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ark}/f{i}/full/800,/0/default.jpg'
        ok = False
        for t in range(4):
            try:
                open(fn, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()); ok = True; break
            except Exception as e:
                s = str(e)
                if '404' in s: ok = None; break
                if '429' in s or '403' in s: print('BLOCK', name, i, s, flush=True); sys.exit()
                time.sleep(8 * (t + 1))
        if ok is None: print('END', name, i, flush=True); break
        time.sleep(3)
    print('VOLDONE', name, flush=True)
