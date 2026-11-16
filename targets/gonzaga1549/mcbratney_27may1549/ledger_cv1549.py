"""Written after the first decode. Ledger: one row per cipher unit of c.31r with the frozen key's value and the letters of the
decipherment (c.12r) it aligns to under decode_cv1549's alignment (frozen references; B3 frozen span).
S = value given by the key and identical to the decipherment; E = value given, not identical; N = no value (hole)."""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import decode_cv1549 as d
key, tr = d.load_key(), d.load_tr()
refs = json.load(open(os.path.join(d.D,'ref_blocks.json'), encoding='utf-8'))
res = d.score(key, tr, refs, detail=True); bl = d.blocks(tr); rows = []; cnt = collections.Counter()
for b in ('B1','B2','B3'):
    units = d.dec(bl[b], key); owner = []
    for i,(ln,tok,v) in enumerate(units): owner += [i]*len(d.norm('#' if v=='?' else v))
    got = collections.defaultdict(list); ai = 0
    for a, r, op in res[b]['ops']:
        if a != '-': got[owner[ai]].append((r, op)); ai += 1
    for i,(ln,tok,v) in enumerate(units):
        g = got.get(i, []); ref = ''.join(r for r,_ in g if r != '-')
        cls = 'N' if v == '?' else ('S' if g and all(op=='M' for _,op in g) else 'E')
        cnt[cls] += 1; rows.append(f'{b}\t{ln}\t{tok}\t{v}\t{ref or "-"}\t{cls}')
with open(os.path.join(d.D,'27may1549_ledger.tsv'),'w') as f:
    f.write('# block\tline\tlabel\tkey value\tdecipherment letters aligned\tS/E/N\n' + '\n'.join(rows) + '\n')
    f.write(f"# totals: S {cnt['S']}, E {cnt['E']}, N {cnt['N']}; {cnt['S']} + {cnt['E']} + {cnt['N']} = {sum(cnt.values())}\n")
print(cnt, sum(cnt.values()))
