"""ONE measurement (PREREG-AMENDEMENT-1317-K2.md): decode the cipher runs of BnF ital. 1584 f. 353r (texts/f353_signs.txt)
with the frozen key K2 (K2_key.tsv) and compare with the reference words taken from the copy f. 352 r-v
(texts/f352_reference.txt). Metric identical to measure_f35.py: first value of x|y; normalisation (lower case, letters only,
v->u, y->i, j->i, h dropped, doubled letters simplified); score = 1 - sum Levenshtein / sum reference length.
Controls: 200 keys shuffled inside classes (word signs = UPPER-CASE labels; nulls = empty value; letters/syllables = the rest),
seed 1447. Labels absent from K2 (e.g. @Nxx new shapes) decode to nothing.
Run: python3 -I measure_f353.py [signs] [reference]"""
import json, re, random, statistics as st, os, sys
here = os.path.dirname(os.path.abspath(__file__))
SIGNS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'texts/f353_signs.txt')
REF = sys.argv[2] if len(sys.argv) > 2 else os.path.join(here, 'texts/f352_reference.txt')
T = {}
for ln in open(os.path.join(here, 'K2_key.tsv'), encoding='utf8'):
    if ln.startswith('#') or not ln.strip():
        continue
    f = ln.rstrip('\n').split('\t')
    T[f[0]] = f[1].split('|')[0]          # multiple values x|y: the first

def norm(s):
    s = s.lower().replace('~', '')
    s = re.sub(r'\[—\]', '', s)
    s = re.sub(r'[^a-z]', '', s).replace('v', 'u').replace('y', 'i').replace('j', 'i').replace('h', '')
    return re.sub(r'(.)\1+', r'\1', s)

runs, cur = {}, None
for ln in open(SIGNS, encoding='utf8'):
    if ln.startswith('## New shapes') or ln.startswith('## Notes'):
        cur = None
    m = re.match(r'^(R\d+) ', ln)
    if m:
        cur = m.group(1); runs[cur] = []; continue
    m = re.match(r'^\s+(v\.)?L\d+:\s*(.*)$', ln)
    if m and cur and not ln.lstrip().startswith('['):
        body = re.sub(r'\[[^\]]*\]', ' ', m.group(2))
        runs[cur] += [t.rstrip('?') for t in body.split()]
ref = {}
for ln in open(REF, encoding='utf8'):
    m = re.match(r'^(R\d+): (.*)$', ln)
    if m:
        ref[m.group(1)] = norm(m.group(2))
missing = set(runs) ^ set(ref)
if missing:
    sys.exit('runs and reference do not match: %s' % sorted(missing))

def lev(a, b):
    p = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        c = [i]
        for j, cb in enumerate(b, 1):
            c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (ca != cb)))
        p = c
    return p[-1]

def score(tab):
    d = n = 0
    for r, toks in runs.items():
        dec = norm(''.join(tab.get(t, '') for t in toks))
        d += lev(dec, ref[r]); n += len(ref[r])
    return 1 - d / n

ntok = sum(len(v) for v in runs.values())
known = sum(1 for v in runs.values() for t in v if t in T)
cls = lambda k: 'null' if T[k] == '' else ('word' if k.isupper() else 'letter')
groups = {}
for k in T:
    groups.setdefault(cls(k), []).append(k)
rnd = random.Random(1447); ctl = []
for _ in range(200):
    tab = dict(T)
    for g, ks in sorted(groups.items()):
        vs = [T[k] for k in ks]; rnd.shuffle(vs); tab.update(zip(ks, vs))
    ctl.append(score(tab))
s = score(T)
out = {'runs': len(runs), 'cipher_signs': ntok, 'signs_with_key_value': known, 'coverage': round(known / ntok, 3),
       'reference_letters': sum(len(v) for v in ref.values()), 'score': round(s, 3), 'control_mean': round(st.mean(ctl), 3),
       'control_sd': round(st.pstdev(ctl), 3), 'control_best': round(max(ctl), 3),
       'z': round((s - st.mean(ctl)) / st.pstdev(ctl), 1)}
out['verdict'] = 'read' if s >= 0.85 and s >= max(ctl) + 0.30 else ('partial' if s >= max(ctl) + 0.30 else 'failed')
out['size_bar'] = 'above (>= 300 signs)' if ntok >= 300 else 'below size bar'
for r, toks in runs.items():
    out['decoded_' + r] = ''.join((T.get(t) if t in T else '·') or '_' for t in toks)
print(json.dumps(out, ensure_ascii=False, indent=1))
