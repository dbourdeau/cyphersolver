import requests, re, sys
sys.stdout.reconfigure(encoding='utf-8')
H = {'User-Agent':'Mozilla/5.0 (cyphersolver research sweep; polite)'}
r = requests.get('http://rgada.info/', headers=H, timeout=20)
r.encoding = r.apparent_encoding
print(r.status_code, r.encoding, len(r.text))
t = r.text
for m in re.finditer(r'href="([^"]+)"[^>]*>([^<]{3,80})<', t):
    print(m.group(1), '|', m.group(2).strip())
