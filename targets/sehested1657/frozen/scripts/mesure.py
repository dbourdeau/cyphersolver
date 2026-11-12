"""mesure.py CLE LM TRANSCR... — UNE mesure (PROTOCOLE.md). Décode les nombres de la réserve avec la clé gelée,
score par caractère (LM allemand) + taux de mots au lexique, contre 3 familles de 300 contrôles (graine fixe 1657)."""
import sys, random, pickle, re, collections
sys.path.insert(0, __file__.rsplit('/', 1)[0]); from lm_de import LM, A
cle = dict((int(a), b) for a, b in (l.strip().split('=') for l in open(sys.argv[1]) if '=' in l and not l.startswith('#')))
m, words = pickle.load(open(sys.argv[2], 'rb')); lex = {w for w, c in words.items() if c >= 2}
mots = []
for f in sys.argv[3:]:
    for l in open(f):
        if l.startswith('#'): continue
        for tok in l.split():
            if tok.startswith('['): continue
            ns = [x for x in tok.strip(':').split(':') if x]
            if ns: mots.append(ns)
nums = [x for w in mots for x in w]; num_int = [int(x) for x in nums if x.isdigit()]
inconnus = sum(1 for x in nums if not x.isdigit() or int(x) not in cle)
def dec(k, ws): return ' '.join(''.join(k.get(int(x), '') if x.isdigit() else '' for x in w) for w in ws)
def score(k, ws):
    t = dec(k, ws); t = re.sub(' +', ' ', t).strip(); ww = [w for w in t.split() if len(w) >= 2]
    return m.per_char(t), (sum(w in lex for w in ww) / max(1, len(ww)))
M = score(cle, mots); rnd = random.Random(1657)
vals = sorted(cle); lets = [cle[v] for v in vals]
freq = collections.Counter(c for w in words.elements() for c in w) if False else None
corp = ''.join(w for w in list(words)[:5000]); fr = collections.Counter(corp); pool = [c for c in A]; wts = [fr[c] + 1 for c in pool]
allv = sorted(set(num_int))
C, D, E = [], [], []
for _ in range(300):
    l2 = lets[:]; rnd.shuffle(l2); C.append(score(dict(zip(vals, l2)), mots))
    D.append(score({v: rnd.choices(pool, wts)[0] for v in allv}, mots))
    flat = nums[:]; rnd.shuffle(flat); it = iter(flat); E.append(score(cle, [[next(it) for _ in w] for w in mots]))
mx = max(x[0] for x in C + D + E); mxl = max(x[1] for x in C + D + E)
print('mots', len(mots), 'nombres', len(nums), 'inconnus', inconnus, f'({inconnus/len(nums):.3f})')
print(f'M per_char {M[0]:.3f}  lexique {M[1]:.3f}')
for n, X in (('C perm', C), ('D aleat', D), ('E melange', E)):
    print(f'{n}: max per_char {max(x[0] for x in X):.3f} max lexique {max(x[1] for x in X):.3f}')
c1 = M[0] >= mx + 0.30; c2 = M[1] >= 0.50 and M[1] >= mxl + 0.25; c3 = inconnus / len(nums) <= 0.05
print(f'C1 {c1} (marge {M[0]-mx:.3f})  C2 {c2} (marge {M[1]-mxl:.3f})  C3 {c3}')
print('DECODE:'); print(dec(cle, mots))
