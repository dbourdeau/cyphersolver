"""Re-estimate digit-confusion costs from a beam_seq.json: cost = -log P(true digit | read digit) with add-0.5 smoothing,
restricted to the pairs in the base table. Writes conf_em.json."""
import json, math, collections, sys
seq = json.load(open(sys.argv[1]))
base = {'0': '086', '1': '17', '2': '273', '3': '3258', '4': '4', '5': '538', '6': '68', '7': '712', '8': '85306', '9': '97'}
c = {p: collections.defaultdict(collections.Counter) for p in 'TUS'}
for t, k, *_ in seq:
    if not k: continue
    a, b = t[1:], k[1:]
    if len(a) == len(b):
        pos = ['S'] if len(a) == 1 else ['T', 'U']
        for p, x, y in zip(pos, a, b): c[p][x][y] += 1
conf = {}
for p in 'TUS':
    conf[p] = {}
    for x, ys in base.items():
        tot = sum(c[p][x][y] + 0.5 for y in ys)
        conf[p][x] = {y: max(0.0, round(-math.log((c[p][x][y] + 0.5) / tot) + math.log((c[p][x][x] + 0.5) / tot), 2)) for y in ys}
json.dump(conf, open('conf_em.json', 'w'), indent=0)
print(conf)
