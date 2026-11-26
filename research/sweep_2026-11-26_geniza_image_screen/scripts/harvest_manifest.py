"""Fallback: for CUDL documents with no image, read the CUDL manifest and download the first two page images."""
import csv, json, os, subprocess, sys, time
csv.field_size_limit(10**9)
S = '/tmp/claude-0/-home-user-cyphersolver/b1a9cfe8-0cc7-5c06-b209-188424217ec7/scratchpad'
rows = {x['pgpid']: x for x in csv.DictReader(open(S + '/pgpdump/documents.csv', encoding='utf-8-sig'))}
no = json.load(open(S + '/screen3/no_image.json'))
def curl(u, out=None):
    time.sleep(1.2)
    r = subprocess.run(['curl', '-sS', '-m', '90', '-A', 'Mozilla/5.0 (research screening; low rate)', '-w', '%{http_code}'] + (['-o', out] if out else []) + [u], capture_output=True)
    return r.stdout[-3:].decode(), r.stdout[:-3]
log = open(S + '/imgs/_log_manifest.jsonl', 'a'); got = 0
for pid in no:
    if os.path.exists(S + '/imgs/%s_1.jpg' % pid): continue
    us = [u for u in rows[pid]['iiif_urls'].replace(';', ' ').replace('|', ' ').split() if u.startswith('http')]
    k = 0
    for u in us:
        code, body = curl(u)
        if code != '200': log.write(json.dumps({'pgpid': pid, 'manifest': u, 'code': code}) + '\n'); continue
        try: m = json.loads(body)
        except Exception: continue
        svcs = []
        for sq in m.get('sequences', []):
            for cv in sq.get('canvases', []):
                for im in cv.get('images', []):
                    s = im.get('resource', {}).get('service', {}); svcs.append(s.get('@id') or s.get('id'))
        for sv in [x for x in svcs if x][:2]:
            if k >= 2: break
            out = S + '/imgs/%s_%d.jpg' % (pid, k + 1)
            c2, _ = curl(sv.rstrip('/') + '/full/!760,900/0/default.jpg', out)
            log.write(json.dumps({'pgpid': pid, 'k': k + 1, 'code': c2, 'svc': sv}) + '\n'); log.flush()
            if c2 == '200' and os.path.getsize(out) > 2000: k += 1
            elif os.path.exists(out): os.remove(out)
    if k: got += 1
print('recovered', got, 'of', len(no))
