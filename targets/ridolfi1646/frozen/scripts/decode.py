# decode.py — décodeur DÉTERMINISTE fidèle à KEY-PROPOSAL.json (Fable 5.2, lot 2, run 20261111-103319).
# Aucune valeur ajoutée : seules les entrées de KEY-PROPOSAL.json["lettres_et_syllabes"] sont appliquées.
# Règles (celles de load.py / ctrl.py de Fable) : point suscrit « ' » retiré ; alternative « a/b » -> première lecture ;
# X -> « . » (ponctuation) ; code 3 chiffres -> [nnn] (inconnu, aucune conjecture appliquée) ; 2 chiffres absent de la clé -> [nn?].
# Usage : python3 -I decode.py PAGES   (ex. 1234) -> sortie au format de DECODE-brut-p1-4.txt
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
KEY = json.load(open(os.path.join(ROOT, 'KEY-PROPOSAL.json')))['lettres_et_syllabes']

def lines(p):
    out = []
    for li, l in enumerate(open(os.path.join(ROOT, 'transcr', 'D107_p%d.txt' % p))):
        if l.startswith('#'): continue
        out.append((li, [t.split('/')[0].replace("'", "") for t in l.split()]))
    return out

def tokens(pages):
    return [t for p in pages for _, ts in lines(p) for t in ts]

def dec_tok(t, K=KEY):
    if t == 'X': return '. '
    if len(t) == 2 and t in K: return K[t]
    if len(t) == 3: return '[%s]' % t
    return '[%s?]' % t

def segments(toks, K=KEY):
    """Segments de lettres décodées ; tout groupe hors clé à 2 chiffres (X, 3 chiffres, inconnu) = coupure."""
    out, cur = [], ''
    for t in toks:
        if len(t) == 2 and t in K: cur += K[t]
        else:
            if cur: out.append(cur)
            cur = ''
    if cur: out.append(cur)
    return out

if __name__ == '__main__':
    for ch in sys.argv[1]:
        p = int(ch)
        for li, ts in lines(p):
            print('%d.%02d\t%s' % (p, li, '·'.join(dec_tok(t) for t in ts)))
