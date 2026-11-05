import requests, sys, re, json, base64
sys.stdout.reconfigure(encoding='utf-8')
H = {'User-Agent':'Mozilla/5.0 (cyphersolver research sweep; polite)'}
r = requests.get('https://www.hungaricana.hu/hu/adatbazisok/leveltar/', headers=H, timeout=30)
print(r.status_code, len(r.text))
print(re.sub(r'\s+',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',r.text,flags=re.S))[:200])
for m in re.finditer(r'href="([^"]+)"', r.text):
    h=m.group(1)
    if 'search' in h or 'kereso' in h or 'leveltar' in h: print(h)
