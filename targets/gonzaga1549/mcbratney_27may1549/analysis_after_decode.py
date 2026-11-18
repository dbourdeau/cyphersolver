"""Written AFTER the first decode (not part of the figure of record).
1) B3 rescored against a reference that runs on to 12r L17 (the frozen B3 reference stopped at 12r L15 'proueea', short of the foot of 31r).
2) Per-label agreement: for each shape label, how many of its units align letter-for-letter with the decipherment, and what the
   decipherment has where they do not. Shows where the key and the decipherment disagree."""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import decode_cv1549 as d
key, tr = d.load_key(), d.load_tr()
refs = json.load(open(os.path.join(d.D,'ref_blocks.json'), encoding='utf-8'))
ext = dict(refs); ext['B3'] = refs['B3'] + ' en el remedio de lo que assy se ha innouado e innouare contra los tractados porque de otra manera no seria tolerable'
out = []
res = d.score(key, tr, ext, detail=True)
r3 = res['B3']; out.append(f"B3 with reference to 12r L17 (free end): matched {r3['matched']} of {r3['ref_letters']} = {100*r3['matched']/r3['ref_letters']:.1f}%")
tm = sum(res[b]['matched'] for b in res); trf = sum(res[b]['ref_letters'] for b in res)
out.append(f"ALL with that B3 span: {tm} of {trf} = {100*tm/trf:.1f}%")
out.append('  B3 decoded:   ' + r3['decoded']); out.append('  B3 reference: ' + r3['ref'])
# per-label agreement
blocks = d.blocks(tr); stat = collections.defaultdict(lambda: [0,0,collections.Counter()])
for b in ('B1','B2','B3'):
    units = d.dec(blocks[b], key)
    owner = []
    for i,(ln,tok,v) in enumerate(units):
        s = d.norm('#' if v=='?' else v)
        owner += [i]*len(s)
    ops = res[b]['ops']; ai = 0; got = collections.defaultdict(list)
    for a, r, op in ops:
        if a != '-':
            got[owner[ai]].append((a, r, op)); ai += 1
    for i,(ln,tok,v) in enumerate(units):
        g = got.get(i, []); ok = all(op=='M' for _,_,op in g) and g
        st = stat[tok]; st[0] += 1; st[1] += bool(ok)
        if not ok: st[2][''.join(r for _,r,_ in g if r!='-') or '(none)'] += 1
out.append('\nlabel\tvalue\tunits\tagree\tdecipherment has (where not)')
for tok,(n,ok,c) in sorted(stat.items(), key=lambda x:-x[1][0]):
    v = key[tok][0] if tok in key else 'code'
    out.append(f"{tok}\t{v}\t{n}\t{ok}\t" + ', '.join(f'{k} {m}' for k,m in c.most_common(6)))
open(os.path.join(d.D,'27may1549_analysis.txt'),'w').write('\n'.join(out)+'\n'); print('\n'.join(out))
