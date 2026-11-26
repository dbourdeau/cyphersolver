"""Fetch screening images for PGP documents. usage: harvest.py <group> ; groups: cudl | pu | gh
Reads pgpdump/documents.csv and tiers.json (t1 first). One request per second per process. Resumable (skips existing files)."""
import csv, json, os, subprocess, sys, time, urllib.parse
csv.field_size_limit(10**9)
S = '/tmp/claude-0/-home-user-cyphersolver/b1a9cfe8-0cc7-5c06-b209-188424217ec7/scratchpad'
group = sys.argv[1]
rows = {x['pgpid']: x for x in csv.DictReader(open(S + '/pgpdump/documents.csv', encoding='utf-8-sig'))}
t = json.load(open(S + '/pgpdump/tiers.json'))
ids = t['t1'] + t['t2']
UA = 'Mozilla/5.0 (research screening; low rate)'
last = [0.0]
def get(url, out=None, tries=2):
    for i in range(tries):
        d = 1.0 - (time.time() - last[0])
        if d > 0: time.sleep(d)
        last[0] = time.time()
        cmd = ['curl', '-sS', '-m', '60', '-A', UA, '-w', '%{http_code}', '-o', out or '-', url]
        r = subprocess.run(cmd, capture_output=True)
        code = r.stdout[-3:].decode() if out else r.stdout[-3:].decode()
        if out:
            if code == '200' and os.path.getsize(out) > 2000: return 200, None
            if code in ('404', '403', '401'): 
                if os.path.exists(out): os.remove(out)
                return int(code), None
        else:
            body = r.stdout[:-3]
            if code == '200': return 200, body
            if code in ('404', '403', '401'): return int(code), None
        time.sleep(3)
    if out and os.path.exists(out): os.remove(out)
    return 0, None
def services(manifest):
    out = []
    try: m = json.loads(manifest)
    except Exception: return out
    for sq in m.get('sequences', []):
        for cv in sq.get('canvases', []):
            for im in cv.get('images', []):
                s = im.get('resource', {}).get('service', {})
                sid = s.get('@id') or s.get('id')
                if sid: out.append(sid)
    for cv in m.get('items', []):
        for ap in cv.get('items', []):
            for an in ap.get('items', []):
                b = an.get('body', {})
                s = b.get('service', [{}])
                s = s[0] if isinstance(s, list) and s else (s if isinstance(s, dict) else {})
                sid = s.get('@id') or s.get('id')
                if sid: out.append(sid)
    return out
log = open(S + '/imgs/_log_%s.jsonl' % group, 'a')
def mine(pid):
    hs = []
    for u in rows[pid]['iiif_urls'].replace(';', ' ').replace('|', ' ').split():
        if u.startswith('http'): hs.append(u)
    if not hs: return None
    h = urllib.parse.urlparse(hs[0]).netloc
    g = 'cudl' if h == 'cudl.lib.cam.ac.uk' else ('gh' if h == 'princetongenizalab.github.io' else 'pu')
    return g if g == group else None
n = 0
for pid in ids:
    if mine(pid) != group: continue
    if os.path.exists(S + '/imgs/%s_1.jpg' % pid) or os.path.exists(S + '/imgs/%s_0.fail' % pid): continue
    k = 0
    urls = [u for u in rows[pid]['iiif_urls'].replace(';', ' ').replace('|', ' ').split() if u.startswith('http')]
    for u in urls:
        if k >= 2: break
        if group == 'cudl':
            base = u.rstrip('/').split('/')[-1]
            for j in (1, 2):
                if k >= 2: break
                svc = 'https://images.lib.cam.ac.uk/iiif/%s-000-%05d.jp2' % (base, j)
                code, _ = get(svc + '/full/!760,900/0/default.jpg', S + '/imgs/%s_%d.jpg' % (pid, k + 1))
                log.write(json.dumps({'pgpid': pid, 'k': k + 1, 'code': code, 'svc': svc}) + '\n'); log.flush()
                if code == 200: k += 1
                else: break
        else:
            code, body = get(u)
            if code != 200: log.write(json.dumps({'pgpid': pid, 'manifest': u, 'code': code}) + '\n'); log.flush(); continue
            for svc in services(body)[:2]:
                if k >= 2: break
                code, _ = get(svc.rstrip('/') + '/full/!760,900/0/default.jpg', S + '/imgs/%s_%d.jpg' % (pid, k + 1))
                log.write(json.dumps({'pgpid': pid, 'k': k + 1, 'code': code, 'svc': svc}) + '\n'); log.flush()
                if code == 200: k += 1
    if k == 0: open(S + '/imgs/%s_0.fail' % pid, 'w').close()
    n += 1
    if n % 100 == 0: print(group, n, flush=True)
print(group, 'done', n, flush=True)
