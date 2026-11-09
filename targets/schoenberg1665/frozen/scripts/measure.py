# Mesure unique (PREREG.md) : H = L6-L9 décodé par K ; lisibilité en mots du lexique ; 200 témoins permutés (graine 1665).
import sys, os, gzip, json, random, unicodedata
sys.path.insert(0, os.path.dirname(__file__)); import parse
base, lexfn = sys.argv[1], sys.argv[2]
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('v', 'u').replace('j', 'i')
lex = {norm(w): c for w, c in json.load(gzip.open(lexfn)).items() if c >= 5}
K = {l.split('\t')[0]: l.split('\t')[1].strip() for l in open(base + '/KEY.tsv', encoding='utf-8')
     if not l.startswith('#') and l.split('\t')[0] != 'chiffre' and '\t' in l}
H = parse.words(base + '/H-CHIFFRE.txt', set(range(6, 10)))
def dec(k): return [norm(''.join(k.get(c, '?') for c in w)) for w in H]
def lis(k):
    d = dec(k); return sum(1 for w in d if '?' not in w and w in lex) / len(d), d
r, d = lis(K)
rng = random.Random(1665); ks = list(K); vs = [K[c] for c in ks]; ctl = []
for _ in range(200):
    v = vs[:]; rng.shuffle(v); ctl.append(lis(dict(zip(ks, v)))[0])
cov = sum(1 for w in H for c in w if c in K) / sum(len(w) for w in H)
marge = r - max(ctl)
verdict = 'VALIDE' if (r >= 0.70 and marge >= 0.30) else ('PARTIEL' if marge >= 0.30 else 'ECHEC')
out = {'mots_H': len(H), 'lis': round(r, 4), 'ctl_max': round(max(ctl), 4), 'ctl_moy': round(sum(ctl) / len(ctl), 4),
       'marge': round(marge, 4), 'couverture': round(cov, 4), 'verdict': verdict,
       'decodage': list(zip(H, d, [('?' not in w and w in lex) for w in d]))}
json.dump(out, open(base + '/MESURE.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False))
