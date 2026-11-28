"""Held-out measure for 2855 and 2865 (one run per protocol).
usage: measure.py PROTOCOL.json
Protocol fields: key (json sign->value), transcription (tsv: line<TAB>tokens), reference (tsv: block<TAB>lines<TAB>gloss),
seed, controls, threshold, margin, result.
Score: for each block, the frozen key decodes the block's cipher tokens ({clear} skipped, a trailing ? dropped, unknown
signs give nothing); letters are normalised (a-z; j->i, v->u, k->c, y->i); gloss words in [] are removed. Matched letters
= difflib.SequenceMatcher(autojunk=False) matching blocks between decode and gloss. Primary score = matched / gloss
letters (summed over blocks). Also reported: the #1014 'char' form, matched / max(len decode, len gloss).
Controls: the key's values shuffled over its signs, `controls` times, random.Random(seed).
Pass: score >= threshold, above every control, and score - best control >= margin."""
import json, sys, re, random, difflib, hashlib, os, statistics, datetime, platform
P = json.load(open(sys.argv[1])); base = os.path.dirname(os.path.abspath(sys.argv[1]))
pth = lambda f: os.path.join(base, f)
if os.path.exists(pth(P['result'])): sys.exit('result exists: refusing to measure twice')
key = json.load(open(pth(P['key'])))
lines = {}
for l in open(pth(P['transcription']), encoding='utf-8'):
    if '\t' in l and not l.startswith('#'):
        a, b = l.rstrip('\n').split('\t', 1); lines[a] = re.sub(r'\{[^}]*\}', ' {clear} ', b).split()
def norm(s):
    s = s.lower().replace('j', 'i').replace('v', 'u').replace('k', 'c').replace('y', 'i')
    return re.sub('[^a-z]', '', s)
blocks = []
for l in open(pth(P['reference']), encoding='utf-8'):
    if l.startswith('#') or '\t' not in l: continue
    b, ls, g = l.rstrip('\n').split('\t')
    g = re.sub(r'\[[^\]]*\]', ' ', g)
    toks = [t.rstrip('?') for ln in ls.split() for t in lines[ln] if t != '{clear}']
    blocks.append((b, toks, norm(g)))
def score(k):
    m = tg = td = 0; per = {}
    for b, toks, g in blocks:
        d = norm(''.join(k.get(t, '') for t in toks))
        sm = difflib.SequenceMatcher(None, d, g, autojunk=False)
        mm = sum(x.size for x in sm.get_matching_blocks()); m += mm; tg += len(g); td += max(len(d), len(g))
        per[b] = [mm, len(g), len(d)]
    return m / tg, m / td, per
s, sc, per = score(key)
rng = random.Random(P['seed']); signs = sorted(key); vals = [key[x] for x in signs]; ctl = []; ctl_c = []
for _ in range(P['controls']):
    v = vals[:]; rng.shuffle(v); a, c, _p = score(dict(zip(signs, v))); ctl.append(a); ctl_c.append(c)
best = max(ctl); mu = statistics.mean(ctl); sd = statistics.pstdev(ctl) or 1e-9
ok = s >= P['threshold'] and s > best and s - best >= P['margin']
h = lambda f: hashlib.sha256(open(f, 'rb').read()).hexdigest()
R = {'score': round(s, 4), 'score_char1014': round(sc, 4), 'per_block': per, 'best_control': round(best, 4),
     'control_mean': round(mu, 4), 'z': round((s - mu) / sd, 2), 'best_control_char1014': round(max(ctl_c), 4),
     'rank': 1 + sum(c >= s for c in ctl), 'controls': P['controls'], 'verdict': 'PASS' if ok else 'MISS',
     'manifest_sha256': h(pth(P['manifest'])), 'script_sha256': h(__file__), 'python': platform.python_version(),
     'run_utc': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}
json.dump(R, open(pth(P['result']), 'w'), indent=1); print(json.dumps(R, indent=1))
