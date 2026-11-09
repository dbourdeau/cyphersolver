# Mesure unique (PREREG) : H (24/12/1647) décodé par K contre les gloses de 0571 ; 200 témoins permutés (graine 1647).
import sys, json, random, difflib, unicodedata, re
base = sys.argv[1]
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub('[^a-z]', '', s.replace('j', 'i').replace('v', 'u'))
def load_key(fn):
    return {l.split('\t')[0]: l.split('\t')[1] for l in open(fn, encoding='utf-8') if l[:1].isdigit()}
K = load_key(base + '/KEY.tsv'); K0 = load_key(base + '/KEY0-0003.tsv')
H = {}
for l in open(base + '/H-CHIFFRE.txt', encoding='utf-8'):
    if l.startswith('H('): pid, nums = l.rstrip('\n').split('\t')[:2]; H[pid] = nums.split('.')
G = {}
for l in open(base + '/H-GLOSES.txt', encoding='utf-8'):
    if l.startswith('H('): pid, g = l.rstrip('\n').split('\t')[:2]; G[pid] = norm(g)
pids = [p for p in H if p in G and G[p]]
def score(key):
    m = tot = 0; dec = {}
    for p in pids:
        d = ''.join(key.get(n, '?') for n in H[p]); dec[p] = d
        m += sum(b.size for b in difflib.SequenceMatcher(None, d, G[p], autojunk=False).get_matching_blocks()); tot += len(G[p])
    return m / tot, dec
def words(dec):
    ok = tot = 0
    for p in pids:
        # accord en mots : mots de la glose retrouvés tels quels dans le décodage (non décisif)
        pass
    return None
car, dec = score(K)
rng = random.Random(1647); nums = list(K); vals = [K[n] for n in nums]; ctl = []
for _ in range(200):
    v = vals[:]; rng.shuffle(v); ctl.append(score(dict(zip(nums, v)))[0])
cov = sum(1 for p in pids for n in H[p] if n in K) / sum(len(H[p]) for p in pids)
marge = car - max(ctl)
verdict = 'VALIDE' if (car >= 0.85 and marge >= 0.30) else ('PARTIEL' if marge >= 0.30 else 'ECHEC')
car0, _ = score(K0)
out = {'passages': pids, 'gloss_letters': sum(len(G[p]) for p in pids), 'car': round(car, 4), 'ctl_max': round(max(ctl), 4),
       'ctl_mean': round(sum(ctl) / len(ctl), 4), 'marge': round(marge, 4), 'couverture': round(cov, 4), 'verdict': verdict,
       'descriptif_K0_seule_car': round(car0, 4), 'decodes': dec, 'gloses': {p: G[p] for p in pids}}
json.dump(out, open(base + '/MESURE.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print({k: v for k, v in out.items() if k not in ('decodes', 'gloses')})
