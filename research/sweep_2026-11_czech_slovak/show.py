import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
base = sys.argv[1] if len(sys.argv) > 1 else ''
for l in open('aron_hits.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if base not in d['base']:
        continue
    txt = (d['name'] or '') + ' | ' + (d['description'] or '')
    if d['term'] in ('klíč', 'klíče') and not re.search(r'šifr|chiffr|tajn|písm|cifr|zifr|dopis|korespond|list', txt, re.I):
        continue
    print(d['term'], '::', d['id'][:8], txt.replace('\n', ' ')[:330])
