"""usage: build_lex.py <dir> <out>  : mots (lettres seules) fréquence>=2, longueur>=2, normalisation v->w é->e ü->y"""
import sys, os, re, collections
def norm(s): return s.lower().replace('v','w').replace('é','e').replace('ü','y')
C = collections.Counter()
for f in sorted(os.listdir(sys.argv[1])):
    if not f.endswith('.txt'): continue
    t = open(os.path.join(sys.argv[1], f), encoding='utf-8', errors='ignore').read()
    t = re.sub(r'<[^>]+>|\{\{[^}]*\}\}|\[\[[^\]|]*\||\]\]|\[\[', ' ', t)
    for w in re.findall(r'[A-Za-zÅÄÖåäöÉéÜü]+', t):
        w = norm(w)
        if len(w) >= 2: C[w] += 1
W = sorted(w for w, c in C.items() if c >= 2)
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(W) + '\n'); print(len(W), 'mots')
