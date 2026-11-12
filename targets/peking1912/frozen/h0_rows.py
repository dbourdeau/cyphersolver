"""H0 : lecture en LIGNES, chaîne continue découpée en codes CTC de 4 chiffres."""
from groups import *
T=table()
rows=[[c[r] for c in COLS if r<len(c)] for r in range(7)]
s=''.join(''.join(r) for r in rows)
print('rows:',rows); print('len',len(s))
codes=[s[i:i+4] for i in range(0,len(s),4)]
for c in codes: print(c, *T.get(c,('?','?')), sep='\t')
