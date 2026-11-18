import sys, json, re, collections
src=sys.argv[1]; out=sys.argv[2]
occ=collections.defaultdict(list)
for line in open(src,encoding='utf-8'):
    if line.startswith('#'): continue
    for tok in re.findall(r'(\d+):(\S+)', line):
        c,g=tok; occ[int(c)].append(g)
T={}
for c in sorted(occ):
    gs=occ[c]; doubt=any(g.endswith('?') for g in gs)
    norm=[g.rstrip('?!') for g in gs]
    vals=collections.Counter(norm)
    v=vals.most_common(1)[0][0]
    st='S' if (not doubt and len(vals)==1) else 'D'
    T[str(c)]={'v':v,'statut':st,'n':len(gs),'gloses':dict(vals)}
json.dump(T,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(T),'codes ;',sum(1 for x in T.values() if x['statut']=='S'),'sûrs')
for c,x in T.items():
    if x['statut']=='D' or len(x['gloses'])>1: print(c,x)
# variantes purement orthographiques de la glose = même valeur (décidé avant le gel)
ORTHO={'19':'k','20':'l','33':'s','74':'t','78':'y','220':'ti'}
for c,v in ORTHO.items():
    T[c]['v']=v; T[c]['statut']='S'; T[c]['note']='variantes orthographiques de la glose'
json.dump(T,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=0)
print('final',len(T),'codes ;',sum(1 for x in T.values() if x['statut']=='S'),'sûrs ;',sum(1 for x in T.values() if x['statut']=='D'),'douteux')
