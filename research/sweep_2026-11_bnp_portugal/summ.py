"""Compact summary of detail records whose shelfmark matches a regex: python summ.py '<shelf regex>' [cipher regex]"""
import json, re, sys, os, glob
HERE = os.path.dirname(os.path.abspath(__file__))
srx = re.compile(sys.argv[1])
crx = re.compile(sys.argv[2] if len(sys.argv) > 2 else r'cifr|chiffr|decifr|zifr|c[óo]dig|chave|segredo|secret', re.I)
seen = set()
for p in sorted(glob.glob(os.path.join(HERE, 'details*.jsonl'))):
    for l in open(p, encoding='utf-8'):
        r = json.loads(l)
        if r['bib'] in seen: continue
        seen.add(r['bib'])
        ex = re.sub(r'^Exemplares\|Cota\|(Fasciculo\|)?Colecao\|Tipo Acesso\|Estado\|', '', r['exemplares'])
        if not srx.search(ex): continue
        t = r['text']
        hits = [t[max(0, m.start()-200):m.end()+200].replace('|', ' ') for m in crx.finditer(t)]
        if not hits: continue
        f = r['fields']
        print('==', r['bib'], '|', ex[:60], '|', r['title'][:230])
        print('   PROD:', f.get('PRODUÇÃO', ''), '| DESC:', f.get('DESCR.FÍSICA', '')[:60])
        for h in hits[:3]: print('   >', h)
