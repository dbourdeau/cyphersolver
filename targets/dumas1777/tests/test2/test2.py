"""Second held-out test: frozen key vs the contemporary glosses on item 93 image 0173 (plan: TEST2_PLAN.md)."""
import json, os, re, random, unicodedata, hashlib
D = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
kp = os.path.join(D, 'key', 'key_positions.json')
sha = hashlib.sha256(open(kp, 'rb').read()).hexdigest()
K = {int(k): v for k, v in json.load(open(kp))['positions'].items()}
norm = lambda c: {'-': '='}.get(unicodedata.normalize('NFD', c)[0].lower(), unicodedata.normalize('NFD', c)[0].lower())
pairs = []
for l in open(os.path.join(D, 'transcriptions', 'R3_A', 'img0173.txt')):
    if re.match(r'L\d+:', l):
        for t in l.split(':', 1)[1].split():
            m = re.match(r'^(\d+)/(.)(\??)$', t)
            if m: pairs.append((int(m.group(1)), m.group(2).lower(), m.group(3) == '?'))
def score(key, sure_only=False):
    P = [p for p in pairs if not (sure_only and p[2])]
    return sum(1 for n, g, _ in P if n in key and norm(key[n]) == g) / len(P), len(P)
real, n = score(K); real_s, ns = score(K, True)
miss = [(n_, g, norm(K[n_])) for n_, g, _ in pairs if norm(K[n_]) != g]
random.seed(20261114); vals = list(K.values()); null = []
for _ in range(200):
    random.shuffle(vals); null.append(score(dict(zip(K.keys(), vals)))[0])
res = {'key_sha256': sha, 'glossed_numbers': n, 'agree_all': round(real, 4), 'glossed_sure': ns, 'agree_sure': round(real_s, 4),
       'misses': miss, 'null_mean': round(sum(null)/len(null), 4), 'null_max': round(max(null), 4),
       'pass': real >= 0.9 and real > max(null)}
json.dump(res, open(os.path.join(D, 'tests', 'test2', 'test2_result.json'), 'w'), indent=1); print(res)
