"""Nationaal Archief: item-title search for terms the Oct sweep (research/nationaal_archief/harvest.py) did not run."""
import json, sys, time, re
sys.path.insert(0, '../nationaal_archief'); import harvest as H
old = set()
for l in open('../nationaal_archief/hits.jsonl', encoding='utf8'):
    d = json.loads(l); old.add((d['ead'], d['title_id']))
TERMS = sys.argv[1:]
out = open('na_hits.jsonl', 'a', encoding='utf8'); seen = set()
for t in TERMS:
    arcs = H.archives(t); n = 0; na = 0
    for a in arcs:
        ead = a.get('eadID') or a.get('eadid') or a.get('id'); per = a.get('period') or a.get('unitdate') or ''
        if H.start_year(per) > 1900 or ead == '1.04.02': continue
        na += 1
        for it in H.items(ead, t):
            k = (ead, it.get('id') or it.get('title_id') or json.dumps(it)[:80])
            if k in seen: continue
            seen.add(k); n += 1
            out.write(json.dumps({'term': t, 'ead': ead, 'archive': a.get('title'), 'period': per, 'item': it}, ensure_ascii=False) + '\n')
        out.flush(); time.sleep(0.4)
    print(t, 'archives', len(arcs), 'pre-1900', na, 'new items', n, flush=True)
