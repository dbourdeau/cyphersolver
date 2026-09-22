# Mark open alpha (α) among the round-a tokens of the 13 July 1572 transcription, from the strips (hand/pieces/*),
# 21 Sept 2026. Per line: the class of each 'a' token in order (A = open alpha with crossing tail -> 'α', a = round a).
# f. 61: 'ð' (barred o) is written O as in the other files; M4 'o' in "m d o c h" is an α on the image.
import re
D={'J1':'Aa','J2':'AAa','J3':'aa','J4':'aA','J5':'aaa','J6':'A','J7':'AAa','J8':'AaAAA','J9':'AAA','J10':'AAa',
'J11':'aAAa','J12':'AA','J13':'A','J14':'Aaaa','J15':'aaAA','J16':'','J17':'AAA','J18':'AAAaaA','J19':'aaAa','J20':'A',
'J21':'aAaA','J22':'aaA','K1':'Aa','M1':'Aa','M2':'aA','M3':'aa','M4':'','M5':'aaA','M6':''}
for src in ['ct_f60.txt','ct_f60v.txt','ct_f61.txt']:
    out=[]
    for l in open(src,encoding='utf-8'):
        if ':' not in l or l.startswith('#'): out.append(l.rstrip('\n')); continue
        lab,rest=l.split(':',1); t=rest.split(); lab=lab.strip()
        t=['@' if x=='@' else x for x in t]
        t=['O' if x=='ð' else x for x in t]
        cls=D[lab]; n=sum(x=='a' for x in t)
        assert n==len(cls),(lab,n,len(cls))
        it=iter(cls); t=[('@' if next(it)=='A' else 'a') if x=='a' else x for x in t]
        if lab=='M4':
            i=[j for j in range(len(t)-2) if t[j]=='d' and t[j+1]=='o' and t[j+2]=='c'][0]; t[i+1]='@'
        out.append('%s: %s'%(lab,' '.join(t)))
    dst=src.replace('.txt','_split.txt')
    open(dst,'w',encoding='utf-8').write('# split pass 21 Sept 2026: @ = open alpha (α), a = round a; see split.py\n'+'\n'.join(out)+'\n')
    print(dst, sum(l.split().count('@') for l in out if ':' in l))
