"""Step 2 of PLAN.md: apply Andrew's 1574 key unchanged to A, B and the reconciled stream; trigram test once."""
import re, json, math, random, collections, unicodedata
key = {s: v['plain'] for s, v in json.load(open('key_guaras1574_from_main_c09aa9ed7d.json'))['key'].items()}
def norm(t):
    t = unicodedata.normalize('NFD', t.lower()); t = ''.join(c for c in t if not unicodedata.combining(c))
    t = t.replace('v', 'u').replace('j', 'i').replace('y', 'i').replace('f', 's').replace('ſ', 's')
    return re.sub(r'[^a-z]+', ' ', t)
Z = norm(open('../claver1497_verify_2026-11-16/raw/zurita1580_bub_gb_XgWt5lHz3_MC_djvu.txt', encoding='utf-8').read())
Zs = re.sub(r' +', '', Z)
tri = collections.Counter(Zs[i:i+3] for i in range(len(Zs) - 2)); bi = collections.Counter(Zs[i:i+2] for i in range(len(Zs) - 1))
V = 26
def lp(run):
    return [math.log((tri[run[i:i+3]] + 1) / (bi[run[i:i+2]] + V)) for i in range(len(run) - 2)]
def score(runs):
    v = [x for r in runs for x in lp(r)]; return sum(v) / len(v) if v else float('nan'), len(v)
def load(fn):
    toks = []
    for ln in open(fn, encoding='utf-8'):
        m = re.match(r'(P[12]L\d\d):\s*(.*)$', ln.rstrip('\n'))
        if not m: continue
        s = re.sub(r'\[\[.*?\]\]', ' ', m.group(2))
        toks += [t.strip('<>') for t in s.split() if t.strip('<>') and t not in ('|', ',', '.', '/', '·')]
    return toks
def decode(toks, k):
    return ''.join(norm(k[t]).strip() if t in k else '#' for t in toks)
def runs(dec): return [r for r in dec.split('#') if len(r) >= 3]
P = norm(open('../claver1497_verify_2026-11-16/raw/pulgar1780_bub_gb_RB9nAr9N5AkC_djvu.txt', encoding='utf-8').read())
P = re.sub(r' +', '', P); P = P[len(P) // 20:]
res = {}
for name in ('transcription_A.txt', 'transcription_B.txt', 'reconciled.txt'):
    toks = load(name); dec = decode(toks, key); cov = sum(t in key for t in toks) / len(toks)
    rr = runs(dec); s, n = score(rr)
    rng = random.Random(1577); signs = list(key); vals = [key[x] for x in signs]; ctrl = []
    for _ in range(200):
        rng.shuffle(vals); kk = dict(zip(signs, vals)); ctrl.append(score(runs(decode(toks, kk)))[0])
    lens = [len(r) for r in rr]; yard = []; rng2 = random.Random(1578)
    for _ in range(200):
        st = rng2.randrange(len(P) - sum(lens) - 10); pos = st; w = []
        for L in lens: w.append(P[pos:pos+L]); pos += L
        yard.append(score(w)[0])
    yard.sort(); p5 = yard[10]
    beats = sum(s > c for c in ctrl)
    verdict = 'reads' if (cov >= 0.80 and beats == 200 and s >= p5) else ('partly fits' if beats == 200 else 'does not read')
    res[name] = dict(tokens=len(toks), coverage=round(cov, 4), trigrams=n, score=round(s, 4), controls_beaten=beats,
                     best_control=round(max(ctrl), 4), median_control=round(sorted(ctrl)[100], 4), pulgar_p5=round(p5, 4),
                     pulgar_median=round(yard[100], 4), verdict=verdict, decode_first_200=dec[:200])
json.dump(res, open('step2_result.json', 'w'), indent=1)
print(json.dumps(res, indent=1))
