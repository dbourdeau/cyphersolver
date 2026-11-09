# Critère d'applicabilité (PREREG-2 § 5) + décodage de P59 par KEY-2. Usage : python3 -I p59_apply.py <dossier> <dossier_txt_edition>
import sys, os, re, glob
D, E = sys.argv[1], sys.argv[2]
key = {}
for ln in open(os.path.join(D, 'KEY-2.tsv'), encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    c, v = ln.rstrip('\n').split('\t')[:2]; key[c] = v.lower()
def norm(s):
    s = s.lower().replace('å', 'aa').replace('j', 'i').replace('w', 'v')
    return ''.join(ch for ch in s if 'a' <= ch <= 'z' or ch in 'æø')
bm = set(); words = []
for ln in open(os.path.join(D, 'P59-CHIFFRE.txt'), encoding='utf-8'):
    if ln.startswith('BERGEN_MATCH'): bm = set(ln.split()[1:]); continue
    if not ln.startswith('L'): continue
    s = re.sub(r'\{clair:[^}]*\}', ' | ', ln.split(None, 1)[1])
    for w in s.split('|'):
        t = [x for x in w.split() if x not in ':.,;!—-']
        if t: words.append(t)
occ = [t for w in words for t in w if t != '[?]']
C1811 = sum(1 for t in occ if t.rstrip('^') in key) / len(occ)
CB = sum(1 for t in occ if t.rstrip('^') in bm) / len(occ)
def dec(t):
    if t == '[?]': return '?'
    b = t.rstrip('^'); v = key.get(b)
    if v is None: return '‹' + b + '›'
    return v + v[-1] if t.endswith('^') else v
lex = set()
for f in glob.glob(os.path.join(E, '*.txt')):
    for w in re.findall(r'[A-Za-zÆØÅæøåéèêàâôûüöäç]+', open(f, encoding='utf-8', errors='ignore').read()):
        n = norm(w)
        if len(n) >= 3: lex.add(n)
decw = [''.join(dec(t) for t in w) for w in words]
cand = [w for w in decw if '?' not in w and '‹' not in w and len(norm(w)) >= 3]
L = sum(1 for w in cand if norm(w) in lex) / len(cand)
print(f'occurrences={len(occ)} mots={len(words)} C1811={C1811:.3f} CBergen={CB:.3f} écart={C1811-CB:.3f}')
print(f'L (mots ≥3 lettres décodés sans « ? » présents dans le lexique de l édition, {len(lex)} formes) = {L:.3f} ({sum(1 for w in cand if norm(w) in lex)}/{len(cand)})')
print('absents du lexique :', [w for w in cand if norm(w) not in lex])
ok1811 = C1811 >= 0.80 and C1811 - CB >= 0.20 and L >= 0.50
okB = CB >= 0.80 and CB - C1811 >= 0.20
print('VERDICT :', 'alphabet de 1811' if ok1811 else ('alphabet de Bergen' if okB else 'INDÉTERMINÉ'))
print('décodage :', ' '.join(decw))
