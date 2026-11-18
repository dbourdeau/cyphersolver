"""ONE measurement (PREREG.md): decode the f. 30 runs (texts/f30_signs.txt) with the frozen table_1448.json and compare with
the f. 29 reference words (texts/f29_reference.txt); 200 within-class shuffled tables, seed 1448. Run: python3 measure_f30.py"""
import json, re, random, statistics as st, os
here = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(here, 'table_1448.json'), encoding='utf8'))['table']
def norm(s):
    s = s.lower().replace('~', '')
    s = re.sub(r'\[—\]', '', s)
    s = re.sub(r'[^a-z]', '', s).replace('v', 'u').replace('y', 'i').replace('j', 'i').replace('h', '')
    return re.sub(r'(.)\1+', r'\1', s)
# runs of f. 30
runs, cur = {}, None
for ln in open(os.path.join(here, 'texts/f30_signs.txt'), encoding='utf8'):
    m = re.match(r'^(R\d+) ', ln)
    if m: cur = m.group(1); runs[cur] = []; continue
    m = re.match(r'^\s+(v\.)?L\d+:\s*(.*)$', ln)
    if m and cur and not ln.lstrip().startswith('['):
        body = re.sub(r'\[[^\]]*\]', ' ', m.group(2))
        runs[cur] += [t.rstrip('?') for t in body.split()]
    if ln.startswith('## New shapes'): cur = None
ref = {}
for ln in open(os.path.join(here, 'texts/f29_reference.txt'), encoding='utf8'):
    m = re.match(r'^(R\d+): (.*)$', ln)
    if m: ref[m.group(1)] = norm(m.group(2))
def lev(a, b):
    p = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        c = [i]
        for j, cb in enumerate(b, 1): c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (ca != cb)))
        p = c
    return p[-1]
def score(tab):
    d = n = 0
    for r, toks in runs.items():
        dec = norm(''.join(tab.get(t, '').replace('_', '') for t in toks))
        d += lev(dec, ref[r]); n += len(ref[r])
    return 1 - d / n
ntok = sum(len(v) for v in runs.values())
known = sum(1 for v in runs.values() for t in v if t in T)
cls = lambda k: 'word' if k.isupper() else ('null' if T[k] == '_' else 'letter')
groups = {}
for k in T: groups.setdefault(cls(k), []).append(k)
rnd = random.Random(1448); ctl = []
for _ in range(200):
    tab = dict(T)
    for g, ks in groups.items():
        vs = [T[k] for k in ks]; rnd.shuffle(vs); tab.update(zip(ks, vs))
    ctl.append(score(tab))
s = score(T)
out = {'runs': len(runs), 'cipher_signs': ntok, 'signs_with_table_value': known, 'coverage': round(known / ntok, 3),
       'reference_letters': sum(len(v) for v in ref.values()), 'score': round(s, 3), 'control_mean': round(st.mean(ctl), 3),
       'control_sd': round(st.pstdev(ctl), 3), 'control_best': round(max(ctl), 3), 'z': round((s - st.mean(ctl)) / st.pstdev(ctl), 1)}
out['verdict'] = 'read' if s >= 0.85 and s >= max(ctl) + 0.30 else ('partial' if s >= max(ctl) + 0.30 else 'failed')
out['size_bar'] = 'above (>= 300 signs)' if ntok >= 300 else 'below size bar'
for r, toks in runs.items():
    out['decoded_' + r] = ''.join((T.get(t) or '·').replace('_', '').replace('~', '') for t in toks)
print(json.dumps(out, ensure_ascii=False, indent=1))
