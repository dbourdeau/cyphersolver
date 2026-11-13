"""mkledger.py KEY TX ELIST OUT : write the ledger. Every cipher word gets S unless its decoded string is listed in ELIST (one decoded string per line,
'string<TAB>label<TAB>note'; labels E, or S? = S under b162's rule read literally but flagged borderline). One judging pass by the reader; this script only lays it out and counts.
Prints S/(S+E+N) with N = 0 (no code groups; name signs '|' are not units), and the floor with every S? counted as E."""
import sys
k={}
for l in open(sys.argv[1]):
    if l.startswith('#'): continue
    for p in l.split(): x,y=p.split('='); k[x]=y
lab={}
for l in open(sys.argv[3]):
    if l.startswith('#') or not l.strip(): continue
    p=l.rstrip('\n').split('\t'); lab[p[0]]=(p[1],p[2] if len(p)>2 else '')
used=set(); rows=[]; ln=0; per=[]
for l in open(sys.argv[2]):
    if l.startswith('#'): continue
    ln+=1; s=e=q=0; ws=[]
    for w in l.split():
        if w=='|': continue
        d=''.join(k.get(c,'?') for c in w); L,note=lab.get(d,('S',''))
        if d in lab: used.add(d)
        if '?' in d: assert L=='E', d
        rows.append('L%d\t%s\t%s\t%s\t%s'%(ln,w,d,L,note))
        s+=L in('S','S?'); q+=L=='S?'; e+=L=='E'
    per.append((ln,s,q,e))
assert used==set(lab), set(lab)-used
S=sum(p[1] for p in per); Q=sum(p[2] for p in per); E=sum(p[3] for p in per); T=S+E
out=open(sys.argv[4],'w')
out.write('# line\tcipher\tdecoded (KEY_v2)\tlabel\tnote\n'+'\n'.join(rows)+'\n')
out.write('# per line S/units: '+' | '.join('L%d %d/%d'%(p[0],p[1],p[1]+p[3]) for p in per)+'\n')
out.write('# S = '+' + '.join(str(p[1]) for p in per)+' = %d ; units = '%S+' + '.join(str(p[1]+p[3]) for p in per)+' = %d ; N = 0\n'%T)
out.write('# STRICT (b162 rule, read literally) S/(S+E+N) = %d/%d = %.2f%%\n'%(S,T,100*S/T))
out.write('# borderline S? units: %d ; FLOOR with every S? counted E = (%d - %d)/%d = %d/%d = %.2f%%\n'%(Q,S,Q,T,S-Q,T,100*(S-Q)/T))
out.close(); print(open(sys.argv[4]).read().split('# per line')[1])
