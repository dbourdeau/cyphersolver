"""Fetch URLs (one a second), save raw under img/raw/, print tag-stripped text around search terms.
python -I -X utf8 fetch_text.py <name> <url> [term ...]   (terms empty -> print first 4000 chars)"""
import sys, os, re, html, time, urllib.request
H = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(H, 'img', 'raw'); os.makedirs(R, exist_ok=True)
name, u, *terms = sys.argv[1:]
p = os.path.join(R, name)
if not os.path.exists(p):
    try:
        b = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90).read()
    except Exception as e:
        print('ERR', e); sys.exit(1)
    open(p, 'wb').write(b); time.sleep(1)
t = open(p, 'rb').read().decode('utf8', 'replace')
t = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', t, flags=re.S)
t = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t)))
print(len(t), 'chars')
if not terms:
    print(t[:4000])
for term in terms:
    hs = [m.start() for m in re.finditer(term, t, re.I)]
    print(f'"{term}": {len(hs)}')
    for h in hs[:12]:
        print('  ...', t[max(0, h - 250):h + 350])
