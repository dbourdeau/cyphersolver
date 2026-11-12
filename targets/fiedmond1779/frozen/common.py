# Avenant C09 (session C11, 11/11/2026) — fonctions communes, FIXÉES avant la mesure.
# Mesure S = part des GROUPES chiffrés couverts par un mot du lexique qui s'étend sur >= 2 groupes
# ou compte >= 5 lettres (segmentation par programmation dynamique, couverture maximale).
import json, re, random, unicodedata, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))           # guyane-1779/
EUR = os.path.abspath(os.path.join(ROOT, '..'))                   # dechiffrements-europe/
LEX = os.path.join(EUR, 'REDACTED-storage-location/lexique-fr-cyphersolver.json')  # redacted for publication: this repo's French lexicon, SHA-256 cdf81c86...
CLAIRS = ['f102_clair.txt', 'c1780_dechiffrement.txt',
          'c09_memoire_laserre_v309-314.txt', 'c09_laserre_aout_v302-308.txt']
HOLD = {('v014g', f'l{i:02d}') for i in range(11, 19)} | {('v025d', f'l{i:02d}') for i in range(27, 32)}
SEED = 20261111
MAXW = 22

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('j', 'i').replace('v', 'u').replace('y', 'i').replace('œ', 'oe').replace('æ', 'ae')
    return re.sub(r'[^a-z]', '', s)

def lexicon():
    lx = set()
    d = json.load(open(LEX, encoding='utf-8'))
    for w in d:
        n = norm(w)
        if len(n) >= 2: lx.add(n)
    for f in CLAIRS:  # clairs d'APPRENTISSAGE (orthographe d'époque) ; aucun ne contient la portion de contrôle
        for ln in open(os.path.join(ROOT, 'transcription', f), encoding='utf-8'):
            if ln.startswith('#'): continue
            txt = ln.split(':', 1)[1] if ':' in ln else ln
            for w in re.split(r"[\s'’.,;:!?()«»\[\]\-—/]+", txt):
                n = norm(w)
                if len(n) >= 2: lx.add(n)
    return lx

def load_key(p):
    k = {}
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('groupe'): continue
        c = ln.rstrip('\n').split('\t')
        if len(c) < 4 or not c[0].strip().isdigit(): continue
        v = norm(c[1])
        if c[3].strip() == 'irresolu' or not v: continue
        k[int(c[0])] = (v, c[3].strip())
    return k

def load_lines(p, keep=None, exclude_hold=True):
    """[(lineid, tokens)] ; token = int (1re lecture si 'a?/b'), 'C' (îlot en clair), '?' (illisible)."""
    out = []
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or ':' not in ln: continue
        lid, txt = ln.split(':', 1)
        lid = tuple(lid.split())
        if keep is not None and lid not in keep: continue
        if keep is None and exclude_hold and lid in HOLD: continue
        txt = re.sub(r'\[[^\]]*\]', '', txt)
        txt = re.sub(r'«[^»]*»?', ' CLAIR ', txt)
        toks = []
        for t in re.split(r'[.\s—]+', txt):
            if not t: continue
            if t == 'CLAIR': toks.append('C'); continue
            m = re.match(r'^(\d+)', t)
            if m: toks.append(int(m.group(1)))
            elif '?' in t: toks.append('?')
        out.append((' '.join(lid), toks))
    return out

def segments(tokens, key):
    """Coupe le flot en segments de lettres ; renvoie [(lettres, idx_groupe_par_lettre)], n_groupes."""
    segs, cur, own = [], [], []
    ng = 0
    for t in tokens:
        if t == 'C':
            if cur: segs.append((''.join(cur), own)); cur, own = [], []
            continue
        gi = ng; ng += 1
        if t == '?' or t not in key:
            if cur: segs.append((''.join(cur), own)); cur, own = [], []
            continue
        v = key[t][0]
        cur.append(v); own += [gi] * len(v)
    if cur: segs.append((''.join(cur), own))
    return segs, ng

def best_words(s, lx):
    n = len(s); best = [(-1, 0)] * (n + 1); best[0] = (0, 0); back = [None] * (n + 1)
    for i in range(1, n + 1):
        cand = (best[i - 1][0], best[i - 1][1] - 1); bk = (i - 1, False)
        for j in range(max(0, i - MAXW), i - 1):
            w = s[j:i]
            if w in lx:
                sc = (best[j][0] + (i - j), best[j][1] - 1)
                if sc > cand: cand, bk = sc, (j, True)
        best[i] = cand; back[i] = bk
    words = []; i = n
    while i > 0:
        j, isw = back[i]
        if isw: words.append((j, i))
        i = j
    return words[::-1]

def S(tokens, key, lx):
    segs, ng = segments(tokens, key)
    if ng == 0: return 0.0, 0, 0
    covered_letters = {}
    for s, own in segs:
        good = [False] * len(s)
        for j, i in best_words(s, lx):
            gs = set(own[j:i])
            if len(gs) >= 2 or (i - j) >= 5:
                for x in range(j, i): good[x] = True
        for x, g in enumerate(own):
            covered_letters.setdefault(g, []).append(good[x])
    cov = sum(1 for g, l in covered_letters.items() if all(l))
    return cov / ng, cov, ng

def witnesses(key, n, rng, kind):
    gs = sorted(key); vals = [key[g] for g in gs]; out = []
    for _ in range(n):
        if kind == 'permutee':
            v = vals[:]; rng.shuffle(v); out.append(dict(zip(gs, v)))
        else:  # 'melangee' : permutation à l'intérieur de chaque classe de longueur de valeur
            by = {}
            for g, v in zip(gs, vals): by.setdefault(len(v[0]), []).append(g)
            k = {}
            for L, members in by.items():
                vv = [key[g] for g in members]; rng.shuffle(vv); k.update(zip(members, vv))
            out.append(k)
    return out

# ---- Modèle de langue de caractères (ajouté pendant l'étalonnage, AVANT le gel et avant toute mesure) ----
import math
from collections import Counter
CORPUS = os.path.join(EUR, 'REDACTED-storage-location/corpus-fr-gutenberg-extrait-1.9Mo.txt')  # redacted for publication (not decisive)
LAMB = (0.02, 0.08, 0.15, 0.30, 0.45)  # poids des ordres 1..5, fixés a priori

def lm_train():
    txt = []
    for ln in open(CORPUS, encoding='utf-8', errors='ignore'):
        txt.append(norm(ln))
    for f in CLAIRS:
        for ln in open(os.path.join(ROOT, 'transcription', f), encoding='utf-8'):
            if ln.startswith('#'): continue
            t = ln.split(':', 1)[1] if ':' in ln else ln
            t = re.sub(r'\[[^\]]*\]', '', t); txt.append(norm(t))
    s = ''.join(txt)
    C = [Counter() for _ in range(6)]
    for n in range(1, 6):
        for i in range(len(s) - n + 1): C[n][s[i:i + n]] += 1
    H = [Counter() for _ in range(6)]
    for n in range(2, 6):
        for g, c in C[n].items(): H[n][g[:-1]] += c
    return C, H, len(s)

def lm_logp(model, ctx, ch):
    C, H, N = model
    p = LAMB[0] * (C[1][ch] + 1) / (N + 26)
    for n in range(2, 6):
        h = ctx[-(n - 1):]
        if len(h) < n - 1: continue
        d = H[n][h]
        if d: p += LAMB[n - 1] * C[n][h + ch] / d
    return math.log10(p)

def LM(tokens, key, model):
    segs, ng = segments(tokens, key)
    tot = 0.0; n = 0
    for s, _ in segs:
        for i, ch in enumerate(s):
            tot += lm_logp(model, s[max(0, i - 4):i], ch); n += 1
    return (tot / n if n else -9.0), n
