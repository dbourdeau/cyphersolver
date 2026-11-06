"""Page through every hit of one catalogue query and fetch each full record (for fonds whose long CONTEM notes the
keyword index misses):  python crawl.py <name> <query> [COLL]   -> crawl_<name>.jsonl (bib, title) then details.jsonl
"""
import json, os, sys, time
import harvest, details
HERE = os.path.dirname(os.path.abspath(__file__))
name, q = sys.argv[1], sys.argv[2]
coll = sys.argv[3] if len(sys.argv) > 3 else ''
lim = '&limitbox_1=COL01+%3D+' + coll if coll else ''
out = os.path.join(HERE, f'crawl_{name}.jsonl')
bibs = []
if os.path.exists(out):
    bibs = [json.loads(l)['bib'] for l in open(out, encoding='utf-8')]
if not bibs:
    total, h = harvest.parse(harvest.get(harvest.BASE + q + lim))
    allh = list(h); page = 2
    while len(allh) < total:
        time.sleep(0.6)
        _, h = harvest.parse(harvest.get(harvest.BASE + q + lim + f'&page={page}'))
        if not h: break
        allh += h; page += 1
    with open(out, 'w', encoding='utf-8') as fh:
        for b, t in allh:
            fh.write(json.dumps({'bib': b, 'title': t}, ensure_ascii=False) + '\n')
    bibs = [b for b, t in allh]
    print(name, total, len(bibs), file=sys.stderr)
sys.argv = ['details.py'] + [str(b) for b in dict.fromkeys(bibs)]
details.main()
