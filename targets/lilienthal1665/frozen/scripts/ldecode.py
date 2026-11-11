# Décode des lignes de codes avec K_L (valeur nue) puis POST ({valeur}) ; code inconnu = ‹code›.
import sys, os
D, F = sys.argv[1], sys.argv[2]; k = {}
for f, post in (('KEY-LILIENTHAL.tsv', False), ('KEY-LILIENTHAL-POST.tsv', True)):
    for ln in open(os.path.join(D, f), encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        p = ln.rstrip('\n').split('\t')
        if p[0] not in k: k[p[0]] = ('{%s}' % p[1]) if post else p[1]
for ln in open(F, encoding='utf-8'):
    if not ln.startswith('L'): continue
    lab, *t = ln.split()
    print(lab, ''.join(' | ' if c == '|' else k.get(c, '‹%s›' % c) for c in t))
