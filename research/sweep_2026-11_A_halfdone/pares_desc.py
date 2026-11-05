"""Fetch PARES description pages (catalogo/description/<id>) for a few ids, one at a time (sweep.fetch spacing),
and append {id, signatura, fechas, titulo, alcance, images} to desc.jsonl.

    python pares_desc.py 1520934 363113 ...
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sweep

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
done = set()
p = os.path.join(HERE, 'desc.jsonl')
if os.path.exists(p):
    done = {json.loads(l)['id'] for l in open(p, encoding='utf-8')}
op = sweep.opener()
for pid in sys.argv[1:]:
    if pid in done:
        continue
    h = sweep.fetch(op, f'{sweep.BASE}/description/{pid}')
    sweep.save_raw('desc_' + pid, 'd', h)
    t = re.sub(r'(?s)<script.*?</script>|<style.*?</style>', '', h)
    t = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t)))
    i = t.find('Resultados de la b')
    j = t.find('Signatura')
    body = t[j:j + 2200] if j >= 0 else t[:1500]
    rec = {'id': pid, 'text': body, 'images': f'catalogo/show/{pid}' in h}
    with open(p, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(pid, 'IMG' if rec['images'] else '-', body[:1100])
    print()
