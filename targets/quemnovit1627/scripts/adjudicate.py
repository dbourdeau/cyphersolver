# adjudicate.py: builds the adjudicated transcriptions from the three-way sign alignment. It does NOT decode.
# Rule (fixed before any decoding of the result):
#   majority:  each reader-1 sign position takes the KEY_B label that at least two of the three readers give
#              (reader 2 and 3 mapped by their own frozen MAPPING files; L/l and h/S merged as value-identical);
#              if no two agree, the sign is '?' (unresolved). An insertion is kept only if readers 2 and 3 both insert the same signs.
#   unanimous: a position is kept only if all three readers agree; otherwise '?'.
# Unit division and code numbers (117, 117, 118) are reader 1's (transcriptions/reader1_units.seg).
import os,importlib.util
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sp=importlib.util.spec_from_file_location('align',os.path.join(R,'scripts','align.py')); al=importlib.util.module_from_spec(sp); sp.loader.exec_module(al)
rows,L1=al.three_way()
maj={};una={}
for ln,p,a,b,c in rows:
    if a=='+':
        if b==c and b!='-': maj[(ln,p,'+')]=b
        continue
    maj[(ln,p)]=a if (a==b or a==c) else (b if (b==c and b not in '-?') else '?')
    una[(ln,p)]=a if a==b==c else '?'
segs=[l.rstrip('\n').split('|') for l in open(os.path.join(R,'transcriptions','reader1_units.seg'),encoding='utf-8') if not l.startswith('#')]
pos={}; out=[]
lines=sorted(L1)
cur={ln:0 for ln in lines}
for lid,u,dec,lab,note in segs:
    if u.isdigit(): out.append((lid,u,u,u)); continue
    ln=int(lid); m='';n=''
    for ch in u:
        if ch=='-': ln+=1; continue
        p=cur[ln]
        assert al.kb1(L1[ln])[p]==al.kb1(ch),(lid,u,ch,p)
        m+=maj.get((ln,p,'+'),'')+maj[(ln,p)]; n+=una[(ln,p)]; cur[ln]+=1
    out.append((lid,u,m,n))
for ln in lines: assert cur[ln]==len(L1[ln]),(ln,cur[ln],len(L1[ln]))
with open(os.path.join(R,'transcriptions','adjudicated.tsv'),'w',encoding='utf-8') as f:
    f.write('# line\treader1 unit\tmajority (>=2 of 3 readers)\tunanimous (all 3)   KEY_B labels, L->l and h->S merged; ? = no agreement\n')
    for r in out: f.write('\t'.join(r)+'\n')
q1=sum(r[2].count('?') for r in out); q2=sum(r[3].count('?') for r in out)
print('units',len(out),'; unresolved signs: majority',q1,', unanimous',q2)
