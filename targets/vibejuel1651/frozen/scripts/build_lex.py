"""Lexique de mesure : da.json.gz (cyphersolver, origin/main 0c051c13e) + mots (fréq >= 2) des 7 vol. de Kong Christian IV egenhændige Breve (archive.org, OCR).
Normalisation 'early' adaptée à l'alphabet du chiffre (23 lettres) : minuscules, æ->ae, ø->oe, å->aa, accents retirés, j->i, v->u, w->u, puis on ne garde que a-z."""
import gzip, json, re, unicodedata, glob, collections, sys
def norm(w):
    w = w.lower().replace('æ','ae').replace('ø','oe').replace('å','aa').replace('ö','oe').replace('ä','ae').replace('ü','u')
    w = ''.join(c for c in unicodedata.normalize('NFD', w) if unicodedata.category(c) != 'Mn')
    w = w.replace('j','i').replace('v','u').replace('w','u')
    return re.sub('[^a-z]', '', w)
lex = set()
for w in json.load(gzip.open(sys.argv[1])): lex.add(norm(w))
c = collections.Counter()
for f in sorted(glob.glob(sys.argv[2] + '/*.txt')):
    for t in re.findall(r"[A-Za-zÆØÅæøåöäüÖÄÜ]+", open(f, errors='replace').read()): c[norm(t)] += 1
lex |= {w for w, n in c.items() if n >= 2 and len(w) >= 2}
lex = sorted(w for w in lex if w)
open(sys.argv[3], 'w').write('\n'.join(lex) + '\n'); print(len(lex))
