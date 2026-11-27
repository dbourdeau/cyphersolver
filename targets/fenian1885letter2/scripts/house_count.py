# The checks were done with AI tools and no person checked each record by hand.
# Usage: python -I scripts/house_count.py READING.txt  (from targets/fenian1885letter2)
import re,sys
t=open(sys.argv[1],encoding='utf-8').read()
words=[]
for m in re.findall(r'⟦([^⟧]*)⟧',t):
    words+=m.split()
# House count rule (Dan Bourdeau, 27 Nov 2026): cipher words only; a word is read when every letter comes from a clean
# pair with nothing supplied, or when it is the writer's dash abbreviation and its expansion is certain.
CERTAIN={'Rus[si]a','Pat[riot]s','nat[iv]e','l[an]d'}
WHY={'DEC':'letters given, referent/expansion unknown','or[ganisation]':'OR-- only; expansion ours, not certain (order?)',
     'R[...]s':'R--S, expansion open','Aut[ono]my':'emended (written AUTNONMY)','C[a]nada':'pair 2 doubtful, A supplied'}
read=holes=0
for w in words:
    w2=w.strip('.,')
    ok = (w2 in CERTAIN) or ('[' not in w2 and w2!='DEC')
    print(('read ' if ok else 'HOLE ')+w2+('' if ok else '  - '+WHY.get(w2,'?')))
    read+=ok; holes+=not ok
n=len(words); print(f'cipher_words {n} read {read} holes {holes} read_share {read/n:.3f}')
