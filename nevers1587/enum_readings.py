"""Enumerate readings of the f.30 run tail and the f.28v dateline under key fr. 3995 no. 11 (null = '')."""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lang import lm
m = lm.load('fr-1600-letters')
def run(name, prefix, cands, suffix):
    out = []
    for combo in itertools.product(*cands):
        s = prefix + ''.join(combo) + suffix
        out.append((m.per_char(lm.norm(s, 'early')), ''.join(c if c else '_' for c in combo), s))
    out.sort(reverse=True)
    print(name)
    for sc, c, s in out[:25]: print(f'  {sc:6.2f}  {s}')
# f.30: π ^ x é | ∞ ƥ F ƨ h Ŧ ◊ 7 o
run('f30', 'passantpreslyon', [['o',''],['a',''],['p','et'],['c',''],['e'],['t','d','f',''],['a','u',''],['i'],['s','']], 'etsansaucunsubiect')
# f.28v dateline: C ∞ 6 ƥ z ι ◊ ∂ ι ⊕
run('f28v', 'de', [['o',''],['r','e'],['a'],['q','n'],['',],['a','u',''],['g','h'],[''],['e']], 'cexxviimars')

print('--- wide')
run('f30w', 'grandealarmepassantpreslyon', [['o','','ou'],['a','p',''],['p','et',''],['c','h',''],['e','h'],['t','f','d','i',''],['a','u',''],['i'],['s','o','']], 'etsansaucunsubiectcariepuisasseurer')
run('f28w', 'de', [['o',''],['r','e','b'],['a','p'],['q','n','z'],['','i'],['a','u',''],['g','h','d'],['','i'],['e','o']], 'cexxviimars')
