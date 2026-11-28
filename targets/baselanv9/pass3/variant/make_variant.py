"""Build decode_p3_noC4C5.py from the frozen scripts/decode_p3.py by two exact text edits (own code, python3 -I)."""
import sys,hashlib
src,dst,mode=sys.argv[1],sys.argv[2],sys.argv[3]
t=open(src,encoding='utf-8').read()
a=",('Cl','Tq'):'rte'"; b="chi=len(B)>=3 and B[0][0]=='X' and B[1][0]=='Tk' and B[2][0]=='Cl'"
assert t.count(a)==1 and t.count(b)==1
if 'C4' in mode: t=t.replace(a,'')
if 'C5' in mode: t=t.replace(b,'chi=False')
open(dst,'w',encoding='utf-8').write(t)
print(mode,hashlib.sha256(t.encode()).hexdigest())
