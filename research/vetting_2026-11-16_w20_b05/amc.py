"""Cipher components of BnF notices, via the Omont audit's am.py (cache in img/amcache).
python -I -X utf8 amc.py cc <n> [...]   |   python -I -X utf8 amc.py fr <N> [...]"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
os.environ['AMCACHE'] = os.path.join(H, 'img', 'amcache')
sys.path.insert(0, os.path.join(H, '..', 'audit_2026-11-16_omont_shelfmarks'))
import am
a = sys.argv[1:]
mode = a.pop(0)
for x in a:
    if mode == 'fr':
        n, d = am.find_fr(int(x))
        if not n:
            print('fr', x, 'NOT FOUND'); continue
    else:
        n = int(x); d = am.parse(am.fetch(n))
    print(f'cc{n} {am.url(n)} | {d["shelf"]} | old {d["old"]} | gallica {d["gallica"]}')
    print('  head:', d['head'][:250])
    for cid, tx in sorted(am.ciph(n).items()):
        full = am.comp(cid)
        print('  *', cid, '|', tx[:200], '||', full[:300])
