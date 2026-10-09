"""setline.py PAGE LINE 'text' : set one re-read (R) line in trans/reading_v3.txt."""
import re,sys
f='trans/reading_v3.txt'; pg0,l0,txt=sys.argv[1],f'{int(sys.argv[2]):02d}',sys.argv[3]
s=open(f,encoding='utf8').read().split('\n'); pg=None
for i,ln in enumerate(s):
    m=re.match(r'## p\. (\d+)',ln)
    if m: pg=m.group(1)
    m=re.match(r'(\d\d) [HMR] \| ',ln)
    if m and pg==pg0 and m.group(1)==l0: s[i]=f'{l0} R | {txt}'
open(f,'w',encoding='utf8').write('\n'.join(s))
