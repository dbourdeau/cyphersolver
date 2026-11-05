import requests, sys, re, json, base64, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')
H = {'User-Agent':'Mozilla/5.0 (cyphersolver research sweep; polite)'}
def txt(t): return re.sub(r'\s+',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S))
for u in ['https://library.hungaricana.hu/hu/search/results/?query=rejtjeles',
          'https://www.hungaricana.hu/hu/search/results/?query=rejtjeles',
          'https://library.hungaricana.hu/hu/collection/leveltari_iratok/',
          'https://library.hungaricana.hu/hu/search/results/?query=rejtjeles&collection=leveltari_iratok']:
    r = requests.get(u, headers=H, timeout=40)
    print(r.status_code, len(r.text), u)
    t = txt(r.text)
    print(re.sub(r'<[^>]+>',' ',t)[:700])
    for m in re.finditer(r'(?:name|id)="([^"]+)"', r.text):
        pass
    print([m for m in re.findall(r'<form[^>]*action="([^"]*)"', r.text)][:5])
    print('---')
