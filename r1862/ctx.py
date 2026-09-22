import sys,collections
from decode import lines, KEY
L=lines(); seq=[(lab,v) for lab,it in L for k,v in it if k=='g']
want=sys.argv[1:] or sorted({v for _,v in seq if v not in KEY}, key=lambda g:-sum(1 for _,x in seq if x==g))
for g in want:
    for i,(lab,v) in enumerate(seq):
        if v==g:
            a=''.join(KEY.get(x,f'[{x}]') for _,x in seq[max(0,i-10):i]); b=''.join(KEY.get(x,f'[{x}]') for _,x in seq[i+1:i+11])
            print(f'{g:5} {lab:7} {a[-40:]:>40} <{g}> {b[:40]}')
