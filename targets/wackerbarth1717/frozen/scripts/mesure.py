# MESURE UNIQUE (PROTOCOLE §4 + Avenant 1). Une seule exécution : python3 scripts/mesure.py > MESURE.txt
import sys, os, re, json, random, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import D, REL, norm, tokens, read_releve
LEXF = os.path.join(os.path.dirname(D), 'PISTES-AUTO/fable-api/lots/lot2/_communs/lexique-fr-cyphersolver.json')

def load_key():
    K = {}
    for line in open(os.path.join(D, 'KEY-W1717.tsv'), encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        f = line.rstrip('\n').split('\t')
        K[f[0]] = norm(f[1].replace('[', '').replace(']', ''))
    return K

def nums_of(path):
    out = []
    for line in open(path, encoding='utf-8'):
        m = re.match(r'[A-Z]\d+ C: ?(.*)', line)
        if m: out += [v for k, v in tokens(m.group(1)) if k == 'n']
    return out

def dec(K, ns): return ''.join(K.get(n, '#') for n in ns)

def carA(F, Dd):
    sm = difflib.SequenceMatcher(None, F, Dd, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size >= 3) / len(F)

def make_cover(LEX):
    ML = max(map(len, LEX))
    def cover(s):
        n = len(s); best = [None] * (n + 1); best[0] = (0, [])
        for i in range(n):
            if best[i] is None: continue
            c, ws = best[i]
            if best[i + 1] is None or best[i + 1][0] < c: best[i + 1] = (c, ws)
            for j in range(i + 2, min(n, i + ML) + 1):
                w = s[i:j]
                if w in LEX and (best[j] is None or best[j][0] < c + len(w)): best[j] = (c + len(w), ws + [w])
        c, ws = best[n]
        return c / n, ws
    return cover

def controls(K, f, rnd):
    codes = list(K); vals = list(K.values()); res = []
    for _ in range(200):
        v = vals[:]; rnd.shuffle(v); res.append(f(dict(zip(codes, v))))
    return res

def verdict(s, mx):
    if s >= 0.85 and s - mx >= 0.30: return 'VALIDÉ'
    if s - mx >= 0.30: return 'PARTIEL'
    return 'ÉCHEC'

K = load_key()
# --- A ---
nA = nums_of(os.path.join(REL, 'A-CHIFFRE-0040.txt'))
ftxt = open(os.path.join(REL, 'A-FEUILLE-0042-0043.txt'), encoding='utf-8').read().split('\n')
body = '\n'.join(l for l in ftxt[1:] if not l.startswith('#'))
body = re.sub(r'⟨|⟩', '', body)
F = norm(body); cut = F.find('uoilacequepourlepresent')
if cut >= 0: F = F[:cut]
DA = dec(K, nA); sA = carA(F, DA)
tA = controls(K, lambda k: carA(F, dec(k, nA)), random.Random(1717))
wF = [norm(w) for w in re.split(r"[\s'’\-.,;:()]+", body.split('Voila ce que')[0]) if len(norm(w)) >= 2]
wA = sum(1 for w in wF if w in DA) / max(1, len(wF))
# --- B ---
nB = []
for line in open(os.path.join(REL, 'B-REL22.txt'), encoding='utf-8'):
    m = re.match(r'[LMN]\d+ C: ?(.*)', line)
    if m: nB += [v for k, v in tokens(m.group(1)) if k == 'n']
nB = nB[:360]
LEX = {w for w in json.load(open(LEXF)) if len(w) >= 2}
LEX |= {w.strip() for w in open(os.path.join(D, 'LEXIQUE-AJOUT-TRAIN.txt')) if len(w.strip()) >= 2}
cover = make_cover(LEX)
DB = dec(K, nB); sB, segB = cover(DB)
tB = controls(K, lambda k: cover(dec(k, nB))[0], random.Random(1717))
covB = sum(1 for n in nB if n in K) / len(nB); covA = sum(1 for n in nA if n in K) / len(nA)
R = dict(A=dict(groupes=len(nA), couverture_cle=round(covA, 4), lettres_F=len(F), carA=round(sA, 4), max_temoins=round(max(tA), 4),
                moy_temoins=round(sum(tA) / 200, 4), marge=round(sA - max(tA), 4), mots_F_retrouves=round(wA, 4), verdict=verdict(sA, max(tA)), decodage=DA, F=F),
         B=dict(groupes=len(nB), couverture_cle=round(covB, 4), scoreB=round(sB, 4), max_temoins=round(max(tB), 4), moy_temoins=round(sum(tB) / 200, 4),
                marge=round(sB - max(tB), 4), verdict=verdict(sB, max(tB)), decodage=DB, segmentation=' '.join(segB)))
json.dump(R, open(os.path.join(D, 'MESURE.json'), 'w'), ensure_ascii=False, indent=1)
for k in 'AB':
    print(k, {x: y for x, y in R[k].items() if x not in ('decodage', 'F', 'segmentation')})
