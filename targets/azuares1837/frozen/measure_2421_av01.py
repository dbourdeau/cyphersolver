"""Mesure AVENANT-01 n° 2421 (gelée avant tout décodage des portions H).
Usage: python3 -I measure_2421_av01.py TRANSCRIPTION-2421-AV01.txt KEY-2421-AV01.json es.json.gz
Par passage : table apprise sur A seulement ; H (lignes désignées dans AVENANT-01.md) décodée par SA table.
Couverture = lettres couvertes par des mots >= 3 lettres du lexique (fréq >= 20), segmentation optimale,
lexique ET texte repliés sur les graphies du XIXe s. (v->b, y->i, x->j, z->c, ge/gi->je/ji, h muet conservé) ;
unité absente de la table = '?' jamais couverte ; '#' (chiffres) coupe le texte et n'est pas compté.
Témoins : pour chaque passage, 200 tables mélangées (valeurs permutées), graine 2421 ; correction pour comparaisons
multiples : la référence est le MAXIMUM des 5 x 200 témoins, commun à toutes les mesures."""
import sys, gzip, json, random, unicodedata, re
H_LINES = {'P062': ['06.12', '06.13', '06.14'], 'P063': ['06.21', '06.22', '06.23'],
           'P081': ['08.07', '08.08', '08.09'], 'P092': ['09.21', '10.01', '10.02'],
           'P112': ['11.07', '11.08', '11.09']}
def fold(s):
    s = s.replace('ñ', 'n'); s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    s = re.sub('g(?=[ei])', 'j', s.lower())
    return s.translate(str.maketrans('vyxz', 'bijc'))
def load_lex(p):
    d = json.load(gzip.open(p)); return {fold(w) for w, c in d.items() if c >= 20 and len(w) >= 3 and w.isalpha()}
def cover(text, lex, maxw=16):
    n = len(text); best = [0] * (n + 1)
    for i in range(1, n + 1):
        best[i] = best[i - 1]
        for j in range(max(0, i - maxw), i - 2):
            w = text[j:i]
            if '?' not in w and w in lex: best[i] = max(best[i], best[j] + (i - j))
    return best[n]
def segs(units):
    out, cur = [], []
    for u in units:
        if u == '#': out.append(cur); cur = []
        else: cur.append(u)
    out.append(cur); return [s for s in out if s]
def score(H, K, lex):
    cov = tot = 0
    for s in H:
        d = ''.join(K.get(u, '?') for u in s)
        # repli appliqué au clair décodé ; '?' préservé
        f = ''.join('?' if c == '?' else fold(c) for c in d)
        cov += cover(re.sub('g(?=[ei])', 'j', f), lex); tot += len(s)
    return cov / tot
if __name__ == '__main__':
    T = {}
    for l in open(sys.argv[1], encoding='utf-8'):
        if l.startswith('#') or '|' not in l: continue
        k, u = l.split('|'); p, v, n = k.strip().split('.'); T.setdefault(p, {})[v + '.' + n] = u.split()
    KEYS = json.load(open(sys.argv[2], encoding='utf-8')); lex = load_lex(sys.argv[3])
    rng = random.Random(2421); res = {}; allc = []
    for p, lines in H_LINES.items():
        units = [u for ln in lines for u in T[p][ln]]; H = segs(units); K = KEYS[p]
        s = score(H, K, lex); ctrl = []
        while len(ctrl) < 200:
            u = list(K); v = list(K.values()); rng.shuffle(v); Kc = dict(zip(u, v))
            if Kc != K: ctrl.append(score(H, Kc, lex))
        allc += ctrl; res[p] = {'units_H': sum(map(len, H)), 'M5': round(s, 4), 'temoins_max_passage': round(max(ctrl), 4),
                                 'temoins_moy_passage': round(sum(ctrl) / 200, 4)}
    M = max(allc)
    for p in res:
        marge = res[p]['M5'] - M
        res[p]['marge_corrigee'] = round(marge, 4)
        res[p]['verdict'] = 'VALIDE' if (res[p]['M5'] >= 0.60 and marge >= 0.30) else ('PARTIEL' if marge >= 0.30 else 'NEGATIF')
    print(json.dumps({'temoins_max_global': round(M, 4), 'n_temoins': len(allc), 'passages': res}, ensure_ascii=False, indent=1))
