"""Read titles + image counts from LWL mets.xml for Ber.A M n (and other series). usage: lwl_titles.py PREFIX lo hi out.jsonl
PREFIX e.g. Ber/Ber.A/Ber.A_M  (a space and the number are appended)"""
import sys, re, json, time, requests, urllib.parse
pre, lo, hi, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0'
f = open(out, 'a', encoding='utf-8')
for n in range(lo, hi + 1):
    name = '%s %d' % (pre.split('/')[-1], n)
    u = 'https://www.lwl.org/325dig-download/Lesesaal-Digitalisate/C_Adelsarchive/%s%%20%d/mets.xml' % (pre, n)
    try:
        r = S.get(u, timeout=60)
    except Exception as e:
        print(n, 'ERR', e); time.sleep(3); continue
    if r.status_code == 429 or r.status_code == 403:
        print('STOP', r.status_code, n); break
    if r.status_code != 200:
        print(n, r.status_code); time.sleep(2); continue
    t = re.search(r'<mods:title>(.*?)</mods:title>', r.text, re.S)
    k = len(set(re.findall(r'xlink:href="([^"]+\.jpg)"', r.text)))
    row = {'name': name, 'title': t.group(1).strip() if t else '', 'images': k, 'url': u}
    f.write(json.dumps(row, ensure_ascii=False) + '\n'); f.flush()
    print(n, k, row['title'][:100], flush=True)
    time.sleep(2.5)
