import csv, re, sys, json
W = sys.argv[1]  # decoding.tsv
def parse_o(s):
    m = re.match(r'^\??(\d*)\??([a-e])\??(\d+)', s)
    alt = re.search(r'\((\d+)\)', s)
    return (m.group(1) or '?', m.group(2), m.group(3)), (alt.group(1) if alt else '')
O = []
for r in csv.DictReader(open(W), delimiter='\t'):
    g, alt = parse_o(r['group_as_written'])
    O.append(dict(id=int(r['id']), letter=int(r['letter']), image=r['image'], ow=r['group_as_written'], o=g, oalt=alt,
                  lookup=r['lookup'], entry=r['entick_1776_entry'], reading=r['reading'], grade=r['grade']))
def load(path, secs):
    rows = [r for r in csv.DictReader(open(path), delimiter='\t') if r['section'] in secs]
    out = []
    for r in rows:
        p = r['page'].strip(); c = r['column'].strip(); l = r['line_value'].strip()
        out.append(dict(g=(p, c, l), sec=r['section'], n=r['n'], wb=r['word_before'], conf=r['confidence'],
                        alt=r['alternatives'], note=r.get('note', ''), end=r['ending'], lw=r['line_written']))
    return out
def sim(a, b):
    s = 0
    for x, y in zip(a, b):
        if x == y and '?' not in x: s += 1
        elif x.replace('?', '') and y.replace('?', '') and (x.replace('?','') in y or y.replace('?','') in x): s += 0.5
    return {3: 3, 2.5: 2.5, 2: 1.5, 1.5: 1, 1: 0, 0.5: -0.5, 0: -1}.get(s, -1)
def align(Oseq, R):
    n, m = len(Oseq), len(R); G = -0.8
    D = [[0]*(m+1) for _ in range(n+1)]; P = [[None]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1): D[i][0] = i*G; P[i][0] = 'u'
    for j in range(1, m+1): D[0][j] = j*G; P[0][j] = 'l'
    for i in range(1, n+1):
        for j in range(1, m+1):
            c = [(D[i-1][j-1] + sim(Oseq[i-1]['o'], R[j-1]['g']), 'd'), (D[i-1][j] + G, 'u'), (D[i][j-1] + G, 'l')]
            D[i][j], P[i][j] = max(c)
    i, j, res = n, m, {}
    extra = []
    while i > 0 or j > 0:
        p = P[i][j]
        if p == 'd': res[Oseq[i-1]['id']] = R[j-1]; i -= 1; j -= 1
        elif p == 'u': i -= 1
        else: extra.append(R[j-1]); j -= 1
    return res, extra
cfg = json.loads(sys.argv[2])  # reader -> {letter: [[file, [secs]], ...]}
out = {}
for reader, letters in cfg.items():
    out[reader] = {}
    for L, srcs in letters.items():
        Oseq = [o for o in O if o['letter'] == int(L)]
        got = {}; extras = []
        for f, secs in srcs:   # earlier sources take precedence
            R = load(f, secs)
            rem = [o for o in Oseq if o['id'] not in got]
            res, ex = align(rem, R)
            for k, v in res.items():
                if sim(next(o['o'] for o in Oseq if o['id']==k), v['g']) > -1 or True: got[k] = v
            extras += ex
        out[reader].update(got)
        out[reader]['extra_'+L] = extras
json.dump({'O': O, 'R': {r: {str(k): v for k, v in d.items()} for r, d in out.items()}}, open('aligned.json', 'w'), indent=0)
print('ok')
