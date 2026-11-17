"""Report raw/datecheck.jsonl: for each clean cipher date, list every Türkei I regest of that date, flagging those that
look like a clear text of the despatch (copy, extract, decipherment, translation, content summary) as CLEAR."""
import json, re, sys
CLEAR = re.compile(r'feloldás\)|feloldás,|feloldás$|\(német feloldás|német más|másolat|kivonat|Extract|Auszug|fordítás|feloldva|clear', re.I)
rows = [json.loads(l) for l in open('raw/datecheck.jsonl', encoding='utf8')]
lead = int(sys.argv[1]) if len(sys.argv) > 1 else None
for r in rows:
    if lead and r['lead'] != lead: continue
    tags = []
    print(f"== {r['lead']} {r['date']} cipher {r['cipher_ids']}")
    for x in r['rows']:
        if 'error' in x: print('   ERR', x['id']); continue
        kind = 'CIPHER' if x['id'] in r['cipher_ids'] else ('CLEAR?' if CLEAR.search(x['desc']) or len(x['desc']) > 250 else '')
        tags.append(kind)
        print(f"   {kind:6} {x['id']} | {x['ref'][17:75]} | {x['date'][:40]} | {x['desc'][:230]}")
    print('   VERDICT:', 'clear copy likely' if 'CLEAR?' in tags else 'no clear copy found')
