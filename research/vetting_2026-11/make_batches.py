"""Cut every lead still in question (no verdict, verdict open, or closed key_lookup) into batches by source.
   python research/vetting_2026-11/make_batches.py   writes in_bNN.json (10 leads each) and prints the batch sizes."""
import collections, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
L = json.loads((HERE.parents[1] / 'research/leads.json').read_text(encoding='utf-8'))['leads']
op = [x for x in L if (x.get('vetting') or {}).get('verdict') in (None, 'open', 'key_lookup')]
by = collections.defaultdict(list)
for x in op:
    by[(x.get('source') or 'none').split(',')[0]].append(x)
batches, cur = [], []
for src in sorted(by, key=lambda s: -len(by[s])):
    for x in sorted(by[src], key=lambda e: e['id']):
        cur.append(x)
        if len(cur) == 10:
            batches.append(cur); cur = []
if cur:
    batches.append(cur)
for n, b in enumerate(batches, 1):
    (HERE / f'in_b{n:02d}.json').write_text(json.dumps(b, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'b{n:02d}', len(b), sorted({(x.get('source') or 'none')[:40] for x in b})[:3])
