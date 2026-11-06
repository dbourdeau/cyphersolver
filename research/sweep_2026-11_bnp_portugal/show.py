"""List manuscript records in details.jsonl that mention cipher terms: python show.py [regex]"""
import json, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
rx = re.compile(sys.argv[1] if len(sys.argv) > 1 else r'cifr|chiffr|cyfr|zifr|cripto|crypto|secret|segredo|chave|clave', re.I)
seen = set()
import glob
for l in (l for p in sorted(glob.glob(os.path.join(HERE, 'details*.jsonl'))) for l in open(p, encoding='utf-8')):
    r = json.loads(l)
    if r['bib'] in seen: continue
    seen.add(r['bib'])
    ms = 'Manuscrito' in r['text'] or 'Manuscritos' in r['exemplares'] or 'Arquivo' in r['exemplares'] or 'Espólio' in r['exemplares'] or 'Espolio' in r['exemplares']
    if not ms: continue
    t = r['text']
    hits = [t[max(0, m.start()-120):m.end()+120] for m in rx.finditer(t)]
    if not hits: continue
    ex = re.sub(r'^Exemplares\|Cota\|Colecao\|Tipo Acesso\|Estado\|', '', r['exemplares'])
    print('==', r['bib'], '|', ex[:90], '|', r['title'][:150], '|', r['fields'].get('PRODUÇÃO', ''))
    for h in hits[:3]: print('   ', h.replace('|', ' '))
