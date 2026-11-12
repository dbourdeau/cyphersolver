import os
here=os.path.dirname(os.path.abspath(__file__))
S=P=I=0
for l in open(os.path.join(here,'reading_0114r.md'),encoding='utf-8'):
    if not l.startswith('IT['): continue
    for w in l.split(':',1)[1].split():
        w=w.strip('.,;:')
        if w.startswith('['): I+=1
        elif w.endswith('*'): P+=1
        else: S+=1
T=S+P+I
print(f'words {T}: sure {S}, probable {P}, unread {I}; sure {S/T:.1%}; sure+probable {(S+P)/T:.1%}')
