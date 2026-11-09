# APRÈS la mesure : décodage complet avec la clé régulière KEY-COMPLET.tsv (descriptif, hors mesure).
import sys, os; sys.path.insert(0, os.path.dirname(__file__)); import parse
K = {l.split('\t')[0]: l.split('\t')[1].strip() for l in open(sys.argv[2], encoding='utf-8') if '\t' in l and not l.startswith(('#', 'chiffre'))}
for n, s in parse.lines(sys.argv[1]):
    print('L%d' % n, ''.join(K.get(c, c.upper() if c.isupper() else c) if c.islower() else ('[' + K.get(c.lower(), '?').upper() + ']' if c.isalpha() else c) for c in s))
