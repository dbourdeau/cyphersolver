"""Modèle de caractères allemand du XVIIe s. (ordre 4, lissage add-0.1) sur Merian, Topographia Hassiae 1655 (Wikisource,
copie corpus/merian_ws_1655.txt). Alphabet du chiffre Sehested : 23 lettres (j->i, y->i, q->k, v->u, umlauts -> voyelle simple) + espace."""
import re, math, unicodedata, collections, sys, pickle
A = 'abcdefghiklmnoprstuwxz'; S = A + ' '
def norm(t):
    t = t.replace('ſ', 's').lower()
    for a, b in (('ä','a'),('ö','o'),('ü','u'),('ß','ss'),('j','i'),('y','i'),('q','k'),('v','u')): t = t.replace(a, b)
    t = ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c) != 'Mn')
    t = re.sub('[^a-z]+', ' ', t)
    return ''.join(c for c in t if c in S)
def clean_wiki(t):
    t = re.sub(r'<noinclude>.*?</noinclude>', ' ', t, flags=re.S)
    t = re.sub(r'=== Seite:.*', ' ', t)
    t = re.sub(r'\{\{[^{}]*\|([^{}|]*)\}\}', r' \1 ', t)
    t = re.sub(r'\{\{[^{}]*\}\}', ' ', t); t = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', r'\1', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    return t
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
if __name__ == '__main__':
    raw = open(sys.argv[1], errors='replace').read(); txt = norm(clean_wiki(raw)); txt = re.sub(' +', ' ', txt)
    m = LM(txt); words = collections.Counter(txt.split())
    pickle.dump((m, words), open(sys.argv[2], 'wb')); print(len(txt), 'car.', len(m.c), 'ngrams', len(words), 'mots')
    print(txt[20000:20400])
