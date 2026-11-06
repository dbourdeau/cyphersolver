"""Page a catalogue query to a bib list only: python crawl_list.py <name> <query> [COLL] -> crawl_<name>.jsonl"""
import json, os, sys, time
import harvest
HERE = os.path.dirname(os.path.abspath(__file__))
name, q = sys.argv[1], sys.argv[2]
coll = sys.argv[3] if len(sys.argv) > 3 else ''
lim = '&limitbox_1=COL01+%3D+' + coll if coll else ''
total, h = harvest.parse(harvest.get(harvest.BASE + q + lim))
allh = list(h); page = 2; fails = 0
while len(allh) < total and fails < 5:
    time.sleep(0.8)
    _, h = harvest.parse(harvest.get(harvest.BASE + q + lim + f'&page={page}'))
    if not h:
        fails += 1; time.sleep(5); continue
    allh += h; page += 1
with open(os.path.join(HERE, f'crawl_{name}.jsonl'), 'w', encoding='utf-8') as fh:
    for b, t in allh:
        fh.write(json.dumps({'bib': b, 'title': t}, ensure_ascii=False) + '\n')
print(name, total, len(allh))
