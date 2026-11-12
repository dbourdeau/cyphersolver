"""Modèle de caractères (ordre 4, espaces, lissage add-0.1) sur le corpus danois ancien :
Danske Magazin 1745-52 (4 vol. archive.org) + Kong Christian IV egenhændige Breve (7 vol.). Alphabet du chiffre (23 lettres) + espace."""
import re, math, unicodedata, collections, glob, sys, pickle
A = 'abcdefghiklmnopqrstuxyz'; S = A + ' '
def norm(t):
    t = t.replace('ſ', 's').lower()
    for a, b in (('æ','ae'),('ø','oe'),('å','aa'),('ö','oe'),('ä','ae'),('ü','u'),('j','i'),('v','u'),('w','u')): t = t.replace(a, b)
    t = ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c) != 'Mn')
    t = re.sub('[^a-z]+', ' ', t)
    return ''.join(c for c in t if c in S)
class LM:
    def __init__(s, text, n=4):
        s.n = n; s.c = collections.Counter(); s.h = collections.Counter()
        t = ' ' * (n - 1) + text
        for i in range(n - 1, len(t)):
            s.c[t[i-n+1:i+1]] += 1; s.h[t[i-n+1:i]] += 1
    def lp(s, ctx, ch): return math.log((s.c[ctx + ch] + 0.1) / (s.h[ctx] + 0.1 * len(S)))
    def per_char(s, text):
        t = ' ' * (s.n - 1) + text; tot = 0
        for i in range(s.n - 1, len(t)): tot += s.lp(t[i-s.n+1:i], t[i])
        return tot / max(1, len(text))
def build(files):
    return LM(' '.join(norm(open(f, errors='replace').read()) for f in files))
if __name__ == '__main__':
    files = sorted(glob.glob(sys.argv[1] + '/*.txt')); m = build(files)
    pickle.dump(m, open(sys.argv[2], 'wb')); print(len(m.c), 'ngrams', files)
