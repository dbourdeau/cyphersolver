"""ledger.py KEY TX OVERRIDES -- strict S/E/N per unit, per line, per letter, with the sums written out."""
import sys,importlib.util
spec=importlib.util.spec_from_file_location('dec','/home/claude/en/trackB/b75_selvatico_undated/scripts/dec.py');dec=importlib.util.module_from_spec(spec);spec.loader.exec_module(dec)
ov={}
for l in open(sys.argv[3],encoding='utf-8'):
    f=l.rstrip('\n').split('\t')
    if f[0]!='line': ov[(f[0],int(f[1]))]=f[2]
tot={}
print('line\tS\tE\tN\tX\tunits (idx:raw=value:mark)')
used=set()
for lid,items in dec.run(sys.argv[1],sys.argv[2]):
    c=dict(S=0,E=0,N=0,X=0);cells=[]
    for k,o in items:
        if k!='unit': continue
        m=o['mark']
        if (lid,o['idx']) in ov:
            used.add((lid,o['idx']))
            assert m in('S','E'),(lid,o['idx'],m)
            if m=='S': m='E*'
        c[m[0]]+=1; cells.append('%d:%s=%s:%s'%(o['idx'],o['raw'],o['val'],m))
    L=lid.split('.')[0]; tot.setdefault(L,[]).append((lid,c))
    print('%s\t%d\t%d\t%d\t%d\t%s'%(lid,c['S'],c['E'],c['N'],c['X'],' '.join(cells)))
assert used==set(ov),set(ov)-used
G=dict(S=0,E=0,N=0)
for L,rows in tot.items():
    for k in 'SEN':
        v=[c[k] for _,c in rows]; print('%s %s: %s = %d'%(L,k,'+'.join(map(str,v)),sum(v)))
    s,e,n=[sum(c[k] for _,c in rows) for k in 'SEN']
    print('%s STRICT %d/(%d+%d+%d) = %d/%d = %.2f%%'%(L,s,s,e,n,s,s+e+n,100*s/(s+e+n)))
    G['S']+=s;G['E']+=e;G['N']+=n
t=G['S']+G['E']+G['N'];print('ALL STRICT %d/(%d+%d+%d) = %d/%d = %.2f%%'%(G['S'],G['S'],G['E'],G['N'],G['S'],t,100*G['S']/t))
