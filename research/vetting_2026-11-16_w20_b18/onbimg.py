"""python onbimg.py <manifest.json> <canvas index> [out] : download canvas image at max size"""
import json, sys, urllib.request
m = json.load(open(sys.argv[1], encoding='utf8')); i = int(sys.argv[2])
u = m['items'][i]['items'][0]['items'][0]['body']['id']
out = sys.argv[3] if len(sys.argv) > 3 else 'img/c%03d.jpg' % i
open(out, 'wb').write(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=120).read())
print(out, u)
