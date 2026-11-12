"""Partie A : lecture CTC standard en clair des groupes de 4 chiffres (Unihan : Taiwan puis Mainland)."""
import sys
def table(path='ctc_table.tsv'):
    T={}
    for l in open(path,encoding='utf8'):
        if l.startswith('#'):continue
        c,m,t=(l.rstrip('\n').split('\t')+['',''])[:3]
        T[c]=(t or m)[:1] or '?'
    return T
T=table()
for f in sys.argv[1:]:
    g=open(f).read().split()
    print(f, len(g))
    print(''.join(T.get(c,'□') for c in g))
    for i in range(0,len(g),10): print('  '+' '.join(f'{c}{T.get(c,"□")}' for c in g[i:i+10]))
