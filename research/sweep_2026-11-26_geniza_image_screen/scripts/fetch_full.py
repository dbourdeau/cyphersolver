"""usage: python3 -I fetch_full.py <pgpid> [k=1|2] [region=pct:x,y,w,h|full] [size=!2000,2000]
Downloads a larger image of a PGP document to scratchpad/full/<pgpid>_<k>[_region].jpg and prints the path."""
import csv, json, os, subprocess, sys, time
csv.field_size_limit(10**9)
S = '/tmp/claude-0/-home-user-cyphersolver/b1a9cfe8-0cc7-5c06-b209-188424217ec7/scratchpad'
pid = sys.argv[1]; k = int(sys.argv[2]) if len(sys.argv) > 2 else 1
region = sys.argv[3] if len(sys.argv) > 3 else 'full'; size = sys.argv[4] if len(sys.argv) > 4 else '!2000,2000'
rows = {x['pgpid']: x for x in csv.DictReader(open(S + '/pgpdump/documents.csv', encoding='utf-8-sig'))}
urls = [u for u in rows[pid]['iiif_urls'].replace(';', ' ').replace('|', ' ').split() if u.startswith('http')]
def curl(u, out=None):
    r = subprocess.run(['curl', '-sS', '-m', '90', '-A', 'Mozilla/5.0 (research)', '-w', '%{http_code}'] + (['-o', out] if out else [u][:0]) + [u], capture_output=True)
    return r
svc = None
u = urls[0]
if 'cudl.lib.cam.ac.uk' in u:
    base = u.rstrip('/').split('/')[-1]; svc = 'https://images.lib.cam.ac.uk/iiif/%s-000-%05d.jp2' % (base, k)
else:
    r = subprocess.run(['curl', '-sS', '-m', '60', '-A', 'Mozilla/5.0 (research)', u], capture_output=True)
    m = json.loads(r.stdout); sv = []
    for sq in m.get('sequences', []):
        for cv in sq.get('canvases', []):
            for im in cv.get('images', []):
                s = im.get('resource', {}).get('service', {}); sv.append(s.get('@id') or s.get('id'))
    for cv in m.get('items', []):
        for ap in cv.get('items', []):
            for an in ap.get('items', []):
                s = an.get('body', {}).get('service', [{}]); s = s[0] if isinstance(s, list) else s; sv.append(s.get('@id') or s.get('id'))
    sv = [x for x in sv if x]
    svc = sv[k - 1].rstrip('/') if len(sv) >= k else None
if not svc: print('no image', pid, k); sys.exit(1)
os.makedirs(S + '/full', exist_ok=True)
out = S + '/full/%s_%d%s.jpg' % (pid, k, '' if region == 'full' else '_' + region.replace(':', '').replace(',', '-'))
time.sleep(1)
subprocess.run(['curl', '-sS', '-m', '120', '-A', 'Mozilla/5.0 (research)', '-o', out, '%s/%s/%s/0/default.jpg' % (svc, region, size)])
print(out, os.path.getsize(out) if os.path.exists(out) else 'FAILED')
