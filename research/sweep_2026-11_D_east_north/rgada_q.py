import requests, re, sys, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')
H = {'User-Agent':'Mozilla/5.0 (cyphersolver research sweep; polite)'}
def get(u):
    r = requests.get(u, headers=H, timeout=30)
    r.encoding = 'utf-8'
    return r.text
for term in ['шифр', 'цифир']:
    u = 'http://rgada.info/kueh/index.php?T1=' + urllib.parse.quote(term) + '&Sk=30&B1=' + urllib.parse.quote('Найти')
    t = get(u)
    print(term, len(t))
    body = re.sub(r'<[^>]+>', ' ', t)
    body = re.sub(r'\s+', ' ', body)
    print(body[:2500])
    print('----')
