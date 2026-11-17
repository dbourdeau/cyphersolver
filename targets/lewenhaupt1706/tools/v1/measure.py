"""MESURE UNIQUE (PREREG). usage: measure.py <cle_K.json> <lexique> <transcription H...>
S = part des caractères décodés couverts par la meilleure segmentation en mots du lexique ; 200 témoins (permutation des valeurs de K)."""
import sys, re, json, random
def norm(s): return s.lower().replace('v','w').replace('é','e').replace('ü','y')
K = json.load(open(sys.argv[1], encoding='utf-8')); LX = set(l.strip() for l in open(sys.argv[2], encoding='utf-8') if l.strip())
MAXW = max(len(w) for w in LX)
runs = []; ngroups = 0; nunk = 0
for f in sys.argv[3:]:
    cur = []
    for line in open(f, encoding='utf-8'):
        if line.startswith('#'): continue
        line = re.sub(r'\[[^\]]*\]', ' ', line.split('#')[0])
        for m in re.finditer(r'\{([^}]*)\}|(\d+)\??', line):
            if m.group(1) is not None:
                if cur: runs.append(cur); cur = []
            else: cur.append(m.group(2)); ngroups += 1
    if cur: runs.append(cur)
def score(key):
    tot = cov = 0
    for r in runs:
        s = ''.join(norm(key[c]) if c in key else '?' for c in r)
        n = len(s); best = [0]*(n+1)
        for i in range(1, n+1):
            b = best[i-1]
            for L in range(2, min(MAXW, i)+1):
                w = s[i-L:i]
                if w in LX and best[i-L] + L > b: b = best[i-L] + L
            best[i] = b
        tot += n; cov += best[n]
    return cov / tot if tot else 0
nunk = sum(1 for r in runs for c in r if c not in K)
sK = score(K)
codes = list(K); vals = [K[c] for c in codes]; rng = random.Random(20261117); ctr = []
for _ in range(200):
    v = vals[:]; rng.shuffle(v); ctr.append(score(dict(zip(codes, v))))
mx = max(ctr)
print(json.dumps({"groupes_H": ngroups, "groupes_inconnus": nunk, "part_inconnus": round(nunk/ngroups, 4), "S_K": round(sK, 4),
  "max_temoins": round(mx, 4), "moy_temoins": round(sum(ctr)/len(ctr), 4), "seuil_1": 0.85, "seuil_2": round(mx + 0.30, 4),
  "succes": bool(sK >= 0.85 and sK >= mx + 0.30)}, ensure_ascii=False, indent=1))
