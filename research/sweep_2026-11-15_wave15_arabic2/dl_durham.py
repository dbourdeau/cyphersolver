import json, os, sys, time, urllib.request
here = os.path.dirname(os.path.abspath(__file__))
for id_, tag in [('t2mks65hc530', 'hil64'), ('t1mh128nf091', 'hil65')]:
    m = json.load(open(os.path.join(here, 'raw', 'man_%s.json' % id_), encoding='utf8'))
    out = os.path.join(here, 'img', tag); os.makedirs(out, exist_ok=True)
    for i, c in enumerate(m['sequences'][0]['canvases']):
        svc = c['images'][0]['resource']['service']['@id']
        fn = os.path.join(out, '%03d_%s.jpg' % (i, ''.join(ch for ch in c['label'].split('/')[-1] if ch.isalnum() or ch in '-_')))
        if os.path.exists(fn) and os.path.getsize(fn) > 5000: continue
        for attempt in range(3):
            try:
                req = urllib.request.Request(svc + '/full/1024,/0/default.jpg', headers={'User-Agent': 'Mozilla/5.0'})
                d = urllib.request.urlopen(req, timeout=120).read()
                open(fn, 'wb').write(d); break
            except Exception as e:
                print('ERR', fn, e, flush=True); time.sleep(5)
        time.sleep(0.8)
print('done', flush=True)
