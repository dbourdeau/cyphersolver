"""agree.py KEY MINE OTHER -- per-line alignment (difflib) of canonical tokens (digits + underline; marks ' ^ ? c ignored).
Counts over lines present in MINE. Struck/illegible units are tokens '[x]' / '#'."""
import sys,difflib,collections,importlib.util
spec=importlib.util.spec_from_file_location('dec','/home/claude/en/trackB/b70_selvatico_read/scripts/dec.py');dec=importlib.util.module_from_spec(spec);spec.loader.exec_module(dec)
def load(p):
    d={}
    for lid,items in dec.run(sys.argv[1],p):
        d[lid]=[(o['canon'] or o['val'],o['val']) for k,o in items if k=='unit']
    return d
A=load(sys.argv[2]);B=load(sys.argv[3])
tot=collections.Counter();per=collections.defaultdict(collections.Counter);miss=[]
for lid,a in A.items():
    pg=lid.split('.')[0]
    if lid not in B: miss.append(lid); per[pg]['mine_only_line']+=len(a); tot['mine_only_line']+=len(a); continue
    b=B[lid]; sm=difflib.SequenceMatcher(None,[x[0] for x in a],[x[0] for x in b],autojunk=False)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': n=i2-i1; per[pg]['same']+=n; tot['same']+=n
        elif op=='replace':
            n=min(i2-i1,j2-j1); per[pg]['differ']+=n; tot['differ']+=n
            # same decoded value despite different token?
            ex=(i2-i1)-n; per[pg]['mine_extra']+=ex; tot['mine_extra']+=ex
            ex=(j2-j1)-n; per[pg]['other_extra']+=ex; tot['other_extra']+=ex
        elif op=='delete': per[pg]['mine_extra']+=i2-i1; tot['mine_extra']+=i2-i1
        elif op=='insert': per[pg]['other_extra']+=j2-j1; tot['other_extra']+=j2-j1
mine=sum(len(a) for a in A.values())
for pg in per: print(' ',pg,dict(per[pg]))
al=tot['same']+tot['differ']
print(f"{sys.argv[3].split('/')[-1]}: my units {mine}; aligned {al}; identical {tot['same']} = {100*tot['same']/mine:.2f}% of mine ({100*tot['same']/al:.2f}% of aligned); differ {tot['differ']}; mine only {tot['mine_extra']}; theirs only {tot['other_extra']}; in lines they lack {tot['mine_only_line']} {miss}")
