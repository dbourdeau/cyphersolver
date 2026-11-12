import sys,difflib,importlib.util
spec=importlib.util.spec_from_file_location('dec','/home/claude/en/trackB/b75_selvatico_undated/scripts/dec.py');dec=importlib.util.module_from_spec(spec);spec.loader.exec_module(dec)
def toks(p,pref):
    out=[]
    for lid,items in dec.run('/home/claude/en/trackB/b75_selvatico_undated/work/KEY_K3.tsv',p):
        if not lid.startswith(pref): continue
        for k,o in items:
            if k=='unit': out.append(o['canon'] or '#')
    return out
for pref,other in [('2r.',sys.argv[2]),('14r.',sys.argv[2]),('14r.',sys.argv[3])]:
    a=toks(sys.argv[1],pref);b=toks(other,pref)
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False); same=sum(x.size for x in sm.get_matching_blocks())
    print(pref,other.split('/')[-1],'mine',len(a),'theirs',len(b),'identical',same,'= %.2f%% of mine'%(100*same/len(a)))
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op!='equal': print('   ',op,a[i1:i2],b[j1:j2])
