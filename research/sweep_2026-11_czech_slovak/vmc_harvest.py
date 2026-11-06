"""Run VadeMeCum full-text terms and append parsed records to vmc_hits.jsonl."""
import json, os, re, sys, time
import vmc
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'vmc_hits.jsonl')
base = sys.argv[1]
seen = set()
if os.path.exists(OUT):
    for l in open(OUT, encoding='utf-8'):
        d = json.loads(l); seen.add((d['base'], d['xid'], d['title']))
with open(OUT, 'a', encoding='utf-8') as fh:
    for t in sys.argv[2:]:
        vmc.S.cookies.clear()
        try:
            r = vmc.search(base, t)
        except Exception as e:
            print('ERR', t, e); continue
        m = re.search(r'Found <b>([\d\s\xa0]+)</b>', r.text)
        n = m.group(1) if m else '?'
        recs = vmc.parse(r.text); new = 0
        for x in recs:
            k = (base, x['xid'], x['title'])
            if k in seen: continue
            seen.add(k); new += 1
            x.update(base=base, term=t); fh.write(json.dumps(x, ensure_ascii=False) + '\n')
        print(f'{t}: found {n}, parsed {len(recs)}, new {new}')
        time.sleep(1)
